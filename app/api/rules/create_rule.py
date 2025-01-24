from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.models.Rule import Rule, RuleStatus
from app.modassembly.database.sql.get_sql_session import get_sql_session

router = APIRouter()

class RuleCreateRequest(BaseModel):
    description: str
    criteria: str
    status: RuleStatus

class RuleCreateResponse(BaseModel):
    rule_id: int
    description: str
    criteria: str
    status: str
    created_at: str
    updated_at: str

@router.post("/rules", response_model=RuleCreateResponse, status_code=201)
def create_rule(rule_data: RuleCreateRequest, db: Session = Depends(get_sql_session)) -> RuleCreateResponse:
    """
    Create a new rule.

    - **description**: A brief description of the rule.
    - **criteria**: The criteria that define the rule.
    - **status**: The current status of the rule (e.g., active, inactive).
    """
    new_rule = Rule(
        description=rule_data.description,
        criteria=rule_data.criteria,
        status=rule_data.status
    )
    db.add(new_rule)
    db.commit()
    db.refresh(new_rule)

    return RuleCreateResponse(
        rule_id=new_rule.rule_id.__int__(),
        description=new_rule.description.__str__(),
        criteria=new_rule.criteria.__str__(),
        status=new_rule.status.value.__str__(),
        created_at=new_rule.created_at.isoformat().__str__(),
        updated_at=new_rule.updated_at.isoformat().__str__()
    )
