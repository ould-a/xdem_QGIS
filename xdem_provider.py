from qgis.core import QgsProcessingProvider

from .terrain_attributes import (Slope,)
from .coreg import (NuutKaab,)


class XDemProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

    def unload(self):
        pass

    def loadAlgorithms(self):
        self.addAlgorithm(Slope())
        self.addAlgorithm(NuutKaab())

    def id(self):
        return 'XDEM'

    def name(self):
        return self.tr('xDEM')

    def icon(self):
        return QgsProcessingProvider.icon(self)

    def longName(self):
        return self.name()
