from typing import Dict, Any

def validate_transaction_data(transaction_data: Dict[str, Any]) -> bool:
    required_fields = ["transaction_id", "amount", "timestamp", "status"]
    
    # Check if all required fields are present
    for field in required_fields:
        if field not in transaction_data:
            raise ValueError(f"Missing required field: {field}")
    
    # Validate field types
    if not isinstance(transaction_data["transaction_id"], int):
        raise TypeError("transaction_id must be an integer")
    
    if not isinstance(transaction_data["amount"], (int, float)):
        raise TypeError("amount must be a number")
    
    if not isinstance(transaction_data["timestamp"], str):
        raise TypeError("timestamp must be a string")
    
    if not isinstance(transaction_data["status"], str):
        raise TypeError("status must be a string")
    
    return True
