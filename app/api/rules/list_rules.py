from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.models.Rule import Rule
from app.modassembly.database.sql.get_sql_session import get_sql_session
from pydantic import BaseModel

router = APIRouter()

class RuleResponse(BaseModel):
    rule_id: int
    description: str
    criteria: str
    status: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

@router.get("/rules", response_model=List[RuleResponse], summary="List all rules", tags=["Rules"])
def list_rules(db: Session = Depends(get_sql_session)) -> List[RuleResponse]:
    """
    Fetches all rules from the Rules table and returns them as a list.

    - **db**: SQLAlchemy session dependency.
    - **return**: List of rules with their details.
    """
    rules = db.query(Rule).all()
    return [RuleResponse(
        rule_id=rule.rule_id,
        description=rule.description.__str__(),
        criteria=rule.criteria.__str__(),
        status=rule.status.value,
        created_at=rule.created_at.isoformat(),
        updated_at=rule.updated_at.isoformat() if rule.updated_at else None
    ) for rule in rules]
