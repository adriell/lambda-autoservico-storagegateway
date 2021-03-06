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

__all__ = ['Stack']


class Stack(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_version: Optional[pulumi.Input[str]] = None,
                 berkshelf_version: Optional[pulumi.Input[str]] = None,
                 color: Optional[pulumi.Input[str]] = None,
                 configuration_manager_name: Optional[pulumi.Input[str]] = None,
                 configuration_manager_version: Optional[pulumi.Input[str]] = None,
                 custom_cookbooks_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackCustomCookbooksSourceArgs']]]]] = None,
                 custom_json: Optional[pulumi.Input[str]] = None,
                 default_availability_zone: Optional[pulumi.Input[str]] = None,
                 default_instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 default_os: Optional[pulumi.Input[str]] = None,
                 default_root_device_type: Optional[pulumi.Input[str]] = None,
                 default_ssh_key_name: Optional[pulumi.Input[str]] = None,
                 default_subnet_id: Optional[pulumi.Input[str]] = None,
                 hostname_theme: Optional[pulumi.Input[str]] = None,
                 manage_berkshelf: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 service_role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_custom_cookbooks: Optional[pulumi.Input[bool]] = None,
                 use_opsworks_security_groups: Optional[pulumi.Input[bool]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an OpsWorks stack resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        main = aws.opsworks.Stack("main",
            region="us-west-1",
            service_role_arn=aws_iam_role["opsworks"]["arn"],
            default_instance_profile_arn=aws_iam_instance_profile["opsworks"]["arn"],
            tags={
                "Name": "foobar-stack",
            },
            custom_json=\"\"\"{
         "foobar": {
            "version": "1.0.0"
          }
        }
        \"\"\")
        ```

        ## Import

        OpsWorks stacks can be imported using the `id`, e.g.

        ```sh
         $ pulumi import aws:opsworks/stack:Stack bar 00000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_version: If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        :param pulumi.Input[str] berkshelf_version: If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        :param pulumi.Input[str] color: Color to paint next to the stack's resources in the OpsWorks console.
        :param pulumi.Input[str] configuration_manager_name: Name of the configuration manager to use. Defaults to "Chef".
        :param pulumi.Input[str] configuration_manager_version: Version of the configuration manager to use. Defaults to "11.4".
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackCustomCookbooksSourceArgs']]]] custom_cookbooks_sources: When `use_custom_cookbooks` is set, provide this sub-object as
               described below.
        :param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the entire stack.
        :param pulumi.Input[str] default_availability_zone: Name of the availability zone where instances will be created
               by default. This is required unless you set `vpc_id`.
        :param pulumi.Input[str] default_instance_profile_arn: The ARN of an IAM Instance Profile that created instances
               will have by default.
        :param pulumi.Input[str] default_os: Name of OS that will be installed on instances by default.
        :param pulumi.Input[str] default_root_device_type: Name of the type of root device instances will have by default.
        :param pulumi.Input[str] default_ssh_key_name: Name of the SSH keypair that instances will have by default.
        :param pulumi.Input[str] default_subnet_id: Id of the subnet in which instances will be created by default. Mandatory
               if `vpc_id` is set, and forbidden if it isn't.
        :param pulumi.Input[str] hostname_theme: Keyword representing the naming scheme that will be used for instance hostnames
               within this stack.
        :param pulumi.Input[bool] manage_berkshelf: Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        :param pulumi.Input[str] name: The name of the stack.
        :param pulumi.Input[str] region: The name of the region where the stack will exist.
        :param pulumi.Input[str] service_role_arn: The ARN of an IAM role that the OpsWorks service will act as.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[bool] use_custom_cookbooks: Boolean value controlling whether the custom cookbook settings are
               enabled.
        :param pulumi.Input[bool] use_opsworks_security_groups: Boolean value controlling whether the standard OpsWorks
               security groups apply to created instances.
        :param pulumi.Input[str] vpc_id: The id of the VPC that this stack belongs to.
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

            __props__['agent_version'] = agent_version
            __props__['berkshelf_version'] = berkshelf_version
            __props__['color'] = color
            __props__['configuration_manager_name'] = configuration_manager_name
            __props__['configuration_manager_version'] = configuration_manager_version
            __props__['custom_cookbooks_sources'] = custom_cookbooks_sources
            __props__['custom_json'] = custom_json
            __props__['default_availability_zone'] = default_availability_zone
            if default_instance_profile_arn is None and not opts.urn:
                raise TypeError("Missing required property 'default_instance_profile_arn'")
            __props__['default_instance_profile_arn'] = default_instance_profile_arn
            __props__['default_os'] = default_os
            __props__['default_root_device_type'] = default_root_device_type
            __props__['default_ssh_key_name'] = default_ssh_key_name
            __props__['default_subnet_id'] = default_subnet_id
            __props__['hostname_theme'] = hostname_theme
            __props__['manage_berkshelf'] = manage_berkshelf
            __props__['name'] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__['region'] = region
            if service_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'service_role_arn'")
            __props__['service_role_arn'] = service_role_arn
            __props__['tags'] = tags
            __props__['use_custom_cookbooks'] = use_custom_cookbooks
            __props__['use_opsworks_security_groups'] = use_opsworks_security_groups
            __props__['vpc_id'] = vpc_id
            __props__['arn'] = None
            __props__['stack_endpoint'] = None
        super(Stack, __self__).__init__(
            'aws:opsworks/stack:Stack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_version: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            berkshelf_version: Optional[pulumi.Input[str]] = None,
            color: Optional[pulumi.Input[str]] = None,
            configuration_manager_name: Optional[pulumi.Input[str]] = None,
            configuration_manager_version: Optional[pulumi.Input[str]] = None,
            custom_cookbooks_sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackCustomCookbooksSourceArgs']]]]] = None,
            custom_json: Optional[pulumi.Input[str]] = None,
            default_availability_zone: Optional[pulumi.Input[str]] = None,
            default_instance_profile_arn: Optional[pulumi.Input[str]] = None,
            default_os: Optional[pulumi.Input[str]] = None,
            default_root_device_type: Optional[pulumi.Input[str]] = None,
            default_ssh_key_name: Optional[pulumi.Input[str]] = None,
            default_subnet_id: Optional[pulumi.Input[str]] = None,
            hostname_theme: Optional[pulumi.Input[str]] = None,
            manage_berkshelf: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            service_role_arn: Optional[pulumi.Input[str]] = None,
            stack_endpoint: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            use_custom_cookbooks: Optional[pulumi.Input[bool]] = None,
            use_opsworks_security_groups: Optional[pulumi.Input[bool]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'Stack':
        """
        Get an existing Stack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_version: If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        :param pulumi.Input[str] berkshelf_version: If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        :param pulumi.Input[str] color: Color to paint next to the stack's resources in the OpsWorks console.
        :param pulumi.Input[str] configuration_manager_name: Name of the configuration manager to use. Defaults to "Chef".
        :param pulumi.Input[str] configuration_manager_version: Version of the configuration manager to use. Defaults to "11.4".
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StackCustomCookbooksSourceArgs']]]] custom_cookbooks_sources: When `use_custom_cookbooks` is set, provide this sub-object as
               described below.
        :param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the entire stack.
        :param pulumi.Input[str] default_availability_zone: Name of the availability zone where instances will be created
               by default. This is required unless you set `vpc_id`.
        :param pulumi.Input[str] default_instance_profile_arn: The ARN of an IAM Instance Profile that created instances
               will have by default.
        :param pulumi.Input[str] default_os: Name of OS that will be installed on instances by default.
        :param pulumi.Input[str] default_root_device_type: Name of the type of root device instances will have by default.
        :param pulumi.Input[str] default_ssh_key_name: Name of the SSH keypair that instances will have by default.
        :param pulumi.Input[str] default_subnet_id: Id of the subnet in which instances will be created by default. Mandatory
               if `vpc_id` is set, and forbidden if it isn't.
        :param pulumi.Input[str] hostname_theme: Keyword representing the naming scheme that will be used for instance hostnames
               within this stack.
        :param pulumi.Input[bool] manage_berkshelf: Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        :param pulumi.Input[str] name: The name of the stack.
        :param pulumi.Input[str] region: The name of the region where the stack will exist.
        :param pulumi.Input[str] service_role_arn: The ARN of an IAM role that the OpsWorks service will act as.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[bool] use_custom_cookbooks: Boolean value controlling whether the custom cookbook settings are
               enabled.
        :param pulumi.Input[bool] use_opsworks_security_groups: Boolean value controlling whether the standard OpsWorks
               security groups apply to created instances.
        :param pulumi.Input[str] vpc_id: The id of the VPC that this stack belongs to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["agent_version"] = agent_version
        __props__["arn"] = arn
        __props__["berkshelf_version"] = berkshelf_version
        __props__["color"] = color
        __props__["configuration_manager_name"] = configuration_manager_name
        __props__["configuration_manager_version"] = configuration_manager_version
        __props__["custom_cookbooks_sources"] = custom_cookbooks_sources
        __props__["custom_json"] = custom_json
        __props__["default_availability_zone"] = default_availability_zone
        __props__["default_instance_profile_arn"] = default_instance_profile_arn
        __props__["default_os"] = default_os
        __props__["default_root_device_type"] = default_root_device_type
        __props__["default_ssh_key_name"] = default_ssh_key_name
        __props__["default_subnet_id"] = default_subnet_id
        __props__["hostname_theme"] = hostname_theme
        __props__["manage_berkshelf"] = manage_berkshelf
        __props__["name"] = name
        __props__["region"] = region
        __props__["service_role_arn"] = service_role_arn
        __props__["stack_endpoint"] = stack_endpoint
        __props__["tags"] = tags
        __props__["use_custom_cookbooks"] = use_custom_cookbooks
        __props__["use_opsworks_security_groups"] = use_opsworks_security_groups
        __props__["vpc_id"] = vpc_id
        return Stack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[str]:
        """
        If set to `"LATEST"`, OpsWorks will automatically install the latest version.
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="berkshelfVersion")
    def berkshelf_version(self) -> pulumi.Output[Optional[str]]:
        """
        If `manage_berkshelf` is enabled, the version of Berkshelf to use.
        """
        return pulumi.get(self, "berkshelf_version")

    @property
    @pulumi.getter
    def color(self) -> pulumi.Output[Optional[str]]:
        """
        Color to paint next to the stack's resources in the OpsWorks console.
        """
        return pulumi.get(self, "color")

    @property
    @pulumi.getter(name="configurationManagerName")
    def configuration_manager_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the configuration manager to use. Defaults to "Chef".
        """
        return pulumi.get(self, "configuration_manager_name")

    @property
    @pulumi.getter(name="configurationManagerVersion")
    def configuration_manager_version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of the configuration manager to use. Defaults to "11.4".
        """
        return pulumi.get(self, "configuration_manager_version")

    @property
    @pulumi.getter(name="customCookbooksSources")
    def custom_cookbooks_sources(self) -> pulumi.Output[Sequence['outputs.StackCustomCookbooksSource']]:
        """
        When `use_custom_cookbooks` is set, provide this sub-object as
        described below.
        """
        return pulumi.get(self, "custom_cookbooks_sources")

    @property
    @pulumi.getter(name="customJson")
    def custom_json(self) -> pulumi.Output[Optional[str]]:
        """
        Custom JSON attributes to apply to the entire stack.
        """
        return pulumi.get(self, "custom_json")

    @property
    @pulumi.getter(name="defaultAvailabilityZone")
    def default_availability_zone(self) -> pulumi.Output[str]:
        """
        Name of the availability zone where instances will be created
        by default. This is required unless you set `vpc_id`.
        """
        return pulumi.get(self, "default_availability_zone")

    @property
    @pulumi.getter(name="defaultInstanceProfileArn")
    def default_instance_profile_arn(self) -> pulumi.Output[str]:
        """
        The ARN of an IAM Instance Profile that created instances
        will have by default.
        """
        return pulumi.get(self, "default_instance_profile_arn")

    @property
    @pulumi.getter(name="defaultOs")
    def default_os(self) -> pulumi.Output[Optional[str]]:
        """
        Name of OS that will be installed on instances by default.
        """
        return pulumi.get(self, "default_os")

    @property
    @pulumi.getter(name="defaultRootDeviceType")
    def default_root_device_type(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the type of root device instances will have by default.
        """
        return pulumi.get(self, "default_root_device_type")

    @property
    @pulumi.getter(name="defaultSshKeyName")
    def default_ssh_key_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the SSH keypair that instances will have by default.
        """
        return pulumi.get(self, "default_ssh_key_name")

    @property
    @pulumi.getter(name="defaultSubnetId")
    def default_subnet_id(self) -> pulumi.Output[str]:
        """
        Id of the subnet in which instances will be created by default. Mandatory
        if `vpc_id` is set, and forbidden if it isn't.
        """
        return pulumi.get(self, "default_subnet_id")

    @property
    @pulumi.getter(name="hostnameTheme")
    def hostname_theme(self) -> pulumi.Output[Optional[str]]:
        """
        Keyword representing the naming scheme that will be used for instance hostnames
        within this stack.
        """
        return pulumi.get(self, "hostname_theme")

    @property
    @pulumi.getter(name="manageBerkshelf")
    def manage_berkshelf(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value controlling whether Opsworks will run Berkshelf for this stack.
        """
        return pulumi.get(self, "manage_berkshelf")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the stack.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The name of the region where the stack will exist.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="serviceRoleArn")
    def service_role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of an IAM role that the OpsWorks service will act as.
        """
        return pulumi.get(self, "service_role_arn")

    @property
    @pulumi.getter(name="stackEndpoint")
    def stack_endpoint(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_endpoint")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useCustomCookbooks")
    def use_custom_cookbooks(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value controlling whether the custom cookbook settings are
        enabled.
        """
        return pulumi.get(self, "use_custom_cookbooks")

    @property
    @pulumi.getter(name="useOpsworksSecurityGroups")
    def use_opsworks_security_groups(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value controlling whether the standard OpsWorks
        security groups apply to created instances.
        """
        return pulumi.get(self, "use_opsworks_security_groups")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        The id of the VPC that this stack belongs to.
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

