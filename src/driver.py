import os
import sqlite3
import pickle
import os
import pandas as pd
import logging
from extract_mbtiles import ExtractMBTiles
from georeference_image import GeoreferenceImage


class Driver(object):
    
    def __init__(self):
        self.mbtile_path = '../data/massachusetts.mbtiles'
    
    def run_driver(self):
        
        # Extract .mbtiles and write image bytes to individual files
        ExtractMBTiles().write_to_file(self.mbtile_path)
        
        # Georeference the individually extracted image files
        GeoreferenceImage().assign_coordinates_to_image()
        
        
        

if __name__ == '__main__':
    Driver().run_driver()
    