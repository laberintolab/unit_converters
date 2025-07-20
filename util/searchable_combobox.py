# searchable_combobox.py
import tkinter as tk
from tkinter import ttk

class SearchableCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._completion_list = []
        self._hits = []
        self.position = 0
        self.bind('<KeyRelease>', self._handle_keyrelease)

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)
        self['values'] = self._completion_list

    def _handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.position = self.index(tk.END)
        elif event.keysym == "Left":
            if self.position < self.index(tk.END):
                self.position = self.position - 1
            return
        elif event.keysym == "Right":
            self.position = self.index(tk.END)
            return
        elif len(event.keysym) == 1 or event.keysym in ("space",):
            pass
        else:
            return

        typed = self.get().lower()
        if typed == '':
            self['values'] = self._completion_list
            return

        self._hits = [item for item in self._completion_list if typed in item.lower()]

        if self._hits:
            self['values'] = self._hits
        else:
            self['values'] = self._completion_list

        self.event_generate('<Down>')
