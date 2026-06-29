# app.py (embedded catalog extension)
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
        # Add any other variants you have
    ]

