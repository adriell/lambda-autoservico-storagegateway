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

__all__ = ['SmbFileShare']


class SmbFileShare(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_based_enumeration: Optional[pulumi.Input[bool]] = None,
                 admin_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 audit_destination_arn: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 cache_attributes: Optional[pulumi.Input[pulumi.InputType['SmbFileShareCacheAttributesArgs']]] = None,
                 case_sensitivity: Optional[pulumi.Input[str]] = None,
                 default_storage_class: Optional[pulumi.Input[str]] = None,
                 file_share_name: Optional[pulumi.Input[str]] = None,
                 gateway_arn: Optional[pulumi.Input[str]] = None,
                 guess_mime_type_enabled: Optional[pulumi.Input[bool]] = None,
                 invalid_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kms_encrypted: Optional[pulumi.Input[bool]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 location_arn: Optional[pulumi.Input[str]] = None,
                 notification_policy: Optional[pulumi.Input[str]] = None,
                 object_acl: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 requester_pays: Optional[pulumi.Input[bool]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 smb_acl_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 valid_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages an AWS Storage Gateway SMB File Share.

        ## Example Usage
        ### Active Directory Authentication

        > **NOTE:** The gateway must have already joined the Active Directory domain prior to SMB file share creation. e.g. via "SMB Settings" in the AWS Storage Gateway console or `smb_active_directory_settings` in the `storagegateway.Gateway` resource.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.SmbFileShare("example",
            authentication="ActiveDirectory",
            gateway_arn=aws_storagegateway_gateway["example"]["arn"],
            location_arn=aws_s3_bucket["example"]["arn"],
            role_arn=aws_iam_role["example"]["arn"])
        ```
        ### Guest Authentication

        > **NOTE:** The gateway must have already had the SMB guest password set prior to SMB file share creation. e.g. via "SMB Settings" in the AWS Storage Gateway console or `smb_guest_password` in the `storagegateway.Gateway` resource.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.storagegateway.SmbFileShare("example",
            authentication="GuestAccess",
            gateway_arn=aws_storagegateway_gateway["example"]["arn"],
            location_arn=aws_s3_bucket["example"]["arn"],
            role_arn=aws_iam_role["example"]["arn"])
        ```

        ## Import

        `aws_storagegateway_smb_file_share` can be imported by using the SMB File Share Amazon Resource Name (ARN), e.g.

        ```sh
         $ pulumi import aws:storagegateway/smbFileShare:SmbFileShare example arn:aws:storagegateway:us-east-1:123456789012:share/share-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] access_based_enumeration: The files and folders on this share will only be visible to users with read access. Default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admin_user_lists: A list of users in the Active Directory that have admin access to the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[str] audit_destination_arn: The Amazon Resource Name (ARN) of the CloudWatch Log Group used for the audit logs.
        :param pulumi.Input[str] authentication: The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
        :param pulumi.Input[pulumi.InputType['SmbFileShareCacheAttributesArgs']] cache_attributes: Refresh cache information. see Cache Attributes for more details.
        :param pulumi.Input[str] case_sensitivity: The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] file_share_name: The name of the file share. Must be set if an S3 prefix name is set in `location_arn`.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] invalid_user_lists: A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input[str] notification_policy: The notification policy of the file share. For more information see the [AWS Documentation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html#StorageGateway-CreateNFSFileShare-request-NotificationPolicy). Default value is `{}`.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[bool] smb_acl_enabled: Set this value to `true` to enable ACL (access control list) on the SMB fileshare. Set it to `false` to map file and directory permissions to the POSIX permissions. This setting applies only to `ActiveDirectory` authentication type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] valid_user_lists: A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
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

            __props__['access_based_enumeration'] = access_based_enumeration
            __props__['admin_user_lists'] = admin_user_lists
            __props__['audit_destination_arn'] = audit_destination_arn
            __props__['authentication'] = authentication
            __props__['cache_attributes'] = cache_attributes
            __props__['case_sensitivity'] = case_sensitivity
            __props__['default_storage_class'] = default_storage_class
            __props__['file_share_name'] = file_share_name
            if gateway_arn is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_arn'")
            __props__['gateway_arn'] = gateway_arn
            __props__['guess_mime_type_enabled'] = guess_mime_type_enabled
            __props__['invalid_user_lists'] = invalid_user_lists
            __props__['kms_encrypted'] = kms_encrypted
            __props__['kms_key_arn'] = kms_key_arn
            if location_arn is None and not opts.urn:
                raise TypeError("Missing required property 'location_arn'")
            __props__['location_arn'] = location_arn
            __props__['notification_policy'] = notification_policy
            __props__['object_acl'] = object_acl
            __props__['read_only'] = read_only
            __props__['requester_pays'] = requester_pays
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__['role_arn'] = role_arn
            __props__['smb_acl_enabled'] = smb_acl_enabled
            __props__['tags'] = tags
            __props__['valid_user_lists'] = valid_user_lists
            __props__['arn'] = None
            __props__['fileshare_id'] = None
            __props__['path'] = None
        super(SmbFileShare, __self__).__init__(
            'aws:storagegateway/smbFileShare:SmbFileShare',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_based_enumeration: Optional[pulumi.Input[bool]] = None,
            admin_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            audit_destination_arn: Optional[pulumi.Input[str]] = None,
            authentication: Optional[pulumi.Input[str]] = None,
            cache_attributes: Optional[pulumi.Input[pulumi.InputType['SmbFileShareCacheAttributesArgs']]] = None,
            case_sensitivity: Optional[pulumi.Input[str]] = None,
            default_storage_class: Optional[pulumi.Input[str]] = None,
            file_share_name: Optional[pulumi.Input[str]] = None,
            fileshare_id: Optional[pulumi.Input[str]] = None,
            gateway_arn: Optional[pulumi.Input[str]] = None,
            guess_mime_type_enabled: Optional[pulumi.Input[bool]] = None,
            invalid_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            kms_encrypted: Optional[pulumi.Input[bool]] = None,
            kms_key_arn: Optional[pulumi.Input[str]] = None,
            location_arn: Optional[pulumi.Input[str]] = None,
            notification_policy: Optional[pulumi.Input[str]] = None,
            object_acl: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            read_only: Optional[pulumi.Input[bool]] = None,
            requester_pays: Optional[pulumi.Input[bool]] = None,
            role_arn: Optional[pulumi.Input[str]] = None,
            smb_acl_enabled: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            valid_user_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'SmbFileShare':
        """
        Get an existing SmbFileShare resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] access_based_enumeration: The files and folders on this share will only be visible to users with read access. Default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] admin_user_lists: A list of users in the Active Directory that have admin access to the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the SMB File Share.
        :param pulumi.Input[str] audit_destination_arn: The Amazon Resource Name (ARN) of the CloudWatch Log Group used for the audit logs.
        :param pulumi.Input[str] authentication: The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
        :param pulumi.Input[pulumi.InputType['SmbFileShareCacheAttributesArgs']] cache_attributes: Refresh cache information. see Cache Attributes for more details.
        :param pulumi.Input[str] case_sensitivity: The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.
        :param pulumi.Input[str] default_storage_class: The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        :param pulumi.Input[str] file_share_name: The name of the file share. Must be set if an S3 prefix name is set in `location_arn`.
        :param pulumi.Input[str] fileshare_id: ID of the SMB File Share.
        :param pulumi.Input[str] gateway_arn: Amazon Resource Name (ARN) of the file gateway.
        :param pulumi.Input[bool] guess_mime_type_enabled: Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] invalid_user_lists: A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        :param pulumi.Input[bool] kms_encrypted: Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        :param pulumi.Input[str] kms_key_arn: Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        :param pulumi.Input[str] location_arn: The ARN of the backed storage used for storing file data.
        :param pulumi.Input[str] notification_policy: The notification policy of the file share. For more information see the [AWS Documentation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html#StorageGateway-CreateNFSFileShare-request-NotificationPolicy). Default value is `{}`.
        :param pulumi.Input[str] object_acl: Access Control List permission for S3 bucket objects. Defaults to `private`.
        :param pulumi.Input[str] path: File share path used by the NFS client to identify the mount point.
        :param pulumi.Input[bool] read_only: Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        :param pulumi.Input[bool] requester_pays: Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        :param pulumi.Input[str] role_arn: The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        :param pulumi.Input[bool] smb_acl_enabled: Set this value to `true` to enable ACL (access control list) on the SMB fileshare. Set it to `false` to map file and directory permissions to the POSIX permissions. This setting applies only to `ActiveDirectory` authentication type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[Sequence[pulumi.Input[str]]] valid_user_lists: A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_based_enumeration"] = access_based_enumeration
        __props__["admin_user_lists"] = admin_user_lists
        __props__["arn"] = arn
        __props__["audit_destination_arn"] = audit_destination_arn
        __props__["authentication"] = authentication
        __props__["cache_attributes"] = cache_attributes
        __props__["case_sensitivity"] = case_sensitivity
        __props__["default_storage_class"] = default_storage_class
        __props__["file_share_name"] = file_share_name
        __props__["fileshare_id"] = fileshare_id
        __props__["gateway_arn"] = gateway_arn
        __props__["guess_mime_type_enabled"] = guess_mime_type_enabled
        __props__["invalid_user_lists"] = invalid_user_lists
        __props__["kms_encrypted"] = kms_encrypted
        __props__["kms_key_arn"] = kms_key_arn
        __props__["location_arn"] = location_arn
        __props__["notification_policy"] = notification_policy
        __props__["object_acl"] = object_acl
        __props__["path"] = path
        __props__["read_only"] = read_only
        __props__["requester_pays"] = requester_pays
        __props__["role_arn"] = role_arn
        __props__["smb_acl_enabled"] = smb_acl_enabled
        __props__["tags"] = tags
        __props__["valid_user_lists"] = valid_user_lists
        return SmbFileShare(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessBasedEnumeration")
    def access_based_enumeration(self) -> pulumi.Output[Optional[bool]]:
        """
        The files and folders on this share will only be visible to users with read access. Default value is `false`.
        """
        return pulumi.get(self, "access_based_enumeration")

    @property
    @pulumi.getter(name="adminUserLists")
    def admin_user_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of users in the Active Directory that have admin access to the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        """
        return pulumi.get(self, "admin_user_lists")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the SMB File Share.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="auditDestinationArn")
    def audit_destination_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the CloudWatch Log Group used for the audit logs.
        """
        return pulumi.get(self, "audit_destination_arn")

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional[str]]:
        """
        The authentication method that users use to access the file share. Defaults to `ActiveDirectory`. Valid values: `ActiveDirectory`, `GuestAccess`.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="cacheAttributes")
    def cache_attributes(self) -> pulumi.Output[Optional['outputs.SmbFileShareCacheAttributes']]:
        """
        Refresh cache information. see Cache Attributes for more details.
        """
        return pulumi.get(self, "cache_attributes")

    @property
    @pulumi.getter(name="caseSensitivity")
    def case_sensitivity(self) -> pulumi.Output[Optional[str]]:
        """
        The case of an object name in an Amazon S3 bucket. For `ClientSpecified`, the client determines the case sensitivity. For `CaseSensitive`, the gateway determines the case sensitivity. The default value is `ClientSpecified`.
        """
        return pulumi.get(self, "case_sensitivity")

    @property
    @pulumi.getter(name="defaultStorageClass")
    def default_storage_class(self) -> pulumi.Output[Optional[str]]:
        """
        The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
        """
        return pulumi.get(self, "default_storage_class")

    @property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> pulumi.Output[str]:
        """
        The name of the file share. Must be set if an S3 prefix name is set in `location_arn`.
        """
        return pulumi.get(self, "file_share_name")

    @property
    @pulumi.getter(name="fileshareId")
    def fileshare_id(self) -> pulumi.Output[str]:
        """
        ID of the SMB File Share.
        """
        return pulumi.get(self, "fileshare_id")

    @property
    @pulumi.getter(name="gatewayArn")
    def gateway_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of the file gateway.
        """
        return pulumi.get(self, "gateway_arn")

    @property
    @pulumi.getter(name="guessMimeTypeEnabled")
    def guess_mime_type_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
        """
        return pulumi.get(self, "guess_mime_type_enabled")

    @property
    @pulumi.getter(name="invalidUserLists")
    def invalid_user_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of users in the Active Directory that are not allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        """
        return pulumi.get(self, "invalid_user_lists")

    @property
    @pulumi.getter(name="kmsEncrypted")
    def kms_encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
        """
        return pulumi.get(self, "kms_encrypted")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the backed storage used for storing file data.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="notificationPolicy")
    def notification_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The notification policy of the file share. For more information see the [AWS Documentation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_CreateNFSFileShare.html#StorageGateway-CreateNFSFileShare-request-NotificationPolicy). Default value is `{}`.
        """
        return pulumi.get(self, "notification_policy")

    @property
    @pulumi.getter(name="objectAcl")
    def object_acl(self) -> pulumi.Output[Optional[str]]:
        """
        Access Control List permission for S3 bucket objects. Defaults to `private`.
        """
        return pulumi.get(self, "object_acl")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        File share path used by the NFS client to identify the mount point.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
        """
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter(name="requesterPays")
    def requester_pays(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
        """
        return pulumi.get(self, "requester_pays")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="smbAclEnabled")
    def smb_acl_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Set this value to `true` to enable ACL (access control list) on the SMB fileshare. Set it to `false` to map file and directory permissions to the POSIX permissions. This setting applies only to `ActiveDirectory` authentication type.
        """
        return pulumi.get(self, "smb_acl_enabled")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="validUserLists")
    def valid_user_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of users in the Active Directory that are allowed to access the file share. Only valid if `authentication` is set to `ActiveDirectory`.
        """
        return pulumi.get(self, "valid_user_lists")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
