from typing import Any, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import (
    AbstractTerraformBlock,
    AbstractTerraformDatasource,
)


@define(kw_only=True, slots=False)
class Filter(AbstractTerraformBlock):
    name: str
    values: Sequence[str]
    _block_type: str = "block"
    _name: str = field(alias="_name", default="filter")


@define(kw_only=True, slots=False)
class Timeouts(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="timeouts")
    read: Optional[str] = None


@define(kw_only=True, slots=False)
class DataAwsEc2InstanceTypeOffering(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ec2_instance_type_offering")
    filter: Optional[Sequence[Filter]] = None
    location_type: Optional[str] = None
    preferred_instance_types: Optional[Sequence[str]] = None
    timeouts: Optional[Timeouts] = None
