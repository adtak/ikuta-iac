from aws_cdk import core
from aws_cdk.aws_ecr import Repository, LifecycleRule, TagStatus


class EcrStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create ECR
        lifecycle_rule = LifecycleRule(
            description="Keep only one image.",
            max_image_count=1,
            rule_priority=1,
            tag_status=TagStatus.ANY,
        )
        self.ikuta_repository = Repository(
            self,
            "ikutaRepository",
            image_scan_on_push=False,
            lifecycle_rules=[lifecycle_rule],
            removal_policy=core.RemovalPolicy.DESTROY,
            repository_name="ikuta",
        )
