from aws_cdk import (
    Stack,
    aws_budgets as budgets
)
from constructs import Construct

class MyBudgetCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        budgets.CfnBudget(self, "MonthlyBudget",
            budget={
                "budgetType": "COST",
                "timeUnit": "MONTHLY",
                "budgetLimit": {
                    "amount": 10,
                    "unit": "USD"
                },
                "budgetName": "DevOps-Monthly-Budget"
            },
            notificationsWithSubscribers=[]
        )
