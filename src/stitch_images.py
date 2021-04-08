import os
import gdal
import logging
from pathlib import Path
from helper_methods import HelperMethods


class StitchImage(object):
    
    
    def __init__(self):
        self.src_path = 'GeoreferencedImages/13/'
        self.dest_path = '../data/'
        self.vrt_path = 'VRTFiles/'
        self.img_format = 'GTIFF'
    
    
    def stitch_tiles(self):
        """
        Stitch the georeferenced images to create a raster mosaic for the entire state.
        
        """
        
        l = []
    
        for f in os.listdir(self.src_path):
            l.append(os.path.join(self.src_path, f))
        
        vrt_path = os.path.join(self.vrt_path, 'mosaic.vrt')
        HelperMethods().safeMakeDir(self.vrt_path)
        vrt = gdal.BuildVRT(vrt_path, l)
        
        result = os.path.join(self.dest_path, 'mosaic.tif')
        gdal.Translate(result, vrt, format=self.img_format)
        
        logging.info('------------Stitching Task Complete------------')
