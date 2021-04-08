import os
import geopandas as gpd
import rasterio
import pickle
import json
import pycrs
import shapely.wkt
from osgeo import gdal
from rasterio.mask import mask
from psycopg2.extras import RealDictCursor
from shapely.geometry import mapping, shape, Point, MultiPolygon, Polygon
from shapely.geometry import box
from fiona.crs import from_epsg
from helper_methods import HelperMethods


class ClipRaster(object):
    
    def __init__(self):
        self.stitched_file_path = '../data/mosaic.tif'
    
    
    def clip_aoi(self, geojson, output_file_name):
        
        stitched_file = rasterio.open(self.stitched_file_path)
        
        # epsg_code = int(stitched_file.crs.data['init'][5:])
        
        coordinates = geojson['features'][0]['geometry']
        
        # Clip the raster with Polygon
        out_img, out_transform = mask(dataset=stitched_file, shapes=[coordinates], crop=True)
        
        # Copy the metadata
        out_meta = stitched_file.meta.copy()
        
        out_meta.update({"driver": "GTiff",
                "height": out_img.shape[1],
                "width": out_img.shape[2],
                "transform": out_transform,
                "crs": pycrs.parse.from_epsg_code('3857').to_proj4()}
                        )
        
        HelperMethods().setDir('ClippedFiles')
        
        with rasterio.open('test' + '_clip.tif', "w", **out_meta) as dest:
            dest.write(out_img)
        
        # clip_file = output_file_name + '_clip.tif'
        # os.chdir('..')
        
        # return clip_file
        
    def getFeatures(self, gdf):
        """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
        
        return [json.loads(gdf.to_json())['features'][0]['geometry']]