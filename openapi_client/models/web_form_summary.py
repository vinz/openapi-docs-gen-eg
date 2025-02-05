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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.web_form_metadata import WebFormMetadata
from openapi_client.models.web_form_properties import WebFormProperties
from openapi_client.models.web_form_state import WebFormState
from typing import Optional, Set
from typing_extensions import Self

class WebFormSummary(BaseModel):
    """
    An object that summarizes an instance of a form that can be used to display a listing
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for a Web Form that is consistent for it's lifetime")
    account_id: Optional[StrictStr] = Field(default=None, description="Account identifier in which the web form resides", alias="accountId")
    is_published: Optional[StrictBool] = Field(default=None, description="Has the form been published", alias="isPublished")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Is the form currently enabled and available for data collection", alias="isEnabled")
    has_draft_changes: Optional[StrictBool] = Field(default=None, description="Does the form have draft changes that need to be published?", alias="hasDraftChanges")
    form_state: Optional[WebFormState] = Field(default=None, alias="formState")
    form_properties: Optional[WebFormProperties] = Field(default=None, alias="formProperties")
    form_metadata: Optional[WebFormMetadata] = Field(default=None, alias="formMetadata")
    __properties: ClassVar[List[str]] = ["id", "accountId", "isPublished", "isEnabled", "hasDraftChanges", "formState", "formProperties", "formMetadata"]

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
        """Create an instance of WebFormSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of form_properties
        if self.form_properties:
            _dict['formProperties'] = self.form_properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of form_metadata
        if self.form_metadata:
            _dict['formMetadata'] = self.form_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebFormSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "isPublished": obj.get("isPublished"),
            "isEnabled": obj.get("isEnabled"),
            "hasDraftChanges": obj.get("hasDraftChanges"),
            "formState": obj.get("formState"),
            "formProperties": WebFormProperties.from_dict(obj["formProperties"]) if obj.get("formProperties") is not None else None,
            "formMetadata": WebFormMetadata.from_dict(obj["formMetadata"]) if obj.get("formMetadata") is not None else None
        })
        return _obj


