import sys
from datetime import datetime
from typing import List
from core.loader import load_catalog_json
from core.models import PiModel

CURRENT_YEAR = datetime.now().year

def print_model(m: PiModel) -> None:
    print(f"Model: {m.model_name}")
    print(f"  Release year: {m.release_year}")
    print(f"  Era: {era_of(m.release_year, CURRENT_YEAR)}")
    print(f"  Price (USD): {m.price_usd if m.price_usd is not None else 'n/a'}")
    print(f"  CPU: {m.specs.cpu}")
    print(f"  RAM: {m.specs.ram or 'n/a'}")
    print()

def era_of(year: int, current_year: int) -> str:
    if year <= current_year - 2:
        return "older"
    if year <= current_year:
        return "current"
    return "future"

def main():
    catalog = load_catalog_json("data/sbc_catalog.json")
    # Filter to Raspberry Pi models if you want
    catalog = [m for m in catalog if "raspberry pi" in m.model_name.lower()]
    print("Pi CLI (Raspberry Pi models only)")
    print("Commands: list | era <older|current|future> | model <name> | exit")
    while True:
        cmd = input(">>> ").strip()
        if not cmd:
            continue
        a = cmd.split(maxsplit=1)
        if a[0] == "list":
            for m in catalog:
                print_model(m)
        elif a[0] == "era" and len(a) > 1:
            era = a[1].lower()
            for m in catalog:
                if era_of(m.release_year, CURRENT_YEAR) == era:
                    print_model(m)
        elif a[0] == "model" and len(a) > 1:
            q = a[1].lower()
            for m in catalog:
                if q in m.model_name.lower():
                    print_model(m)
        elif a[0] == "exit":
            break
        else:
            print("Unknown command. Try 'list' or 'model <name>'.")

if __name__ == "__main__":
    main()

