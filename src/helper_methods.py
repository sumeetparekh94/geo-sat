import os
import time
from pytz import timezone
from datetime import datetime
from random import randint

class HelperMethods(object):
    
    def safeMakeDir(self, d):
        """ 
        Check if directory already exists before creating a new directory.

        Args:
            d: directory name
        """
        if os.path.exists(d):
            return
        os.makedirs(d)
    
    
    def setDir(self, d):
        """
        Set Directory to the newly created directory.

        Args:
            d: directory name
        """
        self.safeMakeDir(d)
        os.chdir(d)
    
    def random_with_N_digits(self, n):
        
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
        
    def generate_unique_id_file(self):
        
        eastern = timezone('US/Eastern')
        
        loc_dt = datetime.now(eastern)
        
        year = loc_dt.strftime('%Y')
        month = loc_dt.strftime('%m')
        day = loc_dt.strftime("%d")
        hour = loc_dt.strftime("%H")
        minute = loc_dt.strftime("%M")
        second = loc_dt.strftime("%S")
        
        random_num = self.random_with_N_digits(10)
        
        unique_id = year + month + day + '_' + hour + minute + second + '_' + str(random_num)
        
        output_file_name = year + month + day + '_' + hour + minute + second + '_' + str(random_num) + '_' + 'omt' 
      
        return output_file_name