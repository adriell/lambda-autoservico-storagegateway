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

__all__ = ['Trigger']


class Trigger(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 predicate: Optional[pulumi.Input[pulumi.InputType['TriggerPredicateArgs']]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 workflow_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Glue Trigger resource.

        ## Example Usage
        ### Conditional Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            type="CONDITIONAL",
            actions=[aws.glue.TriggerActionArgs(
                job_name=aws_glue_job["example1"]["name"],
            )],
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    job_name=aws_glue_job["example2"]["name"],
                    state="SUCCEEDED",
                )],
            ))
        ```
        ### On-Demand Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            type="ON_DEMAND",
            actions=[aws.glue.TriggerActionArgs(
                job_name=aws_glue_job["example"]["name"],
            )])
        ```
        ### Scheduled Trigger

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            schedule="cron(15 12 * * ? *)",
            type="SCHEDULED",
            actions=[aws.glue.TriggerActionArgs(
                job_name=aws_glue_job["example"]["name"],
            )])
        ```
        ### Conditional Trigger with Crawler Action

        **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            type="CONDITIONAL",
            actions=[aws.glue.TriggerActionArgs(
                crawler_name=aws_glue_crawler["example1"]["name"],
            )],
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    job_name=aws_glue_job["example2"]["name"],
                    state="SUCCEEDED",
                )],
            ))
        ```
        ### Conditional Trigger with Crawler Condition

        **Note:** Triggers can have both a crawler action and a crawler condition, just no example provided.

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.glue.Trigger("example",
            type="CONDITIONAL",
            actions=[aws.glue.TriggerActionArgs(
                job_name=aws_glue_job["example1"]["name"],
            )],
            predicate=aws.glue.TriggerPredicateArgs(
                conditions=[aws.glue.TriggerPredicateConditionArgs(
                    crawler_name=aws_glue_crawler["example2"]["name"],
                    crawl_state="SUCCEEDED",
                )],
            ))
        ```

        ## Import

        Glue Triggers can be imported using `name`, e.g.

        ```sh
         $ pulumi import aws:glue/trigger:Trigger MyTrigger MyTrigger
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerActionArgs']]]] actions: List of actions initiated by this trigger when it fires. See Actions Below.
        :param pulumi.Input[str] description: A description of the new trigger.
        :param pulumi.Input[bool] enabled: Start the trigger. Defaults to `true`.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input[pulumi.InputType['TriggerPredicateArgs']] predicate: A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. See Predicate Below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] type: The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        :param pulumi.Input[str] workflow_name: A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
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

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__['actions'] = actions
            __props__['description'] = description
            __props__['enabled'] = enabled
            __props__['name'] = name
            __props__['predicate'] = predicate
            __props__['schedule'] = schedule
            __props__['tags'] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['workflow_name'] = workflow_name
            __props__['arn'] = None
            __props__['state'] = None
        super(Trigger, __self__).__init__(
            'aws:glue/trigger:Trigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerActionArgs']]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            predicate: Optional[pulumi.Input[pulumi.InputType['TriggerPredicateArgs']]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            workflow_name: Optional[pulumi.Input[str]] = None) -> 'Trigger':
        """
        Get an existing Trigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerActionArgs']]]] actions: List of actions initiated by this trigger when it fires. See Actions Below.
        :param pulumi.Input[str] arn: Amazon Resource Name (ARN) of Glue Trigger
        :param pulumi.Input[str] description: A description of the new trigger.
        :param pulumi.Input[bool] enabled: Start the trigger. Defaults to `true`.
        :param pulumi.Input[str] name: The name of the trigger.
        :param pulumi.Input[pulumi.InputType['TriggerPredicateArgs']] predicate: A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. See Predicate Below.
        :param pulumi.Input[str] schedule: A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        :param pulumi.Input[str] state: The condition job state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`. If this is specified, `job_name` must also be specified. Conflicts with `crawler_state`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value map of resource tags
        :param pulumi.Input[str] type: The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        :param pulumi.Input[str] workflow_name: A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["actions"] = actions
        __props__["arn"] = arn
        __props__["description"] = description
        __props__["enabled"] = enabled
        __props__["name"] = name
        __props__["predicate"] = predicate
        __props__["schedule"] = schedule
        __props__["state"] = state
        __props__["tags"] = tags
        __props__["type"] = type
        __props__["workflow_name"] = workflow_name
        return Trigger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence['outputs.TriggerAction']]:
        """
        List of actions initiated by this trigger when it fires. See Actions Below.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) of Glue Trigger
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the new trigger.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Start the trigger. Defaults to `true`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the trigger.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def predicate(self) -> pulumi.Output[Optional['outputs.TriggerPredicate']]:
        """
        A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. See Predicate Below.
        """
        return pulumi.get(self, "predicate")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[str]]:
        """
        A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The condition job state. Currently, the values supported are `SUCCEEDED`, `STOPPED`, `TIMEOUT` and `FAILED`. If this is specified, `job_name` must also be specified. Conflicts with `crawler_state`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value map of resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workflowName")
    def workflow_name(self) -> pulumi.Output[Optional[str]]:
        """
        A workflow to which the trigger should be associated to. Every workflow graph (DAG) needs a starting trigger (`ON_DEMAND` or `SCHEDULED` type) and can contain multiple additional `CONDITIONAL` triggers.
        """
        return pulumi.get(self, "workflow_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
