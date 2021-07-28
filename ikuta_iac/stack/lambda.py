from aws_cdk import core
from aws_cdk.aws_iam import Role, ServicePrincipal, ManagedPolicy
from aws_cdk.aws_lambda import Code, Function, Handler, Runtime


class IkutaEcrStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_exec_role = Role(
            self,
            'lambdaExecRole',
            role_name='ikutaLambdaExecRole',
            assumed_by=ServicePrincipal('lambda.amazonaws.com'),
            managed_policies=[
                ManagedPolicy.from_aws_managed_policy_name(
                    'service-role/AWSLambdaBasicExecutionRole'
                )
            ],
        )

        lambda_code = Code.from_ecr_image(
            kwargs['ikuta_repository'],
            # TODO: update cmd
            cmd=['python'],
            entrypoint=['/lambda-entrypoint.sh'],
            tag='latest',
        )

        _ = Function(
            self,
            'ikutaLambda',
            code=lambda_code,
            role=lambda_exec_role,
            function_name='ikuta',
            runtime=Runtime.FROM_IMAGE,
            handler=Handler.FROM_IMAGE,
            timeout=core.Duration.seconds(30),
        )
