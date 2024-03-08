from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsMemorydbSubnetGroup(AbstractTerraformResource):
    _group: Any
    _top_name: str
    subnet_ids: Sequence[str]
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_memorydb_subnet_group")
    description: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
