from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_lightsail_privilege_type = Union[Literal["GetContainerServices"], Literal["DeleteInstance"], Literal["GetOperationsForResource"], Literal["EnableAddOn"], Literal["GetAutoSnapshots"], Literal["CopySnapshot"], Literal["GetRelationalDatabase"], Literal["GetRelationalDatabaseBundles"], Literal["UpdateBucketBundle"], Literal["CreateInstanceSnapshot"], Literal["StopRelationalDatabase"], Literal["UpdateBucket"], Literal["DeleteDisk"], Literal["AttachStaticIp"], Literal["RegisterContainerImage"], Literal["CreateDomain"], Literal["DeleteAutoSnapshot"], Literal["CreateContactMethod"], Literal["CreateKeyPair"], Literal["UpdateLoadBalancerAttribute"], Literal["GetContainerServiceDeployments"], Literal["GetDiskSnapshots"], Literal["GetDistributions"], Literal["GetInstanceSnapshot"], Literal["CreateContainerServiceDeployment"], Literal["GetDistributionLatestCacheReset"], Literal["PutAlarm"], Literal["DeleteDiskSnapshot"], Literal["GetStaticIp"], Literal["CreateBucketAccessKey"], Literal["GetInstanceState"], Literal["GetDistributionBundles"], Literal["DeleteDomainEntry"], Literal["CreateDistribution"], Literal["ImportKeyPair"], Literal["TagResource"], Literal["CreateCloudFormationStack"], Literal["GetDisks"], Literal["SetIpAddressType"], Literal["GetRelationalDatabaseEvents"], Literal["StopGUISession"], Literal["UnpeerVpc"], Literal["CreateInstancesFromSnapshot"], Literal["UpdateRelationalDatabase"], Literal["GetLoadBalancers"], Literal["StartGUISession"], Literal["UpdateContainerService"], Literal["GetOperations"], Literal["ReleaseStaticIp"], Literal["GetRelationalDatabaseSnapshots"], Literal["DeleteKnownHostKeys"], Literal["GetBucketAccessKeys"], Literal["CreateContainerService"], Literal["DeleteRelationalDatabaseSnapshot"], Literal["DetachCertificateFromDistribution"], Literal["UpdateRelationalDatabaseParameters"], Literal["DetachInstancesFromLoadBalancer"], Literal["GetBuckets"], Literal["CreateDomainEntry"], Literal["DeleteRelationalDatabase"], Literal["GetRelationalDatabaseMetricData"], Literal["GetLoadBalancerTlsCertificates"], Literal["AttachInstancesToLoadBalancer"], Literal["ResetDistributionCache"], Literal["UpdateInstanceMetadataOptions"], Literal["GetDomain"], Literal["GetRegions"], Literal["GetStaticIps"], Literal["CreateLoadBalancer"], Literal["GetLoadBalancerTlsPolicies"], Literal["CreateContainerServiceRegistryLogin"], Literal["IsVpcPeered"], Literal["CreateBucket"], Literal["DeleteKeyPair"], Literal["DeleteDomain"], Literal["DeleteBucket"], Literal["GetBucketBundles"], Literal["GetRelationalDatabaseBlueprints"], Literal["UpdateDistribution"], Literal["GetBundles"], Literal["GetInstances"], Literal["DeleteAlarm"], Literal["CreateDiskSnapshot"], Literal["DeleteContainerService"], Literal["GetRelationalDatabases"], Literal["StartRelationalDatabase"], Literal["GetCloudFormationStackRecords"], Literal["GetLoadBalancerMetricData"], Literal["CreateRelationalDatabaseSnapshot"], Literal["DeleteLoadBalancer"], Literal["GetDistributionMetricData"], Literal["DeleteContainerImage"], Literal["GetExportSnapshotRecords"], Literal["GetInstanceSnapshots"], Literal["DownloadDefaultKeyPair"], Literal["DeleteCertificate"], Literal["CloseInstancePublicPorts"], Literal["CreateRelationalDatabaseFromSnapshot"], Literal["GetContainerLog"], Literal["DeleteLoadBalancerTlsCertificate"], Literal["GetDomains"], Literal["PeerVpc"], Literal["CreateDiskFromSnapshot"], Literal["GetContainerServicePowers"], Literal["DetachDisk"], Literal["CreateGUISessionAccessDetails"], Literal["ExportSnapshot"], Literal["GetContainerAPIMetadata"], Literal["GetContainerServiceMetricData"], Literal["UpdateDistributionBundle"], Literal["DetachStaticIp"], Literal["UpdateDomainEntry"], Literal["GetAlarms"], Literal["GetKeyPairs"], Literal["StartInstance"], Literal["AttachLoadBalancerTlsCertificate"], Literal["GetRelationalDatabaseSnapshot"], Literal["GetContactMethods"], Literal["SendContactMethodVerification"], Literal["GetInstanceMetricData"], Literal["GetBucketMetricData"], Literal["GetCertificates"], Literal["SetResourceAccessForBucket"], Literal["DeleteBucketAccessKey"], Literal["DisableAddOn"], Literal["GetInstanceAccessDetails"], Literal["UntagResource"], Literal["AttachDisk"], Literal["AttachCertificateToDistribution"], Literal["GetInstance"], Literal["CreateLoadBalancerTlsCertificate"], Literal["AllocateStaticIp"], Literal["CreateCertificate"], Literal["GetBlueprints"], Literal["OpenInstancePublicPorts"], Literal["StopInstance"], Literal["CreateRelationalDatabase"], Literal["CreateDisk"], Literal["GetRelationalDatabaseParameters"], Literal["CreateInstances"], Literal["GetContainerImages"], Literal["RebootRelationalDatabase"], Literal["GetLoadBalancer"], Literal["GetOperation"], Literal["GetRelationalDatabaseLogEvents"], Literal["GetInstancePortStates"], Literal["GetDiskSnapshot"], Literal["GetKeyPair"], Literal["GetDisk"], Literal["GetRelationalDatabaseLogStreams"], Literal["RebootInstance"], Literal["GetActiveNames"], Literal["GetRelationalDatabaseMasterUserPassword"], Literal["DeleteInstanceSnapshot"], Literal["TestAlarm"], Literal["GetCostEstimate"], Literal["DeleteDistribution"], Literal["DeleteContactMethod"], Literal["PutInstancePublicPorts"]]
aws_lightsail_condition_type = Union[Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_lightsailStatement(GenericResourceType[aws_lightsail_privilege_type, aws_lightsail_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    