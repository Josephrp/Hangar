from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformDatasource


@define(kw_only=True, slots=False)
class DataAwsIamInstanceProfiles(AbstractTerraformDatasource):
    _group: Any
    _top_name: str
    role_name: str
    _block_type: str = "datasource"
    _name: str = field(alias="_name", default="aws_iam_instance_profiles")
