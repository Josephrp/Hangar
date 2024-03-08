from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_nimble_privilege_type = Union[Literal["GetLaunchProfile"], Literal["UntagResource"], Literal["AcceptEulas"], Literal["GetEula"], Literal["ListLaunchProfileMembers"], Literal["DeleteStudioMember"], Literal["PutStudioMembers"], Literal["CreateStudioComponent"], Literal["GetLaunchProfileInitialization"], Literal["GetFeatureMap"], Literal["GetLaunchProfileMember"], Literal["ListEulaAcceptances"], Literal["DeleteStudio"], Literal["CreateStreamingImage"], Literal["ListStreamingSessionBackups"], Literal["ListStudioComponents"], Literal["ListTagsForResource"], Literal["PutStudioLogEvents"], Literal["GetStudioMember"], Literal["GetStreamingSessionStream"], Literal["ListStudioMembers"], Literal["UpdateLaunchProfileMember"], Literal["DeleteStreamingImage"], Literal["UpdateStreamingImage"], Literal["GetStreamingSessionBackup"], Literal["GetStudio"], Literal["StartStreamingSession"], Literal["DeleteLaunchProfile"], Literal["ListLaunchProfiles"], Literal["ListStudios"], Literal["GetLaunchProfileDetails"], Literal["DeleteLaunchProfileMember"], Literal["StartStudioSSOConfigurationRepair"], Literal["UpdateStudioComponent"], Literal["GetStreamingImage"], Literal["ListStreamingSessions"], Literal["UpdateLaunchProfile"], Literal["GetStreamingSession"], Literal["DeleteStreamingSession"], Literal["CreateLaunchProfile"], Literal["PutLaunchProfileMembers"], Literal["StopStreamingSession"], Literal["CreateStreamingSessionStream"], Literal["ListStreamingImages"], Literal["UpdateStudio"], Literal["TagResource"], Literal["GetStudioComponent"], Literal["DeleteStudioComponent"], Literal["ListEulas"], Literal["CreateStudio"], Literal["CreateStreamingSession"]]
aws_nimble_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["nimble:requesterPrincipalId"], Literal["nimble:createdBy"], Literal["nimble:principalId"], Literal["nimble:ownedBy"], Literal["aws:RequestTag/${TagKey}"]]

class aws_nimbleStatement(GenericResourceType[aws_nimble_privilege_type, aws_nimble_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    