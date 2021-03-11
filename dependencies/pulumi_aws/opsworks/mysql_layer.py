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

__all__ = ['MysqlLayer']


class MysqlLayer(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_assign_elastic_ips: Optional[pulumi.Input[bool]] = None,
                 auto_assign_public_ips: Optional[pulumi.Input[bool]] = None,
                 auto_healing: Optional[pulumi.Input[bool]] = None,
                 custom_configure_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_deploy_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_instance_profile_arn: Optional[pulumi.Input[str]] = None,
                 custom_json: Optional[pulumi.Input[str]] = None,
                 custom_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_setup_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_shutdown_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 custom_undeploy_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 drain_elb_on_shutdown: Optional[pulumi.Input[bool]] = None,
                 ebs_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MysqlLayerEbsVolumeArgs']]]]] = None,
                 elastic_load_balancer: Optional[pulumi.Input[str]] = None,
                 install_updates_on_boot: Optional[pulumi.Input[bool]] = None,
                 instance_shutdown_timeout: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 root_password: Optional[pulumi.Input[str]] = None,
                 root_password_on_all_instances: Optional[pulumi.Input[bool]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 system_packages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 use_ebs_optimized_instances: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an OpsWorks MySQL layer resource.

        > **Note:** All arguments including the root password will be stored in the raw state as plain-text.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        db = aws.opsworks.MysqlLayer("db", stack_id=aws_opsworks_stack["main"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_assign_elastic_ips: Whether to automatically assign an elastic IP address to the layer's instances.
        :param pulumi.Input[bool] auto_assign_public_ips: For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.
        :param pulumi.Input[bool] auto_healing: Whether to enable auto-healing for the layer.
        :param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer's instances.
        :param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_security_group_ids: Ids for a set of security groups to apply to the layer's instances.
        :param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MysqlLayerEbsVolumeArgs']]]] ebs_volumes: `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.
        :param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
        :param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
        :param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
        :param pulumi.Input[str] name: A human-readable name for the layer.
        :param pulumi.Input[str] root_password: Root password to use for MySQL.
        :param pulumi.Input[bool] root_password_on_all_instances: Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
        :param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] system_packages: Names of a set of system packages to install on the layer's instances.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.
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

            __props__['auto_assign_elastic_ips'] = auto_assign_elastic_ips
            __props__['auto_assign_public_ips'] = auto_assign_public_ips
            __props__['auto_healing'] = auto_healing
            __props__['custom_configure_recipes'] = custom_configure_recipes
            __props__['custom_deploy_recipes'] = custom_deploy_recipes
            __props__['custom_instance_profile_arn'] = custom_instance_profile_arn
            __props__['custom_json'] = custom_json
            __props__['custom_security_group_ids'] = custom_security_group_ids
            __props__['custom_setup_recipes'] = custom_setup_recipes
            __props__['custom_shutdown_recipes'] = custom_shutdown_recipes
            __props__['custom_undeploy_recipes'] = custom_undeploy_recipes
            __props__['drain_elb_on_shutdown'] = drain_elb_on_shutdown
            __props__['ebs_volumes'] = ebs_volumes
            __props__['elastic_load_balancer'] = elastic_load_balancer
            __props__['install_updates_on_boot'] = install_updates_on_boot
            __props__['instance_shutdown_timeout'] = instance_shutdown_timeout
            __props__['name'] = name
            __props__['root_password'] = root_password
            __props__['root_password_on_all_instances'] = root_password_on_all_instances
            if stack_id is None and not opts.urn:
                raise TypeError("Missing required property 'stack_id'")
            __props__['stack_id'] = stack_id
            __props__['system_packages'] = system_packages
            __props__['tags'] = tags
            __props__['use_ebs_optimized_instances'] = use_ebs_optimized_instances
            __props__['arn'] = None
        super(MysqlLayer, __self__).__init__(
            'aws:opsworks/mysqlLayer:MysqlLayer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            auto_assign_elastic_ips: Optional[pulumi.Input[bool]] = None,
            auto_assign_public_ips: Optional[pulumi.Input[bool]] = None,
            auto_healing: Optional[pulumi.Input[bool]] = None,
            custom_configure_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_deploy_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_instance_profile_arn: Optional[pulumi.Input[str]] = None,
            custom_json: Optional[pulumi.Input[str]] = None,
            custom_security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_setup_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_shutdown_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            custom_undeploy_recipes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            drain_elb_on_shutdown: Optional[pulumi.Input[bool]] = None,
            ebs_volumes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MysqlLayerEbsVolumeArgs']]]]] = None,
            elastic_load_balancer: Optional[pulumi.Input[str]] = None,
            install_updates_on_boot: Optional[pulumi.Input[bool]] = None,
            instance_shutdown_timeout: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            root_password: Optional[pulumi.Input[str]] = None,
            root_password_on_all_instances: Optional[pulumi.Input[bool]] = None,
            stack_id: Optional[pulumi.Input[str]] = None,
            system_packages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            use_ebs_optimized_instances: Optional[pulumi.Input[bool]] = None) -> 'MysqlLayer':
        """
        Get an existing MysqlLayer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name(ARN) of the layer.
        :param pulumi.Input[bool] auto_assign_elastic_ips: Whether to automatically assign an elastic IP address to the layer's instances.
        :param pulumi.Input[bool] auto_assign_public_ips: For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.
        :param pulumi.Input[bool] auto_healing: Whether to enable auto-healing for the layer.
        :param pulumi.Input[str] custom_instance_profile_arn: The ARN of an IAM profile that will be used for the layer's instances.
        :param pulumi.Input[str] custom_json: Custom JSON attributes to apply to the layer.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_security_group_ids: Ids for a set of security groups to apply to the layer's instances.
        :param pulumi.Input[bool] drain_elb_on_shutdown: Whether to enable Elastic Load Balancing connection draining.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MysqlLayerEbsVolumeArgs']]]] ebs_volumes: `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.
        :param pulumi.Input[str] elastic_load_balancer: Name of an Elastic Load Balancer to attach to this layer
        :param pulumi.Input[bool] install_updates_on_boot: Whether to install OS and package updates on each instance when it boots.
        :param pulumi.Input[int] instance_shutdown_timeout: The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
        :param pulumi.Input[str] name: A human-readable name for the layer.
        :param pulumi.Input[str] root_password: Root password to use for MySQL.
        :param pulumi.Input[bool] root_password_on_all_instances: Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
        :param pulumi.Input[str] stack_id: The id of the stack the layer will belong to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] system_packages: Names of a set of system packages to install on the layer's instances.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[bool] use_ebs_optimized_instances: Whether to use EBS-optimized instances.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["auto_assign_elastic_ips"] = auto_assign_elastic_ips
        __props__["auto_assign_public_ips"] = auto_assign_public_ips
        __props__["auto_healing"] = auto_healing
        __props__["custom_configure_recipes"] = custom_configure_recipes
        __props__["custom_deploy_recipes"] = custom_deploy_recipes
        __props__["custom_instance_profile_arn"] = custom_instance_profile_arn
        __props__["custom_json"] = custom_json
        __props__["custom_security_group_ids"] = custom_security_group_ids
        __props__["custom_setup_recipes"] = custom_setup_recipes
        __props__["custom_shutdown_recipes"] = custom_shutdown_recipes
        __props__["custom_undeploy_recipes"] = custom_undeploy_recipes
        __props__["drain_elb_on_shutdown"] = drain_elb_on_shutdown
        __props__["ebs_volumes"] = ebs_volumes
        __props__["elastic_load_balancer"] = elastic_load_balancer
        __props__["install_updates_on_boot"] = install_updates_on_boot
        __props__["instance_shutdown_timeout"] = instance_shutdown_timeout
        __props__["name"] = name
        __props__["root_password"] = root_password
        __props__["root_password_on_all_instances"] = root_password_on_all_instances
        __props__["stack_id"] = stack_id
        __props__["system_packages"] = system_packages
        __props__["tags"] = tags
        __props__["use_ebs_optimized_instances"] = use_ebs_optimized_instances
        return MysqlLayer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name(ARN) of the layer.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="autoAssignElasticIps")
    def auto_assign_elastic_ips(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to automatically assign an elastic IP address to the layer's instances.
        """
        return pulumi.get(self, "auto_assign_elastic_ips")

    @property
    @pulumi.getter(name="autoAssignPublicIps")
    def auto_assign_public_ips(self) -> pulumi.Output[Optional[bool]]:
        """
        For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.
        """
        return pulumi.get(self, "auto_assign_public_ips")

    @property
    @pulumi.getter(name="autoHealing")
    def auto_healing(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable auto-healing for the layer.
        """
        return pulumi.get(self, "auto_healing")

    @property
    @pulumi.getter(name="customConfigureRecipes")
    def custom_configure_recipes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "custom_configure_recipes")

    @property
    @pulumi.getter(name="customDeployRecipes")
    def custom_deploy_recipes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "custom_deploy_recipes")

    @property
    @pulumi.getter(name="customInstanceProfileArn")
    def custom_instance_profile_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of an IAM profile that will be used for the layer's instances.
        """
        return pulumi.get(self, "custom_instance_profile_arn")

    @property
    @pulumi.getter(name="customJson")
    def custom_json(self) -> pulumi.Output[Optional[str]]:
        """
        Custom JSON attributes to apply to the layer.
        """
        return pulumi.get(self, "custom_json")

    @property
    @pulumi.getter(name="customSecurityGroupIds")
    def custom_security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Ids for a set of security groups to apply to the layer's instances.
        """
        return pulumi.get(self, "custom_security_group_ids")

    @property
    @pulumi.getter(name="customSetupRecipes")
    def custom_setup_recipes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "custom_setup_recipes")

    @property
    @pulumi.getter(name="customShutdownRecipes")
    def custom_shutdown_recipes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "custom_shutdown_recipes")

    @property
    @pulumi.getter(name="customUndeployRecipes")
    def custom_undeploy_recipes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "custom_undeploy_recipes")

    @property
    @pulumi.getter(name="drainElbOnShutdown")
    def drain_elb_on_shutdown(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable Elastic Load Balancing connection draining.
        """
        return pulumi.get(self, "drain_elb_on_shutdown")

    @property
    @pulumi.getter(name="ebsVolumes")
    def ebs_volumes(self) -> pulumi.Output[Optional[Sequence['outputs.MysqlLayerEbsVolume']]]:
        """
        `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.
        """
        return pulumi.get(self, "ebs_volumes")

    @property
    @pulumi.getter(name="elasticLoadBalancer")
    def elastic_load_balancer(self) -> pulumi.Output[Optional[str]]:
        """
        Name of an Elastic Load Balancer to attach to this layer
        """
        return pulumi.get(self, "elastic_load_balancer")

    @property
    @pulumi.getter(name="installUpdatesOnBoot")
    def install_updates_on_boot(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to install OS and package updates on each instance when it boots.
        """
        return pulumi.get(self, "install_updates_on_boot")

    @property
    @pulumi.getter(name="instanceShutdownTimeout")
    def instance_shutdown_timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
        """
        return pulumi.get(self, "instance_shutdown_timeout")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A human-readable name for the layer.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rootPassword")
    def root_password(self) -> pulumi.Output[Optional[str]]:
        """
        Root password to use for MySQL.
        """
        return pulumi.get(self, "root_password")

    @property
    @pulumi.getter(name="rootPasswordOnAllInstances")
    def root_password_on_all_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
        """
        return pulumi.get(self, "root_password_on_all_instances")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        """
        The id of the stack the layer will belong to.
        """
        return pulumi.get(self, "stack_id")

    @property
    @pulumi.getter(name="systemPackages")
    def system_packages(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Names of a set of system packages to install on the layer's instances.
        """
        return pulumi.get(self, "system_packages")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useEbsOptimizedInstances")
    def use_ebs_optimized_instances(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to use EBS-optimized instances.
        """
        return pulumi.get(self, "use_ebs_optimized_instances")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
