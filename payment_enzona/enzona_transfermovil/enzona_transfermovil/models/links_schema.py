# coding: utf-8

"""
    TransferMovilAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LinksSchema(BaseModel):
    """
    LinksSchema
    """ # noqa: E501
    rel: Optional[StrictStr] = None
    method: Optional[StrictStr] = None
    href: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["rel", "method", "href"]

    @field_validator('rel')
    def rel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('confirm'):
            raise ValueError("must be one of enum values ('confirm')")
        return value

    @field_validator('method')
    def method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('REDIRECT'):
            raise ValueError("must be one of enum values ('REDIRECT')")
        return value

    @field_validator('href')
    def href_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('https://enzona.xetid.cu/checkout/1940841ec89d4f32aef06c813825920b/login'):
            raise ValueError("must be one of enum values ('https://enzona.xetid.cu/checkout/1940841ec89d4f32aef06c813825920b/login')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LinksSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LinksSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rel": obj.get("rel"),
            "method": obj.get("method"),
            "href": obj.get("href")
        })
        return _obj


