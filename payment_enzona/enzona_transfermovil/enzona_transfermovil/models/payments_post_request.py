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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from enzona_transfermovil.models.payments_post_request_items_inner import PaymentsPostRequestItemsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PaymentsPostRequest(BaseModel):
    """
    PaymentsPostRequest
    """ # noqa: E501
    description: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    items: Optional[List[PaymentsPostRequestItemsInner]] = None
    merchant_op_id: Optional[StrictStr] = None
    invoice_number: Optional[StrictStr] = None
    return_url: Optional[StrictStr] = None
    cancel_url: Optional[StrictStr] = None
    terminal_id: Optional[StrictStr] = None
    merchant_uuid: Optional[StrictStr] = None
    valid_time: Optional[Union[StrictFloat, StrictInt]] = None
    username: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["description", "currency", "amount", "items", "merchant_op_id", "invoice_number", "return_url", "cancel_url", "terminal_id", "merchant_uuid", "valid_time", "username"]

    @field_validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CUP', 'CUC'):
            raise ValueError("must be one of enum values ('CUP', 'CUC')")
        return value

    @field_validator('merchant_op_id')
    def merchant_op_id_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('123456789123'):
            raise ValueError("must be one of enum values ('123456789123')")
        return value

    @field_validator('invoice_number')
    def invoice_number_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('1212'):
            raise ValueError("must be one of enum values ('1212')")
        return value

    @field_validator('return_url')
    def return_url_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('https://mymerchant.cu/return'):
            raise ValueError("must be one of enum values ('https://mymerchant.cu/return')")
        return value

    @field_validator('cancel_url')
    def cancel_url_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('https://mymerchant.cu/cancel'):
            raise ValueError("must be one of enum values ('https://mymerchant.cu/cancel')")
        return value

    @field_validator('terminal_id')
    def terminal_id_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('12356'):
            raise ValueError("must be one of enum values ('12356')")
        return value

    @field_validator('merchant_uuid')
    def merchant_uuid_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('f89c79c8dfbd43939cdc43cf47b1ee47'):
            raise ValueError("must be one of enum values ('f89c79c8dfbd43939cdc43cf47b1ee47')")
        return value

    @field_validator('username')
    def username_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('user'):
            raise ValueError("must be one of enum values ('user')")
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
        """Create an instance of PaymentsPostRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PaymentsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "currency": obj.get("currency"),
            "amount": obj.get("amount"),
            "items": [PaymentsPostRequestItemsInner.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "merchant_op_id": obj.get("merchant_op_id"),
            "invoice_number": obj.get("invoice_number"),
            "return_url": obj.get("return_url"),
            "cancel_url": obj.get("cancel_url"),
            "terminal_id": obj.get("terminal_id"),
            "merchant_uuid": obj.get("merchant_uuid"),
            "valid_time": obj.get("valid_time"),
            "username": obj.get("username")
        })
        return _obj


