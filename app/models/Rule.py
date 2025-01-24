import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.modassembly.database.sql.get_sql_session import Base

class Rule(Base):
    __tablename__ = "rules"

    rule_id: int = Column(Integer, primary_key=True, index=True)
    description: str = Column(String, nullable=False)
    condition: str = Column(String, nullable=False)
    action: str = Column(String, nullable=False)
