# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'ConfgurationSetDeliveryOptions',
    'ConfigurationSetDeliveryOptions',
    'EventDestinationCloudwatchDestination',
    'EventDestinationKinesisDestination',
    'EventDestinationSnsDestination',
    'ReceiptRuleAddHeaderAction',
    'ReceiptRuleBounceAction',
    'ReceiptRuleLambdaAction',
    'ReceiptRuleS3Action',
    'ReceiptRuleSnsAction',
    'ReceiptRuleStopAction',
    'ReceiptRuleWorkmailAction',
]

@pulumi.output_type
class ConfgurationSetDeliveryOptions(dict):
    def __init__(__self__, *,
                 tls_policy: Optional[str] = None):
        """
        :param str tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established. Valid values: `Require` or `Optional`. Defaults to `Optional`.
        """
        if tls_policy is not None:
            pulumi.set(__self__, "tls_policy", tls_policy)

    @property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[str]:
        """
        Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established. Valid values: `Require` or `Optional`. Defaults to `Optional`.
        """
        return pulumi.get(self, "tls_policy")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ConfigurationSetDeliveryOptions(dict):
    def __init__(__self__, *,
                 tls_policy: Optional[str] = None):
        """
        :param str tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established. Valid values: `Require` or `Optional`. Defaults to `Optional`.
        """
        if tls_policy is not None:
            pulumi.set(__self__, "tls_policy", tls_policy)

    @property
    @pulumi.getter(name="tlsPolicy")
    def tls_policy(self) -> Optional[str]:
        """
        Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require`, messages are only delivered if a TLS connection can be established. If the value is `Optional`, messages can be delivered in plain text if a TLS connection can't be established. Valid values: `Require` or `Optional`. Defaults to `Optional`.
        """
        return pulumi.get(self, "tls_policy")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventDestinationCloudwatchDestination(dict):
    def __init__(__self__, *,
                 default_value: str,
                 dimension_name: str,
                 value_source: str):
        """
        :param str default_value: The default value for the event
        :param str dimension_name: The name for the dimension
        :param str value_source: The source for the value. May be any of `"messageTag"`, `"emailHeader"` or `"linkTag"`.
        """
        pulumi.set(__self__, "default_value", default_value)
        pulumi.set(__self__, "dimension_name", dimension_name)
        pulumi.set(__self__, "value_source", value_source)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> str:
        """
        The default value for the event
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> str:
        """
        The name for the dimension
        """
        return pulumi.get(self, "dimension_name")

    @property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> str:
        """
        The source for the value. May be any of `"messageTag"`, `"emailHeader"` or `"linkTag"`.
        """
        return pulumi.get(self, "value_source")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventDestinationKinesisDestination(dict):
    def __init__(__self__, *,
                 role_arn: str,
                 stream_arn: str):
        """
        :param str role_arn: The ARN of the role that has permissions to access the Kinesis Stream
        :param str stream_arn: The ARN of the Kinesis Stream
        """
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "stream_arn", stream_arn)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> str:
        """
        The ARN of the role that has permissions to access the Kinesis Stream
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> str:
        """
        The ARN of the Kinesis Stream
        """
        return pulumi.get(self, "stream_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EventDestinationSnsDestination(dict):
    def __init__(__self__, *,
                 topic_arn: str):
        """
        :param str topic_arn: The ARN of the SNS topic
        """
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> str:
        """
        The ARN of the SNS topic
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleAddHeaderAction(dict):
    def __init__(__self__, *,
                 header_name: str,
                 header_value: str,
                 position: int):
        """
        :param str header_name: The name of the header to add
        :param str header_value: The value of the header to add
        :param int position: The position of the action in the receipt rule
        """
        pulumi.set(__self__, "header_name", header_name)
        pulumi.set(__self__, "header_value", header_value)
        pulumi.set(__self__, "position", position)

    @property
    @pulumi.getter(name="headerName")
    def header_name(self) -> str:
        """
        The name of the header to add
        """
        return pulumi.get(self, "header_name")

    @property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> str:
        """
        The value of the header to add
        """
        return pulumi.get(self, "header_value")

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleBounceAction(dict):
    def __init__(__self__, *,
                 message: str,
                 position: int,
                 sender: str,
                 smtp_reply_code: str,
                 status_code: Optional[str] = None,
                 topic_arn: Optional[str] = None):
        """
        :param str message: The message to send
        :param int position: The position of the action in the receipt rule
        :param str sender: The email address of the sender
        :param str smtp_reply_code: The RFC 5321 SMTP reply code
        :param str status_code: The RFC 3463 SMTP enhanced status code
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "sender", sender)
        pulumi.set(__self__, "smtp_reply_code", smtp_reply_code)
        if status_code is not None:
            pulumi.set(__self__, "status_code", status_code)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The message to send
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter
    def sender(self) -> str:
        """
        The email address of the sender
        """
        return pulumi.get(self, "sender")

    @property
    @pulumi.getter(name="smtpReplyCode")
    def smtp_reply_code(self) -> str:
        """
        The RFC 5321 SMTP reply code
        """
        return pulumi.get(self, "smtp_reply_code")

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[str]:
        """
        The RFC 3463 SMTP enhanced status code
        """
        return pulumi.get(self, "status_code")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleLambdaAction(dict):
    def __init__(__self__, *,
                 function_arn: str,
                 position: int,
                 invocation_type: Optional[str] = None,
                 topic_arn: Optional[str] = None):
        """
        :param str function_arn: The ARN of the Lambda function to invoke
        :param int position: The position of the action in the receipt rule
        :param str invocation_type: Event or RequestResponse
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "function_arn", function_arn)
        pulumi.set(__self__, "position", position)
        if invocation_type is not None:
            pulumi.set(__self__, "invocation_type", invocation_type)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> str:
        """
        The ARN of the Lambda function to invoke
        """
        return pulumi.get(self, "function_arn")

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> Optional[str]:
        """
        Event or RequestResponse
        """
        return pulumi.get(self, "invocation_type")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleS3Action(dict):
    def __init__(__self__, *,
                 bucket_name: str,
                 position: int,
                 kms_key_arn: Optional[str] = None,
                 object_key_prefix: Optional[str] = None,
                 topic_arn: Optional[str] = None):
        """
        :param str bucket_name: The name of the S3 bucket
        :param int position: The position of the action in the receipt rule
        :param str kms_key_arn: The ARN of the KMS key
        :param str object_key_prefix: The key prefix of the S3 bucket
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "position", position)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if object_key_prefix is not None:
            pulumi.set(__self__, "object_key_prefix", object_key_prefix)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        The name of the S3 bucket
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[str]:
        """
        The ARN of the KMS key
        """
        return pulumi.get(self, "kms_key_arn")

    @property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[str]:
        """
        The key prefix of the S3 bucket
        """
        return pulumi.get(self, "object_key_prefix")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleSnsAction(dict):
    def __init__(__self__, *,
                 position: int,
                 topic_arn: str):
        """
        :param int position: The position of the action in the receipt rule
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> str:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleStopAction(dict):
    def __init__(__self__, *,
                 position: int,
                 scope: str,
                 topic_arn: Optional[str] = None):
        """
        :param int position: The position of the action in the receipt rule
        :param str scope: The scope to apply
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "scope", scope)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter
    def scope(self) -> str:
        """
        The scope to apply
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class ReceiptRuleWorkmailAction(dict):
    def __init__(__self__, *,
                 organization_arn: str,
                 position: int,
                 topic_arn: Optional[str] = None):
        """
        :param str organization_arn: The ARN of the WorkMail organization
        :param int position: The position of the action in the receipt rule
        :param str topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "organization_arn", organization_arn)
        pulumi.set(__self__, "position", position)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="organizationArn")
    def organization_arn(self) -> str:
        """
        The ARN of the WorkMail organization
        """
        return pulumi.get(self, "organization_arn")

    @property
    @pulumi.getter
    def position(self) -> int:
        """
        The position of the action in the receipt rule
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[str]:
        """
        The ARN of an SNS topic to notify
        """
        return pulumi.get(self, "topic_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


