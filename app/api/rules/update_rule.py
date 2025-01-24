from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from app.models.Rule import Rule, RuleStatus
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class RuleUpdateRequest(BaseModel):
    description: Optional[str]
    criteria: Optional[str]
    status: Optional[RuleStatus]

class RuleUpdateResponse(BaseModel):
    rule_id: int
    description: str
    criteria: str
    status: RuleStatus

@router.put("/rules/{rule_id}", response_model=RuleUpdateResponse)
def update_rule(rule_id: int, rule_data: RuleUpdateRequest, db: Session = Depends(get_sql_session)) -> RuleUpdateResponse:
    """
    Update an existing rule in the Rules table.

    - **rule_id**: The ID of the rule to update.
    - **rule_data**: The updated data for the rule.
    """
    rule = db.query(Rule).filter(Rule.rule_id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    if rule_data.description is not None:
        rule.description = rule_data.description
    if rule_data.criteria is not None:
        rule.criteria = rule_data.criteria
    if rule_data.status is not None:
        rule.status = rule_data.status

    db.commit()
    db.refresh(rule)

    return RuleUpdateResponse(
        rule_id=rule.rule_id.__int__(),
        description=rule.description.__str__(),
        criteria=rule.criteria.__str__(),
        status=rule.status
    )
