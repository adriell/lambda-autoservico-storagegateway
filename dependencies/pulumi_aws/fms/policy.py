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

__all__ = ['Policy']


class Policy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_all_policy_resources: Optional[pulumi.Input[bool]] = None,
                 exclude_map: Optional[pulumi.Input[pulumi.InputType['PolicyExcludeMapArgs']]] = None,
                 exclude_resource_tags: Optional[pulumi.Input[bool]] = None,
                 include_map: Optional[pulumi.Input[pulumi.InputType['PolicyIncludeMapArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 remediation_enabled: Optional[pulumi.Input[bool]] = None,
                 resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 security_service_policy_data: Optional[pulumi.Input[pulumi.InputType['PolicySecurityServicePolicyDataArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to create an AWS Firewall Manager policy. You need to be using AWS organizations and have enabled the Firewall Manager administrator account.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example_rule_group = aws.wafregional.RuleGroup("exampleRuleGroup", metric_name="WAFRuleGroupExample")
        example_policy = aws.fms.Policy("examplePolicy",
            exclude_resource_tags=False,
            remediation_enabled=False,
            resource_type_lists=["AWS::ElasticLoadBalancingV2::LoadBalancer"],
            security_service_policy_data=aws.fms.PolicySecurityServicePolicyDataArgs(
                type="WAF",
                managed_service_data=example_rule_group.id.apply(lambda id: json.dumps({
                    "type": "WAF",
                    "ruleGroups": [{
                        "id": id,
                        "overrideAction": {
                            "type": "COUNT",
                        },
                    }],
                    "defaultAction": {
                        "type": "BLOCK",
                    },
                    "overrideCustomerWebACLAssociation": False,
                })),
            ))
        ```

        ## Import

        Firewall Manager policies can be imported using the policy ID, e.g.

        ```sh
         $ pulumi import aws:fms/policy:Policy example 5be49585-a7e3-4c49-dde1-a179fe4a619a
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_all_policy_resources: If true, the request will also perform a clean-up process. Defaults to `true`. More information can be found here [AWS Firewall Manager delete policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html)
        :param pulumi.Input[pulumi.InputType['PolicyExcludeMapArgs']] exclude_map: A map of lists, with a single key named 'account' with a list of AWS Account IDs to exclude from this policy.
        :param pulumi.Input[bool] exclude_resource_tags: A boolean value, if true the tags that are specified in the `resource_tags` are not protected by this policy. If set to false and resource_tags are populated, resources that contain tags will be protected by this policy.
        :param pulumi.Input[pulumi.InputType['PolicyIncludeMapArgs']] include_map: A map of lists, with a single key named 'account' with a list of AWS Account IDs to include for this policy.
        :param pulumi.Input[str] name: The friendly name of the AWS Firewall Manager Policy.
        :param pulumi.Input[bool] remediation_enabled: A boolean value, indicates if the policy should automatically applied to resources that already exist in the account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] resource_tags: A map of resource tags, that if present will filter protections on resources based on the exclude_resource_tags.
        :param pulumi.Input[str] resource_type: A resource type to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`. Conflicts with `resource_type_list`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_type_lists: A list of resource types to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, and `AWS::EC2::VPC`. Conflicts with `resource_type`.
        :param pulumi.Input[pulumi.InputType['PolicySecurityServicePolicyDataArgs']] security_service_policy_data: The objects to include in Security Service Policy Data. Documented below.
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

            __props__['delete_all_policy_resources'] = delete_all_policy_resources
            __props__['exclude_map'] = exclude_map
            if exclude_resource_tags is None and not opts.urn:
                raise TypeError("Missing required property 'exclude_resource_tags'")
            __props__['exclude_resource_tags'] = exclude_resource_tags
            __props__['include_map'] = include_map
            __props__['name'] = name
            __props__['remediation_enabled'] = remediation_enabled
            __props__['resource_tags'] = resource_tags
            __props__['resource_type'] = resource_type
            __props__['resource_type_lists'] = resource_type_lists
            if security_service_policy_data is None and not opts.urn:
                raise TypeError("Missing required property 'security_service_policy_data'")
            __props__['security_service_policy_data'] = security_service_policy_data
            __props__['arn'] = None
            __props__['policy_update_token'] = None
        super(Policy, __self__).__init__(
            'aws:fms/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            delete_all_policy_resources: Optional[pulumi.Input[bool]] = None,
            exclude_map: Optional[pulumi.Input[pulumi.InputType['PolicyExcludeMapArgs']]] = None,
            exclude_resource_tags: Optional[pulumi.Input[bool]] = None,
            include_map: Optional[pulumi.Input[pulumi.InputType['PolicyIncludeMapArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_update_token: Optional[pulumi.Input[str]] = None,
            remediation_enabled: Optional[pulumi.Input[bool]] = None,
            resource_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            resource_type: Optional[pulumi.Input[str]] = None,
            resource_type_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            security_service_policy_data: Optional[pulumi.Input[pulumi.InputType['PolicySecurityServicePolicyDataArgs']]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_all_policy_resources: If true, the request will also perform a clean-up process. Defaults to `true`. More information can be found here [AWS Firewall Manager delete policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html)
        :param pulumi.Input[pulumi.InputType['PolicyExcludeMapArgs']] exclude_map: A map of lists, with a single key named 'account' with a list of AWS Account IDs to exclude from this policy.
        :param pulumi.Input[bool] exclude_resource_tags: A boolean value, if true the tags that are specified in the `resource_tags` are not protected by this policy. If set to false and resource_tags are populated, resources that contain tags will be protected by this policy.
        :param pulumi.Input[pulumi.InputType['PolicyIncludeMapArgs']] include_map: A map of lists, with a single key named 'account' with a list of AWS Account IDs to include for this policy.
        :param pulumi.Input[str] name: The friendly name of the AWS Firewall Manager Policy.
        :param pulumi.Input[str] policy_update_token: A unique identifier for each update to the policy.
        :param pulumi.Input[bool] remediation_enabled: A boolean value, indicates if the policy should automatically applied to resources that already exist in the account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] resource_tags: A map of resource tags, that if present will filter protections on resources based on the exclude_resource_tags.
        :param pulumi.Input[str] resource_type: A resource type to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`. Conflicts with `resource_type_list`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_type_lists: A list of resource types to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, and `AWS::EC2::VPC`. Conflicts with `resource_type`.
        :param pulumi.Input[pulumi.InputType['PolicySecurityServicePolicyDataArgs']] security_service_policy_data: The objects to include in Security Service Policy Data. Documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["delete_all_policy_resources"] = delete_all_policy_resources
        __props__["exclude_map"] = exclude_map
        __props__["exclude_resource_tags"] = exclude_resource_tags
        __props__["include_map"] = include_map
        __props__["name"] = name
        __props__["policy_update_token"] = policy_update_token
        __props__["remediation_enabled"] = remediation_enabled
        __props__["resource_tags"] = resource_tags
        __props__["resource_type"] = resource_type
        __props__["resource_type_lists"] = resource_type_lists
        __props__["security_service_policy_data"] = security_service_policy_data
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deleteAllPolicyResources")
    def delete_all_policy_resources(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, the request will also perform a clean-up process. Defaults to `true`. More information can be found here [AWS Firewall Manager delete policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html)
        """
        return pulumi.get(self, "delete_all_policy_resources")

    @property
    @pulumi.getter(name="excludeMap")
    def exclude_map(self) -> pulumi.Output[Optional['outputs.PolicyExcludeMap']]:
        """
        A map of lists, with a single key named 'account' with a list of AWS Account IDs to exclude from this policy.
        """
        return pulumi.get(self, "exclude_map")

    @property
    @pulumi.getter(name="excludeResourceTags")
    def exclude_resource_tags(self) -> pulumi.Output[bool]:
        """
        A boolean value, if true the tags that are specified in the `resource_tags` are not protected by this policy. If set to false and resource_tags are populated, resources that contain tags will be protected by this policy.
        """
        return pulumi.get(self, "exclude_resource_tags")

    @property
    @pulumi.getter(name="includeMap")
    def include_map(self) -> pulumi.Output[Optional['outputs.PolicyIncludeMap']]:
        """
        A map of lists, with a single key named 'account' with a list of AWS Account IDs to include for this policy.
        """
        return pulumi.get(self, "include_map")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The friendly name of the AWS Firewall Manager Policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyUpdateToken")
    def policy_update_token(self) -> pulumi.Output[str]:
        """
        A unique identifier for each update to the policy.
        """
        return pulumi.get(self, "policy_update_token")

    @property
    @pulumi.getter(name="remediationEnabled")
    def remediation_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean value, indicates if the policy should automatically applied to resources that already exist in the account.
        """
        return pulumi.get(self, "remediation_enabled")

    @property
    @pulumi.getter(name="resourceTags")
    def resource_tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of resource tags, that if present will filter protections on resources based on the exclude_resource_tags.
        """
        return pulumi.get(self, "resource_tags")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        A resource type to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`. Conflicts with `resource_type_list`.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter(name="resourceTypeLists")
    def resource_type_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of resource types to protect, valid values are: `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, and `AWS::EC2::VPC`. Conflicts with `resource_type`.
        """
        return pulumi.get(self, "resource_type_lists")

    @property
    @pulumi.getter(name="securityServicePolicyData")
    def security_service_policy_data(self) -> pulumi.Output['outputs.PolicySecurityServicePolicyData']:
        """
        The objects to include in Security Service Policy Data. Documented below.
        """
        return pulumi.get(self, "security_service_policy_data")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

