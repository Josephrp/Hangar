from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_sms_voice_privilege_type = Union[Literal["DescribeVerifiedDestinationNumbers"], Literal["DescribeConfigurationSets"], Literal["DeleteRegistration"], Literal["RequestPhoneNumber"], Literal["DeleteConfigurationSet"], Literal["PutOptedOutNumber"], Literal["DeleteRegistrationFieldValue"], Literal["UntagResource"], Literal["DeleteOptOutList"], Literal["DescribeOptOutLists"], Literal["DescribeOptedOutNumbers"], Literal["SendTextMessage"], Literal["SetTextMessageSpendLimitOverride"], Literal["DescribePhoneNumbers"], Literal["DescribePools"], Literal["DescribeRegistrationFieldValues"], Literal["ListRegistrationAssociations"], Literal["SetDefaultSenderId"], Literal["UpdateConfigurationSetEventDestination"], Literal["SendDestinationNumberVerificationCode"], Literal["RequestSenderId"], Literal["DeleteDefaultSenderId"], Literal["DescribeRegistrations"], Literal["SetVoiceMessageSpendLimitOverride"], Literal["CreateConfigurationSet"], Literal["DescribeAccountLimits"], Literal["UpdateSenderId"], Literal["DescribeRegistrationAttachments"], Literal["PutKeyword"], Literal["PutRegistrationFieldValue"], Literal["DescribeAccountAttributes"], Literal["ReleaseSenderId"], Literal["DescribeRegistrationTypeDefinitions"], Literal["CreateConfigurationSetEventDestination"], Literal["ListTagsForResource"], Literal["DeleteRegistrationAttachment"], Literal["DeleteVoiceMessageSpendLimitOverride"], Literal["CreateVerifiedDestinationNumber"], Literal["DeleteEventDestination"], Literal["ListPoolOriginationIdentities"], Literal["CreateRegistrationAssociation"], Literal["DeleteKeyword"], Literal["DeletePool"], Literal["UpdatePhoneNumber"], Literal["VerifyDestinationNumber"], Literal["DeleteDefaultMessageType"], Literal["DeleteVerifiedDestinationNumber"], Literal["SendVoiceMessage"], Literal["DeleteConfigurationSetEventDestination"], Literal["DiscardRegistrationVersion"], Literal["DeleteOptedOutNumber"], Literal["UpdateEventDestination"], Literal["ReleasePhoneNumber"], Literal["DescribeSenderIds"], Literal["CreateRegistrationAttachment"], Literal["GetConfigurationSetEventDestinations"], Literal["DeleteTextMessageSpendLimitOverride"], Literal["DescribeRegistrationVersions"], Literal["DescribeRegistrationSectionDefinitions"], Literal["DescribeRegistrationFieldDefinitions"], Literal["CreatePool"], Literal["CreateRegistration"], Literal["CreateRegistrationVersion"], Literal["TagResource"], Literal["UpdatePool"], Literal["CreateEventDestination"], Literal["CreateOptOutList"], Literal["DisassociateOriginationIdentity"], Literal["SubmitRegistrationVersion"], Literal["ListConfigurationSets"], Literal["DescribeKeywords"], Literal["AssociateOriginationIdentity"], Literal["DescribeSpendLimits"], Literal["SetDefaultMessageType"]]
aws_sms_voice_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_sms_voiceStatement(GenericResourceType[aws_sms_voice_privilege_type, aws_sms_voice_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    