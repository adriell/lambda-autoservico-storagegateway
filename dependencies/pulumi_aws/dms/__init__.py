# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .certificate import *
from .endpoint import *
from .event_subscription import *
from .replication_instance import *
from .replication_subnet_group import *
from .replication_task import *
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
            if typ == "aws:dms/certificate:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:dms/endpoint:Endpoint":
                return Endpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:dms/eventSubscription:EventSubscription":
                return EventSubscription(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:dms/replicationInstance:ReplicationInstance":
                return ReplicationInstance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:dms/replicationSubnetGroup:ReplicationSubnetGroup":
                return ReplicationSubnetGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:dms/replicationTask:ReplicationTask":
                return ReplicationTask(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "dms/certificate", _module_instance)
    pulumi.runtime.register_resource_module("aws", "dms/endpoint", _module_instance)
    pulumi.runtime.register_resource_module("aws", "dms/eventSubscription", _module_instance)
    pulumi.runtime.register_resource_module("aws", "dms/replicationInstance", _module_instance)
    pulumi.runtime.register_resource_module("aws", "dms/replicationSubnetGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "dms/replicationTask", _module_instance)

_register_module()