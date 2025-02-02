DOMAIN = "lambda_modbus"
DEFAULT_NAME = "lambda"
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 502
DEFAULT_MODBUS_ADDRESS = 1
DEFAULT_ENERGY_MANAGER = False
DEFAULT_POWER_CONTROL = False
DEFAULT_READ_HP1 = False
DEFAULT_READ_HP2 = False
DEFAULT_READ_HP3 = False
DEFAULT_READ_METER1 = False
DEFAULT_READ_METER2 = False
DEFAULT_READ_METER3 = False
DEFAULT_READ_BATTERY1 = False
DEFAULT_READ_BATTERY2 = False
DEFAULT_READ_BATTERY3 = False
CONF_LAMBDA_HUB = "lambda_hub"
ATTR_MANUFACTURER = "Lambda"
CONF_MODBUS_ADDRESS = "modbus_address"
CONF_ENERGY_MANAGER = "energy_manager"
CONF_POWER_CONTROL = "power_control"
CONF_READ_HP1 = "read_heat_pump_1"
CONF_READ_HP2 = "read_heat_pump_2"
CONF_READ_HP3 = "read_heat_pump_3"
CONF_READ_METER1 = "read_meter_1"
CONF_READ_METER2 = "read_meter_2"
CONF_READ_METER3 = "read_meter_3"
CONF_READ_BATTERY1 = "read_battery_1"
CONF_READ_BATTERY2 = "read_battery_2"
CONF_READ_BATTERY3 = "read_battery_3"
CONF_MAX_EXPORT_CONTROL_SITE_LIMIT = "max_export_control_site_limit"
DEFAULT_MAX_EXPORT_CONTROL_SITE_LIMIT = 10000

AMBIENT_SENSOR_TYPES = {
    "Error_Number": ["Ambient Error Number", "error_number", None, None],
    "Operating_State": ["Ambient Operating State", "operating_state", None, None],
    "Temperature": ["Ambient Temperature", "temperature", "°C", None],
    "Temperature_1h": ["Ambient Temperature 1h", "temperature_1h", "°C", None],
    "Temperature_Calculated": ["Ambient Temperature calculated", "temperature_calculated", "°C", None],
}

AMBIENT_SENSOR_OPERATING_STATES = {
    0: "OFF",
    1: "AUTOMATIK",
    2: "MANUAL",
    3: "ERROR",
}

ENERGY_MANAGER_SENSOR_TYPES = {
    "Error_Number": ["Energy Manager Error Number", "error_number", None, None],
    "Operating_State": ["Energy Manager  Operating State", "operating_state", None, None],
    "Actual_Power": ["Energy Manager Actual Power", "actual_power", "W", "mdi:power"],
    "Actual_Power_Consumption": ["Energy Manager Actual Power Consumption", "actual_power_consumption", "W", "mdi:power"],
    "Setpoint_Power_Consumption": ["Energy Manager Setpoint Power Consumption", "setpoint_power_consumption", "W", "mdi:power"],
}

ENERGY_MANAGER_OPERATING_STATES = {
    0: "OFF",
    1: "AUTOMATIK",
    2: "MANUAL",
    3: "ERROR",
    4: "OFFLINE",
}

HP1_HEAT_PUMP_SENSOR_TYPES = {
    "HP1 Error_State": ["HP1 Heat Pump Error State", "hp1_error_state", None, None],
    "HP1 Error_Number": ["HP1 Heat Pump Error Number", "hp1_error_number", None, None],
    "HP1 State": ["HP1 Heat Pump State", "hp1_state", None, None],
    "HP1 Operating_State": ["HP1 Heat Pump Operating State", "hp1_operating_state", None, None],
    "HP1 Flow_Line_Temperature": ["HP1 Heat Pump Flow Line Temperature", "hp1_flow_line_temperature", "°C", None],
    "HP1 Return_Line_Temperature": ["HP1 Heat Pump Return Line Temperature", "hp1_return_line_temperature", "°C", None],
    "HP1 Heat_Sink_Volume_Flow": ["HP1 Heat Pump Heat Sink Volume Flow", "hp1_heat_sink_volume_flow", "l/h", None],
    "HP1 Energy Source Inlet Temperature": ["HP1 Heat Pump Energy Source Inlet Temperature", "hp1_energy_source_inlet_temperature", "°C", None],
    "HP1 Energy Source Outlet Temperature": ["HP1 Heat Pump Energy Source Outlet Temperature", "hp1_energy_source_outlet_temperature", "°C", None],
    "HP1 Energy_Source_Volume_Flow": ["HP1 Heat Pump Energy Source Volume Flow", "hp1_energy_source_volume_flow", "l/min", None],
    "HP1 Compressor_Unit_Rating": ["HP1 Heat Pump Compressor Rating", "hp1_compressor_unit_rating", "%", None],
    "HP1 Actual_Heating_Capacity": ["HP1 Heat Pump Actual Heating Capacity", "hp1_actual_heating_capacity", "kW", "mdi:power"],
    "HP1 Inverter_Power_Consumption": ["HP1 Heat Pump Inverter Power Consumption", "hp1_inverter_power_consumption", "W", "mdi:power"],
    "HP1 COP": ["HP1 Heat Pump COP", "hp1_cop", "%", None],
    "HP1 Request_Release_Password_Register": ["HP1 Heat Pump Request Release Password Register", "hp1_request_release_password_register", None, None],
    "HP1 Request_Type": ["HP1 Heat Pump Request Type", "p1_request_type", None, None],
    "HP1 Requested_Flow_Line_Temperature": ["HP1 Heat Pump Requested Flow Line Temperature", "hp1_requested_flow_line_temperature", "°C", None],
    "HP1 Requested_Return_Line_Temperature": ["HP1 Heat Pump Requested Return Line Temperature", "hp1_requested_return_line_temperature", "°C", None],
    "HP1 Requested_Heat_Sink_Temperature_Difference": ["HP1 Heat Pump Requested Heat Sink Temperature Difference", "hp1_requested_heat_sink_temperature_difference", "°C", None],
    "HP1 2nd_Heating_Stage_Relais_State": ["HP1 Heat Pump 2nd Heating Stage Relais State", "hp1_2nd_heating_stage_relais_state", None, None],
    "HP1 Compressor_Power_Consumption_Accumulated": ["HP1 Heat Pump Compressor Power Consumption Accumulated", "hp1_compressor_power_consumption_accumulated", "wh", "mdi:power"],
    "HP1 Compressor_Thermal_Energy_Output_Accumulated": ["HP1 Heat Pump Compressor Thermal Energy Output Accumulated", "hp1_compressor_thermal_power_output_accumulated", "wh", "mdi:power"],
}

HP2_HEAT_PUMP_SENSOR_TYPES = {
    "HP2 Error_State": ["HP2 Heat Pump Error State", "hp2_error_state", None, None],
    "HP2 Error_Number": ["HP2 Heat Pump Error Number", "hp2_error_number", None, None],
    "HP2 State": ["HP2 Heat Pump State", "hp2_state", None, None],
    "HP2 Operating_State": ["HP2 Heat Pump Operating State", "hp2_operating_state", None, None],
    "HP2 Flow_Line_Temperature": ["HP2 Heat Pump Flow Line Temperature", "hp2_flow_line_temperature", "°C", None],
    "HP2 Return_Line_Temperature": ["HP2 Heat Pump Return Line Temperature", "hp2_return_line_temperature", "°C", None],
    "HP2 Heat_Sink_Volume_Flow": ["HP2 Heat Pump Heat Sink Volume Flow", "hp2_heat_sink_volume_flow", "l/h", None],
    "HP2 Energy Source Inlet Temperature": ["HP2 Heat Pump Energy Source Inlet Temperature", "hp2_energy_source_inlet_temperature", "°C", None],
    "HP2 Energy Source Outlet Temperature": ["HP2 Heat Pump Energy Source Outlet Temperature", "hp2_energy_source_outlet_temperature", "°C", None],
    "HP2 Energy_Source_Volume_Flow": ["HP2 Heat Pump Energy Source Volume Flow", "hp2_energy_source_volume_flow", "l/min", None],
    "HP2 Compressor_Unit_Rating": ["HP2 Heat Pump Compressor Rating", "hp2_compressor_unit_rating", "%", None],
    "HP2 Actual_Heating_Capacity": ["HP2 Heat Pump Actual Heating Capacity", "hp2_actual_heating_capacity", "kW", "mdi:power"],
    "HP2 Inverter_Power_Consumption": ["HP2 Heat Pump Inverter Power Consumption", "hp2_inverter_power_consumption", "W", "mdi:power"],
    "HP2 COP": ["HP2 Heat Pump COP", "hp2_cop", "%", None],
    "HP2 Request_Release_Password_Register": ["HP2 Heat Pump Request Release Password Register", "hp2_request_release_password_register", None, None],
    "HP2 Request_Type": ["HP2 Heat Pump Request Type", "hp2_request_type", None, None],
    "HP2 Requested_Flow_Line_Temperature": ["HP2 Heat Pump Requested Flow Line Temperature", "hp2_requested_flow_line_temperature", "°C", None],
    "HP2 Requested_Return_Line_Temperature": ["HP2 Heat Pump Requested Return Line Temperature", "hp2_requested_return_line_temperature", "°C", None],
    "HP2 Requested_Heat_Sink_Temperature_Difference": ["HP2 Heat Pump Requested Heat Sink Temperature Difference", "hp2_requested_heat_sink_temperature_difference", "°C", None],
    "HP2 2nd_Heating_Stage_Relais_State": ["HP2 Heat Pump 2nd Heating Stage Relais State", "hp2_2nd_heating_stage_relais_state", None, None],
    "HP2 Compressor_Power_Consumption_Accumulated": ["HP2 Heat Pump Compressor Power Consumption Accumulated", "hp2_compressor_power_consumption_accumulated", "wh", "mdi:power"],
    "HP2 Compressor_Thermal_Energy_Output_Accumulated": ["HP2 Heat Pump Compressor Thermal Energy Output Accumulated", "hp2_compressor_thermal_power_output_accumulated", "wh", "mdi:power"],
}

HP3_HEAT_PUMP_SENSOR_TYPES = {
    "HP3 Error_State": ["HP3 Heat Pump Error State", "hp3_error_state", None, None],
    "HP3 Error_Number": ["HP3 Heat Pump Error Number", "hp3_error_number", None, None],
    "HP3 State": ["HP3 Heat Pump State", "hp3_state", None, None],
    "HP3 Operating_State": ["HP3 Heat Pump Operating State", "hp3_operating_state", None, None],
    "HP3 Flow_Line_Temperature": ["HP3 Heat Pump Flow Line Temperature", "hp3_flow_line_temperature", "°C", None],
    "HP3 Return_Line_Temperature": ["HP3 Heat Pump Return Line Temperature", "hp3_return_line_temperature", "°C", None],
    "HP3 Heat_Sink_Volume_Flow": ["HP3 Heat Pump Heat Sink Volume Flow", "hp3_heat_sink_volume_flow", "l/h", None],
    "HP3 Energy Source Inlet Temperature": ["HP3 Heat Pump Energy Source Inlet Temperature", "hp3_energy_source_inlet_temperature", "°C", None],
    "HP3 Energy Source Outlet Temperature": ["HP3 Heat Pump Energy Source Outlet Temperature", "hp3_energy_source_outlet_temperature", "°C", None],
    "HP3 Energy_Source_Volume_Flow": ["HP3 Heat Pump Energy Source Volume Flow", "hp3_energy_source_volume_flow", "l/min", None],
    "HP3 Compressor_Unit_Rating": ["HP3 Heat Pump Compressor Rating", "hp3_compressor_unit_rating", "%", None],
    "HP3 Actual_Heating_Capacity": ["HP3 Heat Pump Actual Heating Capacity", "hp3_actual_heating_capacity", "kW", "mdi:power"],
    "HP3 Inverter_Power_Consumption": ["HP3 Heat Pump Inverter Power Consumption", "hp3_inverter_power_consumption", "W", "mdi:power"],
    "HP3 COP": ["HP3 Heat Pump COP", "hp3_cop", "%", None],
    "HP3 Request_Release_Password_Register": ["HP3 Heat Pump Request Release Password Register", "hp3_request_release_password_register", None, None],
    "HP3 Request_Type": ["HP3 Heat Pump Request Type", "hp3_request_type", None, None],
    "HP3 Requested_Flow_Line_Temperature": ["HP3 Heat Pump Requested Flow Line Temperature", "hp3_requested_flow_line_temperature", "°C", None],
    "HP3 Requested_Return_Line_Temperature": ["HP3 Heat Pump Requested Return Line Temperature", "hp3_requested_return_line_temperature", "°C", None],
    "HP3 Requested_Heat_Sink_Temperature_Difference": ["HP3 Heat Pump Requested Heat Sink Temperature Difference", "hp3_requested_heat_sink_temperature_difference", "°C", None],
    "HP3 2nd_Heating_Stage_Relais_State": ["HP3 Heat Pump 2nd Heating Stage Relais State", "hp3_2nd_heating_stage_relais_state", None, None],
    "HP3 Compressor_Power_Consumption_Accumulated": ["HP3 Heat Pump Compressor Power Consumption Accumulated", "hp3_compressor_power_consumption_accumulated", "wh", "mdi:power"],
    "HP3 Compressor_Thermal_Energy_Output_Accumulated": ["HP3 Heat Pump Compressor Thermal Energy Output Accumulated", "hp3_compressor_thermal_power_output_accumulated", "wh", "mdi:power"],
}

HEAT_PUMP_ERROR_STATES = {
    0: "NONE",
    1: "MESSAGE",
    2: "WARNING",
    3: "ALARM",
    4: "FAULT",
}

HEAT_PUMP_STATES = {
    0: "INIT",
    1: "REFERENCE",
    2: "RESTART-BLOCK",
    3: "READY",
    4: "START PUMPS",
    5: "START COMPRESSOR",
    6: "PRE-REGULATION",
    7: "REGULATION",
    8: "Not Used",
    9: "COOLING",
    10: "DEFROSTING",
    20: "STOPPING",
    30: "FAULT-LOCK",
    31: "ALARM-BLOCK",
    40: "ERROR-RESET",
}

HEAT_PUMP_OPERATING_STATES = {
    0: "STBY",
    1: "CH",
    2: "DHW",
    3: "CC",
    4: "CIRCULATE",
    5: "DEFROST",
    6: "OFF",
    7: "FROST",
    8: "STBY-FROST",
    9: "Not used",
    10: "SUMMER",
    11: "HOLIDAY",
    12: "ERROR",
    13: "WARNING",
    14: "INFO-MESSAGE",
    15: "TIME-BLOCK",
    16: "RELEASE-BLOCK",
    17: "MINTEMP-BLOCK",
    18: "FIRMWARE-DOWNLOAD",
}
