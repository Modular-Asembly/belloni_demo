from typing import List
from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
from app.models.Rule import Rule
from app.models.Alert import Alert
from app.modassembly.database.sql.get_sql_session import get_sql_session


def evaluate_transaction_rules(transactions: List[Transaction]) -> None:
    with get_sql_session() as session:  # type: Session
        rules = session.query(Rule).filter(Rule.status == "active").all()

        for transaction in transactions:
            for rule in rules:
                if evaluate_criteria(transaction, rule.criteria.__str__()):
                    alert = Alert(
                        transaction_id=transaction.transaction_id,
                        rule_id=rule.rule_id,
                        message=f"Rule {rule.rule_id} triggered for transaction {transaction.transaction_id}"
                    )
                    session.add(alert)
        session.commit()


def evaluate_criteria(transaction: Transaction, criteria: str) -> bool:
    # Placeholder for criteria evaluation logic
    # Implement the logic to evaluate the transaction against the criteria
    return True
