# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['StackSetInstance']


class StackSetInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 retain_stack: Optional[pulumi.Input[bool]] = None,
                 stack_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a CloudFormation StackSet Instance. Instances are managed in the account and region of the StackSet after the target account permissions have been configured. Additional information about StackSets can be found in the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).

        > **NOTE:** All target accounts must have an IAM Role created that matches the name of the execution role configured in the StackSet (the `execution_role_name` argument in the `cloudformation.StackSet` resource) in a trust relationship with the administrative account or administration IAM Role. The execution role must have appropriate permissions to manage resources defined in the template along with those required for StackSets to operate. See the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html) for more details.

        > **NOTE:** To retain the Stack during resource destroy, ensure `retain_stack` has been set to `true` in the state first. This must be completed _before_ a deployment that would destroy the resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.cloudformation.StackSetInstance("example",
            account_id="123456789012",
            region="us-east-1",
            stack_set_name=aws_cloudformation_stack_set["example"]["name"])
        ```
        ### Example IAM Setup in Target Account

        ```python
        import pulumi
        import pulumi_aws as aws

        a_ws_cloud_formation_stack_set_execution_role_assume_role_policy = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            effect="Allow",
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                identifiers=[aws_iam_role["AWSCloudFormationStackSetAdministrationRole"]["arn"]],
                type="AWS",
            )],
        )])
        a_ws_cloud_formation_stack_set_execution_role = aws.iam.Role("aWSCloudFormationStackSetExecutionRole", assume_role_policy=a_ws_cloud_formation_stack_set_execution_role_assume_role_policy.json)
        a_ws_cloud_formation_stack_set_execution_role_minimum_execution_policy_policy_document = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=[
                "cloudformation:*",
                "s3:*",
                "sns:*",
            ],
            effect="Allow",
            resources=["*"],
        )])
        a_ws_cloud_formation_stack_set_execution_role_minimum_execution_policy_role_policy = aws.iam.RolePolicy("aWSCloudFormationStackSetExecutionRoleMinimumExecutionPolicyRolePolicy",
            policy=a_ws_cloud_formation_stack_set_execution_role_minimum_execution_policy_policy_document.json,
            role=a_ws_cloud_formation_stack_set_execution_role.name)
        ```

        ## Import

        CloudFormation StackSet Instances can be imported using the StackSet name, target AWS account ID, and target AWS region separated by commas (`,`) e.g.

        ```sh
         $ pulumi import aws:cloudformation/stackSetInstance:StackSetInstance example example,123456789012,us-east-1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameter_overrides: Key-value map of input parameters to override from the StackSet for this Instance.
        :param pulumi.Input[str] region: Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
        :param pulumi.Input[bool] retain_stack: During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
        :param pulumi.Input[str] stack_set_name: Name of the StackSet.
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

            __props__['account_id'] = account_id
            __props__['parameter_overrides'] = parameter_overrides
            __props__['region'] = region
            __props__['retain_stack'] = retain_stack
            if stack_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'stack_set_name'")
            __props__['stack_set_name'] = stack_set_name
            __props__['stack_id'] = None
        super(StackSetInstance, __self__).__init__(
            'aws:cloudformation/stackSetInstance:StackSetInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            parameter_overrides: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            retain_stack: Optional[pulumi.Input[bool]] = None,
            stack_id: Optional[pulumi.Input[str]] = None,
            stack_set_name: Optional[pulumi.Input[str]] = None) -> 'StackSetInstance':
        """
        Get an existing StackSetInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameter_overrides: Key-value map of input parameters to override from the StackSet for this Instance.
        :param pulumi.Input[str] region: Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
        :param pulumi.Input[bool] retain_stack: During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
        :param pulumi.Input[str] stack_id: Stack identifier
        :param pulumi.Input[str] stack_set_name: Name of the StackSet.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["account_id"] = account_id
        __props__["parameter_overrides"] = parameter_overrides
        __props__["region"] = region
        __props__["retain_stack"] = retain_stack
        __props__["stack_id"] = stack_id
        __props__["stack_set_name"] = stack_set_name
        return StackSetInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Target AWS Account ID to create a Stack based on the StackSet. Defaults to current account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="parameterOverrides")
    def parameter_overrides(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of input parameters to override from the StackSet for this Instance.
        """
        return pulumi.get(self, "parameter_overrides")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Target AWS Region to create a Stack based on the StackSet. Defaults to current region.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="retainStack")
    def retain_stack(self) -> pulumi.Output[Optional[bool]]:
        """
        During resource destroy, remove Instance from StackSet while keeping the Stack and its associated resources. Must be enabled in the state _before_ destroy operation to take effect. You cannot reassociate a retained Stack or add an existing, saved Stack to a new StackSet. Defaults to `false`.
        """
        return pulumi.get(self, "retain_stack")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        """
        Stack identifier
        """
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter(name="stackSetName")
    def stack_set_name(self) -> pulumi.Output[str]:
        """
        Name of the StackSet.
        """
        return pulumi.get(self, "stack_set_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
