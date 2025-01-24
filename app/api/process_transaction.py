from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from app.services.transactions.validate_transaction_data import validate_transaction_data
from app.services.transactions.store_transaction import store_transaction
from app.services.rules.evaluate_transaction_rules import evaluate_transaction_rules
from app.services.alerts.send_alert_email import send_alert_email

router = APIRouter()

class TransactionInput(BaseModel):
    transaction_id: int
    amount: float
    timestamp: str
    status: str

class TransactionResponse(BaseModel):
    message: str

@router.post("/process_transaction", response_model=TransactionResponse)
async def process_transaction(transaction_data: TransactionInput) -> TransactionResponse:
    """
    Receives transaction data, validates it, stores it, evaluates against rules,
    and sends email notifications for any generated alerts.
    
    - **transaction_id**: Unique identifier for the transaction.
    - **amount**: The amount involved in the transaction.
    - **timestamp**: The date and time when the transaction occurred.
    - **status**: The current status of the transaction.
    """
    # Validate transaction data
    if not validate_transaction_data(transaction_data.dict()):
        raise HTTPException(status_code=400, detail="Invalid transaction data")

    # Store transaction
    store_transaction(
        transaction_id=transaction_data.transaction_id,
        amount=transaction_data.amount,
        timestamp=transaction_data.timestamp,
        status=transaction_data.status
    )

    # Evaluate transaction against rules
    evaluate_transaction_rules()

    # Send email notifications for alerts
    send_alert_email()

    return TransactionResponse(message="Transaction processed successfully")
