from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsSsmcontactsContactChannel(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    arn: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_ssmcontacts_contact_channel")