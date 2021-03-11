# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_export import *
from .get_stack import *
from .stack import *
from .stack_set import *
from .stack_set_instance import *

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "aws:cloudformation/stack:Stack":
                return Stack(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:cloudformation/stackSet:StackSet":
                return StackSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:cloudformation/stackSetInstance:StackSetInstance":
                return StackSetInstance(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "cloudformation/stack", _module_instance)
    pulumi.runtime.register_resource_module("aws", "cloudformation/stackSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "cloudformation/stackSetInstance", _module_instance)

_register_module()