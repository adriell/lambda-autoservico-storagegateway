# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['LoadBalancerCookieStickinessPolicy']


class LoadBalancerCookieStickinessPolicy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cookie_expiration_period: Optional[pulumi.Input[int]] = None,
                 lb_port: Optional[pulumi.Input[int]] = None,
                 load_balancer: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a load balancer cookie stickiness policy, which allows an ELB to control the sticky session lifetime of the browser.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        lb = aws.elb.LoadBalancer("lb",
            availability_zones=["us-east-1a"],
            listeners=[aws.elb.LoadBalancerListenerArgs(
                instance_port=8000,
                instance_protocol="http",
                lb_port=80,
                lb_protocol="http",
            )])
        foo = aws.elb.LoadBalancerCookieStickinessPolicy("foo",
            load_balancer=lb.id,
            lb_port=80,
            cookie_expiration_period=600)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cookie_expiration_period: The time period after which
               the session cookie should be considered stale, expressed in seconds.
        :param pulumi.Input[int] lb_port: The load balancer port to which the policy
               should be applied. This must be an active listener on the load
               balancer.
        :param pulumi.Input[str] load_balancer: The load balancer to which the policy
               should be attached.
        :param pulumi.Input[str] name: The name of the stickiness policy.
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

            __props__['cookie_expiration_period'] = cookie_expiration_period
            if lb_port is None and not opts.urn:
                raise TypeError("Missing required property 'lb_port'")
            __props__['lb_port'] = lb_port
            if load_balancer is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer'")
            __props__['load_balancer'] = load_balancer
            __props__['name'] = name
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="aws:elasticloadbalancing/loadBalancerCookieStickinessPolicy:LoadBalancerCookieStickinessPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LoadBalancerCookieStickinessPolicy, __self__).__init__(
            'aws:elb/loadBalancerCookieStickinessPolicy:LoadBalancerCookieStickinessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cookie_expiration_period: Optional[pulumi.Input[int]] = None,
            lb_port: Optional[pulumi.Input[int]] = None,
            load_balancer: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'LoadBalancerCookieStickinessPolicy':
        """
        Get an existing LoadBalancerCookieStickinessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cookie_expiration_period: The time period after which
               the session cookie should be considered stale, expressed in seconds.
        :param pulumi.Input[int] lb_port: The load balancer port to which the policy
               should be applied. This must be an active listener on the load
               balancer.
        :param pulumi.Input[str] load_balancer: The load balancer to which the policy
               should be attached.
        :param pulumi.Input[str] name: The name of the stickiness policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cookie_expiration_period"] = cookie_expiration_period
        __props__["lb_port"] = lb_port
        __props__["load_balancer"] = load_balancer
        __props__["name"] = name
        return LoadBalancerCookieStickinessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cookieExpirationPeriod")
    def cookie_expiration_period(self) -> pulumi.Output[Optional[int]]:
        """
        The time period after which
        the session cookie should be considered stale, expressed in seconds.
        """
        return pulumi.get(self, "cookie_expiration_period")

    @property
    @pulumi.getter(name="lbPort")
    def lb_port(self) -> pulumi.Output[int]:
        """
        The load balancer port to which the policy
        should be applied. This must be an active listener on the load
        balancer.
        """
        return pulumi.get(self, "lb_port")

    @property
    @pulumi.getter(name="loadBalancer")
    def load_balancer(self) -> pulumi.Output[str]:
        """
        The load balancer to which the policy
        should be attached.
        """
        return pulumi.get(self, "load_balancer")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the stickiness policy.
        """
        return pulumi.get(self, "name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
