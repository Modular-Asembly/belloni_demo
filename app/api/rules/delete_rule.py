from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.Rule import Rule
from app.modassembly.database.sql.get_sql_session import get_sql_session
from pydantic import BaseModel

router = APIRouter()

class RuleDeleteResponse(BaseModel):
    message: str

@router.delete("/rules/{rule_id}", response_model=RuleDeleteResponse)
def delete_rule(rule_id: int, db: Session = Depends(get_sql_session)) -> RuleDeleteResponse:
    """
    Delete a rule by its ID.

    - **rule_id**: The ID of the rule to delete.
    """
    rule = db.query(Rule).filter(Rule.rule_id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")

    db.delete(rule)
    db.commit()

    return RuleDeleteResponse(message=f"Rule with ID {rule_id} has been deleted.")
