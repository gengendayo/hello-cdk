from aws_cdk import Stage
from constructs import Construct
from backend.api.api_stack import ApiStack
from backend.database.database_stack import DatabaseStack

class MyAppStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Add both stacks to the stage
        database = DatabaseStack(self, "DatabaseStack")
        api = ApiStack(self, "ApiStack",
                       table_name=database.dynamodb_table.table_name)

        database.dynamodb_table.grant_read_write_data(api.get_all_item_lambda)