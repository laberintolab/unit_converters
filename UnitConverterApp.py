import tkinter as tk
from tkinter import ttk, messagebox
from util import unit_converter_utils as utils
from util.searchable_combobox import SearchableCombobox

class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Unit Converter")
        root.geometry("500x320")
        root.resizable(False, False)

        # Map category to (conversion method, unit dictionary)
        self.categories = {
            "Length": (utils.UnitConverterUtils.convert_length, utils.LENGTH_UNIT_FACTORS),
            "Mass": (utils.UnitConverterUtils.convert_mass, utils.MASS_UNIT_FACTORS),
            "Volume-Dry": (utils.UnitConverterUtils.convert_volume_dry, utils.VOLUME_DRY_UNIT_FACTORS),
            "Area": (utils.UnitConverterUtils.convert_area, utils.AREA_UNIT_FACTORS),
            "Temperature": (utils.UnitConverterUtils.convert_temperature, utils.TEMPERATURE_UNITS),
            "Time": (utils.UnitConverterUtils.convert_time, utils.TIME_UNIT_FACTORS),
            "Angle": (utils.UnitConverterUtils.convert_angle, utils.ANGLE_UNIT_FACTORS),
            "Number Bases": (utils.UnitConverterUtils.convert_number_bases, utils.NUMBER_BASES),
        }

        ttk.Label(root, text="Select Category:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.category_combo = ttk.Combobox(root, values=list(self.categories.keys()), state="readonly")
        self.category_combo.grid(row=0, column=1, padx=10, pady=10)
        self.category_combo.bind("<<ComboboxSelected>>", self.on_category_change)
        self.category_combo.current(0)

        ttk.Label(root, text="From Unit:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_unit_var = tk.StringVar()
        self.from_combo = SearchableCombobox(root, textvariable=self.from_unit_var)
        self.from_combo.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(root, text="To Unit:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_unit_var = tk.StringVar()
        self.to_combo = SearchableCombobox(root, textvariable=self.to_unit_var)
        self.to_combo.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(root, text="Value:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.value_entry = ttk.Entry(root)
        self.value_entry.grid(row=3, column=1, padx=10, pady=10)

        self.convert_btn = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_btn.grid(row=4, column=0, columnspan=2, pady=15)

        self.result_label = ttk.Label(root, text="Result: ")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

        self.on_category_change()
        root.bind('<Return>', lambda event: self.convert())

    def on_category_change(self, event=None):
        category = self.category_combo.get()
        _, units_dict = self.categories.get(category, (None, None))

        if category == "Temperature":
            units = list(units_dict.keys())
        elif category == "Number Bases":
            units = list(units_dict.keys())
        else:
            units = list(units_dict.keys())

        units = sorted(units)

        self.from_combo.set_completion_list(units)
        self.to_combo.set_completion_list(units)

        if units:
            self.from_combo.set(units[0])
            self.to_combo.set(units[0])

        self.result_label.config(text="Result: ")

    def convert(self):
        category = self.category_combo.get()
        convert_func, _ = self.categories.get(category, (None, None))

        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        value_str = self.value_entry.get().strip()

        if not value_str:
            messagebox.showerror("Input Error", "Please enter a value to convert.")
            return

        try:
            if category == "Number Bases":
                result = convert_func(value_str, from_unit, to_unit)
            elif category == "Temperature":
                value = float(value_str)
                result = convert_func(value, from_unit, to_unit)
            else:
                value = float(value_str)
                result = convert_func(value, from_unit, to_unit)

            self.result_label.config(text=f"Result: {result}")
        except ValueError as ve:
            messagebox.showerror("Conversion Error", str(ve))
        except KeyError as ke:
            messagebox.showerror("Conversion Error", str(ke))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    icon = tk.PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    app = UnitConverterApp(root)
    root.mainloop()
