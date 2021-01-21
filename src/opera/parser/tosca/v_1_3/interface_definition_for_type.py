from .notification_definition import NotificationDefinition
from .operation_definition_for_type import OperationDefinitionForType
from .property_definition import PropertyDefinition
from ..entity import Entity
from ..map import Map
from ..reference import Reference


class InterfaceDefinitionForType(Entity):
    ATTRS = dict(
        type=Reference("interface_types"),
        inputs=Map(PropertyDefinition),
        operations=Map(OperationDefinitionForType),
        notifications=Map(NotificationDefinition),
    )
