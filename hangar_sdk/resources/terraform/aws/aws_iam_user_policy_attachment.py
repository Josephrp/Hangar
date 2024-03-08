from typing import Any

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformResource


@define(kw_only=True, slots=False)
class AwsIamUserPolicyAttachment(AbstractTerraformResource):
    _group: Any
    _top_name: str
    policy_arn: str
    user: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_iam_user_policy_attachment")
