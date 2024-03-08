from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_controltower_privilege_type = Union[Literal["DescribeGuardrail"], Literal["EnableControl"], Literal["ListManagedAccountsForGuardrail"], Literal["ListDriftDetails"], Literal["UntagResource"], Literal["DeleteLandingZone"], Literal["GetEnabledControl"], Literal["DescribeManagedOrganizationalUnit"], Literal["ListGuardrails"], Literal["ListExternalConfigRuleCompliance"], Literal["DisableGuardrail"], Literal["DescribeAccountFactoryConfig"], Literal["DescribeRegisterOrganizationalUnitOperation"], Literal["ListEnabledGuardrails"], Literal["SetupLandingZone"], Literal["GetLandingZone"], Literal["ListEnabledControls"], Literal["ResetLandingZone"], Literal["DescribeSingleSignOn"], Literal["GetAvailableUpdates"], Literal["ListTagsForResource"], Literal["GetAccountInfo"], Literal["ListManagedAccountsForParent"], Literal["GetLandingZoneOperation"], Literal["ManageOrganizationalUnit"], Literal["GetLandingZoneDriftStatus"], Literal["ListExtendGovernancePrecheckDetails"], Literal["DescribeCoreService"], Literal["CreateManagedAccount"], Literal["GetHomeRegion"], Literal["DescribeManagedAccount"], Literal["UpdateEnabledControl"], Literal["ListDirectoryGroups"], Literal["UpdateAccountFactoryConfig"], Literal["PerformPreLaunchChecks"], Literal["DescribeGuardrailForTarget"], Literal["CreateLandingZone"], Literal["GetGuardrailComplianceStatus"], Literal["DeregisterManagedAccount"], Literal["GetControlOperation"], Literal["ListGuardrailsForTarget"], Literal["ListGuardrailViolations"], Literal["ListLandingZones"], Literal["TagResource"], Literal["DescribeLandingZoneConfiguration"], Literal["DeregisterOrganizationalUnit"], Literal["GetLandingZoneStatus"], Literal["ListManagedAccounts"], Literal["ListManagedOrganizationalUnitsForGuardrail"], Literal["DisableControl"], Literal["EnableGuardrail"], Literal["UpdateLandingZone"], Literal["ListManagedOrganizationalUnits"]]
aws_controltower_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_controltowerStatement(GenericResourceType[aws_controltower_privilege_type, aws_controltower_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    