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
    
    def run_geo_sat_driver(self, geojson):
      
      unique_id, output_file_name = HelperMethods().generate_unique_id_file()
      
      # Clip area of interest by passing geojson as argument
      ClipRaster().clip_aoi(geojson, unique_id, output_file_name)
      
      # Translate image into png
      TranslateImage('PNG').translate_image()

if __name__ == '__main__':
    geojson = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              -71.09115600585936,
              42.37858270194822
            ],
            [
              -71.08634948730469,
              42.356514317057886
            ],
            [
              -71.02832794189452,
              42.35930500076174
            ],
            [
              -71.03004455566406,
              42.379850764344134
            ],
            [
              -71.09115600585936,
              42.37858270194822
            ]
          ]
        ]
      }
    }
  ]
}
    Driver().run_geo_sat_driver(geojson)
    