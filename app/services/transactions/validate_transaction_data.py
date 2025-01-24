from typing import Dict, Any
from app.models.Transaction import Transaction

def validate_transaction_data(data: Dict[str, Any]) -> bool:
    """
    Validates the incoming transaction data.
    Ensures all required fields are present and correctly formatted.

    :param data: A dictionary containing transaction data.
    :return: True if the data is valid, raises ValueError otherwise.
    """
    required_fields = ["transaction_id", "amount", "timestamp", "status"]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")

    # Validate field types
    if not isinstance(data["transaction_id"], int):
        raise ValueError("transaction_id must be an integer")

    if not isinstance(data["amount"], (int, float)):
        raise ValueError("amount must be a number")

    if not isinstance(data["timestamp"], str):  # Assuming timestamp is a string in ISO format
        raise ValueError("timestamp must be a string in ISO format")

    if not isinstance(data["status"], str):
        raise ValueError("status must be a string")

    return True
