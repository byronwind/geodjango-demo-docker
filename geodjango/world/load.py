from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder
from .models import worldborder_mapping

world_shp = Path(__file__).resolve().parent / "data" / "TM_WORLD_BORDERS-0.3.shp"

def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, 
        worldborder_mapping, transform=False
    )
    lm.save(strict=True, verbose=verbose)