# Geo-Sat
Provides satellite imagery (using OpenMapTiles data) for a randomly shaped polygon. This currently supports satellite imagery for a polygon drawn anywhere in the state of Massachusetts and has the potential to scale across the country.

## Overview
Our knowledge of Earth has been revolutionized by satellite imagery. Obtaining satellite imagery was very expensive back in the day, but the last decade of innovation has made satellite imagery more accessible. AI has played a big role in making sure that data from space is useful for businesses and governments.

There are literally infinite amount of things you can now do with satellite imagery, be it to use for your own geographical analysis or some sort of stastical analysis using programming languages like R/Python or any other language. Most satellite imagery providers provide satellite imagery in the form of scenes which cover a huge amount of area. As a user if you want satellite imagery for a specific area of interest, it is quite a task to obtain it. The goal of Geo-Sat is to solve that problem and provide satellite imagery for areas that interest the user.


## Data
Geo-Sat is currently providing satellite imagery using OpenMapTiles. OpenMapTiles has a spatial resolution of _20m/px_ with a maximum zoom level of _13_ and provides satellite imagery extracts in the form of _.mbtiles_ file. When extracted, the images are square tiles of _256x256 px_ and are _.png_ file format.


## Set Up

* You can clone the repository by using the following command

```
git clone https://github.com/sumeetparekh94/geo-sat.git
```

or download and extract the ZIP file from above and open it in an editor like VS Code or PyCharm.

* Installation of Anaconda is not a must but installing GDAL with Anaconda is an easier approach which is why the installation of Anaconda is required.

  * Step by step guide for [installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
  * Step by step guide for [installing on Linux](https://docs.anaconda.com/anaconda/install/linux/)
  * Step by step guide for [installing on Windows](https://docs.anaconda.com/anaconda/install/windows/)
   
* Steps to create a conda virtual environment and to install GDAL can be found [here](https://chrieke.medium.com/howto-install-python-for-geospatial-applications-1dbc82433c05).


* 
