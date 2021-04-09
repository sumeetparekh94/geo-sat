# Geo-Sat
Provides satellite imagery (using OpenMapTiles data) for a randomly shaped polygon. This currently supports satellite imagery for a polygon drawn anywhere in the state of Massachusetts and has the potential to scale across the country.

## Overview
Our knowledge of Earth has been revolutionized by satellite imagery. Obtaining satellite imagery was very expensive back in the day, but the last decade of innovation has made satellite imagery more accessible. AI has played a big role in making sure that data from space is useful for businesses and governments.

There are literally infinite amount of things you can now do with satellite imagery, be it to use for your own geographical analysis or some sort of stastical analysis using programming languages like R/Python or any other language. Most satellite imagery providers provide satellite imagery in the form of scenes which cover a huge amount of area. As a user, if you want satellite imagery for a specific area of interest, it is quite a task to obtain it. The goal of Geo-Sat is to solve that problem and provide satellite imagery for areas that interest the user by simply passing a geojson file.


## Data
Geo-Sat is currently providing satellite imagery using [OpenMapTiles](https://openmaptiles.org/). OpenMapTiles has a spatial resolution of _20m/px_ with a maximum zoom level of _13_ and provides satellite imagery extracts in the form of _.mbtiles_ file. When extracted, the images are square tiles of _256x256 px_ and are _.png_ file format.


## Initial Set Up

* You can clone the repository by using the following command

```
$ git clone https://github.com/sumeetparekh94/geo-sat.git
```

or download and extract the ZIP file from above and open it in an editor like VS Code or PyCharm.

* Installation of Anaconda is not a must but installing GDAL with Anaconda is an easier approach which is why the installation of Anaconda is required.

  * Step by step guide for [installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
  * Step by step guide for [installing on Linux](https://docs.anaconda.com/anaconda/install/linux/)
  * Step by step guide for [installing on Windows](https://docs.anaconda.com/anaconda/install/windows/)
   
* Steps to create a conda virtual environment and to install GDAL can be found [here](https://chrieke.medium.com/howto-install-python-for-geospatial-applications-1dbc82433c05). Setting up a new virtual environment is important because the installation of GDAL can be quite a hassle.


## Run Geo-Sat and obtain satellite imagery

#### Description of drivers

Now that the intial set up is complete based on the steps above, we can move on to the running portion.

The _src_ folder consists of two drivers namely _pre_processing_driver.py_ and _geo_sat_driver.py_. Each of the drivers perform different tasks.

1. pre_processing_driver:

   * Reads and extracts the mbtiles file for Massachusetts which contain the raw square tiles
   * Geo-references the extracted square tiles by assigning geographical coordinates to the images and converting to _.tif_ file
   * Stitch all the geo-referenced image files to create a raster mosaic of the entire state

   Note: The pre_processing_driver needs to only be run once to generate the geo-referenced images and the stitched file.

2. geo_sat_driver:

   * Generate a unique id and a unique file name for the output image
   * Clip raster or area of interest by passing geojson as argument
   * Translate and crop image to .png file, crop/remove black background and store in the output directory


#### Passing Geojson file 

To run the _geo_sat_driver_, you need to have a geojson file in the data directory for which you want to obtain satellite imagery. You can create random geojson polygons using the tool [geojson.io](https://geojson.io/). 

* Zoom into the state of Massachusetts or use the search option to search for a specific area in Massachusetts
* Using the polygon draw tool on the right top corner of the map, you can draw a random polygon (make sure that the first and last points are the same)
* Save as _GeoJSON_ file by choosing the _Save_ option on the left top corner of the map
* Copy/Cut the saved .geojson file and paste it in the data directory of the project
* Set name for _self.geojson_file_name_ as the file name of the downloaded geojson present at the beginning of the geo_sat_driver.py file

You can also pass in any other .geojson files that you may have and apply the last two steps from above.

#### Commands to run the two drivers

Open up a terminal and using _cd src_ command change directory to _src_.

Run pre_processing_driver:

```
$ python3 pre_processing_driver.py
```

Run geo_sat_driver

```
$ python3 geo_sat_driver.py
```

#### Output

On running the _pre_processing_driver_, the following files get generated in the _src_ directory:

* Directory with the name _"OMTTiles"_ containing the extracted image files from the .mbtiles file
* Directory with the name _"GeoreferencedImages"_ containing the geo-referenced images
* Directory with the name _"VRTFiles_ containing the virtual raster data file while stitching the geo-referenced images
* Stitched raster mosaic file with the name _mosaic.tif_

On running the _geo_sat_driver_, a directory have a unique_id as its name gest generated in the _output_ directory and it has the following files:
* .tif file (This is so that it can be used for map creation or using softwares like QGIS to use image as a layer)
* .png file with black background
* _raw.png file with transparent backgound (so that it can be overlayed onto the drawn geometry)
* .xml file containing the geospatial metadata
