# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .compute_environment import *
from .get_compute_environment import *
from .get_job_queue import *
from .job_definition import *
from .job_queue import *
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
            if typ == "aws:batch/computeEnvironment:ComputeEnvironment":
                return ComputeEnvironment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:batch/jobDefinition:JobDefinition":
                return JobDefinition(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:batch/jobQueue:JobQueue":
                return JobQueue(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "batch/computeEnvironment", _module_instance)
    pulumi.runtime.register_resource_module("aws", "batch/jobDefinition", _module_instance)
    pulumi.runtime.register_resource_module("aws", "batch/jobQueue", _module_instance)

_register_module()