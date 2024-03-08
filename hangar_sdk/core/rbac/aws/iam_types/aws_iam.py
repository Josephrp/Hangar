from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iam_privilege_type = Union[Literal["DeleteServiceSpecificCredential"], Literal["UploadSSHPublicKey"], Literal["DeleteAccountPasswordPolicy"], Literal["DeleteRolePermissionsBoundary"], Literal["ListGroupPolicies"], Literal["ListPoliciesGrantingServiceAccess"], Literal["ListPolicyVersions"], Literal["CreateRole"], Literal["ListAttachedUserPolicies"], Literal["DeleteRole"], Literal["ListUsers"], Literal["TagOpenIDConnectProvider"], Literal["CreateServiceSpecificCredential"], Literal["CreateGroup"], Literal["GetContextKeysForPrincipalPolicy"], Literal["CreateVirtualMFADevice"], Literal["SetSTSRegionalEndpointStatus"], Literal["ListSigningCertificates"], Literal["GetInstanceProfile"], Literal["SetSecurityTokenServicePreferences"], Literal["UntagPolicy"], Literal["AddRoleToInstanceProfile"], Literal["SimulateCustomPolicy"], Literal["UpdateServerCertificate"], Literal["ListPolicyTags"], Literal["DeactivateMFADevice"], Literal["PutUserPermissionsBoundary"], Literal["GetPolicy"], Literal["ResyncMFADevice"], Literal["ChangePassword"], Literal["ListSSHPublicKeys"], Literal["ListOpenIDConnectProviderTags"], Literal["UpdateServiceSpecificCredential"], Literal["ListSAMLProviderTags"], Literal["GetOpenIDConnectProvider"], Literal["GetUserPolicy"], Literal["PutUserPolicy"], Literal["UpdateSSHPublicKey"], Literal["ListRoles"], Literal["ListRolePolicies"], Literal["ListServerCertificates"], Literal["TagServerCertificate"], Literal["DeleteCloudFrontPublicKey"], Literal["UntagInstanceProfile"], Literal["DeleteRolePolicy"], Literal["TagSAMLProvider"], Literal["DeleteSSHPublicKey"], Literal["DeleteGroupPolicy"], Literal["GetAccountSummary"], Literal["ListAttachedGroupPolicies"], Literal["UpdateAccountName"], Literal["GetServiceLastAccessedDetailsWithEntities"], Literal["UpdateRoleDescription"], Literal["DeleteLoginProfile"], Literal["CreateSAMLProvider"], Literal["GetMFADevice"], Literal["ListSAMLProviders"], Literal["GetPolicyVersion"], Literal["UntagUser"], Literal["UploadServerCertificate"], Literal["GetGroupPolicy"], Literal["GetAccessKeyLastUsed"], Literal["UntagRole"], Literal["TagPolicy"], Literal["GetServerCertificate"], Literal["ListInstanceProfilesForRole"], Literal["GetCloudFrontPublicKey"], Literal["SetDefaultPolicyVersion"], Literal["CreatePolicy"], Literal["ListGroups"], Literal["GetServiceLinkedRoleDeletionStatus"], Literal["ListAttachedRolePolicies"], Literal["ListUserPolicies"], Literal["AttachUserPolicy"], Literal["UpdateSigningCertificate"], Literal["UpdateRole"], Literal["RemoveClientIDFromOpenIDConnectProvider"], Literal["PutRolePermissionsBoundary"], Literal["UploadSigningCertificate"], Literal["RemoveRoleFromInstanceProfile"], Literal["ListGroupsForUser"], Literal["DeleteUser"], Literal["UntagOpenIDConnectProvider"], Literal["DeleteAccessKey"], Literal["DeletePolicy"], Literal["GetAccountAuthorizationDetails"], Literal["SimulatePrincipalPolicy"], Literal["UpdateGroup"], Literal["GetContextKeysForCustomPolicy"], Literal["GetRole"], Literal["ListPolicies"], Literal["GenerateCredentialReport"], Literal["UpdateAssumeRolePolicy"], Literal["CreateUser"], Literal["ListEntitiesForPolicy"], Literal["UpdateAccountPasswordPolicy"], Literal["ListAccessKeys"], Literal["UpdateOpenIDConnectProviderThumbprint"], Literal["DeletePolicyVersion"], Literal["ListServiceSpecificCredentials"], Literal["GenerateOrganizationsAccessReport"], Literal["DeleteVirtualMFADevice"], Literal["GenerateServiceLastAccessedDetails"], Literal["GetOrganizationsAccessReport"], Literal["AttachGroupPolicy"], Literal["CreateAccessKey"], Literal["ListRoleTags"], Literal["GetUser"], Literal["ListInstanceProfiles"], Literal["ListSTSRegionalEndpointsStatus"], Literal["CreateServiceLinkedRole"], Literal["GetServiceLastAccessedDetails"], Literal["TagRole"], Literal["DeleteOpenIDConnectProvider"], Literal["PassRole"], Literal["TagInstanceProfile"], Literal["UploadCloudFrontPublicKey"], Literal["DeleteServerCertificate"], Literal["EnableMFADevice"], Literal["ListUserTags"], Literal["UpdateAccessKey"], Literal["AddUserToGroup"], Literal["DeleteUserPolicy"], Literal["GetAccountName"], Literal["DeleteSigningCertificate"], Literal["GetAccountPasswordPolicy"], Literal["GetLoginProfile"], Literal["ListInstanceProfileTags"], Literal["UpdateUser"], Literal["ListMFADevices"], Literal["PutGroupPolicy"], Literal["GetSSHPublicKey"], Literal["DetachRolePolicy"], Literal["DetachGroupPolicy"], Literal["CreateOpenIDConnectProvider"], Literal["CreateInstanceProfile"], Literal["UntagSAMLProvider"], Literal["GetGroup"], Literal["ListServerCertificateTags"], Literal["DeleteSAMLProvider"], Literal["TagUser"], Literal["RemoveUserFromGroup"], Literal["TagMFADevice"], Literal["DetachUserPolicy"], Literal["CreatePolicyVersion"], Literal["AddClientIDToOpenIDConnectProvider"], Literal["ListMFADeviceTags"], Literal["AttachRolePolicy"], Literal["DeleteServiceLinkedRole"], Literal["ListAccountAliases"], Literal["UntagServerCertificate"], Literal["UpdateLoginProfile"], Literal["DeleteAccountAlias"], Literal["DeleteInstanceProfile"], Literal["UntagMFADevice"], Literal["UpdateAccountEmailAddress"], Literal["GetAccountEmailAddress"], Literal["ListVirtualMFADevices"], Literal["PutRolePolicy"], Literal["GetRolePolicy"], Literal["UpdateCloudFrontPublicKey"], Literal["DeleteGroup"], Literal["GetCredentialReport"], Literal["CreateAccountAlias"], Literal["CreateLoginProfile"], Literal["DeleteUserPermissionsBoundary"], Literal["ListCloudFrontPublicKeys"], Literal["ResetServiceSpecificCredential"], Literal["UpdateSAMLProvider"], Literal["GetSAMLProvider"], Literal["ListOpenIDConnectProviders"]]
aws_iam_condition_type = Union[Literal["iam:PermissionsBoundary"], Literal["aws:TagKeys"], Literal["iam:AWSServiceName"], Literal["iam:PolicyARN"], Literal["iam:OrganizationsPolicyId"], Literal["iam:AssociatedResourceArn"], Literal["iam:PassedToService"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iamStatement(GenericResourceType[aws_iam_privilege_type, aws_iam_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    