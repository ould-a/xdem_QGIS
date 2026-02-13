import subprocess
import os

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessingAlgorithm,
                       QgsRasterLayer,
                       QgsProject,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterEnum,
                       QgsProcessingParameterRasterDestination,
                       QgsProcessingParameterDefinition,)
from .xdem_config import (PLUGINDIR,
                         VENVNAME,
                         VENVFOLDER,
                         SUBPRCSFOLD,
                         XDEMPY)

class Slope(QgsProcessingAlgorithm):

    def initAlgorithm(self, config = None):

        self.addParameter(
             QgsProcessingParameterRasterLayer(
                'INPUT',
                self.tr('Input DEM'),
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                'OUTPUT',
                self.tr('Output Slope')
            )
        )
        param = QgsProcessingParameterEnum(
                'METHOD',
                self.tr('Method'),
                options=['Florinsky', 'ZevenbergThorne','Horn'], 
                defaultValue='Florinsky',
                usesStaticStrings=True
            )
        self.addParameter(param)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)


    def processAlgorithm(self, parameters, context, feedback):
        
        script = f"{SCRIPT_PATH}sub_slope.py"
        
        dem_layer = self.parameterAsRasterLayer(
            parameters,
            'INPUT',
            context)
        dem_path = dem_layer.source()
        
        output = self.parameterAsFileOutput(
            parameters,
            'OUTPUT',
            context)
        
        method = self.parameterAsString(
            parameters, 
            "METHOD", 
            context)

        #subprocess.run([VENV, script, dem_path, output, method], check=True)

        def slope (in_path, out_path, method,):

            dem = xdem.DEM(in_path)

            slope = dem.slope(surface_fit = method, degrees = True)

            slope.save(out_path)

            return out_path
        
        slope(dem_path, output, method)

        layer = QgsRasterLayer(output, 'slope')
        QgsProject.instance().addMapLayer(layer)

        return {'OUTPUT' : output}

    def name(self):
        return 'Slope'

    def displayName(self):
        return self.tr(self.name())

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return 'Terrain attributes'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return Slope()
