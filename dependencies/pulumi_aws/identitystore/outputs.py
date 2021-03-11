# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetGroupFilterResult',
    'GetUserFilterResult',
]

@pulumi.output_type
class GetGroupFilterResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: The attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        :param str attribute_value: The value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        The attribute path that is used to specify which attribute name to search. Currently, `DisplayName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        The value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


@pulumi.output_type
class GetUserFilterResult(dict):
    def __init__(__self__, *,
                 attribute_path: str,
                 attribute_value: str):
        """
        :param str attribute_path: The attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        :param str attribute_value: The value for an attribute.
        """
        pulumi.set(__self__, "attribute_path", attribute_path)
        pulumi.set(__self__, "attribute_value", attribute_value)

    @property
    @pulumi.getter(name="attributePath")
    def attribute_path(self) -> str:
        """
        The attribute path that is used to specify which attribute name to search. Currently, `UserName` is the only valid attribute path.
        """
        return pulumi.get(self, "attribute_path")

    @property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> str:
        """
        The value for an attribute.
        """
        return pulumi.get(self, "attribute_value")


