from aws_cdk import core
from aws_cdk.aws_apigateway import RestApi, LambdaIntegration
from aws_cdk.aws_lambda import IFunction

class ApigatewayStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, handler: IFunction, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        apigateway = RestApi(
            self,
            'ikutaEndpoint',
        )
        resource = apigateway.root.add_resource('ikuta')
        resource.add_method(
            'GET',
            LambdaIntegration(
                handler,
                request_templates={'application/json': '{ "statusCode": "200" }'},
            )
        )
