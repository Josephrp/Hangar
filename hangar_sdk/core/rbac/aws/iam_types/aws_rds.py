from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_rds_privilege_type = Union[Literal["AuthorizeDBSecurityGroupIngress"], Literal["RestoreDBClusterToPointInTime"], Literal["RemoveRoleFromDBInstance"], Literal["StartDBInstance"], Literal["DescribeDBClusterSnapshotAttributes"], Literal["PromoteReadReplica"], Literal["RegisterDBProxyTargets"], Literal["DeleteDBParameterGroup"], Literal["CreateCustomDBEngineVersion"], Literal["DescribeDBClusterParameterGroups"], Literal["RestoreDBClusterFromS3"], Literal["DescribeOptionGroups"], Literal["ModifyDBSnapshot"], Literal["CancelExportTask"], Literal["CreateDBClusterParameterGroup"], Literal["StopDBCluster"], Literal["DeleteTenantDatabase"], Literal["RemoveTagsFromResource"], Literal["PromoteReadReplicaDBCluster"], Literal["CreateEventSubscription"], Literal["DescribeSourceRegions"], Literal["DescribeReservedDBInstances"], Literal["CreateDBSnapshot"], Literal["DescribeDBInstanceAutomatedBackups"], Literal["ModifyDBRecommendation"], Literal["CreateDBCluster"], Literal["ResetDBParameterGroup"], Literal["DeleteDBProxy"], Literal["ModifyDBClusterParameterGroup"], Literal["DescribeReservedDBInstancesOfferings"], Literal["ResetDBClusterParameterGroup"], Literal["CreateDBProxy"], Literal["DescribeDBProxyEndpoints"], Literal["ModifyOptionGroup"], Literal["CopyDBClusterParameterGroup"], Literal["ModifyDBInstance"], Literal["AddRoleToDBCluster"], Literal["CopyDBParameterGroup"], Literal["DescribeDBClusters"], Literal["DescribePendingMaintenanceActions"], Literal["DescribeDBSubnetGroups"], Literal["FailoverDBCluster"], Literal["RestoreDBClusterFromSnapshot"], Literal["DescribeDBParameters"], Literal["CreateOptionGroup"], Literal["DescribeDBRecommendations"], Literal["DescribeDBInstances"], Literal["CreateDBSecurityGroup"], Literal["BacktrackDBCluster"], Literal["DescribeOptionGroupOptions"], Literal["AddRoleToDBInstance"], Literal["ModifyDBClusterEndpoint"], Literal["DeleteDBSecurityGroup"], Literal["DeleteDBClusterAutomatedBackup"], Literal["CreateGlobalCluster"], Literal["CreateDBInstanceReadReplica"], Literal["DescribeRecommendations"], Literal["DeleteDBCluster"], Literal["StopDBInstance"], Literal["CreateDBProxyEndpoint"], Literal["DeleteIntegration"], Literal["DescribeBlueGreenDeployments"], Literal["EnableHttpEndpoint"], Literal["DescribeDBClusterEndpoints"], Literal["DescribeTenantDatabases"], Literal["DeleteOptionGroup"], Literal["DescribeEvents"], Literal["ModifyTenantDatabase"], Literal["ModifyEventSubscription"], Literal["RestoreDBInstanceFromDBSnapshot"], Literal["ModifyDBProxyTargetGroup"], Literal["DescribeValidDBInstanceModifications"], Literal["DescribeDBProxyTargetGroups"], Literal["PurchaseReservedDBInstancesOffering"], Literal["RemoveRoleFromDBCluster"], Literal["DescribeEngineDefaultClusterParameters"], Literal["DescribeDBProxyTargets"], Literal["RevokeDBSecurityGroupIngress"], Literal["ModifyRecommendation"], Literal["DeleteDBClusterSnapshot"], Literal["ModifyDBSnapshotAttribute"], Literal["DescribeEventCategories"], Literal["DeleteBlueGreenDeployment"], Literal["ModifyCustomDBEngineVersion"], Literal["DescribeDBSecurityGroups"], Literal["DeleteDBSubnetGroup"], Literal["ModifyDBClusterSnapshotAttribute"], Literal["DeleteEventSubscription"], Literal["DeleteDBClusterParameterGroup"], Literal["DescribeDBClusterAutomatedBackups"], Literal["StartExportTask"], Literal["ModifyDBProxy"], Literal["ModifyDBParameterGroup"], Literal["CreateDBClusterEndpoint"], Literal["DescribeDBParameterGroups"], Literal["FailoverGlobalCluster"], Literal["DescribeDBClusterParameters"], Literal["StartDBInstanceAutomatedBackupsReplication"], Literal["DescribeDBClusterSnapshots"], Literal["ApplyPendingMaintenanceAction"], Literal["DeleteDBSnapshot"], Literal["DescribeDBSnapshotAttributes"], Literal["DisableHttpEndpoint"], Literal["DescribeDBLogFiles"], Literal["CreateDBInstance"], Literal["DescribeEventSubscriptions"], Literal["ModifyGlobalCluster"], Literal["DeleteDBInstanceAutomatedBackup"], Literal["CreateIntegration"], Literal["DescribeGlobalClusters"], Literal["SwitchoverBlueGreenDeployment"], Literal["ModifyCurrentDBClusterCapacity"], Literal["DescribeIntegrations"], Literal["StartDBCluster"], Literal["RebootDBInstance"], Literal["CopyDBSnapshot"], Literal["CopyOptionGroup"], Literal["CopyDBClusterSnapshot"], Literal["DeleteDBProxyEndpoint"], Literal["ModifyDBCluster"], Literal["RestoreDBInstanceFromS3"], Literal["ModifyDBProxyEndpoint"], Literal["AddSourceIdentifierToSubscription"], Literal["CreateTenantDatabase"], Literal["DescribeDBEngineVersions"], Literal["DescribeEngineDefaultParameters"], Literal["CrossRegionCommunication"], Literal["DescribeDbSnapshotTenantDatabases"], Literal["ModifyCertificates"], Literal["RemoveSourceIdentifierFromSubscription"], Literal["SwitchoverReadReplica"], Literal["CreateDBSubnetGroup"], Literal["DeleteGlobalCluster"], Literal["ModifyActivityStream"], Literal["DescribeDBProxies"], Literal["DescribeAccountAttributes"], Literal["DescribeDBSnapshots"], Literal["DeleteDBClusterEndpoint"], Literal["ListTagsForResource"], Literal["RemoveFromGlobalCluster"], Literal["StartActivityStream"], Literal["DownloadCompleteDBLogFile"], Literal["ModifyDBSubnetGroup"], Literal["AddTagsToResource"], Literal["SwitchoverGlobalCluster"], Literal["DescribeRecommendationGroups"], Literal["CreateBlueGreenDeployment"], Literal["RestoreDBInstanceToPointInTime"], Literal["CreateDBClusterSnapshot"], Literal["DescribeDBClusterBacktracks"], Literal["StopDBInstanceAutomatedBackupsReplication"], Literal["DeleteCustomDBEngineVersion"], Literal["RebootDBCluster"], Literal["DownloadDBLogFilePortion"], Literal["DescribeExportTasks"], Literal["StopActivityStream"], Literal["CreateDBParameterGroup"], Literal["DescribeOrderableDBInstanceOptions"], Literal["DescribeCertificates"], Literal["DeleteDBInstance"], Literal["DeregisterDBProxyTargets"]]
aws_rds_condition_type = Union[Literal["rds:Piops"], Literal["rds:MultiTenant"], Literal["rds:StorageEncrypted"], Literal["rds:cluster-tag/${TagKey}"], Literal["rds:cluster-pg-tag/${TagKey}"], Literal["rds:BackupTarget"], Literal["rds:EndpointType"], Literal["rds:req-tag/${TagKey}"], Literal["aws:TagKeys"], Literal["rds:MultiAz"], Literal["rds:DatabaseEngine"], Literal["rds:DatabaseName"], Literal["rds:db-tag/${TagKey}"], Literal["rds:DatabaseClass"], Literal["rds:TenantDatabaseName"], Literal["rds:ManageMasterUserPassword"], Literal["aws:ResourceTag/${TagKey}"], Literal["rds:pg-tag/${TagKey}"], Literal["rds:CopyOptionGroup"], Literal["rds:Vpc"], Literal["rds:StorageSize"], Literal["aws:RequestTag/${TagKey}"]]

class aws_rdsStatement(GenericResourceType[aws_rds_privilege_type, aws_rds_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    