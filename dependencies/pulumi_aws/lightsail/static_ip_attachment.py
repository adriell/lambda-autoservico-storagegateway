# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['StaticIpAttachment']


class StaticIpAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 static_ip_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a static IP address attachment - relationship between a Lightsail static IP & Lightsail instance.

        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_static_ip = aws.lightsail.StaticIp("testStaticIp")
        test_instance = aws.lightsail.Instance("testInstance",
            availability_zone="us-east-1b",
            blueprint_id="string",
            bundle_id="string",
            key_pair_name="some_key_name")
        test_static_ip_attachment = aws.lightsail.StaticIpAttachment("testStaticIpAttachment",
            static_ip_name=test_static_ip.id,
            instance_name=test_instance.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: The name of the Lightsail instance to attach the IP to
        :param pulumi.Input[str] static_ip_name: The name of the allocated static IP
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

            if instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_name'")
            __props__['instance_name'] = instance_name
            if static_ip_name is None and not opts.urn:
                raise TypeError("Missing required property 'static_ip_name'")
            __props__['static_ip_name'] = static_ip_name
            __props__['ip_address'] = None
        super(StaticIpAttachment, __self__).__init__(
            'aws:lightsail/staticIpAttachment:StaticIpAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            static_ip_name: Optional[pulumi.Input[str]] = None) -> 'StaticIpAttachment':
        """
        Get an existing StaticIpAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_name: The name of the Lightsail instance to attach the IP to
        :param pulumi.Input[str] ip_address: The allocated static IP address
        :param pulumi.Input[str] static_ip_name: The name of the allocated static IP
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["instance_name"] = instance_name
        __props__["ip_address"] = ip_address
        __props__["static_ip_name"] = static_ip_name
        return StaticIpAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The name of the Lightsail instance to attach the IP to
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The allocated static IP address
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="staticIpName")
    def static_ip_name(self) -> pulumi.Output[str]:
        """
        The name of the allocated static IP
        """
        return pulumi.get(self, "static_ip_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
