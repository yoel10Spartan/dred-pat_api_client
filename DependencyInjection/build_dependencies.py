from dataclasses import dataclass
from typing import Callable, cast
from Infrastructure.data.repositories import archeology, t12, t27
from Domain.unidades.Protocols.protocol_unidades import ProtocolUnidades
from Domain.archeology.Protocols.protocol_archeology import ProtocolArcheology

@dataclass(frozen=True)
class Dependencies:
    archeology_protocol: ProtocolArcheology
    t12_protocol: ProtocolUnidades
    t27_protocol: ProtocolUnidades

def _build_dependencies() -> Callable[[], Dependencies]:
    generate_dependencies = Dependencies(
        archeology_protocol=cast(ProtocolArcheology, archeology),
        t12_protocol=cast(ProtocolUnidades, t12),
        t27_protocol=cast(ProtocolUnidades, t27)
    )
    
    def dependencies() -> Dependencies:
        return generate_dependencies
    return dependencies

get_dependencies = _build_dependencies()