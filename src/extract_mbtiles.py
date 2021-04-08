import sys
import sqlite3
import pickle
import os
import pandas as pd
sys.path.insert(0, 'utils/helper_methods.py')

class ExtractMBTiles(object):
    
    
    def write_to_file(self, tile_path):
        
        connection = sqlite3.connect(tile_path)
        cursor = connection.cursor()
        query = 'SELECT * from tiles'
        cursor.execute(query)
        # Iterate through the mbtiles data
        for row in cursor:
            print(row)
            tzoom = row[0]
            xtile = row[1]
            ytile = row[2]
            if tzoom > 4:

                HelperMethods().setDir('OMTTiles')
                exit()
                # self.setDir(state)
                # self.setDir(str(tzoom))
                # self.setDir(str(xtile))

        #         with open(str(ytile) + '.png', 'wb') as output_file:
        #             output_file = open(str(ytile) + '.png', 'wb')
        #             output_file.write(row[3])
        #             output_file.close()
                    
        #         os.chdir('..')
        #         os.chdir('..')
        #         os.chdir('..')
        #         os.chdir('..')
    
        # print('------------Writing Image to Individual Files for ' + state + ' Complete------------')
        
    
if __name__ == '__main__':
    ExtractMBTiles().write_to_file('../data/maptiler-satellite-2017-11-02-us_massachusetts.mbtiles')