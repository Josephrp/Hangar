from typing import Any, Dict, Optional, Sequence

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
class DataAwsEc2LocalGatewayRouteTable(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ec2_local_gateway_route_table")
    filter: Optional[Sequence[Filter]] = None
    local_gateway_id: Optional[str] = None
    local_gateway_route_table_id: Optional[str] = None
    outpost_arn: Optional[str] = None
    state: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    timeouts: Optional[Timeouts] = None
