import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='carla_server.proto',
  package='carla_server',
  syntax='proto3',
  serialized_pb=_b('\n\x12\x63\x61rla_server.proto\x12\x0c\x63\x61rla_server\"+\n\x08Vector3D\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"6\n\nRotation3D\x12\r\n\x05pitch\x18\x01 \x01(\x02\x12\x0b\n\x03yaw\x18\x02 \x01(\x02\x12\x0c\n\x04roll\x18\x03 \x01(\x02\"\x92\x01\n\tTransform\x12(\n\x08location\x18\x01 \x01(\x0b\x32\x16.carla_server.Vector3D\x12/\n\x0borientation\x18\x02 \x01(\x0b\x32\x16.carla_server.Vector3DB\x02\x18\x01\x12*\n\x08rotation\x18\x03 \x01(\x0b\x32\x18.carla_server.Rotation3D\"\x80\x01\n\x06Sensor\x12\n\n\x02id\x18\x01 \x01(\x07\x12\'\n\x04type\x18\x02 \x01(\x0e\x32\x19.carla_server.Sensor.Type\x12\x0c\n\x04name\x18\x03 \x01(\t\"3\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43\x41MERA\x10\x01\x12\x12\n\x0eLIDAR_RAY_CAST\x10\x02\"x\n\x07Vehicle\x12*\n\ttransform\x18\x01 \x01(\x0b\x32\x17.carla_server.Transform\x12*\n\nbox_extent\x18\x02 \x01(\x0b\x32\x16.carla_server.Vector3D\x12\x15\n\rforward_speed\x18\x03 \x01(\x02\"{\n\nPedestrian\x12*\n\ttransform\x18\x01 \x01(\x0b\x32\x17.carla_server.Transform\x12*\n\nbox_extent\x18\x02 \x01(\x0b\x32\x16.carla_server.Vector3D\x12\x15\n\rforward_speed\x18\x03 \x01(\x02\"\x94\x01\n\x0cTrafficLight\x12*\n\ttransform\x18\x01 \x01(\x0b\x32\x17.carla_server.Transform\x12/\n\x05state\x18\x02 \x01(\x0e\x32 .carla_server.TrafficLight.State\"\'\n\x05State\x12\t\n\x05GREEN\x10\x00\x12\n\n\x06YELLOW\x10\x01\x12\x07\n\x03RED\x10\x02\"Q\n\x0eSpeedLimitSign\x12*\n\ttransform\x18\x01 \x01(\x0b\x32\x17.carla_server.Transform\x12\x13\n\x0bspeed_limit\x18\x02 \x01(\x02\"\xe5\x01\n\x05\x41gent\x12\n\n\x02id\x18\x01 \x01(\x07\x12(\n\x07vehicle\x18\x02 \x01(\x0b\x32\x15.carla_server.VehicleH\x00\x12.\n\npedestrian\x18\x03 \x01(\x0b\x32\x18.carla_server.PedestrianH\x00\x12\x33\n\rtraffic_light\x18\x04 \x01(\x0b\x32\x1a.carla_server.TrafficLightH\x00\x12\x38\n\x10speed_limit_sign\x18\x05 \x01(\x0b\x32\x1c.carla_server.SpeedLimitSignH\x00\x42\x07\n\x05\x61gent\"%\n\x11RequestNewEpisode\x12\x10\n\x08ini_file\x18\x01 \x01(\t\"n\n\x10SceneDescription\x12\x33\n\x12player_start_spots\x18\x01 \x03(\x0b\x32\x17.carla_server.Transform\x12%\n\x07sensors\x18\x02 \x03(\x0b\x32\x14.carla_server.Sensor\"/\n\x0c\x45pisodeStart\x12\x1f\n\x17player_start_spot_index\x18\x01 \x01(\r\"\x1d\n\x0c\x45pisodeReady\x12\r\n\x05ready\x18\x01 \x01(\x08\"^\n\x07\x43ontrol\x12\r\n\x05steer\x18\x01 \x01(\x02\x12\x10\n\x08throttle\x18\x02 \x01(\x02\x12\r\n\x05\x62rake\x18\x03 \x01(\x02\x12\x12\n\nhand_brake\x18\x04 \x01(\x08\x12\x0f\n\x07reverse\x18\x05 \x01(\x08\"\xb6\x04\n\x0cMeasurements\x12\x1a\n\x12platform_timestamp\x18\x01 \x01(\r\x12\x16\n\x0egame_timestamp\x18\x02 \x01(\r\x12J\n\x13player_measurements\x18\x03 \x01(\x0b\x32-.carla_server.Measurements.PlayerMeasurements\x12.\n\x11non_player_agents\x18\x04 \x03(\x0b\x32\x13.carla_server.Agent\x1a\xf5\x02\n\x12PlayerMeasurements\x12*\n\ttransform\x18\x01 \x01(\x0b\x32\x17.carla_server.Transform\x12*\n\nbox_extent\x18\x0b \x01(\x0b\x32\x16.carla_server.Vector3D\x12,\n\x0c\x61\x63\x63\x65leration\x18\x03 \x01(\x0b\x32\x16.carla_server.Vector3D\x12\x15\n\rforward_speed\x18\x04 \x01(\x02\x12\x1a\n\x12\x63ollision_vehicles\x18\x05 \x01(\x02\x12\x1d\n\x15\x63ollision_pedestrians\x18\x06 \x01(\x02\x12\x17\n\x0f\x63ollision_other\x18\x07 \x01(\x02\x12\x1e\n\x16intersection_otherlane\x18\x08 \x01(\x02\x12\x1c\n\x14intersection_offroad\x18\t \x01(\x02\x12\x30\n\x11\x61utopilot_control\x18\n \x01(\x0b\x32\x15.carla_server.ControlB\x03\xf8\x01\x01\x62\x06proto3')
)



_SENSOR_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='carla_server.Sensor.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR_RAY_CAST', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=364,
  serialized_end=415,
)
_sym_db.RegisterEnumDescriptor(_SENSOR_TYPE)

_TRAFFICLIGHT_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='carla_server.TrafficLight.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GREEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YELLOW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=774,
  serialized_end=813,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICLIGHT_STATE)


_VECTOR3D = _descriptor.Descriptor(
  name='Vector3D',
  full_name='carla_server.Vector3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='carla_server.Vector3D.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='carla_server.Vector3D.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='carla_server.Vector3D.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=79,
)


_ROTATION3D = _descriptor.Descriptor(
  name='Rotation3D',
  full_name='carla_server.Rotation3D',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch', full_name='carla_server.Rotation3D.pitch', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='carla_server.Rotation3D.yaw', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='roll', full_name='carla_server.Rotation3D.roll', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=135,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='carla_server.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='carla_server.Transform.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='carla_server.Transform.orientation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='carla_server.Transform.rotation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=284,
)


_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='carla_server.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='carla_server.Sensor.id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='carla_server.Sensor.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='carla_server.Sensor.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENSOR_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=287,
  serialized_end=415,
)


_VEHICLE = _descriptor.Descriptor(
  name='Vehicle',
  full_name='carla_server.Vehicle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='carla_server.Vehicle.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_extent', full_name='carla_server.Vehicle.box_extent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_speed', full_name='carla_server.Vehicle.forward_speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=537,
)


_PEDESTRIAN = _descriptor.Descriptor(
  name='Pedestrian',
  full_name='carla_server.Pedestrian',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='carla_server.Pedestrian.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_extent', full_name='carla_server.Pedestrian.box_extent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_speed', full_name='carla_server.Pedestrian.forward_speed', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=662,
)


_TRAFFICLIGHT = _descriptor.Descriptor(
  name='TrafficLight',
  full_name='carla_server.TrafficLight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='carla_server.TrafficLight.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='carla_server.TrafficLight.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRAFFICLIGHT_STATE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=813,
)


_SPEEDLIMITSIGN = _descriptor.Descriptor(
  name='SpeedLimitSign',
  full_name='carla_server.SpeedLimitSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='carla_server.SpeedLimitSign.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_limit', full_name='carla_server.SpeedLimitSign.speed_limit', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=815,
  serialized_end=896,
)


_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='carla_server.Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='carla_server.Agent.id', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vehicle', full_name='carla_server.Agent.vehicle', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pedestrian', full_name='carla_server.Agent.pedestrian', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='traffic_light', full_name='carla_server.Agent.traffic_light', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_limit_sign', full_name='carla_server.Agent.speed_limit_sign', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='agent', full_name='carla_server.Agent.agent',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=899,
  serialized_end=1128,
)


_REQUESTNEWEPISODE = _descriptor.Descriptor(
  name='RequestNewEpisode',
  full_name='carla_server.RequestNewEpisode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ini_file', full_name='carla_server.RequestNewEpisode.ini_file', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1130,
  serialized_end=1167,
)


_SCENEDESCRIPTION = _descriptor.Descriptor(
  name='SceneDescription',
  full_name='carla_server.SceneDescription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_start_spots', full_name='carla_server.SceneDescription.player_start_spots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensors', full_name='carla_server.SceneDescription.sensors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1169,
  serialized_end=1279,
)


_EPISODESTART = _descriptor.Descriptor(
  name='EpisodeStart',
  full_name='carla_server.EpisodeStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_start_spot_index', full_name='carla_server.EpisodeStart.player_start_spot_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1281,
  serialized_end=1328,
)


_EPISODEREADY = _descriptor.Descriptor(
  name='EpisodeReady',
  full_name='carla_server.EpisodeReady',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ready', full_name='carla_server.EpisodeReady.ready', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1330,
  serialized_end=1359,
)


_CONTROL = _descriptor.Descriptor(
  name='Control',
  full_name='carla_server.Control',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='steer', full_name='carla_server.Control.steer', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='throttle', full_name='carla_server.Control.throttle', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brake', full_name='carla_server.Control.brake', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hand_brake', full_name='carla_server.Control.hand_brake', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse', full_name='carla_server.Control.reverse', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1361,
  serialized_end=1455,
)


_MEASUREMENTS_PLAYERMEASUREMENTS = _descriptor.Descriptor(
  name='PlayerMeasurements',
  full_name='carla_server.Measurements.PlayerMeasurements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transform', full_name='carla_server.Measurements.PlayerMeasurements.transform', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='box_extent', full_name='carla_server.Measurements.PlayerMeasurements.box_extent', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='acceleration', full_name='carla_server.Measurements.PlayerMeasurements.acceleration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forward_speed', full_name='carla_server.Measurements.PlayerMeasurements.forward_speed', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_vehicles', full_name='carla_server.Measurements.PlayerMeasurements.collision_vehicles', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_pedestrians', full_name='carla_server.Measurements.PlayerMeasurements.collision_pedestrians', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collision_other', full_name='carla_server.Measurements.PlayerMeasurements.collision_other', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intersection_otherlane', full_name='carla_server.Measurements.PlayerMeasurements.intersection_otherlane', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intersection_offroad', full_name='carla_server.Measurements.PlayerMeasurements.intersection_offroad', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='autopilot_control', full_name='carla_server.Measurements.PlayerMeasurements.autopilot_control', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1651,
  serialized_end=2024,
)

_MEASUREMENTS = _descriptor.Descriptor(
  name='Measurements',
  full_name='carla_server.Measurements',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform_timestamp', full_name='carla_server.Measurements.platform_timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_timestamp', full_name='carla_server.Measurements.game_timestamp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='player_measurements', full_name='carla_server.Measurements.player_measurements', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='non_player_agents', full_name='carla_server.Measurements.non_player_agents', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MEASUREMENTS_PLAYERMEASUREMENTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1458,
  serialized_end=2024,
)

_TRANSFORM.fields_by_name['location'].message_type = _VECTOR3D
_TRANSFORM.fields_by_name['orientation'].message_type = _VECTOR3D
_TRANSFORM.fields_by_name['rotation'].message_type = _ROTATION3D
_SENSOR.fields_by_name['type'].enum_type = _SENSOR_TYPE
_SENSOR_TYPE.containing_type = _SENSOR
_VEHICLE.fields_by_name['transform'].message_type = _TRANSFORM
_VEHICLE.fields_by_name['box_extent'].message_type = _VECTOR3D
_PEDESTRIAN.fields_by_name['transform'].message_type = _TRANSFORM
_PEDESTRIAN.fields_by_name['box_extent'].message_type = _VECTOR3D
_TRAFFICLIGHT.fields_by_name['transform'].message_type = _TRANSFORM
_TRAFFICLIGHT.fields_by_name['state'].enum_type = _TRAFFICLIGHT_STATE
_TRAFFICLIGHT_STATE.containing_type = _TRAFFICLIGHT
_SPEEDLIMITSIGN.fields_by_name['transform'].message_type = _TRANSFORM
_AGENT.fields_by_name['vehicle'].message_type = _VEHICLE
_AGENT.fields_by_name['pedestrian'].message_type = _PEDESTRIAN
_AGENT.fields_by_name['traffic_light'].message_type = _TRAFFICLIGHT
_AGENT.fields_by_name['speed_limit_sign'].message_type = _SPEEDLIMITSIGN
_AGENT.oneofs_by_name['agent'].fields.append(
  _AGENT.fields_by_name['vehicle'])
_AGENT.fields_by_name['vehicle'].containing_oneof = _AGENT.oneofs_by_name['agent']
_AGENT.oneofs_by_name['agent'].fields.append(
  _AGENT.fields_by_name['pedestrian'])
_AGENT.fields_by_name['pedestrian'].containing_oneof = _AGENT.oneofs_by_name['agent']
_AGENT.oneofs_by_name['agent'].fields.append(
  _AGENT.fields_by_name['traffic_light'])
_AGENT.fields_by_name['traffic_light'].containing_oneof = _AGENT.oneofs_by_name['agent']
_AGENT.oneofs_by_name['agent'].fields.append(
  _AGENT.fields_by_name['speed_limit_sign'])
_AGENT.fields_by_name['speed_limit_sign'].containing_oneof = _AGENT.oneofs_by_name['agent']
_SCENEDESCRIPTION.fields_by_name['player_start_spots'].message_type = _TRANSFORM
_SCENEDESCRIPTION.fields_by_name['sensors'].message_type = _SENSOR
_MEASUREMENTS_PLAYERMEASUREMENTS.fields_by_name['transform'].message_type = _TRANSFORM
_MEASUREMENTS_PLAYERMEASUREMENTS.fields_by_name['box_extent'].message_type = _VECTOR3D
_MEASUREMENTS_PLAYERMEASUREMENTS.fields_by_name['acceleration'].message_type = _VECTOR3D
_MEASUREMENTS_PLAYERMEASUREMENTS.fields_by_name['autopilot_control'].message_type = _CONTROL
_MEASUREMENTS_PLAYERMEASUREMENTS.containing_type = _MEASUREMENTS
_MEASUREMENTS.fields_by_name['player_measurements'].message_type = _MEASUREMENTS_PLAYERMEASUREMENTS
_MEASUREMENTS.fields_by_name['non_player_agents'].message_type = _AGENT
DESCRIPTOR.message_types_by_name['Vector3D'] = _VECTOR3D
DESCRIPTOR.message_types_by_name['Rotation3D'] = _ROTATION3D
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
DESCRIPTOR.message_types_by_name['Vehicle'] = _VEHICLE
DESCRIPTOR.message_types_by_name['Pedestrian'] = _PEDESTRIAN
DESCRIPTOR.message_types_by_name['TrafficLight'] = _TRAFFICLIGHT
DESCRIPTOR.message_types_by_name['SpeedLimitSign'] = _SPEEDLIMITSIGN
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
DESCRIPTOR.message_types_by_name['RequestNewEpisode'] = _REQUESTNEWEPISODE
DESCRIPTOR.message_types_by_name['SceneDescription'] = _SCENEDESCRIPTION
DESCRIPTOR.message_types_by_name['EpisodeStart'] = _EPISODESTART
DESCRIPTOR.message_types_by_name['EpisodeReady'] = _EPISODEREADY
DESCRIPTOR.message_types_by_name['Control'] = _CONTROL
DESCRIPTOR.message_types_by_name['Measurements'] = _MEASUREMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector3D = _reflection.GeneratedProtocolMessageType('Vector3D', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3D,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Vector3D)
  ))
_sym_db.RegisterMessage(Vector3D)

Rotation3D = _reflection.GeneratedProtocolMessageType('Rotation3D', (_message.Message,), dict(
  DESCRIPTOR = _ROTATION3D,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Rotation3D)
  ))
_sym_db.RegisterMessage(Rotation3D)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Transform)
  ))
_sym_db.RegisterMessage(Transform)

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), dict(
  DESCRIPTOR = _SENSOR,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Sensor)
  ))
_sym_db.RegisterMessage(Sensor)

Vehicle = _reflection.GeneratedProtocolMessageType('Vehicle', (_message.Message,), dict(
  DESCRIPTOR = _VEHICLE,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Vehicle)
  ))
_sym_db.RegisterMessage(Vehicle)

Pedestrian = _reflection.GeneratedProtocolMessageType('Pedestrian', (_message.Message,), dict(
  DESCRIPTOR = _PEDESTRIAN,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Pedestrian)
  ))
_sym_db.RegisterMessage(Pedestrian)

TrafficLight = _reflection.GeneratedProtocolMessageType('TrafficLight', (_message.Message,), dict(
  DESCRIPTOR = _TRAFFICLIGHT,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.TrafficLight)
  ))
_sym_db.RegisterMessage(TrafficLight)

SpeedLimitSign = _reflection.GeneratedProtocolMessageType('SpeedLimitSign', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDLIMITSIGN,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.SpeedLimitSign)
  ))
_sym_db.RegisterMessage(SpeedLimitSign)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), dict(
  DESCRIPTOR = _AGENT,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Agent)
  ))
_sym_db.RegisterMessage(Agent)

RequestNewEpisode = _reflection.GeneratedProtocolMessageType('RequestNewEpisode', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTNEWEPISODE,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.RequestNewEpisode)
  ))
_sym_db.RegisterMessage(RequestNewEpisode)

SceneDescription = _reflection.GeneratedProtocolMessageType('SceneDescription', (_message.Message,), dict(
  DESCRIPTOR = _SCENEDESCRIPTION,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.SceneDescription)
  ))
_sym_db.RegisterMessage(SceneDescription)

EpisodeStart = _reflection.GeneratedProtocolMessageType('EpisodeStart', (_message.Message,), dict(
  DESCRIPTOR = _EPISODESTART,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.EpisodeStart)
  ))
_sym_db.RegisterMessage(EpisodeStart)

EpisodeReady = _reflection.GeneratedProtocolMessageType('EpisodeReady', (_message.Message,), dict(
  DESCRIPTOR = _EPISODEREADY,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.EpisodeReady)
  ))
_sym_db.RegisterMessage(EpisodeReady)

Control = _reflection.GeneratedProtocolMessageType('Control', (_message.Message,), dict(
  DESCRIPTOR = _CONTROL,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Control)
  ))
_sym_db.RegisterMessage(Control)

Measurements = _reflection.GeneratedProtocolMessageType('Measurements', (_message.Message,), dict(

  PlayerMeasurements = _reflection.GeneratedProtocolMessageType('PlayerMeasurements', (_message.Message,), dict(
    DESCRIPTOR = _MEASUREMENTS_PLAYERMEASUREMENTS,
    __module__ = 'carla_server_pb2'
    # @@protoc_insertion_point(class_scope:carla_server.Measurements.PlayerMeasurements)
    ))
  ,
  DESCRIPTOR = _MEASUREMENTS,
  __module__ = 'carla_server_pb2'
  # @@protoc_insertion_point(class_scope:carla_server.Measurements)
  ))
_sym_db.RegisterMessage(Measurements)
_sym_db.RegisterMessage(Measurements.PlayerMeasurements)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
_TRANSFORM.fields_by_name['orientation'].has_options = True
_TRANSFORM.fields_by_name['orientation']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
