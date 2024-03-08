from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_codebuild_privilege_type = Union[Literal["PersistOAuthToken"], Literal["CreateProject"], Literal["BatchGetReportGroups"], Literal["ListCuratedEnvironmentImages"], Literal["RetryBuildBatch"], Literal["ListBuildsForProject"], Literal["CreateReportGroup"], Literal["BatchPutTestCases"], Literal["StopBuildBatch"], Literal["DeleteReportGroup"], Literal["StopBuild"], Literal["BatchDeleteBuilds"], Literal["ListSourceCredentials"], Literal["CreateWebhook"], Literal["UpdateProjectVisibility"], Literal["InvalidateProjectCache"], Literal["DeleteReport"], Literal["ListSharedReportGroups"], Literal["ListBuilds"], Literal["ListRepositories"], Literal["StartBuildBatch"], Literal["BatchGetBuilds"], Literal["ListProjects"], Literal["ListConnectedOAuthAccounts"], Literal["ListReportsForReportGroup"], Literal["UpdateWebhook"], Literal["UpdateReport"], Literal["BatchGetProjects"], Literal["BatchGetBuildBatches"], Literal["ListReportGroups"], Literal["DeleteOAuthToken"], Literal["StartBuild"], Literal["ImportSourceCredentials"], Literal["UpdateProject"], Literal["ListBuildBatches"], Literal["DeleteSourceCredentials"], Literal["PutResourcePolicy"], Literal["GetResourcePolicy"], Literal["RetryBuild"], Literal["DeleteProject"], Literal["CreateReport"], Literal["DescribeCodeCoverages"], Literal["ListBuildBatchesForProject"], Literal["GetReportGroupTrend"], Literal["BatchGetReports"], Literal["DeleteResourcePolicy"], Literal["BatchPutCodeCoverages"], Literal["DescribeTestCases"], Literal["DeleteBuildBatch"], Literal["ListReports"], Literal["ListSharedProjects"], Literal["DeleteWebhook"], Literal["UpdateReportGroup"]]
aws_codebuild_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_codebuildStatement(GenericResourceType[aws_codebuild_privilege_type, aws_codebuild_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    