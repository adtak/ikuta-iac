from aws_cdk import core
from aws_cdk.aws_apigateway import LambdaRestApi
from aws_cdk.aws_lambda import IFunction

class ApigatewayStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, lambda_function: IFunction, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        _ = LambdaRestApi(
            self,
            'ikutaEndpoint',
            handler=lambda_function,
            # proxy=False,
            # deploy_options={},
        )
