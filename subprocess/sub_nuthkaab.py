import xdem
import sys

def nuthkaab (ref_dem, tba_dem, out_path,maxit):

    ref_dem = xdem.DEM(ref_dem)
    tba_dem = xdem.DEM(tba_dem)

    nuth_kaab = xdem.coreg.NuthKaab(max_iterations=maxit)
    coreg = nuth_kaab.fit_and_apply(ref_dem, tba_dem)
    coreg.save(out_path)
    
    return out_path

qgis_in1 = sys.argv[1]
qgis_in2 = sys.argv[2]
qgis_out = sys.argv[3]
qgis_maxit = sys.argv[4]

nuthkaab(qgis_in1, qgis_in2, qgis_out, int(qgis_maxit))