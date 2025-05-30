from aws_cdk import (
    Stack,
    aws_budgets as budgets
)
from constructs import Construct


class MyBudgetCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        budgets.CfnBudget(
            self, "MyBudget",
            budget={
                "budgetType": "COST",
                "timeUnit": "MONTHLY",
                "budgetLimit": {
                    "amount": 5,
                    "unit": "USD"
                },
                "budgetName": "MyDevOpsBudget"
            },
            notifications_with_subscribers=[
                {
                    "notification": {
                        "notificationType": "ACTUAL",
                        "comparisonOperator": "GREATER_THAN",
                        "threshold": 80,
                        "thresholdType": "PERCENTAGE"
                    },
                    "subscribers": [
                        {
                            "subscriptionType": "EMAIL",
                            "address": "devops@gmail.com"
                        }
                    ]
                }
            ]
        )

