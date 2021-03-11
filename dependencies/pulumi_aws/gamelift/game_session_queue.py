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

__all__ = ['GameSessionQueue']


class GameSessionQueue(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destinations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 player_latency_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 timeout_in_seconds: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Gamelift Game Session Queue resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test = aws.gamelift.GameSessionQueue("test",
            destinations=[
                aws_gamelift_fleet["us_west_2_fleet"]["arn"],
                aws_gamelift_fleet["eu_central_1_fleet"]["arn"],
            ],
            player_latency_policies=[
                aws.gamelift.GameSessionQueuePlayerLatencyPolicyArgs(
                    maximum_individual_player_latency_milliseconds=100,
                    policy_duration_seconds=5,
                ),
                aws.gamelift.GameSessionQueuePlayerLatencyPolicyArgs(
                    maximum_individual_player_latency_milliseconds=200,
                ),
            ],
            timeout_in_seconds=60)
        ```

        ## Import

        Gamelift Game Session Queues can be imported by their `name`, e.g.

        ```sh
         $ pulumi import aws:gamelift/gameSessionQueue:GameSessionQueue example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destinations: List of fleet/alias ARNs used by session queue for placing game sessions.
        :param pulumi.Input[str] name: Name of the session queue.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]] player_latency_policies: One or more policies used to choose fleet based on player latency. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[int] timeout_in_seconds: Maximum time a game session request can remain in the queue.
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

            __props__['destinations'] = destinations
            __props__['name'] = name
            __props__['player_latency_policies'] = player_latency_policies
            __props__['tags'] = tags
            __props__['timeout_in_seconds'] = timeout_in_seconds
            __props__['arn'] = None
        super(GameSessionQueue, __self__).__init__(
            'aws:gamelift/gameSessionQueue:GameSessionQueue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            destinations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            player_latency_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            timeout_in_seconds: Optional[pulumi.Input[int]] = None) -> 'GameSessionQueue':
        """
        Get an existing GameSessionQueue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Game Session Queue ARN.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] destinations: List of fleet/alias ARNs used by session queue for placing game sessions.
        :param pulumi.Input[str] name: Name of the session queue.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GameSessionQueuePlayerLatencyPolicyArgs']]]] player_latency_policies: One or more policies used to choose fleet based on player latency. See below.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[int] timeout_in_seconds: Maximum time a game session request can remain in the queue.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["destinations"] = destinations
        __props__["name"] = name
        __props__["player_latency_policies"] = player_latency_policies
        __props__["tags"] = tags
        __props__["timeout_in_seconds"] = timeout_in_seconds
        return GameSessionQueue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Game Session Queue ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def destinations(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of fleet/alias ARNs used by session queue for placing game sessions.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the session queue.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="playerLatencyPolicies")
    def player_latency_policies(self) -> pulumi.Output[Optional[Sequence['outputs.GameSessionQueuePlayerLatencyPolicy']]]:
        """
        One or more policies used to choose fleet based on player latency. See below.
        """
        return pulumi.get(self, "player_latency_policies")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum time a game session request can remain in the queue.
        """
        return pulumi.get(self, "timeout_in_seconds")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
