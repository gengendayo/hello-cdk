#!/usr/bin/env python3
import os
import aws_cdk as cdk
from backend.component import MyAppStage

env_DEV = cdk.Environment(
    account="your_account_id", region="your_region")  # Replace with your AWS account ID and region
env_PRD = cdk.Environment(
    account="your_account_id", region="your_region")  # Replace with your AWS account ID and region

app = cdk.App()

MyAppStage(app, 'Dev', env=env_DEV)
MyAppStage(app, 'Prd', env=env_PRD)

app.synth()