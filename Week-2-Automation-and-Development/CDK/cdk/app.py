#!/usr/bin/env python3

#from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from cdk.cdk_stack import CdkStack
import aws_cdk.aws_s3 as s3

class S3(core.Stack):
    def S3Stack(self):
        s3.Bucket(
            bucket_name="alphaiocloudskillstestbucket24032021"
        )


app = core.App()
S3(app, "cdk")
#CdkStack(app, "CdkStack")

app.synth()
