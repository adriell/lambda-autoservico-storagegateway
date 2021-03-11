# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .http_namespace import *
from .private_dns_namespace import *
from .public_dns_namespace import *
from .service import *
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
            if typ == "aws:servicediscovery/httpNamespace:HttpNamespace":
                return HttpNamespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:servicediscovery/privateDnsNamespace:PrivateDnsNamespace":
                return PrivateDnsNamespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:servicediscovery/publicDnsNamespace:PublicDnsNamespace":
                return PublicDnsNamespace(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:servicediscovery/service:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "servicediscovery/httpNamespace", _module_instance)
    pulumi.runtime.register_resource_module("aws", "servicediscovery/privateDnsNamespace", _module_instance)
    pulumi.runtime.register_resource_module("aws", "servicediscovery/publicDnsNamespace", _module_instance)
    pulumi.runtime.register_resource_module("aws", "servicediscovery/service", _module_instance)

_register_module()