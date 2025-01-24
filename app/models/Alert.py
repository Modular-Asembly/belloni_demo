from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base
from app.models import Transaction, Rule
from datetime import datetime


class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    transaction_id = Column(Integer, ForeignKey("transactions.transaction_id"), nullable=False)
    rule_id = Column(Integer, ForeignKey("rules.rule_id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    message = Column(String, nullable=False)

    transaction = relationship("Transaction", back_populates="alerts")
    rule = relationship("Rule", back_populates="alerts")
