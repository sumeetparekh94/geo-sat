import os
import sqlite3
import pickle
import os
import pandas as pd
import logging
from helper_methods import HelperMethods
from extract_mbtiles import ExtractMBTiles
from georeference_image import GeoreferenceImage
from stitch_images import StitchImage
from clip_raster import ClipRaster
from translate_image import TranslateImage

class Driver(object):
    
    def __init__(self):
      self.mbtile_path = '../data/massachusetts.mbtiles'
    
    def run_driver(self):
        
      # Extract .mbtiles and write image bytes to individual files
      ExtractMBTiles().write_to_file(self.mbtile_path)
      
      # Georeference the individually extracted image files
      GeoreferenceImage().assign_coordinates_to_image()
      
      # Stitch georerferenced images to create a raster mosaic
      StitchImage().stitch_tiles()
      

if __name__ == '__main__':
    Driver().run_driver(geojson)
    