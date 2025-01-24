from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
from app.modassembly.database.sql.get_sql_session import get_sql_session
from typing import Dict


def store_transaction(transaction_data: Dict[str, str]) -> None:
    """
    Stores the validated transaction data in the Transactions table in CloudSQL.

    :param transaction_data: A dictionary containing transaction details.
    """
    with next(get_sql_session()) as session:  # type: Session
        transaction = Transaction(
            amount=float(transaction_data["amount"]),
            status=transaction_data["status"].__str__()
        )
        session.add(transaction)
        session.commit()
