# Unit Converter in Python

## Description

This project is unit converter example application implemented in Python using the Tkinter GUI library.  
It supports multiple categories including Length, Mass, Volume-Dry, Area, Temperature, Time, Angle, and Number Bases.  
The application features a simple and intuitive UI where users can select the category, units, and convert values interactively.

---

## Structure

```sh
UnitConverterApp/
├── dictionary/
│ ├── angle_units.py # Angle units conversion factors
│ ├── area_units.py # Area units conversion factors
│ ├── length_units.py # Length units conversion factors
│ ├── mass_units.py # Mass units conversion factors
│ ├── number_bases.py # Number bases definitions
│ ├── temperature_units.py # Temperature units data (scale and offset)
│ ├── time_units.py # Time units conversion factors
│ └── volume_dry_units.py # Volume-Dry units conversion factors
├── util/
│ ├── searchable_combobox.py # Class to enable a search inside the combo box
│ ├── unit_converter_utils.py # Converter class implementing conversion logic
└── UnitConverterApp.py # Tkinter GUI application for user interaction
```
---

## Dependencies

- Python 3.8 or higher (recommended)  
- Tkinter (usually included with standard Python installations)  
- No external packages required  

---

## Supported Python Versions

- Developed and tested with Python 3.8+  
- Should work with any Python 3.x version that includes Tkinter  

---

## How to Run on Linux

```sh
python3 UnitConverterApp.py 
```


## License
This app is distributed under the terms of the MIT License. See the [license](LICENSE.md) for details.