import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties
counties_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

shp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "data/kenyan-counties/County.shp"))
county_shp = LayerMapping(Counties, shp_path, counties_mapping)
county_shp.save(strict=True,verbose=True)  # Save the layermap, imports the data.
