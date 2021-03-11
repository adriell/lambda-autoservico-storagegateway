# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .attachment import *
from .get_ami_ids import *
from .get_group import *
from .group import *
from .lifecycle_hook import *
from .notification import *
from .policy import *
from .schedule import *
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
            if typ == "aws:autoscaling/attachment:Attachment":
                return Attachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:autoscaling/group:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:autoscaling/lifecycleHook:LifecycleHook":
                return LifecycleHook(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:autoscaling/notification:Notification":
                return Notification(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:autoscaling/policy:Policy":
                return Policy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:autoscaling/schedule:Schedule":
                return Schedule(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "autoscaling/attachment", _module_instance)
    pulumi.runtime.register_resource_module("aws", "autoscaling/group", _module_instance)
    pulumi.runtime.register_resource_module("aws", "autoscaling/lifecycleHook", _module_instance)
    pulumi.runtime.register_resource_module("aws", "autoscaling/notification", _module_instance)
    pulumi.runtime.register_resource_module("aws", "autoscaling/policy", _module_instance)
    pulumi.runtime.register_resource_module("aws", "autoscaling/schedule", _module_instance)

_register_module()