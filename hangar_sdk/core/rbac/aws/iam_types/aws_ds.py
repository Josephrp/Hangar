from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_ds_privilege_type = Union[Literal["AuthorizeApplication"], Literal["UpdateTrust"], Literal["CreateDirectory"], Literal["ShareDirectory"], Literal["RemoveTagsFromResource"], Literal["RestoreFromSnapshot"], Literal["DisableLDAPS"], Literal["UpdateDirectory"], Literal["RegisterCertificate"], Literal["DisableSso"], Literal["DescribeClientAuthenticationSettings"], Literal["ListSchemaExtensions"], Literal["CreateAlias"], Literal["DisableRoleAccess"], Literal["UpdateConditionalForwarder"], Literal["DeleteTrust"], Literal["DescribeRegions"], Literal["CancelSchemaExtension"], Literal["UpdateRadius"], Literal["StartSchemaExtension"], Literal["DeregisterCertificate"], Literal["DescribeUpdateDirectory"], Literal["RemoveIpRoutes"], Literal["DescribeSharedDirectories"], Literal["DescribeTrusts"], Literal["RegisterEventTopic"], Literal["CreateMicrosoftAD"], Literal["DescribeDirectories"], Literal["CreateConditionalForwarder"], Literal["GetDirectoryLimits"], Literal["ListLogSubscriptions"], Literal["EnableRadius"], Literal["DescribeEventTopics"], Literal["ListCertificates"], Literal["DisableClientAuthentication"], Literal["AddRegion"], Literal["DeleteSnapshot"], Literal["GetAuthorizedApplicationDetails"], Literal["VerifyTrust"], Literal["RejectSharedDirectory"], Literal["UpdateAuthorizedApplication"], Literal["DescribeConditionalForwarders"], Literal["CreateIdentityPoolDirectory"], Literal["EnableRoleAccess"], Literal["DeleteLogSubscription"], Literal["UpdateNumberOfDomainControllers"], Literal["DisableRadius"], Literal["CreateSnapshot"], Literal["DeleteConditionalForwarder"], Literal["ListIpRoutes"], Literal["GetSnapshotLimits"], Literal["EnableClientAuthentication"], Literal["CreateComputer"], Literal["EnableLDAPS"], Literal["DeleteDirectory"], Literal["ListAuthorizedApplications"], Literal["UpdateSettings"], Literal["EnableSso"], Literal["ConnectDirectory"], Literal["AcceptSharedDirectory"], Literal["UnauthorizeApplication"], Literal["UnshareDirectory"], Literal["ResetUserPassword"], Literal["DescribeSnapshots"], Literal["DescribeCertificate"], Literal["DeregisterEventTopic"], Literal["DescribeDomainControllers"], Literal["UpdateDirectorySetup"], Literal["AddIpRoutes"], Literal["ListTagsForResource"], Literal["DescribeSettings"], Literal["CreateLogSubscription"], Literal["RemoveRegion"], Literal["AddTagsToResource"], Literal["DescribeLDAPSSettings"], Literal["CreateTrust"], Literal["CheckAlias"]]
aws_ds_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_dsStatement(GenericResourceType[aws_ds_privilege_type, aws_ds_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    