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

__all__ = ['Rule']


class Rule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 input_parameters: Optional[pulumi.Input[str]] = None,
                 maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['RuleScopeArgs']]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['RuleSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an AWS Config Rule.

        > **Note:** Config Rule requires an existing `Configuration Recorder` to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.

        ## Example Usage
        ### AWS Managed Rules

        AWS managed rules can be used by setting the source owner to `AWS` and the source identifier to the name of the managed rule. More information about AWS managed rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).

        ```python
        import pulumi
        import pulumi_aws as aws

        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "config.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }
        \"\"\")
        foo = aws.cfg.Recorder("foo", role_arn=role.arn)
        rule = aws.cfg.Rule("rule", source=aws.cfg.RuleSourceArgs(
            owner="AWS",
            source_identifier="S3_BUCKET_VERSIONING_ENABLED",
        ),
        opts=pulumi.ResourceOptions(depends_on=[foo]))
        role_policy = aws.iam.RolePolicy("rolePolicy",
            role=role.id,
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
          	{
          		"Action": "config:Put*",
          		"Effect": "Allow",
          		"Resource": "*"

          	}
          ]
        }
        \"\"\")
        ```
        ### Custom Rules

        Custom rules can be used by setting the source owner to `CUSTOM_LAMBDA` and the source identifier to the Amazon Resource Name (ARN) of the Lambda Function. The AWS Config service must have permissions to invoke the Lambda Function, e.g. via the `lambda.Permission` resource. More information about custom rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html).

        ```python
        import pulumi
        import pulumi_aws as aws

        example_recorder = aws.cfg.Recorder("exampleRecorder")
        # ... other configuration ...
        example_function = aws.lambda_.Function("exampleFunction")
        # ... other configuration ...
        example_permission = aws.lambda_.Permission("examplePermission",
            action="lambda:InvokeFunction",
            function=example_function.arn,
            principal="config.amazonaws.com")
        # ... other configuration ...
        example_rule = aws.cfg.Rule("exampleRule", source=aws.cfg.RuleSourceArgs(
            owner="CUSTOM_LAMBDA",
            source_identifier=example_function.arn,
        ),
        opts=pulumi.ResourceOptions(depends_on=[
                example_recorder,
                example_permission,
            ]))
        ```

        ## Import

        Config Rule can be imported using the name, e.g.

        ```sh
         $ pulumi import aws:cfg/rule:Rule foo example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the rule
        :param pulumi.Input[str] input_parameters: A string in JSON format that is passed to the AWS Config rule Lambda function.
        :param pulumi.Input[str] maximum_execution_frequency: The frequency that you want AWS Config to run evaluations for a rule that is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[pulumi.InputType['RuleScopeArgs']] scope: Scope defines which resources can trigger an evaluation for the rule as documented below.
        :param pulumi.Input[pulumi.InputType['RuleSourceArgs']] source: Source specifies the rule owner, the rule identifier, and the notifications that cause the function to evaluate your AWS resources as documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
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

            __props__['description'] = description
            __props__['input_parameters'] = input_parameters
            __props__['maximum_execution_frequency'] = maximum_execution_frequency
            __props__['name'] = name
            __props__['scope'] = scope
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__['source'] = source
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['rule_id'] = None
        super(Rule, __self__).__init__(
            'aws:cfg/rule:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            input_parameters: Optional[pulumi.Input[str]] = None,
            maximum_execution_frequency: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rule_id: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[pulumi.InputType['RuleScopeArgs']]] = None,
            source: Optional[pulumi.Input[pulumi.InputType['RuleSourceArgs']]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Rule':
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the config rule
        :param pulumi.Input[str] description: Description of the rule
        :param pulumi.Input[str] input_parameters: A string in JSON format that is passed to the AWS Config rule Lambda function.
        :param pulumi.Input[str] maximum_execution_frequency: The frequency that you want AWS Config to run evaluations for a rule that is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[str] rule_id: The ID of the config rule
        :param pulumi.Input[pulumi.InputType['RuleScopeArgs']] scope: Scope defines which resources can trigger an evaluation for the rule as documented below.
        :param pulumi.Input[pulumi.InputType['RuleSourceArgs']] source: Source specifies the rule owner, the rule identifier, and the notifications that cause the function to evaluate your AWS resources as documented below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["description"] = description
        __props__["input_parameters"] = input_parameters
        __props__["maximum_execution_frequency"] = maximum_execution_frequency
        __props__["name"] = name
        __props__["rule_id"] = rule_id
        __props__["scope"] = scope
        __props__["source"] = source
        __props__["tags"] = tags
        return Rule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the config rule
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the rule
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="inputParameters")
    def input_parameters(self) -> pulumi.Output[Optional[str]]:
        """
        A string in JSON format that is passed to the AWS Config rule Lambda function.
        """
        return pulumi.get(self, "input_parameters")

    @property
    @pulumi.getter(name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> pulumi.Output[Optional[str]]:
        """
        The frequency that you want AWS Config to run evaluations for a rule that is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        """
        return pulumi.get(self, "maximum_execution_frequency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the rule
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Output[str]:
        """
        The ID of the config rule
        """
        return pulumi.get(self, "rule_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.RuleScope']]:
        """
        Scope defines which resources can trigger an evaluation for the rule as documented below.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.RuleSource']:
        """
        Source specifies the rule owner, the rule identifier, and the notifications that cause the function to evaluate your AWS resources as documented below.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
