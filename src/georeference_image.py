class GeoreferenceImage(object):
    
    
    def spherical_mercator_lon_lat(self, px, zoom):
        """
        This function converts screen pixel to longitude and latitude values.

        Args:
            px (list): [x,y] array of geographic coordinates
            zoom (float): zoom level

        Returns:
            [lon,lat]: [longitude,latitude]
        """
        
        R2D = 180 / math.pi
        size = 256 * math.pow(2, zoom)
        bc = (size / 360)
        cc = (size / (2 * math.pi))
        zc = size / 2
        g = (px[1] - zc) / -cc
        lon = (px[0] - zc) / bc
        lat = R2D * (2 * math.atan(math.exp(g)) - 0.5 * math.pi)
        return [lon, lat]
    
    
    def spherical_mercator_bbox(self, x, y, zoom):
        """This function converts xyz value to bounding box of the form [w,s,e,n]

        Args:
            x (float): longitude
            y (float): latitude
            zoom (float): zoom level

        Returns:
            bbox: bounding box coordinates
        """

        # Convert xyz into bbox with srs WGS84
        tsize = 256
        y = (math.pow(2, zoom) - 1) - y

        # compute lower left coordinates
        ll = [x * tsize, (y + 1) * tsize]

        # compute upper right coordinates
        ur = [(x + 1) * tsize, y * tsize]
        
        box1 = self.spherical_mercator_lon_lat(ll, zoom)
        box2 = self.spherical_mercator_lon_lat(ur, zoom)
        bbox = [box1[0], box2[1], box2[0], box1[1]]
        return bbox