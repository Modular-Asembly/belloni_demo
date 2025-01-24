from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.modassembly.database.sql.get_sql_session import Base
import enum


class RuleStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Rule(Base):
    __tablename__ = "rules"

    rule_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String, nullable=False)
    criteria = Column(String, nullable=False)
    status = Column(Enum(RuleStatus), default=RuleStatus.ACTIVE, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=False)
