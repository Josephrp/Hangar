from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class Region(AbstractTerraformBlock):
    name: str
    _block_type: str = "block"
    _name: str = field(alias="_name", default="region")
    kms_key_arn: Optional[str] = None


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    create: Optional[str] = None
    delete: Optional[str] = None
    update: Optional[str] = None


@define(kw_only=True, slots=False)
class AwsSsmincidentsReplicationSet(AbstractTerraformResource):
    _group: Any
    _top_name: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ssmincidents_replication_set")
    region: Optional[Sequence[Region]] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
