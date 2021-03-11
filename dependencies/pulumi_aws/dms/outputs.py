# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'EndpointElasticsearchSettings',
    'EndpointKafkaSettings',
    'EndpointKinesisSettings',
    'EndpointMongodbSettings',
    'EndpointS3Settings',
]

@pulumi.output_type
class EndpointElasticsearchSettings(dict):
    def __init__(__self__, *,
                 endpoint_uri: str,
                 service_access_role_arn: str,
                 error_retry_duration: Optional[int] = None,
                 full_load_error_percentage: Optional[int] = None):
        """
        :param str endpoint_uri: Endpoint for the Elasticsearch cluster.
        :param str service_access_role_arn: Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.
        :param int error_retry_duration: Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
        :param int full_load_error_percentage: Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
        """
        pulumi.set(__self__, "endpoint_uri", endpoint_uri)
        pulumi.set(__self__, "service_access_role_arn", service_access_role_arn)
        if error_retry_duration is not None:
            pulumi.set(__self__, "error_retry_duration", error_retry_duration)
        if full_load_error_percentage is not None:
            pulumi.set(__self__, "full_load_error_percentage", full_load_error_percentage)

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> str:
        """
        Endpoint for the Elasticsearch cluster.
        """
        return pulumi.get(self, "endpoint_uri")

    @property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> str:
        """
        Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Elasticsearch cluster.
        """
        return pulumi.get(self, "service_access_role_arn")

    @property
    @pulumi.getter(name="errorRetryDuration")
    def error_retry_duration(self) -> Optional[int]:
        """
        Maximum number of seconds for which DMS retries failed API requests to the Elasticsearch cluster. Defaults to `300`.
        """
        return pulumi.get(self, "error_retry_duration")

    @property
    @pulumi.getter(name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> Optional[int]:
        """
        Maximum percentage of records that can fail to be written before a full load operation stops. Defaults to `10`.
        """
        return pulumi.get(self, "full_load_error_percentage")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointKafkaSettings(dict):
    def __init__(__self__, *,
                 broker: str,
                 topic: Optional[str] = None):
        """
        :param str broker: Kafka broker location. Specify in the form broker-hostname-or-ip:port.
        :param str topic: Kafka topic for migration. Defaults to `kafka-default-topic`.
        """
        pulumi.set(__self__, "broker", broker)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter
    def broker(self) -> str:
        """
        Kafka broker location. Specify in the form broker-hostname-or-ip:port.
        """
        return pulumi.get(self, "broker")

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        """
        Kafka topic for migration. Defaults to `kafka-default-topic`.
        """
        return pulumi.get(self, "topic")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointKinesisSettings(dict):
    def __init__(__self__, *,
                 message_format: Optional[str] = None,
                 service_access_role_arn: Optional[str] = None,
                 stream_arn: Optional[str] = None):
        """
        :param str message_format: Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
        :param str service_access_role_arn: Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
        :param str stream_arn: Amazon Resource Name (ARN) of the Kinesis data stream.
        """
        if message_format is not None:
            pulumi.set(__self__, "message_format", message_format)
        if service_access_role_arn is not None:
            pulumi.set(__self__, "service_access_role_arn", service_access_role_arn)
        if stream_arn is not None:
            pulumi.set(__self__, "stream_arn", stream_arn)

    @property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[str]:
        """
        Output format for the records created. Defaults to `json`. Valid values are `json` and `json_unformatted` (a single line with no tab).
        """
        return pulumi.get(self, "message_format")

    @property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the IAM Role with permissions to write to the Kinesis data stream.
        """
        return pulumi.get(self, "service_access_role_arn")

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the Kinesis data stream.
        """
        return pulumi.get(self, "stream_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointMongodbSettings(dict):
    def __init__(__self__, *,
                 auth_mechanism: Optional[str] = None,
                 auth_source: Optional[str] = None,
                 auth_type: Optional[str] = None,
                 docs_to_investigate: Optional[str] = None,
                 extract_doc_id: Optional[str] = None,
                 nesting_level: Optional[str] = None):
        """
        :param str auth_mechanism: Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
        :param str auth_source: Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
        :param str auth_type: Authentication type to access the MongoDB source endpoint. Defaults to `password`.
        :param str docs_to_investigate: Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
        :param str extract_doc_id: Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
        :param str nesting_level: Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).
        """
        if auth_mechanism is not None:
            pulumi.set(__self__, "auth_mechanism", auth_mechanism)
        if auth_source is not None:
            pulumi.set(__self__, "auth_source", auth_source)
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if docs_to_investigate is not None:
            pulumi.set(__self__, "docs_to_investigate", docs_to_investigate)
        if extract_doc_id is not None:
            pulumi.set(__self__, "extract_doc_id", extract_doc_id)
        if nesting_level is not None:
            pulumi.set(__self__, "nesting_level", nesting_level)

    @property
    @pulumi.getter(name="authMechanism")
    def auth_mechanism(self) -> Optional[str]:
        """
        Authentication mechanism to access the MongoDB source endpoint. Defaults to `default`.
        """
        return pulumi.get(self, "auth_mechanism")

    @property
    @pulumi.getter(name="authSource")
    def auth_source(self) -> Optional[str]:
        """
        Authentication database name. Not used when `auth_type` is `no`. Defaults to `admin`.
        """
        return pulumi.get(self, "auth_source")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[str]:
        """
        Authentication type to access the MongoDB source endpoint. Defaults to `password`.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="docsToInvestigate")
    def docs_to_investigate(self) -> Optional[str]:
        """
        Number of documents to preview to determine the document organization. Use this setting when `nesting_level` is set to `one`. Defaults to `1000`.
        """
        return pulumi.get(self, "docs_to_investigate")

    @property
    @pulumi.getter(name="extractDocId")
    def extract_doc_id(self) -> Optional[str]:
        """
        Document ID. Use this setting when `nesting_level` is set to `none`. Defaults to `false`.
        """
        return pulumi.get(self, "extract_doc_id")

    @property
    @pulumi.getter(name="nestingLevel")
    def nesting_level(self) -> Optional[str]:
        """
        Specifies either document or table mode. Defaults to `none`. Valid values are `one` (table mode) and `none` (document mode).
        """
        return pulumi.get(self, "nesting_level")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class EndpointS3Settings(dict):
    def __init__(__self__, *,
                 bucket_folder: Optional[str] = None,
                 bucket_name: Optional[str] = None,
                 compression_type: Optional[str] = None,
                 csv_delimiter: Optional[str] = None,
                 csv_row_delimiter: Optional[str] = None,
                 date_partition_enabled: Optional[bool] = None,
                 external_table_definition: Optional[str] = None,
                 service_access_role_arn: Optional[str] = None):
        """
        :param str bucket_folder: S3 Bucket Object prefix.
        :param str bucket_name: S3 Bucket name.
        :param str compression_type: Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
        :param str csv_delimiter: Delimiter used to separate columns in the source files. Defaults to `,`.
        :param str csv_row_delimiter: Delimiter used to separate rows in the source files. Defaults to `\n`.
        :param bool date_partition_enabled: Partition S3 bucket folders based on transaction commit dates. Defaults to `false`.
        :param str external_table_definition: JSON document that describes how AWS DMS should interpret the data.
        :param str service_access_role_arn: Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
        """
        if bucket_folder is not None:
            pulumi.set(__self__, "bucket_folder", bucket_folder)
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if compression_type is not None:
            pulumi.set(__self__, "compression_type", compression_type)
        if csv_delimiter is not None:
            pulumi.set(__self__, "csv_delimiter", csv_delimiter)
        if csv_row_delimiter is not None:
            pulumi.set(__self__, "csv_row_delimiter", csv_row_delimiter)
        if date_partition_enabled is not None:
            pulumi.set(__self__, "date_partition_enabled", date_partition_enabled)
        if external_table_definition is not None:
            pulumi.set(__self__, "external_table_definition", external_table_definition)
        if service_access_role_arn is not None:
            pulumi.set(__self__, "service_access_role_arn", service_access_role_arn)

    @property
    @pulumi.getter(name="bucketFolder")
    def bucket_folder(self) -> Optional[str]:
        """
        S3 Bucket Object prefix.
        """
        return pulumi.get(self, "bucket_folder")

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[str]:
        """
        S3 Bucket name.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="compressionType")
    def compression_type(self) -> Optional[str]:
        """
        Set to compress target files. Defaults to `NONE`. Valid values are `GZIP` and `NONE`.
        """
        return pulumi.get(self, "compression_type")

    @property
    @pulumi.getter(name="csvDelimiter")
    def csv_delimiter(self) -> Optional[str]:
        """
        Delimiter used to separate columns in the source files. Defaults to `,`.
        """
        return pulumi.get(self, "csv_delimiter")

    @property
    @pulumi.getter(name="csvRowDelimiter")
    def csv_row_delimiter(self) -> Optional[str]:
        """
        Delimiter used to separate rows in the source files. Defaults to `\n`.
        """
        return pulumi.get(self, "csv_row_delimiter")

    @property
    @pulumi.getter(name="datePartitionEnabled")
    def date_partition_enabled(self) -> Optional[bool]:
        """
        Partition S3 bucket folders based on transaction commit dates. Defaults to `false`.
        """
        return pulumi.get(self, "date_partition_enabled")

    @property
    @pulumi.getter(name="externalTableDefinition")
    def external_table_definition(self) -> Optional[str]:
        """
        JSON document that describes how AWS DMS should interpret the data.
        """
        return pulumi.get(self, "external_table_definition")

    @property
    @pulumi.getter(name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) of the IAM Role with permissions to read from or write to the S3 Bucket.
        """
        return pulumi.get(self, "service_access_role_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


