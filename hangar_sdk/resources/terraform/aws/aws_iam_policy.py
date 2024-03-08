from typing import Any, Dict, Optional

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamPolicy(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_policy")
    description: Optional[str] = None
    name: Optional[str] = None
    name_prefix: Optional[str] = None
    path: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
