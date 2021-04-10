import os
import sqlite3
import pickle
import os
import pandas as pd
import logging
import json
from helper_methods import HelperMethods
from extract_mbtiles import ExtractMBTiles
from georeference_image import GeoreferenceImage
from stitch_images import StitchImage
from clip_raster import ClipRaster
from translate_image import TranslateImage

class GeoSatDriver(object):
  
  def __init__(self):
    self.geojson_path = '../data'
    self.geojson_file_name = 'map.geojson'
  
  
  def parse_geojson(self):
    """
    Read and parse geojson file.

    Returns:
        geojson: parsed geosjon from the geojson file
    """
    with open(os.path.join(self.geojson_path, self.geojson_file_name)) as geojson:
      data = json.load(geojson)
      
    geojson = data['features'][0]['geometry']
    
    return geojson
  
  def run_geo_sat_driver(self):
    """
    Method to run the geo-sat driver.
    """
    
    geojson = GeoSatDriver().parse_geojson()
    
    unique_id, output_file_name = HelperMethods().generate_unique_id_file()
    
    # Clip area of interest by passing geojson as argument
    ClipRaster().clip_aoi(geojson, unique_id, output_file_name)
    
    # Translate image into png
    TranslateImage('PNG').translate_image()


if __name__ == '__main__':
  GeoSatDriver().run_geo_sat_driver()
    
    