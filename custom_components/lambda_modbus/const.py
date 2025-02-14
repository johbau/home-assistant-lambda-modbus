DOMAIN = "lambda_modbus"
DEFAULT_NAME = "lambda"
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 502
DEFAULT_MODBUS_ADDRESS = 1
DEFAULT_ENERGY_MANAGER = False
DEFAULT_READ_HP1 = False
DEFAULT_READ_HP2 = False
DEFAULT_READ_HP3 = False
DEFAULT_READ_BOILER1 = False
DEFAULT_READ_BOILER2 = False
DEFAULT_READ_BOILER3 = False
DEFAULT_READ_BOILER4 = False
DEFAULT_READ_BOILER5 = False
DEFAULT_READ_BUFFER1 = False
DEFAULT_READ_BUFFER2 = False
DEFAULT_READ_BUFFER3 = False
DEFAULT_READ_BUFFER4 = False
DEFAULT_READ_BUFFER5 = False
DEFAULT_READ_SOLAR1 = False
DEFAULT_READ_SOLAR2 = False
DEFAULT_HEAT_CIRCUIT1 = True
DEFAULT_HEAT_CIRCUIT2 = True
DEFAULT_HEAT_CIRCUIT3 = True
DEFAULT_HEAT_CIRCUIT4 = True
DEFAULT_HEAT_CIRCUIT5 = True
DEFAULT_HEAT_CIRCUIT6 = True
DEFAULT_HEAT_CIRCUIT7 = True
DEFAULT_HEAT_CIRCUIT8 = True
DEFAULT_HEAT_CIRCUIT9 = True
DEFAULT_HEAT_CIRCUIT10 = True
DEFAULT_HEAT_CIRCUIT11 = True
DEFAULT_HEAT_CIRCUIT12 = True
CONF_LAMBDA_HUB = "lambda_hub"
ATTR_MANUFACTURER = "Lambda"
CONF_MODBUS_ADDRESS = "modbus_address"
CONF_ENERGY_MANAGER = "energy_manager"
CONF_POWER_CONTROL = "power_control"
CONF_READ_HP1 = "read_heat_pump_1"
CONF_READ_HP2 = "read_heat_pump_2"
CONF_READ_HP3 = "read_heat_pump_3"
CONF_READ_BOILER1 = "read_boiler_1"
CONF_READ_BOILER2 = "read_boiler_2"
CONF_READ_BOILER3 = "read_boiler_3"
CONF_READ_BOILER4 = "read_boiler_4"
CONF_READ_BOILER5 = "read_boiler_5"
CONF_READ_BUFFER1 = "read_buffer_1"
CONF_READ_BUFFER2 = "read_buffer_2"
CONF_READ_BUFFER3 = "read_buffer_3"
CONF_READ_BUFFER4 = "read_buffer_4"
CONF_READ_BUFFER5 = "read_buffer_5"
CONF_READ_SOLAR1 = "read_solar_1"
CONF_READ_SOLAR2 = "read_solar_2"
CONF_HEAT_CIRCUIT1 = "read_heat_circuit_1"
CONF_HEAT_CIRCUIT2 = "read_heat_circuit_2"
CONF_HEAT_CIRCUIT3 = "read_heat_circuit_3"
CONF_HEAT_CIRCUIT4 = "read_heat_circuit_4"
CONF_HEAT_CIRCUIT5 = "read_heat_circuit_5"
CONF_HEAT_CIRCUIT6 = "read_heat_circuit_6"
CONF_HEAT_CIRCUIT7 = "read_heat_circuit_7"
CONF_HEAT_CIRCUIT8 = "read_heat_circuit_8"
CONF_HEAT_CIRCUIT9 = "read_heat_circuit_9"
CONF_HEAT_CIRCUIT10 = "read_heat_circuit_10"
CONF_HEAT_CIRCUIT11 = "read_heat_circuit_11"
CONF_HEAT_CIRCUIT12 = "read_heat_circuit_12"

AMBIENT_SENSOR_TYPES = {
    "Error_Number": ["Ambient Error Number", "ambient_error_number", None, None],
    "Operating_State": ["Ambient Operating State", "ambient_operating_state", None, None],
    "Temperature": ["Ambient Temperature", "ambient_temperature", "°C", "mdi:temperature-celsius"],
    "Temperature_1h": ["Ambient Temperature 1h", "ambient_temperature_1h", "°C", "mdi:temperature-celsius"],
    "Temperature_Calculated": ["Ambient Temperature calculated", "ambient_temperature_calculated", "°C", "mdi:temperature-celsius"],
}

AMBIENT_SENSOR_OPERATING_STATES = {
    0: "OFF",
    1: "AUTOMATIK",
    2: "MANUAL",
    3: "ERROR",
}

ENERGY_MANAGER_SENSOR_TYPES = {
    "Error_Number": ["Energy Manager Error Number", "energy_manager_error_number", None, None],
    "Operating_State": ["Energy Manager  Operating State", "energy_manager_operating_state", None, None],
    "Actual_Power": ["Energy Manager Actual Power", "energy_manager_actual_power", "W", "mdi:power"],
    "Actual_Power_Consumption": ["Energy Manager Actual Power Consumption", "energy_manager_actual_power_consumption", "W", "mdi:power"],
    "Setpoint_Power_Consumption": ["Energy Manager Setpoint Power Consumption", "energy_manager_setpoint_power_consumption", "W", "mdi:power"],
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
    "HP1 Flow_Line_Temperature": ["HP1 Heat Pump Flow Line Temperature", "hp1_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Return_Line_Temperature": ["HP1 Heat Pump Return Line Temperature", "hp1_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Heat_Sink_Volume_Flow": ["HP1 Heat Pump Heat Sink Volume Flow", "hp1_heat_sink_volume_flow", "l/h", None],
    "HP1 Energy Source Inlet Temperature": ["HP1 Heat Pump Energy Source Inlet Temperature", "hp1_energy_source_inlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Energy Source Outlet Temperature": ["HP1 Heat Pump Energy Source Outlet Temperature", "hp1_energy_source_outlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Energy_Source_Volume_Flow": ["HP1 Heat Pump Energy Source Volume Flow", "hp1_energy_source_volume_flow", "l/min", None],
    "HP1 Compressor_Unit_Rating": ["HP1 Heat Pump Compressor Rating", "hp1_compressor_unit_rating", "%", "mdi:percent"],
    "HP1 Actual_Heating_Capacity": ["HP1 Heat Pump Actual Heating Capacity", "hp1_actual_heating_capacity", "kW", "mdi:power"],
    "HP1 Inverter_Power_Consumption": ["HP1 Heat Pump Inverter Power Consumption", "hp1_inverter_power_consumption", "W", "mdi:power"],
    "HP1 COP": ["HP1 Heat Pump COP", "hp1_cop", None, None],
    "HP1 Request_Release_Password_Register": ["HP1 Heat Pump Request Release Password Register", "hp1_request_release_password_register", None, None],
    "HP1 Request_Type": ["HP1 Heat Pump Request Type", "p1_request_type", None, None],
    "HP1 Requested_Flow_Line_Temperature": ["HP1 Heat Pump Requested Flow Line Temperature", "hp1_requested_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Requested_Return_Line_Temperature": ["HP1 Heat Pump Requested Return Line Temperature", "hp1_requested_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP1 Requested_Heat_Sink_Temperature_Difference": ["HP1 Heat Pump Requested Heat Sink Temperature Difference", "hp1_requested_heat_sink_temperature_difference", "K", "mdi:temperature-kelvin"],
    "HP1 2nd_Heating_Stage_Relais_State": ["HP1 Heat Pump 2nd Heating Stage Relais State", "hp1_2nd_heating_stage_relais_state", None, None],
    "HP1 Compressor_Power_Consumption_Accumulated": ["HP1 Heat Pump Compressor Power Consumption Accumulated", "hp1_compressor_power_consumption_accumulated", "wh", "mdi:power"],
    "HP1 Compressor_Thermal_Energy_Output_Accumulated": ["HP1 Heat Pump Compressor Thermal Energy Output Accumulated", "hp1_compressor_thermal_power_output_accumulated", "wh", "mdi:power"],
}

HP2_HEAT_PUMP_SENSOR_TYPES = {
    "HP2 Error_State": ["HP2 Heat Pump Error State", "hp2_error_state", None, None],
    "HP2 Error_Number": ["HP2 Heat Pump Error Number", "hp2_error_number", None, None],
    "HP2 State": ["HP2 Heat Pump State", "hp2_state", None, None],
    "HP2 Operating_State": ["HP2 Heat Pump Operating State", "hp2_operating_state", None, None],
    "HP2 Flow_Line_Temperature": ["HP2 Heat Pump Flow Line Temperature", "hp2_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Return_Line_Temperature": ["HP2 Heat Pump Return Line Temperature", "hp2_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Heat_Sink_Volume_Flow": ["HP2 Heat Pump Heat Sink Volume Flow", "hp2_heat_sink_volume_flow", "l/h", None],
    "HP2 Energy Source Inlet Temperature": ["HP2 Heat Pump Energy Source Inlet Temperature", "hp2_energy_source_inlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Energy Source Outlet Temperature": ["HP2 Heat Pump Energy Source Outlet Temperature", "hp2_energy_source_outlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Energy_Source_Volume_Flow": ["HP2 Heat Pump Energy Source Volume Flow", "hp2_energy_source_volume_flow", "l/min", None],
    "HP2 Compressor_Unit_Rating": ["HP2 Heat Pump Compressor Rating", "hp2_compressor_unit_rating", "%", "mdi:percent"],
    "HP2 Actual_Heating_Capacity": ["HP2 Heat Pump Actual Heating Capacity", "hp2_actual_heating_capacity", "kW", "mdi:power"],
    "HP2 Inverter_Power_Consumption": ["HP2 Heat Pump Inverter Power Consumption", "hp2_inverter_power_consumption", "W", "mdi:power"],
    "HP2 COP": ["HP2 Heat Pump COP", "hp2_cop", None, None],
    "HP2 Request_Release_Password_Register": ["HP2 Heat Pump Request Release Password Register", "hp2_request_release_password_register", None, None],
    "HP2 Request_Type": ["HP2 Heat Pump Request Type", "hp2_request_type", None, None],
    "HP2 Requested_Flow_Line_Temperature": ["HP2 Heat Pump Requested Flow Line Temperature", "hp2_requested_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Requested_Return_Line_Temperature": ["HP2 Heat Pump Requested Return Line Temperature", "hp2_requested_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP2 Requested_Heat_Sink_Temperature_Difference": ["HP2 Heat Pump Requested Heat Sink Temperature Difference", "hp2_requested_heat_sink_temperature_difference", "K", "mdi:temperature-kelvin"],
    "HP2 2nd_Heating_Stage_Relais_State": ["HP2 Heat Pump 2nd Heating Stage Relais State", "hp2_2nd_heating_stage_relais_state", None, None],
    "HP2 Compressor_Power_Consumption_Accumulated": ["HP2 Heat Pump Compressor Power Consumption Accumulated", "hp2_compressor_power_consumption_accumulated", "wh", "mdi:power"],
    "HP2 Compressor_Thermal_Energy_Output_Accumulated": ["HP2 Heat Pump Compressor Thermal Energy Output Accumulated", "hp2_compressor_thermal_power_output_accumulated", "wh", "mdi:power"],
}

HP3_HEAT_PUMP_SENSOR_TYPES = {
    "HP3 Error_State": ["HP3 Heat Pump Error State", "hp3_error_state", None, None],
    "HP3 Error_Number": ["HP3 Heat Pump Error Number", "hp3_error_number", None, None],
    "HP3 State": ["HP3 Heat Pump State", "hp3_state", None, None],
    "HP3 Operating_State": ["HP3 Heat Pump Operating State", "hp3_operating_state", None, None],
    "HP3 Flow_Line_Temperature": ["HP3 Heat Pump Flow Line Temperature", "hp3_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Return_Line_Temperature": ["HP3 Heat Pump Return Line Temperature", "hp3_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Heat_Sink_Volume_Flow": ["HP3 Heat Pump Heat Sink Volume Flow", "hp3_heat_sink_volume_flow", "l/h", None],
    "HP3 Energy Source Inlet Temperature": ["HP3 Heat Pump Energy Source Inlet Temperature", "hp3_energy_source_inlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Energy Source Outlet Temperature": ["HP3 Heat Pump Energy Source Outlet Temperature", "hp3_energy_source_outlet_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Energy_Source_Volume_Flow": ["HP3 Heat Pump Energy Source Volume Flow", "hp3_energy_source_volume_flow", "l/min", None],
    "HP3 Compressor_Unit_Rating": ["HP3 Heat Pump Compressor Rating", "hp3_compressor_unit_rating", "%", "mdi:percent"],
    "HP3 Actual_Heating_Capacity": ["HP3 Heat Pump Actual Heating Capacity", "hp3_actual_heating_capacity", "kW", "mdi:power"],
    "HP3 Inverter_Power_Consumption": ["HP3 Heat Pump Inverter Power Consumption", "hp3_inverter_power_consumption", "W", "mdi:power"],
    "HP3 COP": ["HP3 Heat Pump COP", "hp3_cop", None, None],
    "HP3 Request_Release_Password_Register": ["HP3 Heat Pump Request Release Password Register", "hp3_request_release_password_register", None, None],
    "HP3 Request_Type": ["HP3 Heat Pump Request Type", "hp3_request_type", None, None],
    "HP3 Requested_Flow_Line_Temperature": ["HP3 Heat Pump Requested Flow Line Temperature", "hp3_requested_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Requested_Return_Line_Temperature": ["HP3 Heat Pump Requested Return Line Temperature", "hp3_requested_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HP3 Requested_Heat_Sink_Temperature_Difference": ["HP3 Heat Pump Requested Heat Sink Temperature Difference", "hp3_requested_heat_sink_temperature_difference", "K", "mdi:temperature-kelvin"],
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

BOILER1_SENSOR_TYPES = {
    "Boiler1 Error_Number": ["Boiler1 Error Number", "boiler1_error_number", None, None],
    "Boiler1 Operating_State": ["Boiler1 Operating State", "boiler1_operating_state", None, None],
    "Boiler1 Actual_High_Temperature": ["Boiler1 Actual High Temperature", "boiler1_high_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler1 Actual_Low_Temperature": ["Boiler1 Actual Low Temperature", "boiler1_low_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler1 Maximum_Temperature": ["Boiler1 Maximum Temperature", "boiler1_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BOILER2_SENSOR_TYPES = {
    "Boiler2 Error_Number": ["Boiler2 Error Number", "boiler2_error_number", None, None],
    "Boiler2 Operating_State": ["Boiler2 Operating State", "boiler2_operating_state", None, None],
    "Boiler2 Actual_High_Temperature": ["Boiler2 Actual High Temperature", "boiler2_high_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler2 Actual_Low_Temperature": ["Boiler2 Actual Low Temperature", "boiler2_low_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler2 Maximum_Temperature": ["Boiler2 Maximum Temperature", "boiler2_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BOILER3_SENSOR_TYPES = {
    "Boiler3 Error_Number": ["Boiler3 Error Number", "boiler3_error_number", None, None],
    "Boiler3 Operating_State": ["Boiler3 Operating State", "boiler3_operating_state", None, None],
    "Boiler3 Actual_High_Temperature": ["Boiler3 Actual High Temperature", "boiler3_high_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler3 Actual_Low_Temperature": ["Boiler3 Actual Low Temperature", "boiler3_low_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler3 Maximum_Temperature": ["Boiler3 Maximum Temperature", "boiler3_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BOILER4_SENSOR_TYPES = {
    "Boiler4 Error_Number": ["Boiler4 Error Number", "boiler4_error_number", None, None],
    "Boiler4 Operating_State": ["Boiler4 Operating State", "boiler4_operating_state", None, None],
    "Boiler4 Actual_High_Temperature": ["Boiler4 Actual High Temperature", "boiler4_high_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler4 Actual_Low_Temperature": ["Boiler4 Actual Low Temperature", "boiler4_low_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler4 Maximum_Temperature": ["Boiler4 Maximum Temperature", "boiler4_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BOILER5_SENSOR_TYPES = {
    "Boiler5 Error_Number": ["Boiler5 Error Number", "boiler5_error_number", None, None],
    "Boiler5 Operating_State": ["Boiler5 Operating State", "boiler5_operating_state", None, None],
    "Boiler5 Actual_High_Temperature": ["Boiler5 Actual High Temperature", "boiler5_high_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler5 Actual_Low_Temperature": ["Boiler5 Actual Low Temperature", "boiler5_low_temperature", "°C", "mdi:temperature-celsius"],
    "Boiler5 Maximum_Temperature": ["Boiler5 Maximum Temperature", "boiler5_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BOILER_OPERATING_STATES = {
    0: "STBY",
    1: "DHW",
    2: "LEGIO",
    3: "SUMMER",
    4: "FROST",
    5: "HOLIDAY",
    6: "PRIO-STOP",
    7: "ERROR",
    8: "OFF",
    9: "PROMPT-DHW",
    10: "TRAILING-STOP",
    11: "TEMP-STOP",
    12: "STBY-FROST",
}

BUFFER1_SENSOR_TYPES = {
    "Buffer1 Error_Number": ["Buffer1 Error Number", "buffer1_error_number", None, None],
    "Buffer1 Operating_State": ["Buffer1 Operating State", "buffer1_operating_state", None, None],
    "Buffer1 Actual_High_Temperature": ["Buffer1 Actual High Temperature", "buffer1_high_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer1 Actual_Low_Temperature": ["Buffer1 Actual Low Temperature", "buffer1_low_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer1 Actual_Modbus_Temperature": ["Buffer1 Actual Modbus Temperature", "buffer1_modbus_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer1 Request_Type": ["Buffer1 Request Type", "buffer1_request_type", None, None],
    "Buffer1 Requested_Flow_Line_Temperature": ["Buffer1 Requested Flow Temperature", "buffer1_requested_flow_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer1 Requested_Return_Line_Temperature": ["Buffer1 Requested Return Temperature", "buffer1_requested_return_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer1 Requested_Temperature_Difference": ["Buffer1 Requested Temperature Difference", "buffer1_requested_temperature_difference", "K", "mdi:temperature-kelvin"],
    "Buffer1 Requested_Capacity": ["Buffer1 Requested Capacity", "buffer1_requested_capacity", None, None],
    "Buffer1 Maximum_Temperature": ["Buffer1 Maximum Temperature", "buffer1_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BUFFER2_SENSOR_TYPES = {
    "Buffer2 Error_Number": ["Buffer2 Error Number", "buffer2_error_number", None, None],
    "Buffer2 Operating_State": ["Buffer2 Operating State", "buffer2_operating_state", None, None],
    "Buffer2 Actual_High_Temperature": ["Buffer2 Actual High Temperature", "buffer2_high_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer2 Actual_Low_Temperature": ["Buffer2 Actual Low Temperature", "buffer2_low_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer2 Actual_Modbus_Temperature": ["Buffer2 Actual Modbus Temperature", "buffer2_modbus_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer2 Request_Type": ["Buffer2 Request Type", "buffer2_request_type", None, None],
    "Buffer2 Requested_Flow_Line_Temperature": ["Buffer2 Requested Flow Temperature", "buffer2_requested_flow_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer2 Requested_Return_Line_Temperature": ["Buffer2 Requested Return Temperature", "buffer2_requested_return_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer2 Requested_Temperature_Difference": ["Buffer2 Requested Temperature Difference", "buffer2_requested_temperature_difference", "K", "mdi:temperature-kelvin"],
    "Buffer2 Requested_Capacity": ["Buffer2 Requested Capacity", "buffer2_requested_capacity", None, None],
    "Buffer2 Maximum_Temperature": ["Buffer2 Maximum Temperature", "buffer2_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BUFFER3_SENSOR_TYPES = {
    "Buffer3 Error_Number": ["Buffer3 Error Number", "buffer3_error_number", None, None],
    "Buffer3 Operating_State": ["Buffer3 Operating State", "buffer3_operating_state", None, None],
    "Buffer3 Actual_High_Temperature": ["Buffer3 Actual High Temperature", "buffer3_high_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer3 Actual_Low_Temperature": ["Buffer3 Actual Low Temperature", "buffer3_low_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer3 Actual_Modbus_Temperature": ["Buffer3 Actual Modbus Temperature", "buffer3_modbus_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer3 Request_Type": ["Buffer3 Request Type", "buffer3_request_type", None, None],
    "Buffer3 Requested_Flow_Line_Temperature": ["Buffer3 Requested Flow Temperature", "buffer3_requested_flow_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer3 Requested_Return_Line_Temperature": ["Buffer3 Requested Return Temperature", "buffer3_requested_return_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer3 Requested_Temperature_Difference": ["Buffer3 Requested Temperature Difference", "buffer3_requested_temperature_difference", "K", "mdi:temperature-kelvin"],
    "Buffer3 Requested_Capacity": ["Buffer3 Requested Capacity", "buffer3_requested_capacity", None, None],
    "Buffer3 Maximum_Temperature": ["Buffer3 Maximum Temperature", "buffer3_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BUFFER4_SENSOR_TYPES = {
    "Buffer4 Error_Number": ["Buffer4 Error Number", "buffer4_error_number", None, None],
    "Buffer4 Operating_State": ["Buffer4 Operating State", "buffer4_operating_state", None, None],
    "Buffer4 Actual_High_Temperature": ["Buffer4 Actual High Temperature", "buffer4_high_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer4 Actual_Low_Temperature": ["Buffer4 Actual Low Temperature", "buffer4_low_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer4 Actual_Modbus_Temperature": ["Buffer4 Actual Modbus Temperature", "buffer4_modbus_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer4 Request_Type": ["Buffer4 Request Type", "buffer4_request_type", None, None],
    "Buffer4 Requested_Flow_Line_Temperature": ["Buffer4 Requested Flow Temperature", "buffer4_requested_flow_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer4 Requested_Return_Line_Temperature": ["Buffer4 Requested Return Temperature", "buffer4_requested_return_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer4 Requested_Temperature_Difference": ["Buffer4 Requested Temperature Difference", "buffer4_requested_temperature_difference", "K", "mdi:temperature-kelvin"],
    "Buffer4 Requested_Capacity": ["Buffer4 Requested Capacity", "buffer4_requested_capacity", None, None],
    "Buffer4 Maximum_Temperature": ["Buffer4 Maximum Temperature", "buffer4_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BUFFER5_SENSOR_TYPES = {
    "Buffer5 Error_Number": ["Buffer5 Error Number", "buffer5_error_number", None, None],
    "Buffer5 Operating_State": ["Buffer5 Operating State", "buffer5_operating_state", None, None],
    "Buffer5 Actual_High_Temperature": ["Buffer5 Actual High Temperature", "buffer5_high_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer5 Actual_Low_Temperature": ["Buffer5 Actual Low Temperature", "buffer5_low_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer5 Actual_Modbus_Temperature": ["Buffer5 Actual Modbus Temperature", "buffer5_modbus_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer5 Request_Type": ["Buffer5 Request Type", "buffer5_request_type", None, None],
    "Buffer5 Requested_Flow_Line_Temperature": ["Buffer5 Requested Flow Temperature", "buffer5_requested_flow_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer5 Requested_Return_Line_Temperature": ["Buffer5 Requested Return Temperature", "buffer5_requested_return_temperature", "°C", "mdi:temperature-celsius"],
    "Buffer5 Requested_Temperature_Difference": ["Buffer5 Requested Temperature Difference", "buffer5_requested_temperature_difference", "K", "mdi:temperature-kelvin"],
    "Buffer5 Requested_Capacity": ["Buffer5 Requested Capacity", "buffer5_requested_capacity", "kW", "mdi:power"],
    "Buffer5 Maximum_Temperature": ["Buffer5 Maximum Temperature", "buffer5_maximum_temperature", "°C", "mdi:temperature-celsius"],
}

BUFFER_OPERATING_STATES = {
    0: "STBY",
    1: "HEATING",
    2: "COOLING",
    3: "SUMMER",
    4: "FROST",
    5: "HOLIDAY",
    6: "PRIO-STOP",
    7: "ERROR",
    8: "OFF",
    9: "STBY-FROST",
}

BUFFER_REQUEST_TYPES = {
    -1: "INVALID REQUEST",
    0: "NO REQUEST",
    1: "FLOW PUMP CIRCULATION",
    2: "CENTRAL HEATING",
    3: "CENTRAL COOLING",
}

SOLAR1_SENSOR_TYPES = {
    "Solar1 Error_Number": ["Solar1 Error Number", "solar1_error_number", None, None],
    "Solar1 Operating_State": ["Solar1 Operating State", "solar1_operating_state", None, None],
    "Solar1 Collector_Temperature": ["Solar1 Collector Temperature", "solar1_collector_temperature", "°C", "mdi:temperature-celsius"],
    "Solar1 Buffer1_Temperature": ["Solar1 Buffer 1 Temperature", "solar1_buffer1_temperature", "°C", "mdi:temperature-celsius"],
    "Solar1 Buffer2_Temperature": ["Solar1 Buffer 2 Temperature", "solar1_buffer2_temperature", "°C", "mdi:temperature-celsius"],
    "Solar1 Maximum_Buffer_Temperature": ["Solar1 Maximum Buffer Temperature", "solar1_maximum_buffer_temperature", "°C", "mdi:temperature-celsius"],
    "Solar1 Buffer_Changeover_Temperature": ["Solar1 Buffer Changeover Temperature", "solar1_buffer_changeover_temperature", "°C", "mdi:temperature-celsius"],
}

SOLAR2_SENSOR_TYPES = {
    "Solar2 Error_Number": ["Solar2 Error Number", "solar2_error_number", None, None],
    "Solar2 Operating_State": ["Solar2 Operating State", "solar2_operating_state", None, None],
    "Solar2 Collector_Temperature": ["Solar2 Collector Temperature", "solar2_collector_temperature", "°C", "mdi:temperature-celsius"],
    "Solar2 Buffer1_Temperature": ["Solar2 Buffer 1 Temperature", "solar2_buffer1_temperature", "°C", "mdi:temperature-celsius"],
    "Solar2 Buffer2_Temperature": ["Solar2 Buffer 2 Temperature", "solar2_buffer2_temperature", "°C", "mdi:temperature-celsius"],
    "Solar2 Maximum_Buffer_Temperature": ["Solar2 Maximum Buffer Temperature", "solar2_maximum_buffer_temperature", "°C", "mdi:temperature-celsius"],
    "Solar2 Buffer_Changeover_Temperature": ["Solar2 Buffer Changeover Temperature", "solar2_buffer_changeover_temperature", "°C", "mdi:temperature-celsius"],
}

SOLAR_OPERATING_STATES = {
    0: "STBY",
    1: "HEATING",
    2: "ERROR",
    3: "OFF",
}

HC1_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC1 Error_Number": ["HC1 Error Number", "hc1_error_number", None, None],
    "HC1 Operating_State": ["HC1 Operating State", "hc1_operating_state", None, None],
    "HC1 Flow_Line_Temperature": ["HC1 Flow Line Temperature", "hc1_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Return_Line_Temperature": ["HC1 Return Line Temperature", "hc1_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Room_Device_Temperature": ["HC1 Room Device Temperature", "hc1_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Setpoint_Flow_Line_Temperature": ["HC1 Setpoint Flow Line Temperature", "hc1_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Operating_Mode": ["HC1 Operating Mode", "hc1_operating_mode", None, None],
    "HC1 Setpoint_Offset_Flow_Line_Temperature": ["HC1 Setpoint Offset Flow Line Temperature", "hc1_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Setpoint_Room_Heating_Temperature": ["HC1 Setpoint Room Heating Temperature", "hc1_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC1 Setpoint_Room_Cooling_Temperature": ["HC1 Setpoint Room Cooling Temperature", "hc1_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC2_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC2 Error_Number": ["HC2 Error Number", "hc2_error_number", None, None],
    "HC2 Operating_State": ["HC2 Operating State", "hc2_operating_state", None, None],
    "HC2 Flow_Line_Temperature": ["HC2 Flow Line Temperature", "hc2_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Return_Line_Temperature": ["HC2 Return Line Temperature", "hc2_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Room_Device_Temperature": ["HC2 Room Device Temperature", "hc2_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Setpoint_Flow_Line_Temperature": ["HC2 Setpoint Flow Line Temperature", "hc2_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Operating_Mode": ["HC2 Operating Mode", "hc2_operating_mode", None, None],
    "HC2 Setpoint_Offset_Flow_Line_Temperature": ["HC2 Setpoint Offset Flow Line Temperature", "hc2_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Setpoint_Room_Heating_Temperature": ["HC2 Setpoint Room Heating Temperature", "hc2_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC2 Setpoint_Room_Cooling_Temperature": ["HC2 Setpoint Room Cooling Temperature", "hc2_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC3_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC3 Error_Number": ["HC3 Error Number", "hc3_error_number", None, None],
    "HC3 Operating_State": ["HC3 Operating State", "hc3_operating_state", None, None],
    "HC3 Flow_Line_Temperature": ["HC3 Flow Line Temperature", "hc3_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Return_Line_Temperature": ["HC3 Return Line Temperature", "hc3_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Room_Device_Temperature": ["HC3 Room Device Temperature", "hc3_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Setpoint_Flow_Line_Temperature": ["HC3 Setpoint Flow Line Temperature", "hc3_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Operating_Mode": ["HC3 Operating Mode", "hc3_operating_mode", None, None],
    "HC3 Setpoint_Offset_Flow_Line_Temperature": ["HC3 Setpoint Offset Flow Line Temperature", "hc3_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Setpoint_Room_Heating_Temperature": ["HC3 Setpoint Room Heating Temperature", "hc3_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC3 Setpoint_Room_Cooling_Temperature": ["HC3 Setpoint Room Cooling Temperature", "hc3_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC4_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC4 Error_Number": ["HC4 Error Number", "hc4_error_number", None, None],
    "HC4 Operating_State": ["HC4 Operating State", "hc4_operating_state", None, None],
    "HC4 Flow_Line_Temperature": ["HC4 Flow Line Temperature", "hc4_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Return_Line_Temperature": ["HC4 Return Line Temperature", "hc4_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Room_Device_Temperature": ["HC4 Room Device Temperature", "hc4_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Setpoint_Flow_Line_Temperature": ["HC4 Setpoint Flow Line Temperature", "hc4_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Operating_Mode": ["HC4 Operating Mode", "hc4_operating_mode", None, None],
    "HC4 Setpoint_Offset_Flow_Line_Temperature": ["HC4 Setpoint Offset Flow Line Temperature", "hc4_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Setpoint_Room_Heating_Temperature": ["HC4 Setpoint Room Heating Temperature", "hc4_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC4 Setpoint_Room_Cooling_Temperature": ["HC4 Setpoint Room Cooling Temperature", "hc4_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC5_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC5 Error_Number": ["HC5 Error Number", "hc5_error_number", None, None],
    "HC5 Operating_State": ["HC5 Operating State", "hc5_operating_state", None, None],
    "HC5 Flow_Line_Temperature": ["HC5 Flow Line Temperature", "hc5_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Return_Line_Temperature": ["HC5 Return Line Temperature", "hc5_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Room_Device_Temperature": ["HC5 Room Device Temperature", "hc5_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Setpoint_Flow_Line_Temperature": ["HC5 Setpoint Flow Line Temperature", "hc5_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Operating_Mode": ["HC5 Operating Mode", "hc5_operating_mode", None, None],
    "HC5 Setpoint_Offset_Flow_Line_Temperature": ["HC5 Setpoint Offset Flow Line Temperature", "hc5_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Setpoint_Room_Heating_Temperature": ["HC5 Setpoint Room Heating Temperature", "hc5_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC5 Setpoint_Room_Cooling_Temperature": ["HC5 Setpoint Room Cooling Temperature", "hc5_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC6_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC6 Error_Number": ["HC6 Error Number", "hc6_error_number", None, None],
    "HC6 Operating_State": ["HC6 Operating State", "hc6_operating_state", None, None],
    "HC6 Flow_Line_Temperature": ["HC6 Flow Line Temperature", "hc6_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Return_Line_Temperature": ["HC6 Return Line Temperature", "hc6_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Room_Device_Temperature": ["HC6 Room Device Temperature", "hc6_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Setpoint_Flow_Line_Temperature": ["HC6 Setpoint Flow Line Temperature", "hc6_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Operating_Mode": ["HC6 Operating Mode", "hc6_operating_mode", None, None],
    "HC6 Setpoint_Offset_Flow_Line_Temperature": ["HC6 Setpoint Offset Flow Line Temperature", "hc6_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Setpoint_Room_Heating_Temperature": ["HC6 Setpoint Room Heating Temperature", "hc6_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC6 Setpoint_Room_Cooling_Temperature": ["HC6 Setpoint Room Cooling Temperature", "hc6_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC7_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC7 Error_Number": ["HC7 Error Number", "hc7_error_number", None, None],
    "HC7 Operating_State": ["HC7 Operating State", "hc7_operating_state", None, None],
    "HC7 Flow_Line_Temperature": ["HC7 Flow Line Temperature", "hc7_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Return_Line_Temperature": ["HC7 Return Line Temperature", "hc7_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Room_Device_Temperature": ["HC7 Room Device Temperature", "hc7_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Setpoint_Flow_Line_Temperature": ["HC7 Setpoint Flow Line Temperature", "hc7_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Operating_Mode": ["HC7 Operating Mode", "hc7_operating_mode", None, None],
    "HC7 Setpoint_Offset_Flow_Line_Temperature": ["HC7 Setpoint Offset Flow Line Temperature", "hc7_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Setpoint_Room_Heating_Temperature": ["HC7 Setpoint Room Heating Temperature", "hc7_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC7 Setpoint_Room_Cooling_Temperature": ["HC7 Setpoint Room Cooling Temperature", "hc7_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC8_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC8 Error_Number": ["HC8 Error Number", "hc8_error_number", None, None],
    "HC8 Operating_State": ["HC8 Operating State", "hc8_operating_state", None, None],
    "HC8 Flow_Line_Temperature": ["HC8 Flow Line Temperature", "hc8_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Return_Line_Temperature": ["HC8 Return Line Temperature", "hc8_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Room_Device_Temperature": ["HC8 Room Device Temperature", "hc8_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Setpoint_Flow_Line_Temperature": ["HC8 Setpoint Flow Line Temperature", "hc8_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Operating_Mode": ["HC8 Operating Mode", "hc8_operating_mode", None, None],
    "HC8 Setpoint_Offset_Flow_Line_Temperature": ["HC8 Setpoint Offset Flow Line Temperature", "hc8_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Setpoint_Room_Heating_Temperature": ["HC8 Setpoint Room Heating Temperature", "hc8_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC8 Setpoint_Room_Cooling_Temperature": ["HC8 Setpoint Room Cooling Temperature", "hc8_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC9_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC9 Error_Number": ["HC9 Error Number", "hc9_error_number", None, None],
    "HC9 Operating_State": ["HC9 Operating State", "hc9_operating_state", None, None],
    "HC9 Flow_Line_Temperature": ["HC9 Flow Line Temperature", "hc9_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Return_Line_Temperature": ["HC9 Return Line Temperature", "hc9_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Room_Device_Temperature": ["HC9 Room Device Temperature", "hc9_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Setpoint_Flow_Line_Temperature": ["HC9 Setpoint Flow Line Temperature", "hc9_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Operating_Mode": ["HC9 Operating Mode", "hc9_operating_mode", None, None],
    "HC9 Setpoint_Offset_Flow_Line_Temperature": ["HC9 Setpoint Offset Flow Line Temperature", "hc9_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Setpoint_Room_Heating_Temperature": ["HC9 Setpoint Room Heating Temperature", "hc9_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC9 Setpoint_Room_Cooling_Temperature": ["HC9 Setpoint Room Cooling Temperature", "hc9_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC10_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC10 Error_Number": ["HC10 Error Number", "hc10_error_number", None, None],
    "HC10 Operating_State": ["HC10 Operating State", "hc10_operating_state", None, None],
    "HC10 Flow_Line_Temperature": ["HC10 Flow Line Temperature", "hc10_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Return_Line_Temperature": ["HC10 Return Line Temperature", "hc10_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Room_Device_Temperature": ["HC10 Room Device Temperature", "hc10_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Setpoint_Flow_Line_Temperature": ["HC10 Setpoint Flow Line Temperature", "hc10_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Operating_Mode": ["HC10 Operating Mode", "hc10_operating_mode", None, None],
    "HC10 Setpoint_Offset_Flow_Line_Temperature": ["HC10 Setpoint Offset Flow Line Temperature", "hc10_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Setpoint_Room_Heating_Temperature": ["HC10 Setpoint Room Heating Temperature", "hc10_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC10 Setpoint_Room_Cooling_Temperature": ["HC10 Setpoint Room Cooling Temperature", "hc10_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC11_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC11 Error_Number": ["HC11 Error Number", "hc11_error_number", None, None],
    "HC11 Operating_State": ["HC11 Operating State", "hc11_operating_state", None, None],
    "HC11 Flow_Line_Temperature": ["HC11 Flow Line Temperature", "hc11_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Return_Line_Temperature": ["HC11 Return Line Temperature", "hc11_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Room_Device_Temperature": ["HC11 Room Device Temperature", "hc11_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Setpoint_Flow_Line_Temperature": ["HC11 Setpoint Flow Line Temperature", "hc11_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Operating_Mode": ["HC11 Operating Mode", "hc11_operating_mode", None, None],
    "HC11 Setpoint_Offset_Flow_Line_Temperature": ["HC11 Setpoint Offset Flow Line Temperature", "hc11_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Setpoint_Room_Heating_Temperature": ["HC11 Setpoint Room Heating Temperature", "hc11_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC11 Setpoint_Room_Cooling_Temperature": ["HC11 Setpoint Room Cooling Temperature", "hc11_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC12_HEAT_CIRCUIT_SENSOR_TYPES = {
    "HC12 Error_Number": ["HC12 Error Number", "hc12_error_number", None, None],
    "HC12 Operating_State": ["HC12 Operating State", "hc12_operating_state", None, None],
    "HC12 Flow_Line_Temperature": ["HC12 Flow Line Temperature", "hc12_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Return_Line_Temperature": ["HC12 Return Line Temperature", "hc12_return_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Room_Device_Temperature": ["HC12 Room Device Temperature", "hc12_room_device_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Setpoint_Flow_Line_Temperature": ["HC12 Setpoint Flow Line Temperature", "hc12_setpoint_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Operating_Mode": ["HC12 Operating Mode", "hc12_operating_mode", None, None],
    "HC12 Setpoint_Offset_Flow_Line_Temperature": ["HC12 Setpoint Offset Flow Line Temperature", "hc12_setpoint_offset_flow_line_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Setpoint_Room_Heating_Temperature": ["HC12 Setpoint Room Heating Temperature", "hc12_setpoint_room_heating_temperature", "°C", "mdi:temperature-celsius"],
    "HC12 Setpoint_Room_Cooling_Temperature": ["HC12 Setpoint Room Cooling Temperature", "hc12_setpoint_room_cooling_temperature", "°C", "mdi:temperature-celsius"],
}

HC_OPERATING_STATES = {
    0: "HEATING",
    1: "ECO",
    2: "COOLING",
    3: "FLOORDRY",
    4: "FROST",
    5: "MAX-TEMP",
    6: "ERROR",
    7: "SERVICE",
    8: "HOLIDAY",
    9: "CH-SUMMER",
    10: "CC-WINTER",
    11: "PRIO-STOP",
    12: "OFF",
    13: "RELEASE-OFF",
    14: "TIME-OFF",
    15: "STBY",
    16: "STBY-HEATING",
    17: "STBY-ECO",
    18: "STBY-COOLING",
    19: "STBY-FROST",
    20: "STBY-FLOORDRY",
}

HC_OPERATING_MODES = {
    0: "OFF",
    1: "MANUAL",
    2: "AUTOMATIK",
    3: "AUTO-HEATING",
    4: "AUTO-COOLING",
    5: "FROST",
    6: "SUMMER",
    7: "FLOOR-DRY",
}

