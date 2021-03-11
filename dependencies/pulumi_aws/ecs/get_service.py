# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
]

@pulumi.output_type
class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, arn=None, cluster_arn=None, desired_count=None, id=None, launch_type=None, scheduling_strategy=None, service_name=None, task_definition=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cluster_arn and not isinstance(cluster_arn, str):
            raise TypeError("Expected argument 'cluster_arn' to be a str")
        pulumi.set(__self__, "cluster_arn", cluster_arn)
        if desired_count and not isinstance(desired_count, int):
            raise TypeError("Expected argument 'desired_count' to be a int")
        pulumi.set(__self__, "desired_count", desired_count)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if launch_type and not isinstance(launch_type, str):
            raise TypeError("Expected argument 'launch_type' to be a str")
        pulumi.set(__self__, "launch_type", launch_type)
        if scheduling_strategy and not isinstance(scheduling_strategy, str):
            raise TypeError("Expected argument 'scheduling_strategy' to be a str")
        pulumi.set(__self__, "scheduling_strategy", scheduling_strategy)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if task_definition and not isinstance(task_definition, str):
            raise TypeError("Expected argument 'task_definition' to be a str")
        pulumi.set(__self__, "task_definition", task_definition)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the ECS Service
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="clusterArn")
    def cluster_arn(self) -> str:
        return pulumi.get(self, "cluster_arn")

    @property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> int:
        """
        The number of tasks for the ECS Service
        """
        return pulumi.get(self, "desired_count")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> str:
        """
        The launch type for the ECS Service
        """
        return pulumi.get(self, "launch_type")

    @property
    @pulumi.getter(name="schedulingStrategy")
    def scheduling_strategy(self) -> str:
        """
        The scheduling strategy for the ECS Service
        """
        return pulumi.get(self, "scheduling_strategy")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> str:
        """
        The family for the latest ACTIVE revision
        """
        return pulumi.get(self, "task_definition")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            arn=self.arn,
            cluster_arn=self.cluster_arn,
            desired_count=self.desired_count,
            id=self.id,
            launch_type=self.launch_type,
            scheduling_strategy=self.scheduling_strategy,
            service_name=self.service_name,
            task_definition=self.task_definition)


def get_service(cluster_arn: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    The ECS Service data source allows access to details of a specific
    Service within a AWS ECS Cluster.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.ecs.get_service(service_name="example",
        cluster_arn=data["aws_ecs_cluster"]["example"]["arn"])
    ```


    :param str cluster_arn: The arn of the ECS Cluster
    :param str service_name: The name of the ECS Service
    """
    __args__ = dict()
    __args__['clusterArn'] = cluster_arn
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ecs/getService:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        arn=__ret__.arn,
        cluster_arn=__ret__.cluster_arn,
        desired_count=__ret__.desired_count,
        id=__ret__.id,
        launch_type=__ret__.launch_type,
        scheduling_strategy=__ret__.scheduling_strategy,
        service_name=__ret__.service_name,
        task_definition=__ret__.task_definition)