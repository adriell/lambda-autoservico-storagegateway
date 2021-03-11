# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, arn=None, id=None, path=None, permissions_boundary=None, tags=None, user_id=None, user_name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if path and not isinstance(path, str):
            raise TypeError("Expected argument 'path' to be a str")
        pulumi.set(__self__, "path", path)
        if permissions_boundary and not isinstance(permissions_boundary, str):
            raise TypeError("Expected argument 'permissions_boundary' to be a str")
        pulumi.set(__self__, "permissions_boundary", permissions_boundary)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) assigned by AWS for this user.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path in which this user was created.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="permissionsBoundary")
    def permissions_boundary(self) -> str:
        """
        The ARN of the policy that is used to set the permissions boundary for the user.
        """
        return pulumi.get(self, "permissions_boundary")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
        """
        Map of key-value pairs associated with the user.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The unique ID assigned by AWS for this user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        The name associated to this User
        """
        return pulumi.get(self, "user_name")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            arn=self.arn,
            id=self.id,
            path=self.path,
            permissions_boundary=self.permissions_boundary,
            tags=self.tags,
            user_id=self.user_id,
            user_name=self.user_name)


def get_user(tags: Optional[Mapping[str, str]] = None,
             user_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    This data source can be used to fetch information about a specific
    IAM user. By using this data source, you can reference IAM user
    properties without having to hard code ARNs or unique IDs as input.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.iam.get_user(user_name="an_example_user_name")
    ```


    :param Mapping[str, str] tags: Map of key-value pairs associated with the user.
    :param str user_name: The friendly IAM user name to match.
    """
    __args__ = dict()
    __args__['tags'] = tags
    __args__['userName'] = user_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        arn=__ret__.arn,
        id=__ret__.id,
        path=__ret__.path,
        permissions_boundary=__ret__.permissions_boundary,
        tags=__ret__.tags,
        user_id=__ret__.user_id,
        user_name=__ret__.user_name)