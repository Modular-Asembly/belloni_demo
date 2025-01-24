from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.modassembly.database.sql.get_sql_session import Base
from datetime import datetime


class Alert(Base):
    __tablename__ = "alerts"

    alert_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    transaction_id = Column(Integer, nullable=False)
    rule_id = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    message = Column(String, nullable=False)

    def __init__(self, transaction_id: int, rule_id: int, message: str):
        self.transaction_id = transaction_id
        self.rule_id = rule_id
        self.message = message
