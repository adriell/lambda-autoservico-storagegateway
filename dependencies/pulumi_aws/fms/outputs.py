# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'PolicyExcludeMap',
    'PolicyIncludeMap',
    'PolicySecurityServicePolicyData',
]

@pulumi.output_type
class PolicyExcludeMap(dict):
    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 orgunits: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "orgunits")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicyIncludeMap(dict):
    def __init__(__self__, *,
                 accounts: Optional[Sequence[str]] = None,
                 orgunits: Optional[Sequence[str]] = None):
        """
        :param Sequence[str] accounts: A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        if accounts is not None:
            pulumi.set(__self__, "accounts", accounts)
        if orgunits is not None:
            pulumi.set(__self__, "orgunits", orgunits)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[Sequence[str]]:
        """
        A list of AWS Organization member Accounts that you want to include for this AWS FMS Policy.
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter
    def orgunits(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "orgunits")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PolicySecurityServicePolicyData(dict):
    def __init__(__self__, *,
                 type: str,
                 managed_service_data: Optional[str] = None):
        """
        :param str type: The service that the policy is using to protect the resources. Valid values are `WAFV2`, `WAF`, `SHIELD_ADVANCED`, `SECURITY_GROUPS_COMMON`, `SECURITY_GROUPS_CONTENT_AUDIT`, and `SECURITY_GROUPS_USAGE_AUDIT`.
        :param str managed_service_data: Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        pulumi.set(__self__, "type", type)
        if managed_service_data is not None:
            pulumi.set(__self__, "managed_service_data", managed_service_data)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The service that the policy is using to protect the resources. Valid values are `WAFV2`, `WAF`, `SHIELD_ADVANCED`, `SECURITY_GROUPS_COMMON`, `SECURITY_GROUPS_CONTENT_AUDIT`, and `SECURITY_GROUPS_USAGE_AUDIT`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="managedServiceData")
    def managed_service_data(self) -> Optional[str]:
        """
        Details about the service that are specific to the service type, in JSON format. For service type `SHIELD_ADVANCED`, this is an empty string. Examples depending on `type` can be found in the [AWS Firewall Manager SecurityServicePolicyData API Reference](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_SecurityServicePolicyData.html).
        """
        return pulumi.get(self, "managed_service_data")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


