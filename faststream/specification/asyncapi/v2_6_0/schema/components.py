from pydantic import BaseModel

from faststream._internal._compat import (
    PYDANTIC_V2,
)
from faststream._internal.basic_types import AnyDict
from faststream.specification.asyncapi.v2_6_0.schema.message import Message


class Components(BaseModel):
    # TODO
    # servers
    # serverVariables
    # channels
    """A class to represent components in a system.

    Attributes:
        messages : Optional dictionary of messages
        schemas : Optional dictionary of schemas

    Note:
        The following attributes are not implemented yet:
        - servers
        - serverVariables
        - channels
        - securitySchemes
        - parameters
        - correlationIds
        - operationTraits
        - messageTraits
        - serverBindings
        - channelBindings
        - operationBindings
        - messageBindings
    """

    messages: dict[str, Message] | None = None
    schemas: dict[str, AnyDict] | None = None
    securitySchemes: dict[str, AnyDict] | None = None

    if PYDANTIC_V2:
        model_config = {"extra": "allow"}

    else:

        class Config:
            extra = "allow"
