from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.services.transactions.validate_transaction_data import validate_transaction_data
from app.services.transactions.store_transaction import store_transaction
from app.services.rules.evaluate_transaction_rules import evaluate_transaction_rules
from app.services.alerts.send_alert_email import send_alert_email
from app.models.Transaction import Transaction

router = APIRouter()

class TransactionRequest(BaseModel):
    transaction_id: int
    amount: float
    timestamp: str
    status: str

class TransactionResponse(BaseModel):
    message: str

@router.post("/transactions", response_model=TransactionResponse, status_code=201)
def process_transaction(transaction_data: TransactionRequest) -> TransactionResponse:
    """
    Process a transaction by validating, storing, evaluating against rules, and sending alerts.

    - **transaction_data**: The transaction data to process.
    """
    # Validate transaction data
    if not validate_transaction_data(transaction_data.dict()):
        raise HTTPException(status_code=400, detail="Invalid transaction data")

    # Store transaction
    store_transaction(transaction_data.dict())

    # Evaluate transaction against rules
    transaction = Transaction(
        transaction_id=transaction_data.transaction_id,
        amount=transaction_data.amount,
        timestamp=transaction_data.timestamp,
        status=transaction_data.status
    )
    evaluate_transaction_rules([transaction])

    # Send alert emails
    send_alert_email()

    return TransactionResponse(message="Transaction processed successfully.")
