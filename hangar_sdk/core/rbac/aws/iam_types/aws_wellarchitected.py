from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_wellarchitected_privilege_type = Union[Literal["DisassociateLenses"], Literal["GetLensReviewReport"], Literal["CreateTemplateShare"], Literal["ListLensReviewImprovements"], Literal["CreateMilestone"], Literal["ListLensReviews"], Literal["ListTemplateShares"], Literal["UntagResource"], Literal["ListProfileNotifications"], Literal["GetReviewTemplateLensReview"], Literal["UpgradeLensReview"], Literal["UpdateReviewTemplateAnswer"], Literal["ListLensShares"], Literal["CreateProfileShare"], Literal["GetMilestone"], Literal["DisassociateProfiles"], Literal["GetProfileTemplate"], Literal["GetConsolidatedReport"], Literal["UpdateWorkload"], Literal["ListCheckSummaries"], Literal["GetLens"], Literal["DeleteProfile"], Literal["DeleteLensShare"], Literal["UpdateGlobalSettings"], Literal["UpgradeReviewTemplateLensReview"], Literal["UpdateProfile"], Literal["GetReviewTemplateAnswer"], Literal["ListTagsForResource"], Literal["ListAnswers"], Literal["AssociateProfiles"], Literal["DeleteProfileShare"], Literal["ListWorkloadShares"], Literal["GetLensVersionDifference"], Literal["UpdateLensReview"], Literal["CreateWorkload"], Literal["ListNotifications"], Literal["GetProfile"], Literal["ListReviewTemplateAnswers"], Literal["DeleteReviewTemplate"], Literal["ListWorkloads"], Literal["UpdateAnswer"], Literal["ListMilestones"], Literal["UpgradeProfileVersion"], Literal["UpdateReviewTemplateLensReview"], Literal["UpdateShareInvitation"], Literal["DeleteWorkloadShare"], Literal["DeleteWorkload"], Literal["CreateWorkloadShare"], Literal["CreateProfile"], Literal["GetAnswer"], Literal["DeleteLens"], Literal["ListShareInvitations"], Literal["DeleteTemplateShare"], Literal["GetWorkload"], Literal["UpdateReviewTemplate"], Literal["ListReviewTemplates"], Literal["CreateLensShare"], Literal["ExportLens"], Literal["ImportLens"], Literal["ListProfileShares"], Literal["GetReviewTemplate"], Literal["ListCheckDetails"], Literal["TagResource"], Literal["ListProfiles"], Literal["ListLenses"], Literal["UpdateWorkloadShare"], Literal["CreateLensVersion"], Literal["CreateReviewTemplate"], Literal["GetLensReview"], Literal["AssociateLenses"]]
aws_wellarchitected_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["aws:RequestTag/${TagKey}"]]

class aws_wellarchitectedStatement(GenericResourceType[aws_wellarchitected_privilege_type, aws_wellarchitected_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    