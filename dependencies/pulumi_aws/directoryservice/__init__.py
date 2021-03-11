# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .conditional_forwader import *
from .directory import *
from .get_directory import *
from .log_service import *
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
            if typ == "aws:directoryservice/conditionalForwader:ConditionalForwader":
                return ConditionalForwader(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:directoryservice/directory:Directory":
                return Directory(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:directoryservice/logService:LogService":
                return LogService(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "directoryservice/conditionalForwader", _module_instance)
    pulumi.runtime.register_resource_module("aws", "directoryservice/directory", _module_instance)
    pulumi.runtime.register_resource_module("aws", "directoryservice/logService", _module_instance)

_register_module()