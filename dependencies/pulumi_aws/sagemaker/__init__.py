# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .app import *
from .app_image_config import *
from .code_repository import *
from .domain import *
from .endpoint import *
from .endpoint_configuration import *
from .feature_group import *
from .get_prebuilt_ecr_image import *
from .image import *
from .image_version import *
from .model import *
from .model_package_group import *
from .notebook_instance import *
from .notebook_instance_lifecycle_configuration import *
from .user_profile import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:sagemaker/app:App":
                return App(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/appImageConfig:AppImageConfig":
                return AppImageConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/codeRepository:CodeRepository":
                return CodeRepository(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/domain:Domain":
                return Domain(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/endpoint:Endpoint":
                return Endpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/endpointConfiguration:EndpointConfiguration":
                return EndpointConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/featureGroup:FeatureGroup":
                return FeatureGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/image:Image":
                return Image(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/imageVersion:ImageVersion":
                return ImageVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/model:Model":
                return Model(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/modelPackageGroup:ModelPackageGroup":
                return ModelPackageGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/notebookInstance:NotebookInstance":
                return NotebookInstance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/notebookInstanceLifecycleConfiguration:NotebookInstanceLifecycleConfiguration":
                return NotebookInstanceLifecycleConfiguration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sagemaker/userProfile:UserProfile":
                return UserProfile(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "sagemaker/app", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/appImageConfig", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/codeRepository", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/domain", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/endpoint", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/endpointConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/featureGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/image", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/imageVersion", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/model", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/modelPackageGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/notebookInstance", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/notebookInstanceLifecycleConfiguration", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sagemaker/userProfile", _module_instance)

_register_module()
