# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetPolicyDocumentResult',
    'AwaitableGetPolicyDocumentResult',
    'get_policy_document',
]

@pulumi.output_type
class GetPolicyDocumentResult:
    """
    A collection of values returned by getPolicyDocument.
    """
    def __init__(__self__, id=None, json=None, override_json=None, override_policy_documents=None, policy_id=None, source_json=None, source_policy_documents=None, statements=None, version=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if override_json and not isinstance(override_json, str):
            raise TypeError("Expected argument 'override_json' to be a str")
        pulumi.set(__self__, "override_json", override_json)
        if override_policy_documents and not isinstance(override_policy_documents, list):
            raise TypeError("Expected argument 'override_policy_documents' to be a list")
        pulumi.set(__self__, "override_policy_documents", override_policy_documents)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if source_json and not isinstance(source_json, str):
            raise TypeError("Expected argument 'source_json' to be a str")
        pulumi.set(__self__, "source_json", source_json)
        if source_policy_documents and not isinstance(source_policy_documents, list):
            raise TypeError("Expected argument 'source_policy_documents' to be a list")
        pulumi.set(__self__, "source_policy_documents", source_policy_documents)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        """
        Standard JSON policy document rendered based on the arguments above.
        """
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="overrideJson")
    def override_json(self) -> Optional[str]:
        return pulumi.get(self, "override_json")

    @property
    @pulumi.getter(name="overridePolicyDocuments")
    def override_policy_documents(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "override_policy_documents")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="sourceJson")
    def source_json(self) -> Optional[str]:
        return pulumi.get(self, "source_json")

    @property
    @pulumi.getter(name="sourcePolicyDocuments")
    def source_policy_documents(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "source_policy_documents")

    @property
    @pulumi.getter
    def statements(self) -> Optional[Sequence['outputs.GetPolicyDocumentStatementResult']]:
        return pulumi.get(self, "statements")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetPolicyDocumentResult(GetPolicyDocumentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPolicyDocumentResult(
            id=self.id,
            json=self.json,
            override_json=self.override_json,
            override_policy_documents=self.override_policy_documents,
            policy_id=self.policy_id,
            source_json=self.source_json,
            source_policy_documents=self.source_policy_documents,
            statements=self.statements,
            version=self.version)


def get_policy_document(override_json: Optional[str] = None,
                        override_policy_documents: Optional[Sequence[str]] = None,
                        policy_id: Optional[str] = None,
                        source_json: Optional[str] = None,
                        source_policy_documents: Optional[Sequence[str]] = None,
                        statements: Optional[Sequence[pulumi.InputType['GetPolicyDocumentStatementArgs']]] = None,
                        version: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPolicyDocumentResult:
    """
    Use this data source to access information about an existing resource.

    :param str override_json: IAM policy document whose statements with non-blank `sid`s will override statements with the same `sid` from documents assigned to the `source_json`, `source_policy_documents`, and `override_policy_documents` arguments. Non-overriding statements will be added to the exported document.
    :param Sequence[str] override_policy_documents: List of IAM policy documents that are merged together into the exported document. In merging, statements with non-blank `sid`s will override statements with the same `sid` from earlier documents in the list. Statements with non-blank `sid`s will also override statements with the same `sid` from documents provided in the `source_json` and `source_policy_documents` arguments.  Non-overriding statements will be added to the exported document.
    :param str policy_id: ID for the policy document.
    :param str source_json: IAM policy document used as a base for the exported policy document. Statements with the same `sid` from documents assigned to the `override_json` and `override_policy_documents` arguments will override source statements.
    :param Sequence[str] source_policy_documents: List of IAM policy documents that are merged together into the exported document. Statements defined in `source_policy_documents` or `source_json` must have unique `sid`s. Statements with the same `sid` from documents assigned to the `override_json` and `override_policy_documents` arguments will override source statements.
    :param Sequence[pulumi.InputType['GetPolicyDocumentStatementArgs']] statements: Configuration block for a policy statement. Detailed below.
    :param str version: IAM policy document version. Valid values are `2008-10-17` and `2012-10-17`. Defaults to `2012-10-17`. For more information, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_version.html).
    """
    __args__ = dict()
    __args__['overrideJson'] = override_json
    __args__['overridePolicyDocuments'] = override_policy_documents
    __args__['policyId'] = policy_id
    __args__['sourceJson'] = source_json
    __args__['sourcePolicyDocuments'] = source_policy_documents
    __args__['statements'] = statements
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:iam/getPolicyDocument:getPolicyDocument', __args__, opts=opts, typ=GetPolicyDocumentResult).value

    return AwaitableGetPolicyDocumentResult(
        id=__ret__.id,
        json=__ret__.json,
        override_json=__ret__.override_json,
        override_policy_documents=__ret__.override_policy_documents,
        policy_id=__ret__.policy_id,
        source_json=__ret__.source_json,
        source_policy_documents=__ret__.source_policy_documents,
        statements=__ret__.statements,
        version=__ret__.version)