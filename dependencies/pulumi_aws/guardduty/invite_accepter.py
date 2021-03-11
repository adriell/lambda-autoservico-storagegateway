# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['InviteAccepter']


class InviteAccepter(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 master_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct primary account on read, and disassociate with the primary account upon removal.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_pulumi as pulumi

        primary = pulumi.providers.Aws("primary")
        member = pulumi.providers.Aws("member")
        primary_detector = aws.guardduty.Detector("primaryDetector", opts=pulumi.ResourceOptions(provider=aws["primary"]))
        member_detector = aws.guardduty.Detector("memberDetector", opts=pulumi.ResourceOptions(provider=aws["member"]))
        member_member = aws.guardduty.Member("memberMember",
            account_id=member_detector.account_id,
            detector_id=primary_detector.id,
            email="required@example.com",
            invite=True,
            opts=pulumi.ResourceOptions(provider=aws["primary"]))
        member_invite_accepter = aws.guardduty.InviteAccepter("memberInviteAccepter",
            detector_id=member_detector.id,
            master_account_id=primary_detector.account_id,
            opts=pulumi.ResourceOptions(provider=aws["member"],
                depends_on=[member_member]))
        ```

        ## Import

        `aws_guardduty_invite_accepter` can be imported using the the member GuardDuty detector ID, e.g.

        ```sh
         $ pulumi import aws:guardduty/inviteAccepter:InviteAccepter member 00b00fd5aecc0ab60a708659477e9617
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
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

            if detector_id is None and not opts.urn:
                raise TypeError("Missing required property 'detector_id'")
            __props__['detector_id'] = detector_id
            if master_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'master_account_id'")
            __props__['master_account_id'] = master_account_id
        super(InviteAccepter, __self__).__init__(
            'aws:guardduty/inviteAccepter:InviteAccepter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            detector_id: Optional[pulumi.Input[str]] = None,
            master_account_id: Optional[pulumi.Input[str]] = None) -> 'InviteAccepter':
        """
        Get an existing InviteAccepter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_id: The detector ID of the member GuardDuty account.
        :param pulumi.Input[str] master_account_id: AWS account ID for primary account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["detector_id"] = detector_id
        __props__["master_account_id"] = master_account_id
        return InviteAccepter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        """
        The detector ID of the member GuardDuty account.
        """
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="masterAccountId")
    def master_account_id(self) -> pulumi.Output[str]:
        """
        AWS account ID for primary account.
        """
        return pulumi.get(self, "master_account_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
