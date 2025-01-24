import os
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from app.modassembly.database.sql.get_sql_session import Base

class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id: int = Column(Integer, primary_key=True, index=True)
    amount: float = Column(Float, nullable=False)
    timestamp: str = Column(DateTime, nullable=False)
    status: str = Column(String, nullable=False)
