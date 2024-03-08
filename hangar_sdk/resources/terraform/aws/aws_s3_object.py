from typing import Any, Dict, Optional, Sequence

from attr import define, field

from hangar_sdk.resources.terraform import AbstractTerraformBlock, AbstractTerraformResource


@define(kw_only=True, slots=False)
class DefaultTags(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="default_tags")
    tags: Optional[Dict[str, str]] = None


@define(kw_only=True, slots=False)
class OverrideProvider(AbstractTerraformBlock):
    _block_type: str = "block"
    _name: str = field(alias="_name", default="override_provider")
    default_tags: Optional[Sequence[DefaultTags]] = None


@define(kw_only=True, slots=False)
class AwsS3Object(AbstractTerraformResource):
    _group: Any
    _top_name: str
    bucket: str
    key: str
    _block_type: str = "resource"
    _name: str = field(alias="_name", default="aws_s3_object")
    acl: Optional[str] = None
    bucket_key_enabled: Optional[bool] = None
    cache_control: Optional[str] = None
    checksum_algorithm: Optional[str] = None
    content: Optional[str] = None
    content_base64: Optional[str] = None
    content_disposition: Optional[str] = None
    content_encoding: Optional[str] = None
    content_language: Optional[str] = None
    content_type: Optional[str] = None
    etag: Optional[str] = None
    force_destroy: Optional[bool] = None
    kms_key_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    object_lock_legal_hold_status: Optional[str] = None
    object_lock_mode: Optional[str] = None
    object_lock_retain_until_date: Optional[str] = None
    override_provider: Optional[Sequence[OverrideProvider]] = None
    server_side_encryption: Optional[str] = None
    source: Optional[str] = None
    source_hash: Optional[str] = None
    storage_class: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    tags_all: Optional[Dict[str, str]] = None
    website_redirect: Optional[str] = None
