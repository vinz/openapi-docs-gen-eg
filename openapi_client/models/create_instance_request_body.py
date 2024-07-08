# coding: utf-8

"""
    Web Forms API version 1.1

    The Web Forms API facilitates generating semantic HTML forms around everyday contracts. 

    The version of the OpenAPI document: 1.1.0
    Contact: devcenter@docusign.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.authentication_method import AuthenticationMethod
from typing import Optional, Set
from typing_extensions import Self

class CreateInstanceRequestBody(BaseModel):
    """
    Request body containing properties that will be used to create instance.
    """ # noqa: E501
    form_values: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="Key-value pairs (where key is the component name and value is the form value) used to create a form instance. For key of type TextBox, Email, Date, Select and RadioButtonGroup the value is of string type. For key of type Number, the value is of number type. For key of type of CheckboxGroup, the value is of type array of string.", alias="formValues")
    client_user_id: Annotated[str, Field(strict=True, max_length=100)] = Field(description="A unique identifier for a user that should originate from client's system. This value can be anything your backend system would use to track individual form instances. Examples include employee IDs, email addresses, surrogate key values, etc.", alias="clientUserId")
    authentication_instant: Optional[StrictStr] = Field(default=None, description="A sender-generated value that indicates the date and time that the signer was authenticated.", alias="authenticationInstant")
    authentication_method: Optional[AuthenticationMethod] = Field(default=None, alias="authenticationMethod")
    assertion_id: Optional[StrictStr] = Field(default=None, description="A unique identifier of the authentication event executed by the client application.", alias="assertionId")
    security_domain: Optional[StrictStr] = Field(default=None, description="The domain in which the user authenticated.", alias="securityDomain")
    return_url: Optional[StrictStr] = Field(default=None, description="The url to which the user is redirected after the signing is completed", alias="returnUrl")
    expiration_offset: Optional[Annotated[int, Field(le=23976, strict=True, ge=1)]] = Field(default=None, description="Specify the number of hours after which the form instance expires. For example, if the form expiration is set to 5 days, you should specify 120. The default value is 720 hours (30 days).", alias="expirationOffset")
    tags: Optional[List[StrictStr]] = Field(default=None, description="List of tags provided by the user with each request. This field is optional.")
    __properties: ClassVar[List[str]] = ["formValues", "clientUserId", "authenticationInstant", "authenticationMethod", "assertionId", "securityDomain", "returnUrl", "expirationOffset", "tags"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateInstanceRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateInstanceRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "formValues": obj.get("formValues"),
            "clientUserId": obj.get("clientUserId"),
            "authenticationInstant": obj.get("authenticationInstant"),
            "authenticationMethod": obj.get("authenticationMethod"),
            "assertionId": obj.get("assertionId"),
            "securityDomain": obj.get("securityDomain"),
            "returnUrl": obj.get("returnUrl"),
            "expirationOffset": obj.get("expirationOffset"),
            "tags": obj.get("tags")
        })
        return _obj


