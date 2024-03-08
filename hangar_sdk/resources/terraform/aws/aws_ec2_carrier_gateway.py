from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsEc2CarrierGateway(AbstractTerraformResource):
    _group: Any
    _top_name: str
    vpc_id: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_ec2_carrier_gateway")
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
