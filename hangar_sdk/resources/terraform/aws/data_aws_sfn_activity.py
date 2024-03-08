from typing import Any, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSfnActivity(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_sfn_activity")
    arn: Optional[str] = None
    name: Optional[str] = None
