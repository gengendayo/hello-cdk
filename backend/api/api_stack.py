from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

class ApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, *, table_name: str) -> None:
        super().__init__(scope, construct_id)

        # Lambda関数の作成
        self.get_all_item_lambda = _lambda.Function(
            self, 'Api',
            code=_lambda.Code.from_asset('backend/api/runtime'),
            handler='lambda_handler.handler',
            function_name='usersFunction',
            runtime=_lambda.Runtime.PYTHON_3_12,
            environment={"DYNAMODB_TABLE_NAME": table_name},
        )

        # API Gatewayの作成
        api = apigateway.RestApi(self, "users-api")
        users = api.root.add_resource("users")
        get_users_integration = apigateway.LambdaIntegration(
            self.get_all_item_lambda)
        users.add_method("GET", get_users_integration)