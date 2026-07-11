from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb
)
from constructs import Construct

# Define the database stack

class DatabaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your database goes here
        self.dynamodb_table = dynamodb.Table(
            self,
            "usertable",
            table_name='Users',
            partition_key=dynamodb.Attribute(
                name="username",
                type=dynamodb.AttributeType.STRING
            )
        )