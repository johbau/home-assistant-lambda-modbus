DOMAIN = "lambda_modbus"
DEFAULT_NAME = "lambda"
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 502
DEFAULT_MODBUS_ADDRESS = 1
DEFAULT_ENERGY_MANAGER = False
DEFAULT_POWER_CONTROL = False
DEFAULT_HEAT_PUMP1 = False
DEFAULT_HEAT_PUMP2 = False
DEFAULT_HEAT_PUMP3 = False
DEFAULT_READ_METER1 = False
DEFAULT_READ_METER2 = False
DEFAULT_READ_METER3 = False
DEFAULT_READ_BATTERY1 = False
DEFAULT_READ_BATTERY2 = False
DEFAULT_READ_BATTERY3 = False
CONF_LAMBDA_HUB = "lambda_hub"
ATTR_STATUS_DESCRIPTION = "status_description"
ATTR_MANUFACTURER = "Lambda"
CONF_MODBUS_ADDRESS = "modbus_address"
CONF_ENERGY_MANAGER = "energy_manager"
CONF_POWER_CONTROL = "power_control"
CONF_HEAT_PUMP1 = "heat_pump_1"
CONF_HEAT_PUMP2 = "heat_pump_2"
CONF_HEAT_PUMP3 = "heat_pump_3"
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

INVERTER_SENSOR_TYPES = {
    "AC_Current": ["AC Current", "accurrent", "A", "mdi:current-ac"],
    "AC_CurrentA": ["AC Current A", "accurrenta", "A", "mdi:current-ac"],
    "AC_CurrentB": ["AC Current B", "accurrentb", "A", "mdi:current-ac"],
    "AC_CurrentC": ["AC Current C", "accurrentc", "A", "mdi:current-ac"],
    "AC_VoltageAB": ["AC Voltage AB", "acvoltageab", "V", None],
    "AC_VoltageBC": ["AC Voltage BC", "acvoltagebc", "V", None],
    "AC_VoltageCA": ["AC Voltage CA", "acvoltageca", "V", None],
    "AC_VoltageAN": ["AC Voltage AN", "acvoltagean", "V", None],
    "AC_VoltageBN": ["AC Voltage BN", "acvoltagebn", "V", None],
    "AC_VoltageCN": ["AC Voltage CN", "acvoltagecn", "V", None],
    "AC_Power": ["AC Power", "acpower", "W", "mdi:solar-power"],
    "AC_Frequency": ["AC Frequency", "acfreq", "Hz", None],
    "AC_VA": ["AC VA", "acva", "VA", None],
    "AC_VAR": ["AC VAR", "acvar", "VAR", None],
    "AC_PF": ["AC PF", "acpf", "%", None],
    "AC_Energy_kWh": ["AC Energy kWh", "acenergy", "kWh", "mdi:solar-power"],
    "DC_Current": ["DC Current", "dccurrent", "A", "mdi:current-dc"],
    "DC_Voltage": ["DC Voltage", "dcvoltage", "V", None],
    "DC_Power": ["DC Power", "dcpower", "W", "mdi:solar-power"],
    "Temp_Sink": ["Temp Sink", "tempsink", "°C", None],
    "Status": ["Status", "status", None, None],
    "Status_Vendor": ["Status Vendor", "statusvendor", None, None],
}


METER1_SENSOR_TYPES = {
    "M1_AC_Current": ["M1 AC Current", "m1_accurrent", "A", "mdi:current-ac"],
    "M1_AC_Current_A": ["M1 AC Current_A", "m1_accurrenta", "A", "mdi:current-ac"],
    "M1_AC_Current_B": ["M1 AC Current_B", "m1_accurrentb", "A", "mdi:current-ac"],
    "M1_AC_Current_C": ["M1 AC Current_C", "m1_accurrentc", "A", "mdi:current-ac"],
    "M1_AC_Voltage_LN": ["M1 AC Voltage LN", "m1_acvoltageln", "V", None],
    "M1_AC_Voltage_AN": ["M1 AC Voltage AN", "m1_acvoltagean", "V", None],
    "M1_AC_Voltage_BN": ["M1 AC Voltage BN", "m1_acvoltagebn", "V", None],
    "M1_AC_Voltage_CN": ["M1 AC Voltage CN", "m1_acvoltagecn", "V", None],
    "M1_AC_Voltage_LL": ["M1 AC Voltage LL", "m1_acvoltagell", "V", None],
    "M1_AC_Voltage_AB": ["M1 AC Voltage AB", "m1_acvoltageab", "V", None],
    "M1_AC_Voltage_BC": ["M1 AC Voltage BC", "m1_acvoltagebc", "V", None],
    "M1_AC_Voltage_CA": ["M1 AC Voltage CA", "m1_acvoltageca", "V", None],
    "M1_AC_Frequency": ["M1 AC Frequency", "m1_acfreq", "Hz", None],
    "M1_AC_Power": ["M1 AC Power", "m1_acpower", "W", None],
    "M1_AC_Power_A": ["M1 AC Power A", "m1_acpowera", "W", None],
    "M1_AC_Power_B": ["M1 AC Power B", "m1_acpowerb", "W", None],
    "M1_AC_Power_C": ["M1 AC Power C", "m1_acpowerc", "W", None],
    "M1_AC_VA": ["M1 AC VA", "m1_acva", "VA", None],
    "M1_AC_VA_A": ["M1 AC VA A", "m1_acvaa", "VA", None],
    "M1_AC_VA_B": ["M1 AC VA B", "m1_acvab", "VA", None],
    "M1_AC_VA_C": ["M1 AC VA C", "m1_acvac", "VA", None],
    "M1_AC_VAR": ["M1 AC VAR", "m1_acvar", "VAR", None],
    "M1_AC_VAR_A": ["M1 AC VAR A", "m1_acvara", "VAR", None],
    "M1_AC_VAR_B": ["M1 AC VAR B", "m1_acvarb", "VAR", None],
    "M1_AC_VAR_C": ["M1 AC VAR C", "m1_acvarc", "VAR", None],
    "M1_AC_PF": ["M1 AC PF", "m1_acpf", "%", None],
    "M1_AC_PF_A": ["M1 AC PF A", "m1_acpfa", "%", None],
    "M1_AC_PF_B": ["M1 AC PF B", "m1_acpfb", "%", None],
    "M1_AC_PF_C": ["M1 AC PF C", "m1_acpfc", "%", None],
    "M1_EXPORTED_KWH": ["M1 EXPORTED KWH", "m1_exported", "kWh", None],
    "M1_EXPORTED_A_KWH": ["M1 EXPORTED A KWH", "m1_exporteda", "kWh", None],
    "M1_EXPORTED_B_KWH": ["M1 EXPORTED B KWH", "m1_exportedb", "kWh", None],
    "M1_EXPORTED_C_KWH": ["M1 EXPORTED C KWH", "m1_exportedc", "kWh", None],
    "M1_IMPORTED_KWH": ["M1 IMPORTED KWH", "m1_imported", "kWh", None],
    "M1_IMPORTED_KWH_A": ["M1 IMPORTED A KWH", "m1_importeda", "kWh", None],
    "M1_IMPORTED_KWH_B": ["M1 IMPORTED B KWH", "m1_importedb", "kWh", None],
    "M1_IMPORTED_KWH_C": ["M1 IMPORTED C KWH", "m1_importedc", "kWh", None],
    "M1_EXPORTED_VA": ["M1 EXPORTED VAh", "m1_exportedva", "VAh", None],
    "M1_EXPORTED_VA_A": ["M1 EXPORTED A VAh", "m1_exportedvaa", "VAh", None],
    "M1_EXPORTED_VA_B": ["M1 EXPORTED B VAh", "m1_exportedvab", "VAh", None],
    "M1_EXPORTED_VA_C": ["M1 EXPORTED C VAh", "m1_exportedvac", "VAh", None],
    "M1_IMPORTED_VA": ["M1 IMPORTED VAh", "m1_importedva", "VAh", None],
    "M1_IMPORTED_VA_A": ["M1 IMPORTED A VAh", "m1_importedvaa", "VAh", None],
    "M1_IMPORTED_VA_B": ["M1 IMPORTED B VAh", "m1_importedvab", "VAh", None],
    "M1_IMPORTED_VA_C": ["M1 IMPORTED C VAh", "m1_importedvac", "VAh", None],
    "M1_IMPORT_VARH_Q1": ["M1 IMPORT VARH Q1", "m1_importvarhq1", "VARh", None],
    "M1_IMPORT_VARH_Q1_A": ["M1 IMPORT VARH Q1 A", "m1_importvarhq1a", "VARh", None],
    "M1_IMPORT_VARH_Q1_B": ["M1 IMPORT VARH Q1 B", "m1_importvarhq1b", "VARh", None],
    "M1_IMPORT_VARH_Q1_C": ["M1 IMPORT VARH Q1 C", "m1_importvarhq1c", "VARh", None],
    "M1_IMPORT_VARH_Q2": ["M1 IMPORT VARH Q2", "m1_importvarhq2", "VARh", None],
    "M1_IMPORT_VARH_Q2_A": ["M1 IMPORT VARH Q2 A", "m1_importvarhq2a", "VARh", None],
    "M1_IMPORT_VARH_Q2_B": ["M1 IMPORT VARH Q2 B", "m1_importvarhq2b", "VARh", None],
    "M1_IMPORT_VARH_Q2_C": ["M1 IMPORT VARH Q2 C", "m1_importvarhq2c", "VARh", None],
    "M1_IMPORT_VARH_Q3": ["M1 IMPORT VARH Q3", "m1_importvarhq3", "VARh", None],
    "M1_IMPORT_VARH_Q3_A": ["M1 IMPORT VARH Q3 A", "m1_importvarhq3a", "VARh", None],
    "M1_IMPORT_VARH_Q3_B": ["M1 IMPORT VARH Q3 B", "m1_importvarhq3b", "VARh", None],
    "M1_IMPORT_VARH_Q3_C": ["M1 IMPORT VARH Q3 C", "m1_importvarhq3c", "VARh", None],
    "M1_IMPORT_VARH_Q4": ["M1 IMPORT VARH Q4", "m1_importvarhq4", "VARh", None],
    "M1_IMPORT_VARH_Q4_A": ["M1 IMPORT VARH Q4 A", "m1_importvarhq4a", "VARh", None],
    "M1_IMPORT_VARH_Q4_B": ["M1 IMPORT VARH Q4 B", "m1_importvarhq4b", "VARh", None],
    "M1_IMPORT_VARH_Q4_C": ["M1 IMPORT VARH Q4 C", "m1_importvarhq4c", "VARh", None],
}

METER2_SENSOR_TYPES = {
    "M2_AC_Current": ["M2 AC Current", "m2_accurrent", "A", "mdi:current-ac"],
    "M2_AC_Current_A": ["M2 AC Current_A", "m2_accurrenta", "A", "mdi:current-ac"],
    "M2_AC_Current_B": ["M2 AC Current_B", "m2_accurrentb", "A", "mdi:current-ac"],
    "M2_AC_Current_C": ["M2 AC Current_C", "m2_accurrentc", "A", "mdi:current-ac"],
    "M2_AC_Voltage_LN": ["M2 AC Voltage LN", "m2_acvoltageln", "V", None],
    "M2_AC_Voltage_AN": ["M2 AC Voltage AN", "m2_acvoltagean", "V", None],
    "M2_AC_Voltage_BN": ["M2 AC Voltage BN", "m2_acvoltagebn", "V", None],
    "M2_AC_Voltage_CN": ["M2 AC Voltage CN", "m2_acvoltagecn", "V", None],
    "M2_AC_Voltage_LL": ["M2 AC Voltage LL", "m2_acvoltagell", "V", None],
    "M2_AC_Voltage_AB": ["M2 AC Voltage AB", "m2_acvoltageab", "V", None],
    "M2_AC_Voltage_BC": ["M2 AC Voltage BC", "m2_acvoltagebc", "V", None],
    "M2_AC_Voltage_CA": ["M2 AC Voltage CA", "m2_acvoltageca", "V", None],
    "M2_AC_Frequency": ["M2 AC Frequency", "m2_acfreq", "Hz", None],
    "M2_AC_Power": ["M2 AC Power", "m2_acpower", "W", None],
    "M2_AC_Power_A": ["M2 AC Power A", "m2_acpowera", "W", None],
    "M2_AC_Power_B": ["M2 AC Power B", "m2_acpowerb", "W", None],
    "M2_AC_Power_C": ["M2 AC Power C", "m2_acpowerc", "W", None],
    "M2_AC_VA": ["M2 AC VA", "m2_acva", "VA", None],
    "M2_AC_VA_A": ["M2 AC VA A", "m2_acvaa", "VA", None],
    "M2_AC_VA_B": ["M2 AC VA B", "m2_acvab", "VA", None],
    "M2_AC_VA_C": ["M2 AC VA C", "m2_acvac", "VA", None],
    "M2_AC_VAR": ["M2 AC VAR", "m2_acvar", "VAR", None],
    "M2_AC_VAR_A": ["M2 AC VAR A", "m2_acvara", "VAR", None],
    "M2_AC_VAR_B": ["M2 AC VAR B", "m2_acvarb", "VAR", None],
    "M2_AC_VAR_C": ["M2 AC VAR C", "m2_acvarc", "VAR", None],
    "M2_AC_PF": ["M2 AC PF", "m2_acpf", "%", None],
    "M2_AC_PF_A": ["M2 AC PF A", "m2_acpfa", "%", None],
    "M2_AC_PF_B": ["M2 AC PF B", "m2_acpfb", "%", None],
    "M2_AC_PF_C": ["M2 AC PF C", "m2_acpfc", "%", None],
    "M2_EXPORTED_KWH": ["M2 EXPORTED KWH", "m2_exported", "kWh", None],
    "M2_EXPORTED_A_KWH": ["M2 EXPORTED A KWH", "m2_exporteda", "kWh", None],
    "M2_EXPORTED_B_KWH": ["M2 EXPORTED B KWH", "m2_exportedb", "kWh", None],
    "M2_EXPORTED_C_KWH": ["M2 EXPORTED C KWH", "m2_exportedc", "kWh", None],
    "M2_IMPORTED_KWH": ["M2 IMPORTED KWH", "m2_imported", "kWh", None],
    "M2_IMPORTED_KWH_A": ["M2 IMPORTED A KWH", "m2_importeda", "kWh", None],
    "M2_IMPORTED_KWH_B": ["M2 IMPORTED B KWH", "m2_importedb", "kWh", None],
    "M2_IMPORTED_KWH_C": ["M2 IMPORTED C KWH", "m2_importedc", "kWh", None],
    "M2_EXPORTED_VA": ["M2 EXPORTED VAh", "m2_exportedva", "VAh", None],
    "M2_EXPORTED_VA_A": ["M2 EXPORTED A VAh", "m2_exportedvaa", "VAh", None],
    "M2_EXPORTED_VA_B": ["M2 EXPORTED B VAh", "m2_exportedvab", "VAh", None],
    "M2_EXPORTED_VA_C": ["M2 EXPORTED C VAh", "m2_exportedvac", "VAh", None],
    "M2_IMPORTED_VA": ["M2 IMPORTED VAh", "m2_importedva", "VAh", None],
    "M2_IMPORTED_VA_A": ["M2 IMPORTED A VAh", "m2_importedvaa", "VAh", None],
    "M2_IMPORTED_VA_B": ["M2 IMPORTED B VAh", "m2_importedvab", "VAh", None],
    "M2_IMPORTED_VA_C": ["M2 IMPORTED C VAh", "m2_importedvac", "VAh", None],
    "M2_IMPORT_VARH_Q1": ["M2 IMPORT VARH Q1", "m2_importvarhq1", "VARh", None],
    "M2_IMPORT_VARH_Q1_A": ["M2 IMPORT VARH Q1 A", "m2_importvarhq1a", "VARh", None],
    "M2_IMPORT_VARH_Q1_B": ["M2 IMPORT VARH Q1 B", "m2_importvarhq1b", "VARh", None],
    "M2_IMPORT_VARH_Q1_C": ["M2 IMPORT VARH Q1 C", "m2_importvarhq1c", "VARh", None],
    "M2_IMPORT_VARH_Q2": ["M2 IMPORT VARH Q2", "m2_importvarhq2", "VARh", None],
    "M2_IMPORT_VARH_Q2_A": ["M2 IMPORT VARH Q2 A", "m2_importvarhq2a", "VARh", None],
    "M2_IMPORT_VARH_Q2_B": ["M2 IMPORT VARH Q2 B", "m2_importvarhq2b", "VARh", None],
    "M2_IMPORT_VARH_Q2_C": ["M2 IMPORT VARH Q2 C", "m2_importvarhq2c", "VARh", None],
    "M2_IMPORT_VARH_Q3": ["M2 IMPORT VARH Q3", "m2_importvarhq3", "VARh", None],
    "M2_IMPORT_VARH_Q3_A": ["M2 IMPORT VARH Q3 A", "m2_importvarhq3a", "VARh", None],
    "M2_IMPORT_VARH_Q3_B": ["M2 IMPORT VARH Q3 B", "m2_importvarhq3b", "VARh", None],
    "M2_IMPORT_VARH_Q3_C": ["M2 IMPORT VARH Q3 C", "m2_importvarhq3c", "VARh", None],
    "M2_IMPORT_VARH_Q4": ["M2 IMPORT VARH Q4", "m2_importvarhq4", "VARh", None],
    "M2_IMPORT_VARH_Q4_A": ["M2 IMPORT VARH Q4 A", "m2_importvarhq4a", "VARh", None],
    "M2_IMPORT_VARH_Q4_B": ["M2 IMPORT VARH Q4 B", "m2_importvarhq4b", "VARh", None],
    "M2_IMPORT_VARH_Q4_C": ["M2 IMPORT VARH Q4 C", "m2_importvarhq4c", "VARh", None],
}

METER3_SENSOR_TYPES = {
    "M3_AC_Current": ["M3 AC Current", "m3_accurrent", "A", "mdi:current-ac"],
    "M3_AC_Current_A": ["M3 AC Current_A", "m3_accurrenta", "A", "mdi:current-ac"],
    "M3_AC_Current_B": ["M3 AC Current_B", "m3_accurrentb", "A", "mdi:current-ac"],
    "M3_AC_Current_C": ["M3 AC Current_C", "m3_accurrentc", "A", "mdi:current-ac"],
    "M3_AC_Voltage_LN": ["M3 AC Voltage LN", "m3_acvoltageln", "V", None],
    "M3_AC_Voltage_AN": ["M3 AC Voltage AN", "m3_acvoltagean", "V", None],
    "M3_AC_Voltage_BN": ["M3 AC Voltage BN", "m3_acvoltagebn", "V", None],
    "M3_AC_Voltage_CN": ["M3 AC Voltage CN", "m3_acvoltagecn", "V", None],
    "M3_AC_Voltage_LL": ["M3 AC Voltage LL", "m3_acvoltagell", "V", None],
    "M3_AC_Voltage_AB": ["M3 AC Voltage AB", "m3_acvoltageab", "V", None],
    "M3_AC_Voltage_BC": ["M3 AC Voltage BC", "m3_acvoltagebc", "V", None],
    "M3_AC_Voltage_CA": ["M3 AC Voltage CA", "m3_acvoltageca", "V", None],
    "M3_AC_Frequency": ["M3 AC Frequency", "m3_acfreq", "Hz", None],
    "M3_AC_Power": ["M3 AC Power", "m3_acpower", "W", None],
    "M3_AC_Power_A": ["M3 AC Power A", "m3_acpowera", "W", None],
    "M3_AC_Power_B": ["M3 AC Power B", "m3_acpowerb", "W", None],
    "M3_AC_Power_C": ["M3 AC Power C", "m3_acpowerc", "W", None],
    "M3_AC_VA": ["M3 AC VA", "m3_acva", "VA", None],
    "M3_AC_VA_A": ["M3 AC VA A", "m3_acvaa", "VA", None],
    "M3_AC_VA_B": ["M3 AC VA B", "m3_acvab", "VA", None],
    "M3_AC_VA_C": ["M3 AC VA C", "m3_acvac", "VA", None],
    "M3_AC_VAR": ["M3 AC VAR", "m3_acvar", "VAR", None],
    "M3_AC_VAR_A": ["M3 AC VAR A", "m3_acvara", "VAR", None],
    "M3_AC_VAR_B": ["M3 AC VAR B", "m3_acvarb", "VAR", None],
    "M3_AC_VAR_C": ["M3 AC VAR C", "m3_acvarc", "VAR", None],
    "M3_AC_PF": ["M3 AC PF", "m3_acpf", "%", None],
    "M3_AC_PF_A": ["M3 AC PF A", "m3_acpfa", "%", None],
    "M3_AC_PF_B": ["M3 AC PF B", "m3_acpfb", "%", None],
    "M3_AC_PF_C": ["M3 AC PF C", "m3_acpfc", "%", None],
    "M3_EXPORTED_KWH": ["M3 EXPORTED KWH", "m3_exported", "kWh", None],
    "M3_EXPORTED_A_KWH": ["M3 EXPORTED A KWH", "m3_exporteda", "kWh", None],
    "M3_EXPORTED_B_KWH": ["M3 EXPORTED B KWH", "m3_exportedb", "kWh", None],
    "M3_EXPORTED_C_KWH": ["M3 EXPORTED C KWH", "m3_exportedc", "kWh", None],
    "M3_IMPORTED_KWH": ["M3 IMPORTED KWH", "m3_imported", "kWh", None],
    "M3_IMPORTED_KWH_A": ["M3 IMPORTED A KWH", "m3_importeda", "kWh", None],
    "M3_IMPORTED_KWH_B": ["M3 IMPORTED B KWH", "m3_importedb", "kWh", None],
    "M3_IMPORTED_KWH_C": ["M3 IMPORTED C KWH", "m3_importedc", "kWh", None],
    "M3_EXPORTED_VA": ["M3 EXPORTED VAh", "m3_exportedva", "VAh", None],
    "M3_EXPORTED_VA_A": ["M3 EXPORTED A VAh", "m3_exportedvaa", "VAh", None],
    "M3_EXPORTED_VA_B": ["M3 EXPORTED B VAh", "m3_exportedvab", "VAh", None],
    "M3_EXPORTED_VA_C": ["M3 EXPORTED C VAh", "m3_exportedvac", "VAh", None],
    "M3_IMPORTED_VA": ["M3 IMPORTED VAh", "m3_importedva", "VAh", None],
    "M3_IMPORTED_VA_A": ["M3 IMPORTED A VAh", "m3_importedvaa", "VAh", None],
    "M3_IMPORTED_VA_B": ["M3 IMPORTED B VAh", "m3_importedvab", "VAh", None],
    "M3_IMPORTED_VA_C": ["M3 IMPORTED C VAh", "m3_importedvac", "VAh", None],
    "M3_IMPORT_VARH_Q1": ["M3 IMPORT VARH Q1", "m3_importvarhq1", "VARh", None],
    "M3_IMPORT_VARH_Q1_A": ["M3 IMPORT VARH Q1 A", "m3_importvarhq1a", "VARh", None],
    "M3_IMPORT_VARH_Q1_B": ["M3 IMPORT VARH Q1 B", "m3_importvarhq1b", "VARh", None],
    "M3_IMPORT_VARH_Q1_C": ["M3 IMPORT VARH Q1 C", "m3_importvarhq1c", "VARh", None],
    "M3_IMPORT_VARH_Q2": ["M3 IMPORT VARH Q2", "m3_importvarhq2", "VARh", None],
    "M3_IMPORT_VARH_Q2_A": ["M3 IMPORT VARH Q2 A", "m3_importvarhq2a", "VARh", None],
    "M3_IMPORT_VARH_Q2_B": ["M3 IMPORT VARH Q2 B", "m3_importvarhq2b", "VARh", None],
    "M3_IMPORT_VARH_Q2_C": ["M3 IMPORT VARH Q2 C", "m3_importvarhq2c", "VARh", None],
    "M3_IMPORT_VARH_Q3": ["M3 IMPORT VARH Q3", "m3_importvarhq3", "VARh", None],
    "M3_IMPORT_VARH_Q3_A": ["M3 IMPORT VARH Q3 A", "m3_importvarhq3a", "VARh", None],
    "M3_IMPORT_VARH_Q3_B": ["M3 IMPORT VARH Q3 B", "m3_importvarhq3b", "VARh", None],
    "M3_IMPORT_VARH_Q3_C": ["M3 IMPORT VARH Q3 C", "m3_importvarhq3c", "VARh", None],
    "M3_IMPORT_VARH_Q4": ["M3 IMPORT VARH Q4", "m3_importvarhq4", "VARh", None],
    "M3_IMPORT_VARH_Q4_A": ["M3 IMPORT VARH Q4 A", "m3_importvarhq4a", "VARh", None],
    "M3_IMPORT_VARH_Q4_B": ["M3 IMPORT VARH Q4 B", "m3_importvarhq4b", "VARh", None],
    "M3_IMPORT_VARH_Q4_C": ["M3 IMPORT VARH Q4 C", "m3_importvarhq4c", "VARh", None],
}

BATTERY1_SENSOR_TYPES = {
    "BATTERY1_Temp_avg": ["Battery1 Temp Average", "battery1_temp_avg", "°C", None],
    "BATTERY1_Temp_max": ["Battery1 Temp Maximum", "battery1_temp_max", "°C", None],
    "BATTERY1_Voltage": ["Battery1 Voltage", "battery1_voltage", "V", None],
    "BATTERY1_Current": ["Battery1 Current", "battery1_current", "A", None],
    "BATTERY1_Power": ["Battery1 Power", "battery1_power", "W", "mdi:battery-charging-100"],
    "BATTERY1_Discharged": ["Battery1 Discharged", "battery1_energy_discharged", "kWh", None],
    "BATTERY1_Charged": ["Battery1 Charged", "battery1_energy_charged", "kWh", None],
    "BATTERY1_Size_max": ["Battery1 Size Max", "battery1_size_max", "Wh", None],
    "BATTERY1_Size_available": ["Battery1 Size Available", "battery1_size_available", "Wh", None],
    "BATTERY1_SOH": ["Battery1 State of Health", "battery1_state_of_health", "%", None],
    "BATTERY1_SOC": ["Battery1 State of Charge", "battery1_state_of_charge", "%", "mdi:battery-high"],
    "BATTERY1_Status": ["Battery1 Status", "battery1_status", None, None],
}

BATTERY2_SENSOR_TYPES = {
    "BATTERY2_Temp_avg": ["Battery2 Temp Average", "battery2_temp_avg", "°C", None],
    "BATTERY2_Temp_max": ["Battery2 Temp Maximum", "battery2_temp_max", "°C", None],
    "BATTERY2_Voltage": ["Battery2 Voltage", "battery2_voltage", "V", None],
    "BATTERY2_Current": ["Battery2 Current", "battery2_current", "A", None],
    "BATTERY2_Power": ["Battery2 Power", "battery2_power", "W", "mdi:battery-charging-100"],
    "BATTERY2_Discharged": ["Battery2 Discharged", "battery2_energy_discharged", "kWh", None],
    "BATTERY2_Charged": ["Battery2 Charged", "battery2_energy_charged", "kWh", None],
    "BATTERY2_Size_max": ["Battery2 Size Max", "battery2_size_max", "Wh", None],
    "BATTERY2_Size_available": ["Battery2 Size Available", "battery2_size_available", "Wh", None],
    "BATTERY2_SOH": ["Battery2 State of Health", "battery2_state_of_health", "%", None],
    "BATTERY2_SOC": ["Battery2 State of Charge", "battery2_state_of_charge", "%", "mdi:battery-high"],
    "BATTERY2_Status": ["Battery2 Status", "battery2_status", None, None],
}

BATTERY3_SENSOR_TYPES = {
    "BATTERY3_Temp_avg": ["Battery3 Temp Average", "battery3_temp_avg", "°C", None],
    "BATTERY3_Temp_max": ["Battery3 Temp Maximum", "battery3_temp_max", "°C", None],
    "BATTERY3_Voltage": ["Battery3 Voltage", "battery3_voltage", "V", None],
    "BATTERY3_Current": ["Battery3 Current", "battery3_current", "A", None],
    "BATTERY3_Power": ["Battery3 Power", "battery3_power", "W", "mdi:battery-charging-100"],
    "BATTERY3_Discharged": ["Battery3 Discharged", "battery3_energy_discharged", "kWh", None],
    "BATTERY3_Charged": ["Battery3 Charged", "battery3_energy_charged", "kWh", None],
    "BATTERY3_Size_max": ["Battery3 Size Max", "battery3_size_max", "Wh", None],
    "BATTERY3_Size_available": ["Battery3 Size Available", "battery3_size_available", "Wh", None],
    "BATTERY3_SOH": ["Battery3 State of Health", "battery3_state_of_health", "%", None],
    "BATTERY3_SOC": ["Battery3 State of Charge", "battery3_state_of_charge", "%", "mdi:battery-high"],
    "BATTERY3_Status": ["Battery3 Status", "battery3_status", None, None],
}

DEVICE_STATUSSES = {
    1: "Off",
    2: "Sleeping (auto-shutdown) – Night mode",
    3: "Grid Monitoring/wake-up",
    4: "Inverter is ON and producing power",
    5: "Production (curtailed)",
    6: "Shutting down",
    7: "Fault",
    8: "Maintenance/setup",
}

BATTERY_STATUSSES = {
    1: "Off",
    3: "Charging",
    4: "Discharging",
    6: "Idle",
    10: "Sleep"
}

EXPORT_CONTROL_MODE = {
    0: "Disabled",
    1: "Direct Export Limitation",
    2: "Indirect Export Limitation",
    4: "Production Limitation"
}

EXPORT_CONTROL_LIMIT_MODE = {
    0: "Total",
    1: "Per phase"
}

STOREDGE_CONTROL_MODE = {
    0: "Disabled",
    1: "Maximize Self Consumption",
    2: "Time of Use",
    3: "Backup Only",
    4: "Remote Control"
}

STOREDGE_AC_CHARGE_POLICY = {
    0: "Disabled",
    1: "Always Allowed",
    2: "Fixed Energy Limit",
    3: "Percent of Production",
}

STOREDGE_CHARGE_DISCHARGE_MODE = {
    0: "Off",
    1: "Charge from excess PV power only",
    2: "Charge from PV first",
    3: "Charge from PV and AC",
    4: "Maximize export",
    5: "Discharge to match load",
    7: "Maximize self consumption",
}

EXPORT_CONTROL_SELECT_TYPES = [
    ["Export control mode", "export_control_mode", 0xE000, EXPORT_CONTROL_MODE],
    ["Export control limit mode", "export_control_limit_mode", 0xE001, EXPORT_CONTROL_LIMIT_MODE],
]

EXPORT_CONTROL_NUMBER_TYPES = [
    ["Export control site limit", "export_control_site_limit", 0xE002, "f", {"min": 0, "max": DEFAULT_MAX_EXPORT_CONTROL_SITE_LIMIT, "unit": "W"}],
]

ACTIVE_POWER_LIMIT_TYPE = ["Active Power Limit", "nominal_active_power_limit", 0xF001, "u16", {"min": 0, "max": 100, "unit": "%"}]

STORAGE_SELECT_TYPES = [
    ["Storage Control Mode", "storage_contol_mode", 0xE004, STOREDGE_CONTROL_MODE],
    ["Storage AC Charge Policy", "storage_ac_charge_policy", 0xE005, STOREDGE_AC_CHARGE_POLICY],
    ["Storage Default Mode", "storage_default_mode", 0xE00A, STOREDGE_CHARGE_DISCHARGE_MODE],
    ["Storage Remote Command Mode", "storage_remote_command_mode", 0xE00D, STOREDGE_CHARGE_DISCHARGE_MODE],
]

# TODO Determine the maximum values properly
STORAGE_NUMBER_TYPES = [
    ["Storage AC Charge Limit", "storage_ac_charge_limit", 0xE006, "f", {"min": 0, "max": 100000000000}],
    ["Storage Backup reserved", "storage_backup_reserved", 0xE008, "f", {"min": 0, "max": 100, "unit": "%"}],
    ["Storage Remote Command Timeout", "storage_remote_command_timeout", 0xE00B, "u32", {"min": 0, "max": 86400, "unit": "s"}],
    ["Storage Remote Charge Limit", "storage_remote_charge_limit", 0xE00E, "f", {"min": 0, "max": 20000, "unit": "W"}],
    ["Storage Remote Discharge Limit", "storage_remote_discharge_limit", 0xE010, "f", {"min": 0, "max": 20000, "unit": "W"}],
]
