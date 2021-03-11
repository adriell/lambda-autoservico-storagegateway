# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetVpcLinkResult',
    'AwaitableGetVpcLinkResult',
    'get_vpc_link',
]

@pulumi.output_type
class GetVpcLinkResult:
    """
    A collection of values returned by getVpcLink.
    """
    def __init__(__self__, description=None, id=None, name=None, status=None, status_message=None, tags=None, target_arns=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_arns and not isinstance(target_arns, list):
            raise TypeError("Expected argument 'target_arns' to be a list")
        pulumi.set(__self__, "target_arns", target_arns)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the VPC link.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Set to the ID of the found API Gateway VPC Link.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the VPC link.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> str:
        """
        The status message of the VPC link.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetArns")
    def target_arns(self) -> Sequence[str]:
        """
        The list of network load balancer arns in the VPC targeted by the VPC link. Currently AWS only supports 1 target.
        """
        return pulumi.get(self, "target_arns")


class AwaitableGetVpcLinkResult(GetVpcLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcLinkResult(
            description=self.description,
            id=self.id,
            name=self.name,
            status=self.status,
            status_message=self.status_message,
            tags=self.tags,
            target_arns=self.target_arns)


def get_vpc_link(name: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcLinkResult:
    """
    Use this data source to get the id of a VPC Link in
    API Gateway. To fetch the VPC Link you must provide a name to match against.
    As there is no unique name constraint on API Gateway VPC Links this data source will
    error if there is more than one match.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    my_api_gateway_vpc_link = aws.apigateway.get_vpc_link(name="my-vpc-link")
    ```


    :param str name: The name of the API Gateway VPC Link to look up. If no API Gateway VPC Link is found with this name, an error will be returned.
           If multiple API Gateway VPC Links are found with this name, an error will be returned.
    :param Mapping[str, str] tags: Key-value map of resource tags
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:apigateway/getVpcLink:getVpcLink', __args__, opts=opts, typ=GetVpcLinkResult).value

    return AwaitableGetVpcLinkResult(
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        status=__ret__.status,
        status_message=__ret__.status_message,
        tags=__ret__.tags,
        target_arns=__ret__.target_arns)