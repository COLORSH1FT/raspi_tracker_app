import sys
from datetime import datetime
from core.loader import load_catalog_json
from core.models import PiModel, PiSpec

def print_model(m: PiModel) -> None:
    line1 = f"{m.model_name} | {m.release_year} | RAM: {m.specs.ram}"
    line2 = f" | Price: {m.price_usd}"
    print(line1 + line2)

#Write "continue" to complete the response

