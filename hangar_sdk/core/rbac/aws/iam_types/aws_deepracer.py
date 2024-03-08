from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_deepracer_privilege_type = Union[Literal["CreateLeaderboard"], Literal["StartEvaluation"], Literal["GetEvaluation"], Literal["UntagResource"], Literal["MigrateModels"], Literal["AdminSetAccountConfig"], Literal["GetModel"], Literal["GetAccountConfig"], Literal["TestRewardFunction"], Literal["AdminListAssociatedResources"], Literal["CreateLeaderboardAccessToken"], Literal["ListLeaderboardEvaluations"], Literal["GetCar"], Literal["GetTrainingJob"], Literal["ListLeaderboards"], Literal["GetTrack"], Literal["GetRankedUserSubmission"], Literal["GetPrivateLeaderboard"], Literal["ListEvaluations"], Literal["RemoveLeaderboardAccessPermission"], Literal["CreateCar"], Literal["GetLeaderboard"], Literal["StopTrainingReinforcementLearningModel"], Literal["ListTagsForResource"], Literal["CreateLeaderboardSubmission"], Literal["ListPrivateLeaderboardParticipants"], Literal["GetLatestUserSubmission"], Literal["UpdateCar"], Literal["PerformLeaderboardOperation"], Literal["ListTrainingJobs"], Literal["EditLeaderboard"], Literal["AdminListAssociatedUsers"], Literal["AdminGetAccountConfig"], Literal["StopEvaluation"], Literal["CloneReinforcementLearningModel"], Literal["ListTracks"], Literal["DeleteModel"], Literal["CreateReinforcementLearningModel"], Literal["AdminManageUser"], Literal["ListLeaderboardSubmissions"], Literal["GetCars"], Literal["ListPrivateLeaderboards"], Literal["ListModels"], Literal["AddLeaderboardAccessPermission"], Literal["ListSubscribedPrivateLeaderboards"], Literal["TagResource"], Literal["GetAssetUrl"], Literal["GetAlias"], Literal["SetAlias"], Literal["DeleteLeaderboard"], Literal["ImportModel"]]
aws_deepracer_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["deepracer:MultiUser"], Literal["deepracer:UserToken"], Literal["aws:RequestTag/${TagKey}"]]

class aws_deepracerStatement(GenericResourceType[aws_deepracer_privilege_type, aws_deepracer_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    