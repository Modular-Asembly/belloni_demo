from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transactions.validate_transaction_data import validate_transaction_data
from app.services.transactions.store_transaction import store_transaction

router = APIRouter()

class TransactionInput(BaseModel):
    transaction_id: int
    amount: float
    timestamp: str
    status: str

class TransactionOutput(BaseModel):
    message: str

@router.post("/transactions", response_model=TransactionOutput)
async def receive_transaction(transaction: TransactionInput) -> TransactionOutput:
    """
    Receives transaction data via an HTTP request, validates it, and stores it.

    - **transaction_id**: Unique identifier for the transaction.
    - **amount**: The amount involved in the transaction.
    - **timestamp**: The date and time when the transaction occurred.
    - **status**: The current status of the transaction.
    """
    # Validate transaction data
    validate_transaction_data(transaction.dict())

    # Store transaction data
    store_transaction(
        transaction_id=transaction.transaction_id,
        amount=transaction.amount,
        timestamp=transaction.timestamp,
        status=transaction.status
    )

    return TransactionOutput(message="Transaction successfully processed.")
