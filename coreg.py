import subprocess
import os

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessingAlgorithm,
                       QgsRasterLayer,
                       QgsProject,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterDefinition,
                       QgsProcessingParameterRasterDestination)


plugin_dir = os.path.dirname(__file__)
VENV = f"{plugin_dir}/xdemvenv/bin/python"
SCRIPT_PATH = f"{plugin_dir}/subprocess/"


class NuutKaab(QgsProcessingAlgorithm):

    def initAlgorithm(self, config = None):

        self.addParameter(
             QgsProcessingParameterRasterLayer(
                'INPUT1',
                self.tr('Ref DEM'),
            )
        )
        self.addParameter(
             QgsProcessingParameterRasterLayer(
                'INPUT2',
                self.tr('Tba DEM'),
            )
        )
        self.addParameter(
            QgsProcessingParameterRasterDestination(
                'OUTPUT',
                self.tr('Output')
            )
        )
        param = QgsProcessingParameterNumber(
                'MAXIT',
                self.tr('Max iterations'),
                minValue = 5,
                maxValue = 20,
                defaultValue = 10
            )
        self.addParameter(param)
        param.setFlags(param.flags() | QgsProcessingParameterDefinition.FlagAdvanced)


    def processAlgorithm(self, parameters, context, feedback):

        script = f"{SCRIPT_PATH}sub_nuthkaab.py"
        
        ref_layer = self.parameterAsRasterLayer(
            parameters,
            'INPUT1',
            context)
        ref_path = ref_layer.source()

        tba_layer = self.parameterAsRasterLayer(
            parameters,
            'INPUT2',
            context)
        tba_path = tba_layer.source()
        
        output = self.parameterAsFileOutput(
            parameters,
            'OUTPUT',
            context)
        
        maxit = self.parameterAsString(
            parameters,
            'MAXIT',
            context)

        subprocess.run([VENV, script, ref_path, tba_path, output, maxit], check=True)

        layer = QgsRasterLayer(output, 'Nuth Kaab Coregistration')
        QgsProject.instance().addMapLayer(layer)

        return {'OUTPUT' : output}

    def name(self):
        return 'Nuth Kaab'

    def displayName(self):
        return self.tr(self.name())

    def group(self):
        return self.tr(self.groupId())

    def groupId(self):
        return 'Coregistration'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return NuutKaab()
