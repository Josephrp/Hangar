from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_cloudtrail_privilege_type = Union[Literal["RemoveTags"], Literal["ListQueries"], Literal["UpdateChannel"], Literal["DisableFederation"], Literal["RegisterOrganizationDelegatedAdmin"], Literal["ListTags"], Literal["CreateChannel"], Literal["GetServiceLinkedChannel"], Literal["StartQuery"], Literal["StopEventDataStoreIngestion"], Literal["EnableFederation"], Literal["GetTrail"], Literal["ListChannels"], Literal["ListEventDataStores"], Literal["DeleteTrail"], Literal["ListTrails"], Literal["GetEventSelectors"], Literal["PutInsightSelectors"], Literal["RestoreEventDataStore"], Literal["LookupEvents"], Literal["CreateEventDataStore"], Literal["StartEventDataStoreIngestion"], Literal["ListPublicKeys"], Literal["DescribeQuery"], Literal["GetTrailStatus"], Literal["CreateTrail"], Literal["StartImport"], Literal["GetChannel"], Literal["DescribeTrails"], Literal["DeregisterOrganizationDelegatedAdmin"], Literal["GetEventDataStoreData"], Literal["CreateServiceLinkedChannel"], Literal["GetInsightSelectors"], Literal["PutEventSelectors"], Literal["PutResourcePolicy"], Literal["StopLogging"], Literal["AddTags"], Literal["UpdateEventDataStore"], Literal["GetQueryResults"], Literal["GetImport"], Literal["ListServiceLinkedChannels"], Literal["ListImports"], Literal["DeleteEventDataStore"], Literal["StartLogging"], Literal["CancelQuery"], Literal["DeleteResourcePolicy"], Literal["GetEventDataStore"], Literal["StopImport"], Literal["DeleteChannel"], Literal["ListImportFailures"], Literal["DeleteServiceLinkedChannel"], Literal["UpdateTrail"], Literal["GetResourcePolicy"], Literal["UpdateServiceLinkedChannel"]]
aws_cloudtrail_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_cloudtrailStatement(GenericResourceType[aws_cloudtrail_privilege_type, aws_cloudtrail_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    