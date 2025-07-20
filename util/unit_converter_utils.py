# unit_converter_utils.py
from dictionary.length_units import LENGTH_UNIT_FACTORS
from dictionary.mass_units import MASS_UNIT_FACTORS
from dictionary.volume_dry_units import VOLUME_DRY_UNIT_FACTORS
from dictionary.area_units import AREA_UNIT_FACTORS
from dictionary.temperature_units import TEMPERATURE_UNITS
from dictionary.time_units import TIME_UNIT_FACTORS
from dictionary.angle_units import ANGLE_UNIT_FACTORS
from dictionary.number_bases import NUMBER_BASES

class UnitConverterUtils:
    DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def get_factor(unit_name: str, factors: dict) -> float:
        # unit_name = unit_name.lower()  # Uncomment if needed
        if unit_name not in factors:
            raise KeyError(f"Unit '{unit_name}' not found.")
        return factors[unit_name]

    @classmethod
    def convert_units(cls, value: float, from_unit: str, to_unit: str, factors: dict) -> float:
        from_factor = cls.get_factor(from_unit, factors)
        to_factor = cls.get_factor(to_unit, factors)
        return value * from_factor / to_factor

    @classmethod
    def convert_length(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, LENGTH_UNIT_FACTORS)

    @classmethod
    def convert_mass(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, MASS_UNIT_FACTORS)

    @classmethod
    def convert_volume_dry(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, VOLUME_DRY_UNIT_FACTORS)

    @classmethod
    def convert_area(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, AREA_UNIT_FACTORS)

    @classmethod
    def convert_time(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, TIME_UNIT_FACTORS)

    @classmethod
    def convert_angle(cls, value: float, from_unit: str, to_unit: str) -> float:
        return cls.convert_units(value, from_unit, to_unit, ANGLE_UNIT_FACTORS)

    @staticmethod
    def to_kelvin(value: float, from_unit: str) -> float:
        unit = from_unit.lower()
        if unit not in TEMPERATURE_UNITS:
            raise ValueError(f"Temperature unit '{from_unit}' not supported.")
        scale, offset, _ = TEMPERATURE_UNITS[unit][1:4]
        return value * scale + offset

    @staticmethod
    def from_kelvin(value: float, to_unit: str) -> float:
        unit = to_unit.lower()
        if unit not in TEMPERATURE_UNITS:
            raise ValueError(f"Temperature unit '{to_unit}' not supported.")
        scale, offset, _ = TEMPERATURE_UNITS[unit][1:4]
        return (value - offset) / scale

    @classmethod
    def convert_temperature(cls, value: float, from_unit: str, to_unit: str) -> float:
        kelvin = cls.to_kelvin(value, from_unit)
        return cls.from_kelvin(kelvin, to_unit)

    @classmethod
    def validate_base(cls, base_name: str) -> int:
        base_name = base_name.lower()
        if base_name not in NUMBER_BASES:
            raise ValueError(f"Base '{base_name}' not supported.")
        return NUMBER_BASES[base_name]

    @classmethod
    def to_decimal(cls, number_str: str, base: int) -> int:
        return int(number_str, base)

    @classmethod
    def from_decimal(cls, number: int, base: int) -> str:
        if number == 0:
            return "0"
        digits = []
        n = number
        while n > 0:
            digits.append(cls.DIGITS[n % base])
            n //= base
        return ''.join(reversed(digits))

    @classmethod
    def convert_number_bases(cls, number_str: str, from_base_name: str, to_base_name: str) -> str:
        from_base = cls.validate_base(from_base_name)
        to_base = cls.validate_base(to_base_name)
        decimal_number = cls.to_decimal(number_str.upper(), from_base)
        return cls.from_decimal(decimal_number, to_base)
