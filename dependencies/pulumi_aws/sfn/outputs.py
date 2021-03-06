# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'StateMachineLoggingConfiguration',
]

@pulumi.output_type
class StateMachineLoggingConfiguration(dict):
    def __init__(__self__, *,
                 include_execution_data: Optional[bool] = None,
                 level: Optional[str] = None,
                 log_destination: Optional[str] = None):
        """
        :param bool include_execution_data: Determines whether execution data is included in your log. When set to FALSE, data is excluded.
        :param str level: Defines which category of execution history events are logged. Valid Values: ALL | ERROR | FATAL | OFF
        :param str log_destination: Amazon Resource Name (ARN) of CloudWatch log group. Make sure the State Machine does have the right IAM Policies for Logging. The ARN must end with `:*`
        """
        if include_execution_data is not None:
            pulumi.set(__self__, "include_execution_data", include_execution_data)
        if level is not None:
            pulumi.set(__self__, "level", level)
        if log_destination is not None:
            pulumi.set(__self__, "log_destination", log_destination)

    @property
    @pulumi.getter(name="includeExecutionData")
    def include_execution_data(self) -> Optional[bool]:
        """
        Determines whether execution data is included in your log. When set to FALSE, data is excluded.
        """
        return pulumi.get(self, "include_execution_data")

    @property
    @pulumi.getter
    def level(self) -> Optional[str]:
        """
        Defines which category of execution history events are logged. Valid Values: ALL | ERROR | FATAL | OFF
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of CloudWatch log group. Make sure the State Machine does have the right IAM Policies for Logging. The ARN must end with `:*`
        """
        return pulumi.get(self, "log_destination")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


