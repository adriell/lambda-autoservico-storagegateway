# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['DefaultSubnet']


class DefaultSubnet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 customer_owned_ipv4_pool: Optional[pulumi.Input[str]] = None,
                 map_customer_owned_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
                 outpost_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to manage a [default AWS VPC subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html#default-vpc-basics) in the current region.

        The `ec2.DefaultSubnet` behaves differently from normal resources, in that this provider does not _create_ this resource but instead "adopts" it into management.

        The `ec2.DefaultSubnet` resource allows you to manage a region's default VPC subnet but this provider cannot destroy it. Removing this resource from your configuration will remove it from your statefile and the provider management.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        default_az1 = aws.ec2.DefaultSubnet("defaultAz1",
            availability_zone="us-west-2a",
            tags={
                "Name": "Default subnet for us-west-2a",
            })
        ```

        ## Import

        Subnets can be imported using the `subnet id`, e.g.

        ```sh
         $ pulumi import aws:ec2/defaultSubnet:DefaultSubnet public_subnet subnet-9d4a7b6c
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone: AZ for the subnet.
        :param pulumi.Input[bool] map_public_ip_on_launch: Whether instances launched into the subnet should be assigned a public IP address.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource.
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

            if availability_zone is None and not opts.urn:
                raise TypeError("Missing required property 'availability_zone'")
            __props__['availability_zone'] = availability_zone
            __props__['customer_owned_ipv4_pool'] = customer_owned_ipv4_pool
            __props__['map_customer_owned_ip_on_launch'] = map_customer_owned_ip_on_launch
            __props__['map_public_ip_on_launch'] = map_public_ip_on_launch
            __props__['outpost_arn'] = outpost_arn
            __props__['tags'] = tags
            __props__['arn'] = None
            __props__['assign_ipv6_address_on_creation'] = None
            __props__['availability_zone_id'] = None
            __props__['cidr_block'] = None
            __props__['ipv6_cidr_block'] = None
            __props__['ipv6_cidr_block_association_id'] = None
            __props__['owner_id'] = None
            __props__['vpc_id'] = None
        super(DefaultSubnet, __self__).__init__(
            'aws:ec2/defaultSubnet:DefaultSubnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            assign_ipv6_address_on_creation: Optional[pulumi.Input[bool]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            availability_zone_id: Optional[pulumi.Input[str]] = None,
            cidr_block: Optional[pulumi.Input[str]] = None,
            customer_owned_ipv4_pool: Optional[pulumi.Input[str]] = None,
            ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
            ipv6_cidr_block_association_id: Optional[pulumi.Input[str]] = None,
            map_customer_owned_ip_on_launch: Optional[pulumi.Input[bool]] = None,
            map_public_ip_on_launch: Optional[pulumi.Input[bool]] = None,
            outpost_arn: Optional[pulumi.Input[str]] = None,
            owner_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None) -> 'DefaultSubnet':
        """
        Get an existing DefaultSubnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN for the subnet.
        :param pulumi.Input[bool] assign_ipv6_address_on_creation: Whether IPv6 addresses are assigned on creation.
               * `availability_zone_id`- AZ ID of the subnet.
        :param pulumi.Input[str] availability_zone: AZ for the subnet.
        :param pulumi.Input[str] cidr_block: CIDR block for the subnet.
        :param pulumi.Input[str] ipv6_cidr_block: IPv6 CIDR block.
        :param pulumi.Input[bool] map_public_ip_on_launch: Whether instances launched into the subnet should be assigned a public IP address.
        :param pulumi.Input[str] owner_id: ID of the AWS account that owns the subnet.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Map of tags to assign to the resource.
        :param pulumi.Input[str] vpc_id: VPC ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["assign_ipv6_address_on_creation"] = assign_ipv6_address_on_creation
        __props__["availability_zone"] = availability_zone
        __props__["availability_zone_id"] = availability_zone_id
        __props__["cidr_block"] = cidr_block
        __props__["customer_owned_ipv4_pool"] = customer_owned_ipv4_pool
        __props__["ipv6_cidr_block"] = ipv6_cidr_block
        __props__["ipv6_cidr_block_association_id"] = ipv6_cidr_block_association_id
        __props__["map_customer_owned_ip_on_launch"] = map_customer_owned_ip_on_launch
        __props__["map_public_ip_on_launch"] = map_public_ip_on_launch
        __props__["outpost_arn"] = outpost_arn
        __props__["owner_id"] = owner_id
        __props__["tags"] = tags
        __props__["vpc_id"] = vpc_id
        return DefaultSubnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN for the subnet.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="assignIpv6AddressOnCreation")
    def assign_ipv6_address_on_creation(self) -> pulumi.Output[bool]:
        """
        Whether IPv6 addresses are assigned on creation.
        * `availability_zone_id`- AZ ID of the subnet.
        """
        return pulumi.get(self, "assign_ipv6_address_on_creation")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        AZ for the subnet.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> pulumi.Output[str]:
        """
        CIDR block for the subnet.
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter(name="customerOwnedIpv4Pool")
    def customer_owned_ipv4_pool(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "customer_owned_ipv4_pool")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[str]:
        """
        IPv6 CIDR block.
        """
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="ipv6CidrBlockAssociationId")
    def ipv6_cidr_block_association_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ipv6_cidr_block_association_id")

    @property
    @pulumi.getter(name="mapCustomerOwnedIpOnLaunch")
    def map_customer_owned_ip_on_launch(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "map_customer_owned_ip_on_launch")

    @property
    @pulumi.getter(name="mapPublicIpOnLaunch")
    def map_public_ip_on_launch(self) -> pulumi.Output[bool]:
        """
        Whether instances launched into the subnet should be assigned a public IP address.
        """
        return pulumi.get(self, "map_public_ip_on_launch")

    @property
    @pulumi.getter(name="outpostArn")
    def outpost_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "outpost_arn")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        ID of the AWS account that owns the subnet.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Map of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        """
        VPC ID.
        """
        return pulumi.get(self, "vpc_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

