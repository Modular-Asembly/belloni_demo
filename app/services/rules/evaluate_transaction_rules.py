from typing import List
from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
from app.models.Rule import Rule
from app.models.Alert import Alert
from app.modassembly.database.sql.get_sql_session import get_sql_session

def evaluate_transaction_rules() -> None:
    with get_sql_session() as session:  # type: Session
        # Fetch all rules
        rules: List[Rule] = session.query(Rule).all()

        # Fetch all transactions
        transactions: List[Transaction] = session.query(Transaction).all()

        for transaction in transactions:
            for rule in rules:
                # Evaluate the transaction against the rule's condition
                if eval(rule.condition.__str__()):  # Assuming condition is a valid Python expression
                    # Generate an alert
                    alert = Alert(
                        transaction_id=transaction.transaction_id,
                        rule_id=rule.rule_id,
                        message=f"Rule {rule.rule_id} triggered for transaction {transaction.transaction_id}"
                    )
                    # Store the alert in the Alerts table
                    session.add(alert)
        session.commit()
