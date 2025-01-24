from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
from app.modassembly.database.sql.get_sql_session import get_sql_session

def store_transaction(transaction_id: int, amount: float, timestamp: str, status: str) -> None:
    with next(get_sql_session()) as session:  # type: Session
        transaction = Transaction(
            transaction_id=transaction_id,
            amount=amount,
            timestamp=timestamp,
            status=status
        )
        session.add(transaction)
        session.commit()
