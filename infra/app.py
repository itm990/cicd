#!/usr/bin/env python3
import os

import aws_cdk as cdk

from alb_fargate.alb_fargate_stack import AlbFargateStack


app = cdk.App()
AlbFargateStack(app, "AlbFargateStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
