from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_datazone_privilege_type = Union[Literal["GetIamPortalLoginUrl"], Literal["DeleteEnvironmentBlueprintConfiguration"], Literal["RefreshToken"], Literal["CreateAsset"], Literal["GetEnvironmentProfile"], Literal["CreateGroupProfile"], Literal["GetListing"], Literal["ListEnvironmentBlueprints"], Literal["CreateEnvironmentProfile"], Literal["ListSubscriptionGrants"], Literal["ProvisionDomain"], Literal["UpdateUserProfile"], Literal["UpdateDataSource"], Literal["UpdateDomain"], Literal["DeleteListing"], Literal["SsoLogin"], Literal["DeleteFormType"], Literal["AcceptPredictions"], Literal["CreateDomain"], Literal["ListAssetRevisions"], Literal["StopMetadataGenerationRun"], Literal["GetEnvironmentActionLink"], Literal["UpdateProject"], Literal["GetSubscriptionRequestDetails"], Literal["ListDataSourceRunActivities"], Literal["UpdateSubscriptionGrantStatus"], Literal["CreateAssetRevision"], Literal["GetSubscriptionGrant"], Literal["TagResource"], Literal["DeleteDomainSharingPolicy"], Literal["CreateProject"], Literal["UpdateSubscriptionTarget"], Literal["SearchGroupProfiles"], Literal["GetGroupProfile"], Literal["GetMetadataGenerationRun"], Literal["CreateProjectMembership"], Literal["GetSubscriptionTarget"], Literal["SsoLogout"], Literal["DeleteAssetType"], Literal["GetEnvironmentBlueprintConfiguration"], Literal["RejectSubscriptionRequest"], Literal["UpdateEnvironmentBlueprint"], Literal["UpdateEnvironmentConfiguration"], Literal["DeleteEnvironmentProfile"], Literal["ListProjectMemberships"], Literal["ListDataSources"], Literal["ListProjects"], Literal["PutDomainSharingPolicy"], Literal["DeleteGlossary"], Literal["ListSubscriptionTargets"], Literal["GetDomain"], Literal["GetGlossary"], Literal["ListSubscriptionRequests"], Literal["ListSubscriptions"], Literal["CreateSubscriptionGrant"], Literal["ValidatePassRole"], Literal["DeleteProject"], Literal["SearchUserProfiles"], Literal["StartMetadataGenerationRun"], Literal["CreateGlossary"], Literal["StartDataSourceRun"], Literal["DeleteDomain"], Literal["ListGroupsForUser"], Literal["ListEnvironments"], Literal["DeleteAsset"], Literal["DeleteEnvironment"], Literal["DeleteSubscriptionRequest"], Literal["DeleteSubscriptionGrant"], Literal["UpdateEnvironmentProfile"], Literal["CreateEnvironmentBlueprint"], Literal["ListEnvironmentProfiles"], Literal["UpdateSubscriptionRequest"], Literal["ListWarehouseMetadata"], Literal["SearchTypes"], Literal["GetEnvironment"], Literal["GetDataSource"], Literal["SearchListings"], Literal["ListEnvironmentBlueprintConfigurations"], Literal["CreateListingChangeSet"], Literal["GetGlossaryTerm"], Literal["GetFormType"], Literal["ListNotifications"], Literal["UpdateEnvironment"], Literal["CreateGlossaryTerm"], Literal["CreateFormType"], Literal["AcceptSubscriptionRequest"], Literal["ListDataSourceRuns"], Literal["GetEnvironmentCredentials"], Literal["CreateDataSource"], Literal["UpdateGlossaryTerm"], Literal["GetProject"], Literal["CancelSubscription"], Literal["GetSubscriptionEligibility"], Literal["UpdateEnvironmentDeploymentStatus"], Literal["DeleteSubscriptionTarget"], Literal["GetDomainSharingPolicy"], Literal["DeleteDataSource"], Literal["ListAccountEnvironments"], Literal["ListDomains"], Literal["UntagResource"], Literal["PutEnvironmentBlueprintConfiguration"], Literal["GetAssetType"], Literal["DeleteProjectMembership"], Literal["GetEnvironmentBlueprint"], Literal["Search"], Literal["CreateEnvironment"], Literal["GetDataSourceRun"], Literal["UpdateGlossary"], Literal["GetSubscription"], Literal["CreateUserProfile"], Literal["DeleteEnvironmentBlueprint"], Literal["ListTagsForResource"], Literal["CreateSubscriptionRequest"], Literal["UpdateGroupProfile"], Literal["DeleteGlossaryTerm"], Literal["RejectPredictions"], Literal["RevokeSubscription"], Literal["GetUserProfile"], Literal["GetAsset"], Literal["ListMetadataGenerationRuns"], Literal["CreateAssetType"], Literal["CreateSubscriptionTarget"]]
aws_datazone_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_datazoneStatement(GenericResourceType[aws_datazone_privilege_type, aws_datazone_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    