from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from app.modassembly.database.sql.get_sql_session import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount: float = Column(Float, nullable=False)
    timestamp: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
    status: str = Column(String, nullable=False)

    def __init__(self, amount: float, status: str):
        self.amount = amount
        self.status = status
