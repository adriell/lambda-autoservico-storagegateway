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

__all__ = ['MethodSettings']


class MethodSettings(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 method_path: Optional[pulumi.Input[str]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[pulumi.InputType['MethodSettingsSettingsArgs']]] = None,
                 stage_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        `aws_api_gateway_method_settings` can be imported using `REST-API-ID/STAGE-NAME/METHOD-PATH`, e.g.

        ```sh
         $ pulumi import aws:apigateway/methodSettings:MethodSettings example 12345abcde/example/test/GET
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] method_path: Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*/*` for overriding all methods in the stage. Ensure to trim any leading forward slashes in the path (e.g. `trimprefix(aws_api_gateway_resource.example.path, "/")`).
        :param pulumi.Input[str] rest_api: The ID of the REST API
        :param pulumi.Input[pulumi.InputType['MethodSettingsSettingsArgs']] settings: The settings block, see below.
        :param pulumi.Input[str] stage_name: The name of the stage
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

            if method_path is None and not opts.urn:
                raise TypeError("Missing required property 'method_path'")
            __props__['method_path'] = method_path
            if rest_api is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api'")
            __props__['rest_api'] = rest_api
            if settings is None and not opts.urn:
                raise TypeError("Missing required property 'settings'")
            __props__['settings'] = settings
            if stage_name is None and not opts.urn:
                raise TypeError("Missing required property 'stage_name'")
            __props__['stage_name'] = stage_name
        super(MethodSettings, __self__).__init__(
            'aws:apigateway/methodSettings:MethodSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            method_path: Optional[pulumi.Input[str]] = None,
            rest_api: Optional[pulumi.Input[str]] = None,
            settings: Optional[pulumi.Input[pulumi.InputType['MethodSettingsSettingsArgs']]] = None,
            stage_name: Optional[pulumi.Input[str]] = None) -> 'MethodSettings':
        """
        Get an existing MethodSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] method_path: Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*/*` for overriding all methods in the stage. Ensure to trim any leading forward slashes in the path (e.g. `trimprefix(aws_api_gateway_resource.example.path, "/")`).
        :param pulumi.Input[str] rest_api: The ID of the REST API
        :param pulumi.Input[pulumi.InputType['MethodSettingsSettingsArgs']] settings: The settings block, see below.
        :param pulumi.Input[str] stage_name: The name of the stage
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["method_path"] = method_path
        __props__["rest_api"] = rest_api
        __props__["settings"] = settings
        __props__["stage_name"] = stage_name
        return MethodSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="methodPath")
    def method_path(self) -> pulumi.Output[str]:
        """
        Method path defined as `{resource_path}/{http_method}` for an individual method override, or `*/*` for overriding all methods in the stage. Ensure to trim any leading forward slashes in the path (e.g. `trimprefix(aws_api_gateway_resource.example.path, "/")`).
        """
        return pulumi.get(self, "method_path")

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[str]:
        """
        The ID of the REST API
        """
        return pulumi.get(self, "rest_api")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output['outputs.MethodSettingsSettings']:
        """
        The settings block, see below.
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Output[str]:
        """
        The name of the stage
        """
        return pulumi.get(self, "stage_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
