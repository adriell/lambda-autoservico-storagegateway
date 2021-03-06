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

__all__ = ['Repository']


class Repository(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_data: Optional[pulumi.Input[pulumi.InputType['RepositoryCatalogDataArgs']]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Public Elastic Container Registry Repository.

        ## Import

        ECR Public Repositories can be imported using the `repository_name`, e.g.

        ```sh
         $ pulumi import aws:ecrpublic/repository:Repository example example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RepositoryCatalogDataArgs']] catalog_data: Catalog data configuration for the repository. See below for schema.
        :param pulumi.Input[str] repository_name: Name of the repository.
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

            __props__['catalog_data'] = catalog_data
            __props__['force_destroy'] = force_destroy
            if repository_name is None and not opts.urn:
                raise TypeError("Missing required property 'repository_name'")
            __props__['repository_name'] = repository_name
            __props__['arn'] = None
            __props__['registry_id'] = None
            __props__['repository_uri'] = None
        super(Repository, __self__).__init__(
            'aws:ecrpublic/repository:Repository',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            catalog_data: Optional[pulumi.Input[pulumi.InputType['RepositoryCatalogDataArgs']]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            registry_id: Optional[pulumi.Input[str]] = None,
            repository_name: Optional[pulumi.Input[str]] = None,
            repository_uri: Optional[pulumi.Input[str]] = None) -> 'Repository':
        """
        Get an existing Repository resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: Full ARN of the repository.
        :param pulumi.Input[pulumi.InputType['RepositoryCatalogDataArgs']] catalog_data: Catalog data configuration for the repository. See below for schema.
        :param pulumi.Input[str] registry_id: The registry ID where the repository was created.
        :param pulumi.Input[str] repository_name: Name of the repository.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["catalog_data"] = catalog_data
        __props__["force_destroy"] = force_destroy
        __props__["registry_id"] = registry_id
        __props__["repository_name"] = repository_name
        __props__["repository_uri"] = repository_uri
        return Repository(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Full ARN of the repository.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="catalogData")
    def catalog_data(self) -> pulumi.Output[Optional['outputs.RepositoryCatalogData']]:
        """
        Catalog data configuration for the repository. See below for schema.
        """
        return pulumi.get(self, "catalog_data")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> pulumi.Output[str]:
        """
        The registry ID where the repository was created.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[str]:
        """
        Name of the repository.
        """
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter(name="repositoryUri")
    def repository_uri(self) -> pulumi.Output[str]:
        return pulumi.get(self, "repository_uri")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

