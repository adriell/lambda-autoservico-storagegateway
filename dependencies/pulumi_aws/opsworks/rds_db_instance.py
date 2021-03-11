# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['RdsDbInstance']


class RdsDbInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 db_password: Optional[pulumi.Input[str]] = None,
                 db_user: Optional[pulumi.Input[str]] = None,
                 rds_db_instance_arn: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an OpsWorks RDS DB Instance resource.

        > **Note:** All arguments including the username and password will be stored in the raw state as plain-text.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        my_instance = aws.opsworks.RdsDbInstance("myInstance",
            stack_id=aws_opsworks_stack["my_stack"]["id"],
            rds_db_instance_arn=aws_db_instance["my_instance"]["arn"],
            db_user="someUser",
            db_password="somePass")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_password: A db password
        :param pulumi.Input[str] db_user: A db username
        :param pulumi.Input[str] rds_db_instance_arn: The db instance to register for this stack. Changing this will force a new resource.
        :param pulumi.Input[str] stack_id: The stack to register a db instance for. Changing this will force a new resource.
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

            if db_password is None and not opts.urn:
                raise TypeError("Missing required property 'db_password'")
            __props__['db_password'] = db_password
            if db_user is None and not opts.urn:
                raise TypeError("Missing required property 'db_user'")
            __props__['db_user'] = db_user
            if rds_db_instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'rds_db_instance_arn'")
            __props__['rds_db_instance_arn'] = rds_db_instance_arn
            if stack_id is None and not opts.urn:
                raise TypeError("Missing required property 'stack_id'")
            __props__['stack_id'] = stack_id
        super(RdsDbInstance, __self__).__init__(
            'aws:opsworks/rdsDbInstance:RdsDbInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            db_password: Optional[pulumi.Input[str]] = None,
            db_user: Optional[pulumi.Input[str]] = None,
            rds_db_instance_arn: Optional[pulumi.Input[str]] = None,
            stack_id: Optional[pulumi.Input[str]] = None) -> 'RdsDbInstance':
        """
        Get an existing RdsDbInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] db_password: A db password
        :param pulumi.Input[str] db_user: A db username
        :param pulumi.Input[str] rds_db_instance_arn: The db instance to register for this stack. Changing this will force a new resource.
        :param pulumi.Input[str] stack_id: The stack to register a db instance for. Changing this will force a new resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["db_password"] = db_password
        __props__["db_user"] = db_user
        __props__["rds_db_instance_arn"] = rds_db_instance_arn
        __props__["stack_id"] = stack_id
        return RdsDbInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dbPassword")
    def db_password(self) -> pulumi.Output[str]:
        """
        A db password
        """
        return pulumi.get(self, "db_password")

    @property
    @pulumi.getter(name="dbUser")
    def db_user(self) -> pulumi.Output[str]:
        """
        A db username
        """
        return pulumi.get(self, "db_user")

    @property
    @pulumi.getter(name="rdsDbInstanceArn")
    def rds_db_instance_arn(self) -> pulumi.Output[str]:
        """
        The db instance to register for this stack. Changing this will force a new resource.
        """
        return pulumi.get(self, "rds_db_instance_arn")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        """
        The stack to register a db instance for. Changing this will force a new resource.
        """
        return pulumi.get(self, "stack_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
