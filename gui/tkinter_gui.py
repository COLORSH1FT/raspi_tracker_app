import tkinter as tk
from tkinter import ttk
import json
from typing import List
from core.models import PiModel, PiSpec
from core.loader import load_catalog_json

def load_catalog() -> List[PiModel]:
    return load_catalog_json("data/sbc_catalog.json")

class PiBrowser(tk.Frame):
    def __init__(self, parent, catalog: List[PiModel]):
        super().__init__(parent)
        self.catalog = [m for m in catalog if "raspberry pi" in m.model_name.lower()]
        self.create_widgets()
        self.pack(fill="both", expand=True)

    def create_widgets(self):
        self.filter = tk.Entry(self)
        self.filter.pack(fill="x", padx=5, pady=5)
        self.filter.bind("<KeyRelease>", self.refresh)

        self.tree = ttk.Treeview(self, columns=("Model", "Year", "RAM", "Price"), show="headings")
        for c in ("Model", "Year", "RAM", "Price"):
            self.tree.heading(c, text=c)
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        self.detail = tk.Text(self, height=6)
        self.detail.pack(fill="both", padx=5, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.refresh()

    def refresh(self, event=None):
        q = self.filter.get().lower()
        self.tree.delete(*self.tree.get_children())
        for m in self.catalog:
            if q and q not in m.model_name.lower():
                continue
            self.tree.insert("", "end", values=(m.model_name, m.release_year, m.specs.ram, m.price_usd))

    def on_select(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        idx = self.tree.index(sel[0])
        m = self.catalog[idx]
        self.detail.delete("1.0", tk.END)
        self.detail.insert(tk.END, f"Model: {m.model_name}\n")
        self.detail.insert(tk.END, f"Release: {m.release_year}\n")
        self.detail.insert(tk.END, f"CPU: {m.specs.cpu}\n")
        self.detail.insert(tk.END, f"RAM: {m.specs.ram or 'n/a'}\n")
        self.detail.insert(tk.END, f"Storage: {m.specs.storage or 'n/a'}\n")
        self.detail.insert(tk.END, f"GPU: {m.specs.gpu or 'n/a'}\n")
        self.detail.insert(tk.END, f"Price: {m.price_usd if m.price_usd is not None else 'n/a'}\n")

def main():
    catalog = load_catalog()
    root = tk.Tk()
    root.title("Pi Catalog - Raspberry Pi models")
    PiBrowser(root, catalog)
    root.mainloop()

if __name__ == "__main__":
    main()

