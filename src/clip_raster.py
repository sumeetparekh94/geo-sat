import os
import geopandas as gpd
import rasterio
import pickle
import json
import psycopg2
import pycrs
import shapely.wkt
from osgeo import gdal
from rasterio.mask import mask
from psycopg2.extras import RealDictCursor
from shapely.geometry import mapping, shape, Point, MultiPolygon, Polygon
from shapely.geometry import box
from fiona.crs import from_epsg

class ClipRaster(object):
    
    
    def clip_aoi(self, geojson, output_file_name):
        
        stitched_file = rasterio.open(os.path.join(self.stitched_file_path, output_file_name + '.tif'))
    
        coordinates = geojson['geometry']

        coords = [shape(coordinates)]
        
        # Clip the raster with Polygon
        out_img, out_transform = mask(dataset=stitched_file, shapes=coords, crop=True)
        
        # Copy the metadata
        out_meta = stitched_file.meta.copy()
        # print(out_meta)

        epsg_code = int(stitched_file.crs.data['init'][5:])
        
        out_meta.update({"driver": "GTiff",
                "height": out_img.shape[1],
                "width": out_img.shape[2],
                "transform": out_transform,
                "crs": pycrs.parse.from_epsg_code(epsg_code).to_proj4()}
                        )
        
        self.setDir('ClippedFiles')
        with rasterio.open(output_file_name + '_clip.tif', "w", **out_meta) as dest:
            dest.write(out_img)
        
        clip_file = output_file_name + '_clip.tif'
        os.chdir('..')
        
        return clip_file