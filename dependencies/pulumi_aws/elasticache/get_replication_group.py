# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetReplicationGroupResult',
    'AwaitableGetReplicationGroupResult',
    'get_replication_group',
]

@pulumi.output_type
class GetReplicationGroupResult:
    """
    A collection of values returned by getReplicationGroup.
    """
    def __init__(__self__, arn=None, auth_token_enabled=None, automatic_failover_enabled=None, configuration_endpoint_address=None, id=None, member_clusters=None, multi_az_enabled=None, node_type=None, number_cache_clusters=None, port=None, primary_endpoint_address=None, reader_endpoint_address=None, replication_group_description=None, replication_group_id=None, snapshot_retention_limit=None, snapshot_window=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if auth_token_enabled and not isinstance(auth_token_enabled, bool):
            raise TypeError("Expected argument 'auth_token_enabled' to be a bool")
        pulumi.set(__self__, "auth_token_enabled", auth_token_enabled)
        if automatic_failover_enabled and not isinstance(automatic_failover_enabled, bool):
            raise TypeError("Expected argument 'automatic_failover_enabled' to be a bool")
        pulumi.set(__self__, "automatic_failover_enabled", automatic_failover_enabled)
        if configuration_endpoint_address and not isinstance(configuration_endpoint_address, str):
            raise TypeError("Expected argument 'configuration_endpoint_address' to be a str")
        pulumi.set(__self__, "configuration_endpoint_address", configuration_endpoint_address)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_clusters and not isinstance(member_clusters, list):
            raise TypeError("Expected argument 'member_clusters' to be a list")
        pulumi.set(__self__, "member_clusters", member_clusters)
        if multi_az_enabled and not isinstance(multi_az_enabled, bool):
            raise TypeError("Expected argument 'multi_az_enabled' to be a bool")
        pulumi.set(__self__, "multi_az_enabled", multi_az_enabled)
        if node_type and not isinstance(node_type, str):
            raise TypeError("Expected argument 'node_type' to be a str")
        pulumi.set(__self__, "node_type", node_type)
        if number_cache_clusters and not isinstance(number_cache_clusters, int):
            raise TypeError("Expected argument 'number_cache_clusters' to be a int")
        pulumi.set(__self__, "number_cache_clusters", number_cache_clusters)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if primary_endpoint_address and not isinstance(primary_endpoint_address, str):
            raise TypeError("Expected argument 'primary_endpoint_address' to be a str")
        pulumi.set(__self__, "primary_endpoint_address", primary_endpoint_address)
        if reader_endpoint_address and not isinstance(reader_endpoint_address, str):
            raise TypeError("Expected argument 'reader_endpoint_address' to be a str")
        pulumi.set(__self__, "reader_endpoint_address", reader_endpoint_address)
        if replication_group_description and not isinstance(replication_group_description, str):
            raise TypeError("Expected argument 'replication_group_description' to be a str")
        pulumi.set(__self__, "replication_group_description", replication_group_description)
        if replication_group_id and not isinstance(replication_group_id, str):
            raise TypeError("Expected argument 'replication_group_id' to be a str")
        pulumi.set(__self__, "replication_group_id", replication_group_id)
        if snapshot_retention_limit and not isinstance(snapshot_retention_limit, int):
            raise TypeError("Expected argument 'snapshot_retention_limit' to be a int")
        pulumi.set(__self__, "snapshot_retention_limit", snapshot_retention_limit)
        if snapshot_window and not isinstance(snapshot_window, str):
            raise TypeError("Expected argument 'snapshot_window' to be a str")
        pulumi.set(__self__, "snapshot_window", snapshot_window)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the created ElastiCache Replication Group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authTokenEnabled")
    def auth_token_enabled(self) -> bool:
        """
        Specifies whether an AuthToken (password) is enabled.
        """
        return pulumi.get(self, "auth_token_enabled")

    @property
    @pulumi.getter(name="automaticFailoverEnabled")
    def automatic_failover_enabled(self) -> bool:
        """
        A flag whether a read-only replica will be automatically promoted to read/write primary if the existing primary fails.
        """
        return pulumi.get(self, "automatic_failover_enabled")

    @property
    @pulumi.getter(name="configurationEndpointAddress")
    def configuration_endpoint_address(self) -> str:
        """
        The configuration endpoint address to allow host discovery.
        """
        return pulumi.get(self, "configuration_endpoint_address")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberClusters")
    def member_clusters(self) -> Sequence[str]:
        """
        The identifiers of all the nodes that are part of this replication group.
        """
        return pulumi.get(self, "member_clusters")

    @property
    @pulumi.getter(name="multiAzEnabled")
    def multi_az_enabled(self) -> bool:
        """
        Specifies whether Multi-AZ Support is enabled for the replication group.
        """
        return pulumi.get(self, "multi_az_enabled")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> str:
        """
        The cluster node type.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="numberCacheClusters")
    def number_cache_clusters(self) -> int:
        """
        The number of cache clusters that the replication group has.
        """
        return pulumi.get(self, "number_cache_clusters")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port number on which the configuration endpoint will accept connections.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="primaryEndpointAddress")
    def primary_endpoint_address(self) -> str:
        """
        The endpoint of the primary node in this node group (shard).
        """
        return pulumi.get(self, "primary_endpoint_address")

    @property
    @pulumi.getter(name="readerEndpointAddress")
    def reader_endpoint_address(self) -> str:
        """
        The endpoint of the reader node in this node group (shard).
        """
        return pulumi.get(self, "reader_endpoint_address")

    @property
    @pulumi.getter(name="replicationGroupDescription")
    def replication_group_description(self) -> str:
        """
        The description of the replication group.
        """
        return pulumi.get(self, "replication_group_description")

    @property
    @pulumi.getter(name="replicationGroupId")
    def replication_group_id(self) -> str:
        return pulumi.get(self, "replication_group_id")

    @property
    @pulumi.getter(name="snapshotRetentionLimit")
    def snapshot_retention_limit(self) -> int:
        """
        The number of days for which ElastiCache retains automatic cache cluster snapshots before deleting them.
        """
        return pulumi.get(self, "snapshot_retention_limit")

    @property
    @pulumi.getter(name="snapshotWindow")
    def snapshot_window(self) -> str:
        """
        The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
        """
        return pulumi.get(self, "snapshot_window")


class AwaitableGetReplicationGroupResult(GetReplicationGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationGroupResult(
            arn=self.arn,
            auth_token_enabled=self.auth_token_enabled,
            automatic_failover_enabled=self.automatic_failover_enabled,
            configuration_endpoint_address=self.configuration_endpoint_address,
            id=self.id,
            member_clusters=self.member_clusters,
            multi_az_enabled=self.multi_az_enabled,
            node_type=self.node_type,
            number_cache_clusters=self.number_cache_clusters,
            port=self.port,
            primary_endpoint_address=self.primary_endpoint_address,
            reader_endpoint_address=self.reader_endpoint_address,
            replication_group_description=self.replication_group_description,
            replication_group_id=self.replication_group_id,
            snapshot_retention_limit=self.snapshot_retention_limit,
            snapshot_window=self.snapshot_window)


def get_replication_group(replication_group_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationGroupResult:
    """
    Use this data source to get information about an Elasticache Replication Group.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    bar = aws.elasticache.get_replication_group(replication_group_id="example")
    ```


    :param str replication_group_id: The identifier for the replication group.
    """
    __args__ = dict()
    __args__['replicationGroupId'] = replication_group_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:elasticache/getReplicationGroup:getReplicationGroup', __args__, opts=opts, typ=GetReplicationGroupResult).value

    return AwaitableGetReplicationGroupResult(
        arn=__ret__.arn,
        auth_token_enabled=__ret__.auth_token_enabled,
        automatic_failover_enabled=__ret__.automatic_failover_enabled,
        configuration_endpoint_address=__ret__.configuration_endpoint_address,
        id=__ret__.id,
        member_clusters=__ret__.member_clusters,
        multi_az_enabled=__ret__.multi_az_enabled,
        node_type=__ret__.node_type,
        number_cache_clusters=__ret__.number_cache_clusters,
        port=__ret__.port,
        primary_endpoint_address=__ret__.primary_endpoint_address,
        reader_endpoint_address=__ret__.reader_endpoint_address,
        replication_group_description=__ret__.replication_group_description,
        replication_group_id=__ret__.replication_group_id,
        snapshot_retention_limit=__ret__.snapshot_retention_limit,
        snapshot_window=__ret__.snapshot_window)
