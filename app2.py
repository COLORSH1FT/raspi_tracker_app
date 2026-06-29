# app.py
from __future__ import annotations
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

CURRENT_YEAR = datetime.now().year

@dataclass
class PiSpec:
    cpu: str
    gpu: Optional[str] = None
    ram: Optional[str] = None
    storage: Optional[str] = None
    other: Optional[str] = None

@dataclass
class PiModel:
    model_name: str
    specs: PiSpec
    price_usd: Optional[float]
    release_year: Optional[int]

def era_of(year: Optional[int]) -> str:
    if year is None:
        return "unknown"
    if year <= CURRENT_YEAR - 2:
        return "older"
    if year <= CURRENT_YEAR:
        return "current"
    return "future"

def print_model(m: PiModel) -> None:
    print(f"Model: {m.model_name}")
    print(f"  Release year: {m.release_year or 'unknown'}")
    print(f"  Era: {era_of(m.release_year)}")
    print(f"  Price (USD): {m.price_usd if m.price_usd is not None else 'n/a'}")
    print(f"  Specs:")
    print(f"    CPU: {m.specs.cpu}")
    print(f"    GPU: {m.specs.gpu or 'n/a'}")
    print(f"    RAM: {m.specs.ram or 'n/a'}")
    print(f"    Storage: {m.specs.storage or 'n/a'}")
    print(f"    Other: {m.specs.other or 'n/a'}")
    print()

def build_catalog() -> List[PiModel]:
    return [
            PiModel(
            model_name="Raspberry Pi 1 Model B",
            specs=PiSpec(cpu="ARM1176JZF-S @ 700MHz", gpu=None, ram="256MB/512MB", storage="SD card", other="Basic GPIO"),
            price_usd=25.0, release_year=2012
        ),
        PiModel(
            model_name="Raspberry Pi 1 Model A",
            specs=PiSpec(cpu="ARM11 @ 700MHz", gpu=None, ram="256MB", storage="SD card", other="Limited GPIO"),
            price_usd=20.0, release_year=2013
        ),
        PiModel(
            model_name="Raspberry Pi 1 Model A+",
            specs=PiSpec(cpu="ARM11 @ 700MHz", gpu=None, ram="256MB", storage="SD card", other="Same as A but smaller PCB"),
            price_usd=20.0, release_year=2014
        ),
        PiModel(
            model_name="Raspberry Pi 2 Model B",
            specs=PiSpec(cpu="Quad-core ARM Cortex-A7 @ 900MHz", gpu="Broadcom VideoCore IV (VC6)", ram="1GB", storage="SD card", other="Broadcom GPU upgrade"),
            price_usd=35.0, release_year=2015
        ),
        PiModel(
            model_name="Raspberry Pi 3 Model B",
            specs=PiSpec(cpu="Broadcom BCM2837 @ 1.2GHz", gpu="VideoCore IV", ram="1GB", storage="microSD", other="Wi-Fi, Bluetooth"),
            price_usd=35.0, release_year=2016
        ),
        PiModel(
            model_name="Raspberry Pi 3 Model B+",
            specs=PiSpec(cpu="Broadcom BCM2837B0 @ 1.4GHz", gpu="VideoCore IV", ram="1GB", storage="microSD", other="Enhanced Wi‑Fi/Bluetooth"),
            price_usd=35.0, release_year=2018
        ),
        PiModel(
            model_name="Raspberry Pi 3A+",
            specs=PiSpec(cpu="Broadcom BCM2837B0 @ 1.4GHz", gpu="VideoCore IV", ram="1GB", storage="microSD", other="Compact form factor"),
            price_usd=25.0, release_year=2018
        ),
        PiModel(
            model_name="Raspberry Pi 4 Model B",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A72 @ 1.5-1.8GHz", gpu="VideoCore VI", ram="2GB/4GB/8GB", storage="microSD", other="Dual-monitor via micro HDMI, USB 3.0"),
            price_usd=55.0, release_year=2019
        ),
        PiModel(
            model_name="Raspberry Pi 4 Model B (8GB)",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A72 @ 1.8GHz", gpu="VideoCore VI", ram="8GB", storage="microSD", other="Dual-monitor via micro HDMI, USB 3.0"),
            price_usd=75.0, release_year=2020
        ),
        PiModel(
            model_name="Raspberry Pi Zero",
            specs=PiSpec(cpu="Broadcom BCM2835 @ 1GHz", gpu=None, ram="512MB", storage="microSD", other="Compact"),
            price_usd=5.0, release_year=2015
        ),
        PiModel(
            model_name="Raspberry Pi Zero W",
            specs=PiSpec(cpu="Broadcom BCM2835 @ 1GHz", gpu=None, ram="512MB", storage="microSD", other="Wi-Fi, Bluetooth"),
            price_usd=10.0, release_year=2017
        ),
        PiModel(
            model_name="Raspberry Pi Zero W2",
            specs=PiSpec(cpu="Broadcom BCM2710A1? (RP2040-based style)", gpu=None, ram="512MB", storage="microSD", other="Updates/cheap variant"),
            price_usd=12.0, release_year=2021
        ),
        PiModel(
            model_name="Raspberry Pi 400",
            specs=PiSpec(cpu="Broadcom BCM2711 @ 1.8GHz", gpu="VideoCore VI", ram="4GB", storage="microSD", other="Keyboard-integrated"),
            price_usd=90.0, release_year=2020
        ),
        PiModel(
            model_name="Raspberry Pi Pico",
            specs=PiSpec(cpu="RP2040 dual-core @ 133MHz", gpu=None, ram="264KB", storage="On-chip", other="USB 0/1"),
            price_usd=4.0, release_year=2021
        ),
        PiModel(
            model_name="Raspberry Pi 5 Model B 1GB",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A76", gpu="VideoCore VI", ram="1GB", storage="microSD", other="PCIe via USB-C adapter"),
            price_usd=40.0,
            release_year=2023,
        ),
        PiModel(
            model_name="Raspberry Pi 5 Model B 2GB",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A76", gpu="VideoCore VI", ram="2GB", storage="microSD", other="PCIe via USB-C adapter"),
            price_usd=50.0,
            release_year=2023,
        ),
        PiModel(
            model_name="Raspberry Pi 5 Model B 4GB",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A76", gpu="VideoCore VI", ram="4GB", storage="microSD", other="PCIe via USB-C adapter"),
            price_usd=60.0,
            release_year=2023,
        ),
        PiModel(
            model_name="Raspberry Pi 5 Model B 8GB",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A76", gpu="VideoCore VI", ram="8GB", storage="microSD", other="PCIe via USB-C adapter"),
            price_usd=80.0,
            release_year=2023,
        ),
        PiModel(
            model_name="Raspberry Pi 5 Model B 16GB",
            specs=PiSpec(cpu="Broadcom BCM2711, Cortex-A76", gpu="VideoCore VI", ram="16GB", storage="microSD", other="PCIe via USB-C adapter"),
            price_usd=120.0,
            release_year=2023,
        ),
        # ...existing entries continue here
        ]


def main():
    catalog = build_catalog()
    print("Pi Catalog CLI (all Raspberry Pi models embedded)")
    print("Commands: list | era <older|current|future> | model <name> | exit")
    while True:
        try:
            cmd = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not cmd:
            continue
        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "list":
            for m in catalog:
                print_model(m)
        elif action == "era" and len(parts) > 1:
            era = parts[1].lower()
            for m in catalog:
                if era_of(m.release_year) == era:
                    print_model(m)
        elif action == "model" and len(parts) > 1:
            q = parts[1].lower()
            for m in catalog:
                if q in m.model_name.lower():
                    print_model(m)
        elif action == "exit":
            break
        else:
            print("Unknown command. Try: list | era <older|current|future> | model <name>")

if __name__ == "__main__":
    main()

