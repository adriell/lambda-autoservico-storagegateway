# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'GetCipherTextResult',
    'AwaitableGetCipherTextResult',
    'get_cipher_text',
]

@pulumi.output_type
class GetCipherTextResult:
    """
    A collection of values returned by getCipherText.
    """
    def __init__(__self__, ciphertext_blob=None, context=None, id=None, key_id=None, plaintext=None):
        if ciphertext_blob and not isinstance(ciphertext_blob, str):
            raise TypeError("Expected argument 'ciphertext_blob' to be a str")
        pulumi.set(__self__, "ciphertext_blob", ciphertext_blob)
        if context and not isinstance(context, dict):
            raise TypeError("Expected argument 'context' to be a dict")
        pulumi.set(__self__, "context", context)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_id and not isinstance(key_id, str):
            raise TypeError("Expected argument 'key_id' to be a str")
        pulumi.set(__self__, "key_id", key_id)
        if plaintext and not isinstance(plaintext, str):
            raise TypeError("Expected argument 'plaintext' to be a str")
        pulumi.set(__self__, "plaintext", plaintext)

    @property
    @pulumi.getter(name="ciphertextBlob")
    def ciphertext_blob(self) -> str:
        """
        Base64 encoded ciphertext
        """
        return pulumi.get(self, "ciphertext_blob")

    @property
    @pulumi.getter
    def context(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "context")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> str:
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def plaintext(self) -> str:
        return pulumi.get(self, "plaintext")


class AwaitableGetCipherTextResult(GetCipherTextResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCipherTextResult(
            ciphertext_blob=self.ciphertext_blob,
            context=self.context,
            id=self.id,
            key_id=self.key_id,
            plaintext=self.plaintext)


def get_cipher_text(context: Optional[Mapping[str, str]] = None,
                    key_id: Optional[str] = None,
                    plaintext: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCipherTextResult:
    """
    The KMS ciphertext data source allows you to encrypt plaintext into ciphertext
    by using an AWS KMS customer master key. The value returned by this data source
    changes every apply. For a stable ciphertext value, see the `kms.Ciphertext`
    resource.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    oauth_config = aws.kms.Key("oauthConfig",
        description="oauth config",
        is_enabled=True)
    oauth = oauth_config.key_id.apply(lambda key_id: aws.kms.get_cipher_text(key_id=key_id,
        plaintext=\"\"\"{
      "client_id": "e587dbae22222f55da22",
      "client_secret": "8289575d00000ace55e1815ec13673955721b8a5"
    }
    \"\"\"))
    ```


    :param Mapping[str, str] context: An optional mapping that makes up the encryption context.
    :param str key_id: Globally unique key ID for the customer master key.
    :param str plaintext: Data to be encrypted. Note that this may show up in logs, and it will be stored in the state file.
    """
    __args__ = dict()
    __args__['context'] = context
    __args__['keyId'] = key_id
    __args__['plaintext'] = plaintext
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:kms/getCipherText:getCipherText', __args__, opts=opts, typ=GetCipherTextResult).value

    return AwaitableGetCipherTextResult(
        ciphertext_blob=__ret__.ciphertext_blob,
        context=__ret__.context,
        id=__ret__.id,
        key_id=__ret__.key_id,
        plaintext=__ret__.plaintext)
