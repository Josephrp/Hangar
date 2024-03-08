from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_athena_privilege_type = Union[Literal["ListApplicationDPUSizes"], Literal["ListExecutors"], Literal["ListTableMetadata"], Literal["CreateCapacityReservation"], Literal["GetNamedQuery"], Literal["GetQueryRuntimeStatistics"], Literal["UpdateWorkGroup"], Literal["CreateNotebook"], Literal["ListDatabases"], Literal["CreateWorkGroup"], Literal["DeleteDataCatalog"], Literal["GetTables"], Literal["StartSession"], Literal["DeleteCapacityReservation"], Literal["ListPreparedStatements"], Literal["GetQueryResults"], Literal["UpdateNotebook"], Literal["UpdatePreparedStatement"], Literal["GetDataCatalog"], Literal["GetExecutionEngine"], Literal["TagResource"], Literal["ListDataCatalogs"], Literal["GetNamespace"], Literal["GetQueryResultsStream"], Literal["GetCalculationExecutionStatus"], Literal["GetCapacityReservation"], Literal["GetTable"], Literal["StopQueryExecution"], Literal["ListQueryExecutions"], Literal["GetQueryExecution"], Literal["GetSession"], Literal["TerminateSession"], Literal["CreateNamedQuery"], Literal["DeletePreparedStatement"], Literal["ListEngineVersions"], Literal["DeleteNamedQuery"], Literal["CreateDataCatalog"], Literal["CreatePresignedNotebookUrl"], Literal["ListCalculationExecutions"], Literal["CreatePreparedStatement"], Literal["ExportNotebook"], Literal["GetDatabase"], Literal["UpdateDataCatalog"], Literal["CancelQueryExecution"], Literal["GetCatalogs"], Literal["GetExecutionEngines"], Literal["StartQueryExecution"], Literal["ListNotebookMetadata"], Literal["GetNamespaces"], Literal["GetNotebookMetadata"], Literal["UpdateNotebookMetadata"], Literal["ListSessions"], Literal["ListNamedQueries"], Literal["BatchGetQueryExecution"], Literal["PutCapacityAssignmentConfiguration"], Literal["GetQueryExecutions"], Literal["GetSessionStatus"], Literal["BatchGetPreparedStatement"], Literal["CancelCapacityReservation"], Literal["RunQuery"], Literal["UntagResource"], Literal["UpdateCapacityReservation"], Literal["DeleteWorkGroup"], Literal["GetTableMetadata"], Literal["UpdateNamedQuery"], Literal["GetPreparedStatement"], Literal["StartCalculationExecution"], Literal["ListNotebookSessions"], Literal["ListTagsForResource"], Literal["ImportNotebook"], Literal["StopCalculationExecution"], Literal["ListWorkGroups"], Literal["GetCapacityAssignmentConfiguration"], Literal["GetCalculationExecutionCode"], Literal["ListCapacityReservations"], Literal["GetWorkGroup"], Literal["GetCalculationExecution"], Literal["BatchGetNamedQuery"], Literal["DeleteNotebook"]]
aws_athena_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_athenaStatement(GenericResourceType[aws_athena_privilege_type, aws_athena_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    