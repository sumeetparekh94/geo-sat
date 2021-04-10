import sys
import sqlite3
import pickle
import os
import pandas as pd
import logging
from helper_methods import HelperMethods


class ExtractMBTiles(object):
    
    def __init__(self):
        self.omt_dir_name = 'OMTTiles'
    
    
    def write_to_file(self, tile_path):
        """Method to extract .mbtiles file and write image bytes to individual files(.png).

        Args:
            tile_path (string): path to the .mbtiles file
        """
        
        # Connect to the mbtiles file using sqlite
        connection = sqlite3.connect(tile_path)
        cursor = connection.cursor()
        query = 'SELECT * from tiles'
        cursor.execute(query)
        
        
        # Iterate through the mbtiles data
        for row in cursor:
            
            tzoom = row[0]
            xtile = row[1]
            ytile = row[2]
            
            # Provide best resolution image which would be 13 for OpenMapTiles
            if tzoom == 13:

                HelperMethods().setDir(self.omt_dir_name)
                HelperMethods().setDir(str(tzoom))
                HelperMethods().setDir(str(xtile))

                with open(str(ytile) + '.png', 'wb') as output_file:
                    output_file = open(str(ytile) + '.png', 'wb')
                    output_file.write(row[3])
                    output_file.close()
                
                os.chdir('..')
                os.chdir('..')
                os.chdir('..')
                    
    
        logging.info('------------Writing Image to Individual Files Complete------------')
        
