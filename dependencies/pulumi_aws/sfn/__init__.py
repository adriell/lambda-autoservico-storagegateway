# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .activity import *
from .get_activity import *
from .get_state_machine import *
from .state_machine import *
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
            if typ == "aws:sfn/activity:Activity":
                return Activity(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:sfn/stateMachine:StateMachine":
                return StateMachine(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "sfn/activity", _module_instance)
    pulumi.runtime.register_resource_module("aws", "sfn/stateMachine", _module_instance)

_register_module()