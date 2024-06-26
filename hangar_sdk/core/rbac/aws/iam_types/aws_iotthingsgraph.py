from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_iotthingsgraph_privilege_type = Union[Literal["UntagResource"], Literal["DescribeNamespace"], Literal["GetNamespaceDeletionStatus"], Literal["DeleteSystemTemplate"], Literal["SearchFlowTemplates"], Literal["UpdateSystemTemplate"], Literal["AssociateEntityToThing"], Literal["SearchEntities"], Literal["GetSystemInstance"], Literal["GetUploadStatus"], Literal["GetFlowTemplate"], Literal["GetEntities"], Literal["SearchThings"], Literal["ListTagsForResource"], Literal["CreateSystemTemplate"], Literal["SearchFlowExecutions"], Literal["DeploySystemInstance"], Literal["GetSystemTemplateRevisions"], Literal["DeleteNamespace"], Literal["UndeploySystemInstance"], Literal["UploadEntityDefinitions"], Literal["CreateFlowTemplate"], Literal["DeprecateSystemTemplate"], Literal["DissociateEntityFromThing"], Literal["DeleteFlowTemplate"], Literal["TagResource"], Literal["GetFlowTemplateRevisions"], Literal["GetSystemTemplate"], Literal["ListFlowExecutionMessages"], Literal["SearchSystemInstances"], Literal["SearchSystemTemplates"], Literal["DeleteSystemInstance"], Literal["DeprecateFlowTemplate"], Literal["CreateSystemInstance"], Literal["UpdateFlowTemplate"]]
aws_iotthingsgraph_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_iotthingsgraphStatement(GenericResourceType[aws_iotthingsgraph_privilege_type, aws_iotthingsgraph_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    