#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.aws_lambda import Handler
from ikuta_iac.stack.aws_apigateway import ApigatewayStack
from ikuta_iac.stack.aws_ecr import EcrStack
from ikuta_iac.stack.aws_lambda import LambdaStack

app = core.App()

ecr_stack = EcrStack(app, 'ikutaEcrStack')
lambda_stack = LambdaStack(app, 'ikutaLambdaStack', repository=ecr_stack.ikuta_repository)
apigateway_stack = ApigatewayStack(app, 'ikutaApigatewayStack', handler=lambda_stack.ikuta_lambda_function)

app.synth()
