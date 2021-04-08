import os


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