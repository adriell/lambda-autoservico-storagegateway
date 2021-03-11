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

__all__ = ['ResolverEndpoint']


class ResolverEndpoint(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Route 53 Resolver endpoint resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo = aws.route53.ResolverEndpoint("foo",
            direction="INBOUND",
            security_group_ids=[
                aws_security_group["sg1"]["id"],
                aws_security_group["sg2"]["id"],
            ],
            ip_addresses=[
                aws.route53.ResolverEndpointIpAddressArgs(
                    subnet_id=aws_subnet["sn1"]["id"],
                ),
                aws.route53.ResolverEndpointIpAddressArgs(
                    subnet_id=aws_subnet["sn2"]["id"],
                    ip="10.0.64.4",
                ),
            ],
            tags={
                "Environment": "Prod",
            })
        ```

        ## Import

         Route 53 Resolver endpoints can be imported using the Route 53 Resolver endpoint ID, e.g.

        ```sh
         $ pulumi import aws:route53/resolverEndpoint:ResolverEndpoint foo rslvr-in-abcdef01234567890
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] direction: The direction of DNS queries to or from the Route 53 Resolver endpoint.
               Valid values are `INBOUND` (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
               or `OUTBOUND` (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressArgs']]]] ip_addresses: The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
               to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.
        :param pulumi.Input[str] name: The friendly name of the Route 53 Resolver endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The ID of one or more security groups that you want to use to control access to this VPC.
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

            if direction is None and not opts.urn:
                raise TypeError("Missing required property 'direction'")
            __props__['direction'] = direction
            if ip_addresses is None and not opts.urn:
                raise TypeError("Missing required property 'ip_addresses'")
            __props__['ip_addresses'] = ip_addresses
            __props__['name'] = name
            if security_group_ids is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__['security_group_ids'] = security_group_ids
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['host_vpc_id'] = None
        super(ResolverEndpoint, __self__).__init__(
            'aws:route53/resolverEndpoint:ResolverEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            host_vpc_id: Optional[pulumi.Input[str]] = None,
            ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ResolverEndpoint':
        """
        Get an existing ResolverEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Route 53 Resolver endpoint.
        :param pulumi.Input[str] direction: The direction of DNS queries to or from the Route 53 Resolver endpoint.
               Valid values are `INBOUND` (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
               or `OUTBOUND` (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).
        :param pulumi.Input[str] host_vpc_id: The ID of the VPC that you want to create the resolver endpoint in.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResolverEndpointIpAddressArgs']]]] ip_addresses: The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
               to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.
        :param pulumi.Input[str] name: The friendly name of the Route 53 Resolver endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The ID of one or more security groups that you want to use to control access to this VPC.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["direction"] = direction
        __props__["host_vpc_id"] = host_vpc_id
        __props__["ip_addresses"] = ip_addresses
        __props__["name"] = name
        __props__["security_group_ids"] = security_group_ids
        __props__["tags"] = tags
        return ResolverEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Route 53 Resolver endpoint.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        The direction of DNS queries to or from the Route 53 Resolver endpoint.
        Valid values are `INBOUND` (resolver forwards DNS queries to the DNS service for a VPC from your network or another VPC)
        or `OUTBOUND` (resolver forwards DNS queries from the DNS service for a VPC to your network or another VPC).
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="hostVpcId")
    def host_vpc_id(self) -> pulumi.Output[str]:
        """
        The ID of the VPC that you want to create the resolver endpoint in.
        """
        return pulumi.get(self, "host_vpc_id")

    @property
    @pulumi.getter(name="ipAddresses")
    def ip_addresses(self) -> pulumi.Output[Sequence['outputs.ResolverEndpointIpAddress']]:
        """
        The subnets and IP addresses in your VPC that you want DNS queries to pass through on the way from your VPCs
        to your network (for outbound endpoints) or on the way from your network to your VPCs (for inbound endpoints). Described below.
        """
        return pulumi.get(self, "ip_addresses")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The friendly name of the Route 53 Resolver endpoint.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The ID of one or more security groups that you want to use to control access to this VPC.
        """
        return pulumi.get(self, "security_group_ids")

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
