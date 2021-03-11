# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .byte_match_set import *
from .geo_match_set import *
from .get_ipset import *
from .get_rate_based_mod import *
from .get_rule import *
from .get_web_acl import *
from .ip_set import *
from .rate_based_rule import *
from .regex_match_set import *
from .regex_pattern_set import *
from .rule import *
from .rule_group import *
from .size_constraint_set import *
from .sql_injection_match_set import *
from .web_acl import *
from .web_acl_association import *
from .xss_match_set import *
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
            if typ == "aws:wafregional/byteMatchSet:ByteMatchSet":
                return ByteMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/geoMatchSet:GeoMatchSet":
                return GeoMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/ipSet:IpSet":
                return IpSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/rateBasedRule:RateBasedRule":
                return RateBasedRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/regexMatchSet:RegexMatchSet":
                return RegexMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/regexPatternSet:RegexPatternSet":
                return RegexPatternSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/rule:Rule":
                return Rule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/ruleGroup:RuleGroup":
                return RuleGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/sizeConstraintSet:SizeConstraintSet":
                return SizeConstraintSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/sqlInjectionMatchSet:SqlInjectionMatchSet":
                return SqlInjectionMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/webAcl:WebAcl":
                return WebAcl(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/webAclAssociation:WebAclAssociation":
                return WebAclAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "aws:wafregional/xssMatchSet:XssMatchSet":
                return XssMatchSet(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("aws", "wafregional/byteMatchSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/geoMatchSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/ipSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/rateBasedRule", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/regexMatchSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/regexPatternSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/rule", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/ruleGroup", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/sizeConstraintSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/sqlInjectionMatchSet", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/webAcl", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/webAclAssociation", _module_instance)
    pulumi.runtime.register_resource_module("aws", "wafregional/xssMatchSet", _module_instance)

_register_module()
