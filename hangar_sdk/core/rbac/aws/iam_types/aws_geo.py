from typing import Union, Literal, List
from hangar_sdk.core.rbac.aws.base_type import GenericResourceType
from hangar_sdk.resources.terraform import AbstractTerraformResource

aws_geo_privilege_type = Union[Literal["DeleteRouteCalculator"], Literal["BatchUpdateDevicePosition"], Literal["CreateMap"], Literal["UntagResource"], Literal["DeleteMap"], Literal["ListGeofenceCollections"], Literal["DeletePlaceIndex"], Literal["ListKeys"], Literal["PutGeofence"], Literal["DeleteTracker"], Literal["BatchEvaluateGeofences"], Literal["DescribeMap"], Literal["ListGeofences"], Literal["ListMaps"], Literal["CalculateRouteMatrix"], Literal["ListTrackerConsumers"], Literal["DescribeGeofenceCollection"], Literal["CreatePlaceIndex"], Literal["GetDevicePositionHistory"], Literal["GetMapTile"], Literal["UpdateMap"], Literal["ListTrackers"], Literal["GetMapGlyphs"], Literal["BatchDeleteDevicePositionHistory"], Literal["AssociateTrackerConsumer"], Literal["CreateTracker"], Literal["ListTagsForResource"], Literal["DescribeKey"], Literal["CalculateRoute"], Literal["SearchPlaceIndexForPosition"], Literal["DescribeTracker"], Literal["BatchPutGeofence"], Literal["UpdateKey"], Literal["SearchPlaceIndexForText"], Literal["DescribeRouteCalculator"], Literal["DeleteGeofenceCollection"], Literal["UpdateTracker"], Literal["BatchDeleteGeofence"], Literal["UpdateRouteCalculator"], Literal["ListPlaceIndexes"], Literal["SearchPlaceIndexForSuggestions"], Literal["UpdateGeofenceCollection"], Literal["DescribePlaceIndex"], Literal["GetMapStyleDescriptor"], Literal["CreateGeofenceCollection"], Literal["GetMapSprites"], Literal["TagResource"], Literal["CreateKey"], Literal["UpdatePlaceIndex"], Literal["BatchGetDevicePosition"], Literal["DeleteKey"], Literal["ListRouteCalculators"], Literal["GetDevicePosition"], Literal["ListDevicePositions"], Literal["DisassociateTrackerConsumer"], Literal["GetGeofence"], Literal["CreateRouteCalculator"], Literal["GetPlace"]]
aws_geo_condition_type = Union[Literal["geo:GeofenceIds"], Literal["geo:DeviceIds"], Literal["aws:TagKeys"], Literal["aws:RequestTag/${TagKey}"]]

class aws_geoStatement(GenericResourceType[aws_geo_privilege_type, aws_geo_condition_type]):
    def __init__(self, policy=None,  arns: List = [],  resources: List[AbstractTerraformResource] = None):
        super().__init__(policy, arns, resources)
    