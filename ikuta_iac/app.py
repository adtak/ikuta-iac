#!/usr/bin/env python3

from aws_cdk import core
from ikuta_iac.stack.aws_ecr import IkutaEcrStack
from ikuta_iac.stack.aws_lambda import IkutaLambdaStack


app = core.App()

ecr_stack = IkutaEcrStack(app, 'ikutaEcrStack')
lambda_stack = IkutaLambdaStack(app, 'ikutaLambdaStack', repository=ecr_stack.ikuta_repository)

app.synth()
