import json
from typing import List, Optional
from .models import PiModel, PiSpec

def load_catalog_json(path: str) -> List[PiModel]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    catalog: List[PiModel] = []
    for item in data:
        specs = PiSpec(**item["specs"])
        catalog.append(PiModel(
            model_name=item["model_name"],
            specs=specs,
            price_usd=item.get("price_usd"),
            release_year=item.get("release_year"),
        ))
    return catalog

