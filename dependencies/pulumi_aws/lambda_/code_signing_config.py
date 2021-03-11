# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['CodeSigningConfig']


class CodeSigningConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_publishers: Optional[pulumi.Input[pulumi.InputType['CodeSigningConfigAllowedPublishersArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[pulumi.InputType['CodeSigningConfigPoliciesArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Lambda Code Signing Config resource. A code signing configuration defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).

        For information about Lambda code signing configurations and how to use them, see [configuring code signing for Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        new_csc = aws.lambda_.CodeSigningConfig("newCsc",
            allowed_publishers=aws.lambda..CodeSigningConfigAllowedPublishersArgs(
                signing_profile_version_arns=[
                    aws_signer_signing_profile["example1"]["arn"],
                    aws_signer_signing_profile["example2"]["arn"],
                ],
            ),
            policies=aws.lambda..CodeSigningConfigPoliciesArgs(
                untrusted_artifact_on_deployment="Warn",
            ),
            description="My awesome code signing config.")
        ```

        ## Import

        Code Signing Configs can be imported using their ARN, e.g.

        ```sh
         $ pulumi import aws:lambda/codeSigningConfig:CodeSigningConfig imported_csc arn:aws:lambda:us-west-2:123456789012:code-signing-config:csc-0f6c334abcdea4d8b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CodeSigningConfigAllowedPublishersArgs']] allowed_publishers: A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
        :param pulumi.Input[str] description: Descriptive name for this code signing configuration.
        :param pulumi.Input[pulumi.InputType['CodeSigningConfigPoliciesArgs']] policies: A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if allowed_publishers is None and not opts.urn:
                raise TypeError("Missing required property 'allowed_publishers'")
            __props__['allowed_publishers'] = allowed_publishers
            __props__['description'] = description
            __props__['policies'] = policies
            __props__['arn'] = None
            __props__['config_id'] = None
            __props__['last_modified'] = None
        super(CodeSigningConfig, __self__).__init__(
            'aws:lambda/codeSigningConfig:CodeSigningConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allowed_publishers: Optional[pulumi.Input[pulumi.InputType['CodeSigningConfigAllowedPublishersArgs']]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            config_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            last_modified: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[pulumi.InputType['CodeSigningConfigPoliciesArgs']]] = None) -> 'CodeSigningConfig':
        """
        Get an existing CodeSigningConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CodeSigningConfigAllowedPublishersArgs']] allowed_publishers: A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the code signing configuration.
        :param pulumi.Input[str] config_id: Unique identifier for the code signing configuration.
        :param pulumi.Input[str] description: Descriptive name for this code signing configuration.
        :param pulumi.Input[str] last_modified: The date and time that the code signing configuration was last modified.
        :param pulumi.Input[pulumi.InputType['CodeSigningConfigPoliciesArgs']] policies: A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allowed_publishers"] = allowed_publishers
        __props__["arn"] = arn
        __props__["config_id"] = config_id
        __props__["description"] = description
        __props__["last_modified"] = last_modified
        __props__["policies"] = policies
        return CodeSigningConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedPublishers")
    def allowed_publishers(self) -> pulumi.Output['outputs.CodeSigningConfigAllowedPublishers']:
        """
        A configuration block of allowed publishers as signing profiles for this code signing configuration. Detailed below.
        """
        return pulumi.get(self, "allowed_publishers")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the code signing configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="configId")
    def config_id(self) -> pulumi.Output[str]:
        """
        Unique identifier for the code signing configuration.
        """
        return pulumi.get(self, "config_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Descriptive name for this code signing configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The date and time that the code signing configuration was last modified.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output['outputs.CodeSigningConfigPolicies']:
        """
        A configuration block of code signing policies that define the actions to take if the validation checks fail. Detailed below.
        """
        return pulumi.get(self, "policies")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

