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

__all__ = ['SigningJob']


class SigningJob(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[pulumi.InputType['SigningJobDestinationArgs']]] = None,
                 ignore_signing_job_failure: Optional[pulumi.Input[bool]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['SigningJobSourceArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Signer Signing Job.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_sp = aws.signer.SigningProfile("testSp", platform_id="AWSLambda-SHA384-ECDSA")
        build_signing_job = aws.signer.SigningJob("buildSigningJob",
            profile_name=test_sp.name,
            source=aws.signer.SigningJobSourceArgs(
                s3=aws.signer.SigningJobSourceS3Args(
                    bucket="s3-bucket-name",
                    key="object-to-be-signed.zip",
                    version="jADjFYYYEXAMPLETszPjOmCMFDzd9dN1",
                ),
            ),
            destination=aws.signer.SigningJobDestinationArgs(
                s3=aws.signer.SigningJobDestinationS3Args(
                    bucket="s3-bucket-name",
                    prefix="signed/",
                ),
            ),
            ignore_signing_job_failure=True)
        ```

        ## Import

        Signer signing jobs can be imported using the `job_id`, e.g.

        ```sh
         $ pulumi import aws:signer/signingJob:SigningJob test_signer_signing_job 9ed7e5c3-b8d4-4da0-8459-44e0b068f7ee
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['SigningJobDestinationArgs']] destination: The S3 bucket in which to save your signed object. See Destination below for details.
        :param pulumi.Input[bool] ignore_signing_job_failure: Set this argument to `true` to ignore signing job failures and retrieve failed status and reason. Default `false`.
        :param pulumi.Input[str] profile_name: The name of the profile to initiate the signing operation.
        :param pulumi.Input[pulumi.InputType['SigningJobSourceArgs']] source: The S3 bucket that contains the object to sign. See Source below for details.
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

            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__['destination'] = destination
            __props__['ignore_signing_job_failure'] = ignore_signing_job_failure
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__['profile_name'] = profile_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__['source'] = source
            __props__['completed_at'] = None
            __props__['created_at'] = None
            __props__['job_id'] = None
            __props__['job_invoker'] = None
            __props__['job_owner'] = None
            __props__['platform_display_name'] = None
            __props__['platform_id'] = None
            __props__['profile_version'] = None
            __props__['requested_by'] = None
            __props__['revocation_records'] = None
            __props__['signature_expires_at'] = None
            __props__['signed_objects'] = None
            __props__['status'] = None
            __props__['status_reason'] = None
        super(SigningJob, __self__).__init__(
            'aws:signer/signingJob:SigningJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            completed_at: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            destination: Optional[pulumi.Input[pulumi.InputType['SigningJobDestinationArgs']]] = None,
            ignore_signing_job_failure: Optional[pulumi.Input[bool]] = None,
            job_id: Optional[pulumi.Input[str]] = None,
            job_invoker: Optional[pulumi.Input[str]] = None,
            job_owner: Optional[pulumi.Input[str]] = None,
            platform_display_name: Optional[pulumi.Input[str]] = None,
            platform_id: Optional[pulumi.Input[str]] = None,
            profile_name: Optional[pulumi.Input[str]] = None,
            profile_version: Optional[pulumi.Input[str]] = None,
            requested_by: Optional[pulumi.Input[str]] = None,
            revocation_records: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningJobRevocationRecordArgs']]]]] = None,
            signature_expires_at: Optional[pulumi.Input[str]] = None,
            signed_objects: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningJobSignedObjectArgs']]]]] = None,
            source: Optional[pulumi.Input[pulumi.InputType['SigningJobSourceArgs']]] = None,
            status: Optional[pulumi.Input[str]] = None,
            status_reason: Optional[pulumi.Input[str]] = None) -> 'SigningJob':
        """
        Get an existing SigningJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] completed_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing job was completed.
        :param pulumi.Input[str] created_at: Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing job was created.
        :param pulumi.Input[pulumi.InputType['SigningJobDestinationArgs']] destination: The S3 bucket in which to save your signed object. See Destination below for details.
        :param pulumi.Input[bool] ignore_signing_job_failure: Set this argument to `true` to ignore signing job failures and retrieve failed status and reason. Default `false`.
        :param pulumi.Input[str] job_id: The ID of the signing job on output.
        :param pulumi.Input[str] job_invoker: The IAM entity that initiated the signing job.
        :param pulumi.Input[str] job_owner: The AWS account ID of the job owner.
        :param pulumi.Input[str] platform_display_name: A human-readable name for the signing platform associated with the signing job.
        :param pulumi.Input[str] platform_id: The platform to which your signed code image will be distributed.
        :param pulumi.Input[str] profile_name: The name of the profile to initiate the signing operation.
        :param pulumi.Input[str] profile_version: The version of the signing profile used to initiate the signing job.
        :param pulumi.Input[str] requested_by: The IAM principal that requested the signing job.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningJobRevocationRecordArgs']]]] revocation_records: A revocation record if the signature generated by the signing job has been revoked. Contains a timestamp and the ID of the IAM entity that revoked the signature.
        :param pulumi.Input[str] signature_expires_at: The time when the signature of a signing job expires.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SigningJobSignedObjectArgs']]]] signed_objects: Name of the S3 bucket where the signed code image is saved by code signing.
        :param pulumi.Input[pulumi.InputType['SigningJobSourceArgs']] source: The S3 bucket that contains the object to sign. See Source below for details.
        :param pulumi.Input[str] status: Status of the signing job.
        :param pulumi.Input[str] status_reason: String value that contains the status reason.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["completed_at"] = completed_at
        __props__["created_at"] = created_at
        __props__["destination"] = destination
        __props__["ignore_signing_job_failure"] = ignore_signing_job_failure
        __props__["job_id"] = job_id
        __props__["job_invoker"] = job_invoker
        __props__["job_owner"] = job_owner
        __props__["platform_display_name"] = platform_display_name
        __props__["platform_id"] = platform_id
        __props__["profile_name"] = profile_name
        __props__["profile_version"] = profile_version
        __props__["requested_by"] = requested_by
        __props__["revocation_records"] = revocation_records
        __props__["signature_expires_at"] = signature_expires_at
        __props__["signed_objects"] = signed_objects
        __props__["source"] = source
        __props__["status"] = status
        __props__["status_reason"] = status_reason
        return SigningJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="completedAt")
    def completed_at(self) -> pulumi.Output[str]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing job was completed.
        """
        return pulumi.get(self, "completed_at")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Date and time in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) that the signing job was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output['outputs.SigningJobDestination']:
        """
        The S3 bucket in which to save your signed object. See Destination below for details.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="ignoreSigningJobFailure")
    def ignore_signing_job_failure(self) -> pulumi.Output[Optional[bool]]:
        """
        Set this argument to `true` to ignore signing job failures and retrieve failed status and reason. Default `false`.
        """
        return pulumi.get(self, "ignore_signing_job_failure")

    @property
    @pulumi.getter(name="jobId")
    def job_id(self) -> pulumi.Output[str]:
        """
        The ID of the signing job on output.
        """
        return pulumi.get(self, "job_id")

    @property
    @pulumi.getter(name="jobInvoker")
    def job_invoker(self) -> pulumi.Output[str]:
        """
        The IAM entity that initiated the signing job.
        """
        return pulumi.get(self, "job_invoker")

    @property
    @pulumi.getter(name="jobOwner")
    def job_owner(self) -> pulumi.Output[str]:
        """
        The AWS account ID of the job owner.
        """
        return pulumi.get(self, "job_owner")

    @property
    @pulumi.getter(name="platformDisplayName")
    def platform_display_name(self) -> pulumi.Output[str]:
        """
        A human-readable name for the signing platform associated with the signing job.
        """
        return pulumi.get(self, "platform_display_name")

    @property
    @pulumi.getter(name="platformId")
    def platform_id(self) -> pulumi.Output[str]:
        """
        The platform to which your signed code image will be distributed.
        """
        return pulumi.get(self, "platform_id")

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Output[str]:
        """
        The name of the profile to initiate the signing operation.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="profileVersion")
    def profile_version(self) -> pulumi.Output[str]:
        """
        The version of the signing profile used to initiate the signing job.
        """
        return pulumi.get(self, "profile_version")

    @property
    @pulumi.getter(name="requestedBy")
    def requested_by(self) -> pulumi.Output[str]:
        """
        The IAM principal that requested the signing job.
        """
        return pulumi.get(self, "requested_by")

    @property
    @pulumi.getter(name="revocationRecords")
    def revocation_records(self) -> pulumi.Output[Sequence['outputs.SigningJobRevocationRecord']]:
        """
        A revocation record if the signature generated by the signing job has been revoked. Contains a timestamp and the ID of the IAM entity that revoked the signature.
        """
        return pulumi.get(self, "revocation_records")

    @property
    @pulumi.getter(name="signatureExpiresAt")
    def signature_expires_at(self) -> pulumi.Output[str]:
        """
        The time when the signature of a signing job expires.
        """
        return pulumi.get(self, "signature_expires_at")

    @property
    @pulumi.getter(name="signedObjects")
    def signed_objects(self) -> pulumi.Output[Sequence['outputs.SigningJobSignedObject']]:
        """
        Name of the S3 bucket where the signed code image is saved by code signing.
        """
        return pulumi.get(self, "signed_objects")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output['outputs.SigningJobSource']:
        """
        The S3 bucket that contains the object to sign. See Source below for details.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the signing job.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusReason")
    def status_reason(self) -> pulumi.Output[str]:
        """
        String value that contains the status reason.
        """
        return pulumi.get(self, "status_reason")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

