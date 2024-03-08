from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codecommit_privilege_type = Union[Literal["BatchGetPullRequests"], Literal["BatchDescribeMergeConflicts"], Literal["EvaluatePullRequestApprovalRules"], Literal["ListRepositoriesForApprovalRuleTemplate"], Literal["GetObjectIdentifier"], Literal["CreateRepository"], Literal["TestRepositoryTriggers"], Literal["AssociateApprovalRuleTemplateWithRepository"], Literal["GetUploadArchiveStatus"], Literal["UpdatePullRequestTitle"], Literal["UpdateRepositoryEncryptionKey"], Literal["MergeBranchesBySquash"], Literal["PostCommentReply"], Literal["GetPullRequestApprovalStates"], Literal["DescribePullRequestEvents"], Literal["BatchAssociateApprovalRuleTemplateWithRepositories"], Literal["CancelUploadArchive"], Literal["CreatePullRequestApprovalRule"], Literal["DisassociateApprovalRuleTemplateFromRepository"], Literal["GetDifferences"], Literal["TagResource"], Literal["DeleteRepository"], Literal["GetCommitsFromMergeBase"], Literal["MergeBranchesByFastForward"], Literal["UpdateComment"], Literal["GetPullRequestOverrideState"], Literal["DeletePullRequestApprovalRule"], Literal["GetRepositoryTriggers"], Literal["GetBlob"], Literal["GetBranch"], Literal["DeleteFile"], Literal["DescribeMergeConflicts"], Literal["GetMergeConflicts"], Literal["GetReferences"], Literal["UpdateApprovalRuleTemplateDescription"], Literal["DeleteBranch"], Literal["GitPush"], Literal["MergePullRequestByThreeWay"], Literal["UpdatePullRequestStatus"], Literal["GetFolder"], Literal["UploadArchive"], Literal["ListApprovalRuleTemplates"], Literal["CreateUnreferencedMergeCommit"], Literal["MergePullRequestBySquash"], Literal["GetTree"], Literal["PostCommentForComparedCommit"], Literal["CreateApprovalRuleTemplate"], Literal["UpdatePullRequestDescription"], Literal["OverridePullRequestApprovalRules"], Literal["GetCommentsForPullRequest"], Literal["ListAssociatedApprovalRuleTemplatesForRepository"], Literal["GetCommitHistory"], Literal["CreatePullRequest"], Literal["GetCommentReactions"], Literal["GetPullRequest"], Literal["UpdatePullRequestApprovalRuleContent"], Literal["BatchGetRepositories"], Literal["ListFileCommitHistory"], Literal["ListBranches"], Literal["UpdateDefaultBranch"], Literal["PostCommentForPullRequest"], Literal["UpdateRepositoryDescription"], Literal["MergeBranchesByThreeWay"], Literal["PutFile"], Literal["UpdatePullRequestApprovalState"], Literal["UpdateRepositoryName"], Literal["UpdateApprovalRuleTemplateContent"], Literal["PutRepositoryTriggers"], Literal["CreateCommit"], Literal["GetMergeCommit"], Literal["MergePullRequestByFastForward"], Literal["UntagResource"], Literal["GetCommentsForComparedCommit"], Literal["DeleteApprovalRuleTemplate"], Literal["GetFile"], Literal["GetCommit"], Literal["UpdateApprovalRuleTemplateName"], Literal["ListRepositories"], Literal["GetApprovalRuleTemplate"], Literal["ListTagsForResource"], Literal["GitPull"], Literal["BatchDisassociateApprovalRuleTemplateFromRepositories"], Literal["GetRepository"], Literal["PutCommentReaction"], Literal["BatchGetCommits"], Literal["DeleteCommentContent"], Literal["GetMergeOptions"], Literal["ListPullRequests"], Literal["GetComment"], Literal["CreateBranch"]]
aws_codecommit_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:ResourceTag/${TagKey}"], Literal["codecommit:References"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codecommitStatement(GenericResourceType[aws_codecommit_privilege_type, aws_codecommit_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    