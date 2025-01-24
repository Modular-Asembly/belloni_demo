from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transactions.validate_transaction_data import validate_transaction_data
from app.services.transactions.store_transaction import store_transaction

router = APIRouter()

class TransactionRequest(BaseModel):
    transaction_id: int
    amount: float
    timestamp: str
    status: str

class TransactionResponse(BaseModel):
    message: str

@router.post("/transactions", response_model=TransactionResponse, status_code=201)
def receive_transaction(transaction_data: TransactionRequest) -> TransactionResponse:
    """
    Receives transaction data via an HTTP request, validates it, and stores it.

    - **transaction_id**: Unique identifier for the transaction.
    - **amount**: The amount involved in the transaction.
    - **timestamp**: The date and time when the transaction occurred.
    - **status**: The current status of the transaction.
    """
    # Validate transaction data
    if not validate_transaction_data(transaction_data.dict()):
        raise HTTPException(status_code=400, detail="Invalid transaction data")

    # Store transaction data
    store_transaction(transaction_data.dict())

    return TransactionResponse(message="Transaction successfully received and stored.")
