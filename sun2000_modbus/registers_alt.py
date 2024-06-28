from enum import Enum

from . import datatypes
from . import mappings


class AccessType(Enum):
    RO = "ro"
    RW = "rw"
    WO = "wo"


class Register:
    address: int
    quantity: int
    data_type: datatypes.DataType
    gain: float
    unit: str
    access_type: AccessType
    mapping: dict

    def __init__(self, address, quantity, data_type, gain, unit, access_type, mapping):
        self.address = address
        self.quantity = quantity
        self.data_type = data_type
        self.gain = gain
        self.unit = unit
        self.access_type = access_type
        self.mapping = mapping

# 1 Rated inverter power U16 N/A 1 40710 1
# 2 ESN MLD N/A 1 40713 10
# 3 Hardware version MLD N/A 1 40789 15
# 4 Software version MLD N/A 1 40819 15
# 5 M od B us protocol version MLD N/A 1 40834 15

# 1 PV1 Voltage/PV1 V I16 V 10 40500 1 For all power classes
# 2 PV2 Voltage/PV2 V I16 V 10 40501 1 For all power classes
# 3 PV3 Voltage/PV3 V I16 V 10 40502 1 For all power classes
# 4 PV4 Voltage/PV4 V I16 V 10 40503 1 For all power classes
# 5 PV5 Voltage/PV5 V I16 V 10 40504 1 For all power classes
# 6 PV6 Voltage/PV6 V I16 V 10 40505 1 For all power classes
# 7 PV1 Current/PV1 I I16 A 100 40506 1 For all power classes
# 8 PV2 Current/PV2 I I16 A 100 40507 1 For all power classes
# 9 PV3 Current/PV3 I I16 A 100 40508 1 For all power classes
# 10 PV4 Current/PV4 I I16 A 100 40509 1 For all power classes
# 11 PV5 Current/PV5 I I16 A 100 40510 1 For all power classes
# 12 PV6 Current/PV6 I I16 A 100 40511 1 For all power classes
# 13 CO2 r eduction U32 kg 100 40523 2
# 14 Active power I32 kW 1000 40525 2
# 15 Uab U16 V 100 40527 1
# 16 Ubc U16 V 100 40528 1
# 17 Uca U16 V 100 40529 1
# 18 Power factor I16 N/A 1000 40532 1
# 19 Cabinet temperature I16 ℃ 10 40533 1
# 20 Reactive output power I32 kVar 1000 40544 2
# 21 Frequency U16 Hz 100 40546 1
# 22 E Total U32 kWh 100 40560 2
# 23 Current-day yield U32 kWh 100 40562 2
# 24 Ia I16 A 100 40572 1
# 25 Ib I16 A 100 40573 1
# 26 Ic I16 A 100 40574 1
# 27 Inverter start time U32 Sec 1 40613 2
# 28 Inverter shutdown time U32 Sec 1 40615 2
# 29 Inverter efficiency U16 % 100 40685 1
# 30 MPPT1 total input power U32 kW 1000 40686 2
# 31 MPPT2 total input power U32 kW 1000 40688 2
# 32 MPPT3 total input power U32 kW 1000 40690 2
# 33 Total input power U32 kW 1000 40692 2
# 34 Zero voltage ride through
# protection
# U16 N/A 1 40696 1 0: no 1: yes
# 35 LVRT protection U16 N/A 1 40697 1 0: no 1: yes
# 36 Anti islanding U16 N/A 1 40698 1 0: no 1: yes
# 37 Locking U16 N/A 1 40699 1 0: lock 1: not lock
# 38 Inverter on/off status U16 N/A 1 40931 1 Bit 1: 1: grid-tied 0: shutdown
# 39 Inverter status U16 N/A 1 40939 1 0x0000: Idle: Initializing 0x0001: Idle: ISO Detecting 0x0002: Idle: Irradiation Detecting 0x0100: Starting 0x0200: On-grid 0x0201: On-grid: Limited 0x0300: Shutdown: Abnormal 0x0301: Shutdown: Forced 0x0401: Grid Dispatch: cosψ-P Curve 0x0402: Grid Dispatch: Q-U Curve 0xA000: Idle: No Irradiation


class InverterEquipmentRegister(Enum):
    SN = Register(40713, 10, datatypes.DataType.STRING, None, None, AccessType.RO, None)
    
    ActivePower = Register(40525, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    PhaseAVoltage = Register(40527, 1, datatypes.DataType.UINT16_BE, 100, "V", AccessType.RO, None)
    PhaseBVoltage = Register(40528, 1, datatypes.DataType.UINT16_BE, 100, "V", AccessType.RO, None)
    PhaseCVoltage = Register(40529, 1, datatypes.DataType.UINT16_BE, 100, "V", AccessType.RO, None)
    PhaseACurrent = Register(40572, 1, datatypes.DataType.INT32_BE, 100, "A", AccessType.RO, None)
    PhaseBCurrent = Register(40573, 1, datatypes.DataType.INT16_BE, 100, "A", AccessType.RO, None)
    PhaseCCurrent = Register(40574, 1, datatypes.DataType.INT16_BE, 100, "A", AccessType.RO, None)
    InputPower = Register(40692, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    MaximumActivePower = Register(40710, 1, datatypes.DataType.UINT16_BE, 1, "W", AccessType.RO, None)
    AccumulatedEnergyYield = Register(40560, 2, datatypes.DataType.UINT32_BE, 100, "kWh", AccessType.RO, None)
    GridFrequency = Register(40546, 1, datatypes.DataType.UINT16_BE, 100, "Hz", AccessType.RO, None)
    PowerFactor = Register(40532, 1, datatypes.DataType.INT16_BE, 1000, None, AccessType.RO, None)
    State1 = Register(40939, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, mappings.DeviceStatus)