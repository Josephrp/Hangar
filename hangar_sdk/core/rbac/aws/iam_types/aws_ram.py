from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ram_privilege_type = Union[Literal["DeletePermissionVersion"], Literal["ListResources"], Literal["ListPermissions"], Literal["GetResourceShareInvitations"], Literal["UntagResource"], Literal["UpdateResourceShare"], Literal["DisassociateResourceSharePermission"], Literal["CreateResourceShare"], Literal["DeletePermission"], Literal["GetResourcePolicies"], Literal["ListReplacePermissionAssociationsWork"], Literal["SetDefaultPermissionVersion"], Literal["AssociateResourceShare"], Literal["ListPermissionAssociations"], Literal["DeleteResourceShare"], Literal["ReplacePermissionAssociations"], Literal["ListResourceTypes"], Literal["PromotePermissionCreatedFromPolicy"], Literal["GetResourceShares"], Literal["ListPermissionVersions"], Literal["ListPrincipals"], Literal["GetPermission"], Literal["GetResourceShareAssociations"], Literal["CreatePermissionVersion"], Literal["ListPendingInvitationResources"], Literal["AcceptResourceShareInvitation"], Literal["EnableSharingWithAwsOrganization"], Literal["PromoteResourceShareCreatedFromPolicy"], Literal["RejectResourceShareInvitation"], Literal["TagResource"], Literal["ListResourceSharePermissions"], Literal["DisassociateResourceShare"], Literal["CreatePermission"], Literal["AssociateResourceSharePermission"]]
aws_ram_condition_type = Union[Literal["ram:ResourceArn"], Literal["ram:ShareOwnerAccountId"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:TagKeys"], Literal["ram:AllowsExternalPrincipals"], Literal["ram:RequestedResourceType"], Literal["ram:ResourceTag/${TagKey}"], Literal["ram:ResourceShareName"], Literal["ram:PermissionArn"], Literal["ram:RequestedAllowsExternalPrincipals"], Literal["ram:Principal"], Literal["ram:PermissionResourceType"], Literal["aws:RequestTag/${TagKey}"]]

class aws_ramStatement(GenericResourceType[aws_ram_privilege_type, aws_ram_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    