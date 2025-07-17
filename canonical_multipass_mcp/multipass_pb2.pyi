from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LaunchRequest(_message.Message):
    __slots__ = ("instance_name", "image", "kernel_name", "num_cores", "mem_size", "disk_space", "time_zone", "cloud_init_user_data", "remote_name", "verbosity_level", "network_options", "permission_to_bridge", "timeout", "password")
    class NetworkOptions(_message.Message):
        __slots__ = ("id", "mode", "mac_address")
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUTO: _ClassVar[LaunchRequest.NetworkOptions.Mode]
            MANUAL: _ClassVar[LaunchRequest.NetworkOptions.Mode]
        AUTO: LaunchRequest.NetworkOptions.Mode
        MANUAL: LaunchRequest.NetworkOptions.Mode
        ID_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        id: str
        mode: LaunchRequest.NetworkOptions.Mode
        mac_address: str
        def __init__(self, id: _Optional[str] = ..., mode: _Optional[_Union[LaunchRequest.NetworkOptions.Mode, str]] = ..., mac_address: _Optional[str] = ...) -> None: ...
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    KERNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_CORES_FIELD_NUMBER: _ClassVar[int]
    MEM_SIZE_FIELD_NUMBER: _ClassVar[int]
    DISK_SPACE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_INIT_USER_DATA_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_TO_BRIDGE_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    image: str
    kernel_name: str
    num_cores: int
    mem_size: str
    disk_space: str
    time_zone: str
    cloud_init_user_data: str
    remote_name: str
    verbosity_level: int
    network_options: _containers.RepeatedCompositeFieldContainer[LaunchRequest.NetworkOptions]
    permission_to_bridge: bool
    timeout: int
    password: str
    def __init__(self, instance_name: _Optional[str] = ..., image: _Optional[str] = ..., kernel_name: _Optional[str] = ..., num_cores: _Optional[int] = ..., mem_size: _Optional[str] = ..., disk_space: _Optional[str] = ..., time_zone: _Optional[str] = ..., cloud_init_user_data: _Optional[str] = ..., remote_name: _Optional[str] = ..., verbosity_level: _Optional[int] = ..., network_options: _Optional[_Iterable[_Union[LaunchRequest.NetworkOptions, _Mapping]]] = ..., permission_to_bridge: bool = ..., timeout: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class LaunchError(_message.Message):
    __slots__ = ("error_codes",)
    class ErrorCodes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OK: _ClassVar[LaunchError.ErrorCodes]
        INVALID_MEM_SIZE: _ClassVar[LaunchError.ErrorCodes]
        INVALID_DISK_SIZE: _ClassVar[LaunchError.ErrorCodes]
        INVALID_HOSTNAME: _ClassVar[LaunchError.ErrorCodes]
        INVALID_NETWORK: _ClassVar[LaunchError.ErrorCodes]
    OK: LaunchError.ErrorCodes
    INVALID_MEM_SIZE: LaunchError.ErrorCodes
    INVALID_DISK_SIZE: LaunchError.ErrorCodes
    INVALID_HOSTNAME: LaunchError.ErrorCodes
    INVALID_NETWORK: LaunchError.ErrorCodes
    ERROR_CODES_FIELD_NUMBER: _ClassVar[int]
    error_codes: _containers.RepeatedScalarFieldContainer[LaunchError.ErrorCodes]
    def __init__(self, error_codes: _Optional[_Iterable[_Union[LaunchError.ErrorCodes, str]]] = ...) -> None: ...

class LaunchProgress(_message.Message):
    __slots__ = ("type", "percent_complete")
    class ProgressTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE: _ClassVar[LaunchProgress.ProgressTypes]
        EXTRACT: _ClassVar[LaunchProgress.ProgressTypes]
        VERIFY: _ClassVar[LaunchProgress.ProgressTypes]
        WAITING: _ClassVar[LaunchProgress.ProgressTypes]
    IMAGE: LaunchProgress.ProgressTypes
    EXTRACT: LaunchProgress.ProgressTypes
    VERIFY: LaunchProgress.ProgressTypes
    WAITING: LaunchProgress.ProgressTypes
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PERCENT_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    type: LaunchProgress.ProgressTypes
    percent_complete: str
    def __init__(self, type: _Optional[_Union[LaunchProgress.ProgressTypes, str]] = ..., percent_complete: _Optional[str] = ...) -> None: ...

class UpdateInfo(_message.Message):
    __slots__ = ("version", "url", "title", "description")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    version: str
    url: str
    title: str
    description: str
    def __init__(self, version: _Optional[str] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class LaunchReply(_message.Message):
    __slots__ = ("vm_instance_name", "launch_progress", "create_message", "log_line", "update_info", "reply_message", "nets_need_bridging", "aliases_to_be_created", "workspaces_to_be_created", "password_requested")
    class Alias(_message.Message):
        __slots__ = ("name", "instance", "command", "working_directory")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_FIELD_NUMBER: _ClassVar[int]
        COMMAND_FIELD_NUMBER: _ClassVar[int]
        WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        name: str
        instance: str
        command: str
        working_directory: str
        def __init__(self, name: _Optional[str] = ..., instance: _Optional[str] = ..., command: _Optional[str] = ..., working_directory: _Optional[str] = ...) -> None: ...
    VM_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NETS_NEED_BRIDGING_FIELD_NUMBER: _ClassVar[int]
    ALIASES_TO_BE_CREATED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACES_TO_BE_CREATED_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    vm_instance_name: str
    launch_progress: LaunchProgress
    create_message: str
    log_line: str
    update_info: UpdateInfo
    reply_message: str
    nets_need_bridging: _containers.RepeatedScalarFieldContainer[str]
    aliases_to_be_created: _containers.RepeatedCompositeFieldContainer[LaunchReply.Alias]
    workspaces_to_be_created: _containers.RepeatedScalarFieldContainer[str]
    password_requested: bool
    def __init__(self, vm_instance_name: _Optional[str] = ..., launch_progress: _Optional[_Union[LaunchProgress, _Mapping]] = ..., create_message: _Optional[str] = ..., log_line: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ..., reply_message: _Optional[str] = ..., nets_need_bridging: _Optional[_Iterable[str]] = ..., aliases_to_be_created: _Optional[_Iterable[_Union[LaunchReply.Alias, _Mapping]]] = ..., workspaces_to_be_created: _Optional[_Iterable[str]] = ..., password_requested: bool = ...) -> None: ...

class PurgeRequest(_message.Message):
    __slots__ = ("verbosity_level",)
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    def __init__(self, verbosity_level: _Optional[int] = ...) -> None: ...

class PurgeReply(_message.Message):
    __slots__ = ("log_line", "purged_instances")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    PURGED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    purged_instances: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, log_line: _Optional[str] = ..., purged_instances: _Optional[_Iterable[str]] = ...) -> None: ...

class FindRequest(_message.Message):
    __slots__ = ("search_string", "remote_name", "verbosity_level", "allow_unsupported", "show_images", "show_blueprints", "force_manifest_network_download")
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    REMOTE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ALLOW_UNSUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SHOW_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SHOW_BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    FORCE_MANIFEST_NETWORK_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    remote_name: str
    verbosity_level: int
    allow_unsupported: bool
    show_images: bool
    show_blueprints: bool
    force_manifest_network_download: bool
    def __init__(self, search_string: _Optional[str] = ..., remote_name: _Optional[str] = ..., verbosity_level: _Optional[int] = ..., allow_unsupported: bool = ..., show_images: bool = ..., show_blueprints: bool = ..., force_manifest_network_download: bool = ...) -> None: ...

class FindReply(_message.Message):
    __slots__ = ("show_images", "show_blueprints", "images_info", "blueprints_info", "log_line")
    class AliasInfo(_message.Message):
        __slots__ = ("remote_name", "alias")
        REMOTE_NAME_FIELD_NUMBER: _ClassVar[int]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        remote_name: str
        alias: str
        def __init__(self, remote_name: _Optional[str] = ..., alias: _Optional[str] = ...) -> None: ...
    class ImageInfo(_message.Message):
        __slots__ = ("os", "release", "version", "aliases_info", "codename")
        OS_FIELD_NUMBER: _ClassVar[int]
        RELEASE_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        ALIASES_INFO_FIELD_NUMBER: _ClassVar[int]
        CODENAME_FIELD_NUMBER: _ClassVar[int]
        os: str
        release: str
        version: str
        aliases_info: _containers.RepeatedCompositeFieldContainer[FindReply.AliasInfo]
        codename: str
        def __init__(self, os: _Optional[str] = ..., release: _Optional[str] = ..., version: _Optional[str] = ..., aliases_info: _Optional[_Iterable[_Union[FindReply.AliasInfo, _Mapping]]] = ..., codename: _Optional[str] = ...) -> None: ...
    SHOW_IMAGES_FIELD_NUMBER: _ClassVar[int]
    SHOW_BLUEPRINTS_FIELD_NUMBER: _ClassVar[int]
    IMAGES_INFO_FIELD_NUMBER: _ClassVar[int]
    BLUEPRINTS_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    show_images: bool
    show_blueprints: bool
    images_info: _containers.RepeatedCompositeFieldContainer[FindReply.ImageInfo]
    blueprints_info: _containers.RepeatedCompositeFieldContainer[FindReply.ImageInfo]
    log_line: str
    def __init__(self, show_images: bool = ..., show_blueprints: bool = ..., images_info: _Optional[_Iterable[_Union[FindReply.ImageInfo, _Mapping]]] = ..., blueprints_info: _Optional[_Iterable[_Union[FindReply.ImageInfo, _Mapping]]] = ..., log_line: _Optional[str] = ...) -> None: ...

class InstanceSnapshotPair(_message.Message):
    __slots__ = ("instance_name", "snapshot_name")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    snapshot_name: str
    def __init__(self, instance_name: _Optional[str] = ..., snapshot_name: _Optional[str] = ...) -> None: ...

class InfoRequest(_message.Message):
    __slots__ = ("instance_snapshot_pairs", "verbosity_level", "no_runtime_information", "snapshots")
    INSTANCE_SNAPSHOT_PAIRS_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NO_RUNTIME_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    instance_snapshot_pairs: _containers.RepeatedCompositeFieldContainer[InstanceSnapshotPair]
    verbosity_level: int
    no_runtime_information: bool
    snapshots: bool
    def __init__(self, instance_snapshot_pairs: _Optional[_Iterable[_Union[InstanceSnapshotPair, _Mapping]]] = ..., verbosity_level: _Optional[int] = ..., no_runtime_information: bool = ..., snapshots: bool = ...) -> None: ...

class IdMap(_message.Message):
    __slots__ = ("host_id", "instance_id")
    HOST_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    host_id: int
    instance_id: int
    def __init__(self, host_id: _Optional[int] = ..., instance_id: _Optional[int] = ...) -> None: ...

class MountMaps(_message.Message):
    __slots__ = ("uid_mappings", "gid_mappings")
    UID_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    GID_MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    uid_mappings: _containers.RepeatedCompositeFieldContainer[IdMap]
    gid_mappings: _containers.RepeatedCompositeFieldContainer[IdMap]
    def __init__(self, uid_mappings: _Optional[_Iterable[_Union[IdMap, _Mapping]]] = ..., gid_mappings: _Optional[_Iterable[_Union[IdMap, _Mapping]]] = ...) -> None: ...

class MountInfo(_message.Message):
    __slots__ = ("longest_path_len", "mount_paths")
    class MountPaths(_message.Message):
        __slots__ = ("source_path", "target_path", "mount_maps")
        SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
        TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
        MOUNT_MAPS_FIELD_NUMBER: _ClassVar[int]
        source_path: str
        target_path: str
        mount_maps: MountMaps
        def __init__(self, source_path: _Optional[str] = ..., target_path: _Optional[str] = ..., mount_maps: _Optional[_Union[MountMaps, _Mapping]] = ...) -> None: ...
    LONGEST_PATH_LEN_FIELD_NUMBER: _ClassVar[int]
    MOUNT_PATHS_FIELD_NUMBER: _ClassVar[int]
    longest_path_len: int
    mount_paths: _containers.RepeatedCompositeFieldContainer[MountInfo.MountPaths]
    def __init__(self, longest_path_len: _Optional[int] = ..., mount_paths: _Optional[_Iterable[_Union[MountInfo.MountPaths, _Mapping]]] = ...) -> None: ...

class InstanceStatus(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[InstanceStatus.Status]
        RUNNING: _ClassVar[InstanceStatus.Status]
        STARTING: _ClassVar[InstanceStatus.Status]
        RESTARTING: _ClassVar[InstanceStatus.Status]
        STOPPED: _ClassVar[InstanceStatus.Status]
        DELETED: _ClassVar[InstanceStatus.Status]
        DELAYED_SHUTDOWN: _ClassVar[InstanceStatus.Status]
        SUSPENDING: _ClassVar[InstanceStatus.Status]
        SUSPENDED: _ClassVar[InstanceStatus.Status]
    UNKNOWN: InstanceStatus.Status
    RUNNING: InstanceStatus.Status
    STARTING: InstanceStatus.Status
    RESTARTING: InstanceStatus.Status
    STOPPED: InstanceStatus.Status
    DELETED: InstanceStatus.Status
    DELAYED_SHUTDOWN: InstanceStatus.Status
    SUSPENDING: InstanceStatus.Status
    SUSPENDED: InstanceStatus.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: InstanceStatus.Status
    def __init__(self, status: _Optional[_Union[InstanceStatus.Status, str]] = ...) -> None: ...

class InstanceDetails(_message.Message):
    __slots__ = ("image_release", "current_release", "id", "load", "memory_usage", "disk_usage", "ipv4", "ipv6", "num_snapshots", "cpu_times", "uptime", "creation_timestamp")
    IMAGE_RELEASE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RELEASE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    DISK_USAGE_FIELD_NUMBER: _ClassVar[int]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    NUM_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    CPU_TIMES_FIELD_NUMBER: _ClassVar[int]
    UPTIME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    image_release: str
    current_release: str
    id: str
    load: str
    memory_usage: str
    disk_usage: str
    ipv4: _containers.RepeatedScalarFieldContainer[str]
    ipv6: _containers.RepeatedScalarFieldContainer[str]
    num_snapshots: int
    cpu_times: str
    uptime: str
    creation_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, image_release: _Optional[str] = ..., current_release: _Optional[str] = ..., id: _Optional[str] = ..., load: _Optional[str] = ..., memory_usage: _Optional[str] = ..., disk_usage: _Optional[str] = ..., ipv4: _Optional[_Iterable[str]] = ..., ipv6: _Optional[_Iterable[str]] = ..., num_snapshots: _Optional[int] = ..., cpu_times: _Optional[str] = ..., uptime: _Optional[str] = ..., creation_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SnapshotFundamentals(_message.Message):
    __slots__ = ("snapshot_name", "parent", "comment", "creation_timestamp")
    SNAPSHOT_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    snapshot_name: str
    parent: str
    comment: str
    creation_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, snapshot_name: _Optional[str] = ..., parent: _Optional[str] = ..., comment: _Optional[str] = ..., creation_timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SnapshotDetails(_message.Message):
    __slots__ = ("fundamentals", "size", "children")
    FUNDAMENTALS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    fundamentals: SnapshotFundamentals
    size: str
    children: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, fundamentals: _Optional[_Union[SnapshotFundamentals, _Mapping]] = ..., size: _Optional[str] = ..., children: _Optional[_Iterable[str]] = ...) -> None: ...

class DetailedInfoItem(_message.Message):
    __slots__ = ("name", "instance_status", "memory_total", "disk_total", "cpu_count", "mount_info", "instance_info", "snapshot_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_TOTAL_FIELD_NUMBER: _ClassVar[int]
    DISK_TOTAL_FIELD_NUMBER: _ClassVar[int]
    CPU_COUNT_FIELD_NUMBER: _ClassVar[int]
    MOUNT_INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_status: InstanceStatus
    memory_total: str
    disk_total: str
    cpu_count: str
    mount_info: MountInfo
    instance_info: InstanceDetails
    snapshot_info: SnapshotDetails
    def __init__(self, name: _Optional[str] = ..., instance_status: _Optional[_Union[InstanceStatus, _Mapping]] = ..., memory_total: _Optional[str] = ..., disk_total: _Optional[str] = ..., cpu_count: _Optional[str] = ..., mount_info: _Optional[_Union[MountInfo, _Mapping]] = ..., instance_info: _Optional[_Union[InstanceDetails, _Mapping]] = ..., snapshot_info: _Optional[_Union[SnapshotDetails, _Mapping]] = ...) -> None: ...

class InfoReply(_message.Message):
    __slots__ = ("details", "snapshots", "log_line", "update_info")
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[DetailedInfoItem]
    snapshots: bool
    log_line: str
    update_info: UpdateInfo
    def __init__(self, details: _Optional[_Iterable[_Union[DetailedInfoItem, _Mapping]]] = ..., snapshots: bool = ..., log_line: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("verbosity_level", "snapshots", "request_ipv4")
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_IPV4_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    snapshots: bool
    request_ipv4: bool
    def __init__(self, verbosity_level: _Optional[int] = ..., snapshots: bool = ..., request_ipv4: bool = ...) -> None: ...

class ListVMInstance(_message.Message):
    __slots__ = ("name", "instance_status", "ipv4", "ipv6", "current_release")
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_STATUS_FIELD_NUMBER: _ClassVar[int]
    IPV4_FIELD_NUMBER: _ClassVar[int]
    IPV6_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RELEASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    instance_status: InstanceStatus
    ipv4: _containers.RepeatedScalarFieldContainer[str]
    ipv6: _containers.RepeatedScalarFieldContainer[str]
    current_release: str
    def __init__(self, name: _Optional[str] = ..., instance_status: _Optional[_Union[InstanceStatus, _Mapping]] = ..., ipv4: _Optional[_Iterable[str]] = ..., ipv6: _Optional[_Iterable[str]] = ..., current_release: _Optional[str] = ...) -> None: ...

class ListVMSnapshot(_message.Message):
    __slots__ = ("name", "fundamentals")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FUNDAMENTALS_FIELD_NUMBER: _ClassVar[int]
    name: str
    fundamentals: SnapshotFundamentals
    def __init__(self, name: _Optional[str] = ..., fundamentals: _Optional[_Union[SnapshotFundamentals, _Mapping]] = ...) -> None: ...

class InstancesList(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[ListVMInstance]
    def __init__(self, instances: _Optional[_Iterable[_Union[ListVMInstance, _Mapping]]] = ...) -> None: ...

class SnapshotsList(_message.Message):
    __slots__ = ("snapshots",)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[ListVMSnapshot]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[ListVMSnapshot, _Mapping]]] = ...) -> None: ...

class ListReply(_message.Message):
    __slots__ = ("instance_list", "snapshot_list", "log_line", "update_info")
    INSTANCE_LIST_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_LIST_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    instance_list: InstancesList
    snapshot_list: SnapshotsList
    log_line: str
    update_info: UpdateInfo
    def __init__(self, instance_list: _Optional[_Union[InstancesList, _Mapping]] = ..., snapshot_list: _Optional[_Union[SnapshotsList, _Mapping]] = ..., log_line: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ...) -> None: ...

class NetworksRequest(_message.Message):
    __slots__ = ("verbosity_level",)
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    def __init__(self, verbosity_level: _Optional[int] = ...) -> None: ...

class NetInterface(_message.Message):
    __slots__ = ("name", "type", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class NetworksReply(_message.Message):
    __slots__ = ("interfaces", "log_line", "update_info")
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    interfaces: _containers.RepeatedCompositeFieldContainer[NetInterface]
    log_line: str
    update_info: UpdateInfo
    def __init__(self, interfaces: _Optional[_Iterable[_Union[NetInterface, _Mapping]]] = ..., log_line: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ...) -> None: ...

class TargetPathInfo(_message.Message):
    __slots__ = ("instance_name", "target_path")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    instance_name: str
    target_path: str
    def __init__(self, instance_name: _Optional[str] = ..., target_path: _Optional[str] = ...) -> None: ...

class MountRequest(_message.Message):
    __slots__ = ("source_path", "target_paths", "mount_maps", "verbosity_level", "mount_type", "password")
    class MountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASSIC: _ClassVar[MountRequest.MountType]
        NATIVE: _ClassVar[MountRequest.MountType]
    CLASSIC: MountRequest.MountType
    NATIVE: MountRequest.MountType
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATHS_FIELD_NUMBER: _ClassVar[int]
    MOUNT_MAPS_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    source_path: str
    target_paths: _containers.RepeatedCompositeFieldContainer[TargetPathInfo]
    mount_maps: MountMaps
    verbosity_level: int
    mount_type: MountRequest.MountType
    password: str
    def __init__(self, source_path: _Optional[str] = ..., target_paths: _Optional[_Iterable[_Union[TargetPathInfo, _Mapping]]] = ..., mount_maps: _Optional[_Union[MountMaps, _Mapping]] = ..., verbosity_level: _Optional[int] = ..., mount_type: _Optional[_Union[MountRequest.MountType, str]] = ..., password: _Optional[str] = ...) -> None: ...

class MountReply(_message.Message):
    __slots__ = ("log_line", "reply_message", "password_requested")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    reply_message: str
    password_requested: bool
    def __init__(self, log_line: _Optional[str] = ..., reply_message: _Optional[str] = ..., password_requested: bool = ...) -> None: ...

class PingRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PingReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InstanceNames(_message.Message):
    __slots__ = ("instance_name",)
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    instance_name: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instance_name: _Optional[_Iterable[str]] = ...) -> None: ...

class RecoverRequest(_message.Message):
    __slots__ = ("instance_names", "verbosity_level")
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance_names: InstanceNames
    verbosity_level: int
    def __init__(self, instance_names: _Optional[_Union[InstanceNames, _Mapping]] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class RecoverReply(_message.Message):
    __slots__ = ("log_line",)
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    def __init__(self, log_line: _Optional[str] = ...) -> None: ...

class SSHInfoRequest(_message.Message):
    __slots__ = ("instance_name", "verbosity_level")
    INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance_name: _containers.RepeatedScalarFieldContainer[str]
    verbosity_level: int
    def __init__(self, instance_name: _Optional[_Iterable[str]] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class SSHInfo(_message.Message):
    __slots__ = ("port", "priv_key_base64", "host", "username")
    PORT_FIELD_NUMBER: _ClassVar[int]
    PRIV_KEY_BASE64_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    port: int
    priv_key_base64: str
    host: str
    username: str
    def __init__(self, port: _Optional[int] = ..., priv_key_base64: _Optional[str] = ..., host: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...

class SSHInfoReply(_message.Message):
    __slots__ = ("ssh_info", "log_line")
    class SshInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SSHInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SSHInfo, _Mapping]] = ...) -> None: ...
    SSH_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    ssh_info: _containers.MessageMap[str, SSHInfo]
    log_line: str
    def __init__(self, ssh_info: _Optional[_Mapping[str, SSHInfo]] = ..., log_line: _Optional[str] = ...) -> None: ...

class StartError(_message.Message):
    __slots__ = ("instance_errors",)
    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OK: _ClassVar[StartError.ErrorCode]
        DOES_NOT_EXIST: _ClassVar[StartError.ErrorCode]
        INSTANCE_DELETED: _ClassVar[StartError.ErrorCode]
        OTHER: _ClassVar[StartError.ErrorCode]
    OK: StartError.ErrorCode
    DOES_NOT_EXIST: StartError.ErrorCode
    INSTANCE_DELETED: StartError.ErrorCode
    OTHER: StartError.ErrorCode
    class InstanceErrorsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StartError.ErrorCode
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StartError.ErrorCode, str]] = ...) -> None: ...
    INSTANCE_ERRORS_FIELD_NUMBER: _ClassVar[int]
    instance_errors: _containers.ScalarMap[str, StartError.ErrorCode]
    def __init__(self, instance_errors: _Optional[_Mapping[str, StartError.ErrorCode]] = ...) -> None: ...

class StartRequest(_message.Message):
    __slots__ = ("instance_names", "verbosity_level", "timeout", "password")
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    instance_names: InstanceNames
    verbosity_level: int
    timeout: int
    password: str
    def __init__(self, instance_names: _Optional[_Union[InstanceNames, _Mapping]] = ..., verbosity_level: _Optional[int] = ..., timeout: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class StartReply(_message.Message):
    __slots__ = ("log_line", "reply_message", "update_info", "password_requested")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    reply_message: str
    update_info: UpdateInfo
    password_requested: bool
    def __init__(self, log_line: _Optional[str] = ..., reply_message: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ..., password_requested: bool = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = ("instance_names", "time_minutes", "cancel_shutdown", "verbosity_level", "force_stop")
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    TIME_MINUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_SHUTDOWN_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FORCE_STOP_FIELD_NUMBER: _ClassVar[int]
    instance_names: InstanceNames
    time_minutes: int
    cancel_shutdown: bool
    verbosity_level: int
    force_stop: bool
    def __init__(self, instance_names: _Optional[_Union[InstanceNames, _Mapping]] = ..., time_minutes: _Optional[int] = ..., cancel_shutdown: bool = ..., verbosity_level: _Optional[int] = ..., force_stop: bool = ...) -> None: ...

class StopReply(_message.Message):
    __slots__ = ("log_line",)
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    def __init__(self, log_line: _Optional[str] = ...) -> None: ...

class SuspendRequest(_message.Message):
    __slots__ = ("instance_names", "verbosity_level")
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance_names: InstanceNames
    verbosity_level: int
    def __init__(self, instance_names: _Optional[_Union[InstanceNames, _Mapping]] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class SuspendReply(_message.Message):
    __slots__ = ("log_line",)
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    def __init__(self, log_line: _Optional[str] = ...) -> None: ...

class RestartRequest(_message.Message):
    __slots__ = ("instance_names", "verbosity_level", "timeout", "password")
    INSTANCE_NAMES_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    instance_names: InstanceNames
    verbosity_level: int
    timeout: int
    password: str
    def __init__(self, instance_names: _Optional[_Union[InstanceNames, _Mapping]] = ..., verbosity_level: _Optional[int] = ..., timeout: _Optional[int] = ..., password: _Optional[str] = ...) -> None: ...

class RestartReply(_message.Message):
    __slots__ = ("log_line", "reply_message", "update_info", "password_requested")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    reply_message: str
    update_info: UpdateInfo
    password_requested: bool
    def __init__(self, log_line: _Optional[str] = ..., reply_message: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ..., password_requested: bool = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("instance_snapshot_pairs", "purge", "verbosity_level", "purge_snapshots")
    INSTANCE_SNAPSHOT_PAIRS_FIELD_NUMBER: _ClassVar[int]
    PURGE_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PURGE_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    instance_snapshot_pairs: _containers.RepeatedCompositeFieldContainer[InstanceSnapshotPair]
    purge: bool
    verbosity_level: int
    purge_snapshots: bool
    def __init__(self, instance_snapshot_pairs: _Optional[_Iterable[_Union[InstanceSnapshotPair, _Mapping]]] = ..., purge: bool = ..., verbosity_level: _Optional[int] = ..., purge_snapshots: bool = ...) -> None: ...

class DeleteReply(_message.Message):
    __slots__ = ("log_line", "purged_instances", "confirm_snapshot_purging")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    PURGED_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_SNAPSHOT_PURGING_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    purged_instances: _containers.RepeatedScalarFieldContainer[str]
    confirm_snapshot_purging: bool
    def __init__(self, log_line: _Optional[str] = ..., purged_instances: _Optional[_Iterable[str]] = ..., confirm_snapshot_purging: bool = ...) -> None: ...

class UmountRequest(_message.Message):
    __slots__ = ("target_paths", "verbosity_level")
    TARGET_PATHS_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    target_paths: _containers.RepeatedCompositeFieldContainer[TargetPathInfo]
    verbosity_level: int
    def __init__(self, target_paths: _Optional[_Iterable[_Union[TargetPathInfo, _Mapping]]] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class UmountReply(_message.Message):
    __slots__ = ("log_line",)
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    def __init__(self, log_line: _Optional[str] = ...) -> None: ...

class VersionRequest(_message.Message):
    __slots__ = ("verbosity_level",)
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    def __init__(self, verbosity_level: _Optional[int] = ...) -> None: ...

class VersionReply(_message.Message):
    __slots__ = ("version", "log_line", "update_info")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
    version: str
    log_line: str
    update_info: UpdateInfo
    def __init__(self, version: _Optional[str] = ..., log_line: _Optional[str] = ..., update_info: _Optional[_Union[UpdateInfo, _Mapping]] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("key", "verbosity_level")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    key: str
    verbosity_level: int
    def __init__(self, key: _Optional[str] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class GetReply(_message.Message):
    __slots__ = ("value", "log_line")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    value: str
    log_line: str
    def __init__(self, value: _Optional[str] = ..., log_line: _Optional[str] = ...) -> None: ...

class SetRequest(_message.Message):
    __slots__ = ("key", "val", "verbosity_level", "authorized")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VAL_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    key: str
    val: str
    verbosity_level: int
    authorized: bool
    def __init__(self, key: _Optional[str] = ..., val: _Optional[str] = ..., verbosity_level: _Optional[int] = ..., authorized: bool = ...) -> None: ...

class SetReply(_message.Message):
    __slots__ = ("log_line", "reply_message", "needs_authorization")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEEDS_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    reply_message: str
    needs_authorization: bool
    def __init__(self, log_line: _Optional[str] = ..., reply_message: _Optional[str] = ..., needs_authorization: bool = ...) -> None: ...

class KeysRequest(_message.Message):
    __slots__ = ("verbosity_level",)
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    def __init__(self, verbosity_level: _Optional[int] = ...) -> None: ...

class KeysReply(_message.Message):
    __slots__ = ("log_line", "settings_keys")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_KEYS_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    settings_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, log_line: _Optional[str] = ..., settings_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthenticateRequest(_message.Message):
    __slots__ = ("passphrase", "verbosity_level")
    PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    passphrase: str
    verbosity_level: int
    def __init__(self, passphrase: _Optional[str] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class AuthenticateReply(_message.Message):
    __slots__ = ("log_line",)
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    def __init__(self, log_line: _Optional[str] = ...) -> None: ...

class SnapshotRequest(_message.Message):
    __slots__ = ("instance", "snapshot", "comment", "verbosity_level")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance: str
    snapshot: str
    comment: str
    verbosity_level: int
    def __init__(self, instance: _Optional[str] = ..., snapshot: _Optional[str] = ..., comment: _Optional[str] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class SnapshotReply(_message.Message):
    __slots__ = ("snapshot", "log_line")
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    snapshot: str
    log_line: str
    def __init__(self, snapshot: _Optional[str] = ..., log_line: _Optional[str] = ...) -> None: ...

class RestoreRequest(_message.Message):
    __slots__ = ("instance", "snapshot", "destructive", "verbosity_level")
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    DESTRUCTIVE_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    instance: str
    snapshot: str
    destructive: bool
    verbosity_level: int
    def __init__(self, instance: _Optional[str] = ..., snapshot: _Optional[str] = ..., destructive: bool = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class RestoreReply(_message.Message):
    __slots__ = ("log_line", "reply_message", "confirm_destructive")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_DESTRUCTIVE_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    reply_message: str
    confirm_destructive: bool
    def __init__(self, log_line: _Optional[str] = ..., reply_message: _Optional[str] = ..., confirm_destructive: bool = ...) -> None: ...

class CloneRequest(_message.Message):
    __slots__ = ("source_name", "destination_name", "verbosity_level")
    SOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    source_name: str
    destination_name: str
    verbosity_level: int
    def __init__(self, source_name: _Optional[str] = ..., destination_name: _Optional[str] = ..., verbosity_level: _Optional[int] = ...) -> None: ...

class CloneReply(_message.Message):
    __slots__ = ("reply_message", "log_line")
    REPLY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    reply_message: str
    log_line: str
    def __init__(self, reply_message: _Optional[str] = ..., log_line: _Optional[str] = ...) -> None: ...

class DaemonInfoRequest(_message.Message):
    __slots__ = ("verbosity_level",)
    VERBOSITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    verbosity_level: int
    def __init__(self, verbosity_level: _Optional[int] = ...) -> None: ...

class DaemonInfoReply(_message.Message):
    __slots__ = ("log_line", "available_space", "cpus", "memory")
    LOG_LINE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SPACE_FIELD_NUMBER: _ClassVar[int]
    CPUS_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    log_line: str
    available_space: int
    cpus: int
    memory: int
    def __init__(self, log_line: _Optional[str] = ..., available_space: _Optional[int] = ..., cpus: _Optional[int] = ..., memory: _Optional[int] = ...) -> None: ...
