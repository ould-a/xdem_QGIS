import xdem
import sys

def slope (in_path, out_path, method,):

    dem = xdem.DEM(in_path)

    slope = dem.slope(surface_fit = method, degrees = True)

    slope.save(out_path)

    return out_path

qgis_in = sys.argv[1]
qgis_out = sys.argv[2]
qgis_method = sys.argv[3]

slope(qgis_in, qgis_out, qgis_method)