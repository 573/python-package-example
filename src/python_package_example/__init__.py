# A simple "gis_capabilities" module as a packaging example for python apps.

import osgeo.ogr
import pyproj
import os
this_dir, this_filename = os.path.split(__file__)
GIS_DATA_PATH = os.path.join(this_dir, "data", "tl_2009_us_state.shp")

# {{{ see p. 35 in EPP by Tarek Zadie
def _treatment(pos, element):
     return '%d: %s' % (pos, element)

def base_run():
    seq = ["one", "two", "three"]
    return [_treatment(i, el) for i, el in enumerate(seq)]
# }}}

def base_command():
    print "res: %s." % base_run()

def osgeogo():
    shapefile = osgeo.ogr.Open(GIS_DATA_PATH)
    layer = shapefile.GetLayer(0)
    feature = layer.GetFeature(2)
    print "Feature 2 has the following attributes:"
    print
    attributes = feature.items()
    for key,value in attributes.items():
        print "  %s = %s" % (key, value)
        print
    geometry = feature.GetGeometryRef()
    geometryName = geometry.GetGeometryName()
    return geometryName

def osgeo_run():
    print "Feature's geometry data consists of a %s." % osgeogo()

def pyprojgo():
    UTM_X = 565718.523517
    UTM_Y = 3980998.9244
    srcProj = pyproj.Proj(proj="utm", zone="11",   
    ellps="clrk66", units="m")
    dstProj = pyproj.Proj(proj='longlat', ellps='WGS84',  
     datum='WGS84')
    long,lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
    return (UTM_X, UTM_Y, lat, long)

def pyproj_run():
    print "UTM zone 17 coordinate (%0.4f, %0.4f) = %0.4f, %0.4f." % pyprojgo()
