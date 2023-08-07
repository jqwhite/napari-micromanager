import napari
import numpy as np
from pymmcore_plus import CMMCorePlus, DeviceType
from pymmcore_plus import find_micromanager

micromanager = find_micromanager()

print(f'\n{micromanager}')

mmc = CMMCorePlus.instance()

# stage_dev_list = list(self._mmc.getLoadedDevicesOfType(DeviceType.XYStage))
mmc.loadSystemConfiguration()
# cfg = mmc.events.systemConfigurationLoaded()
microscope = mmc.getSystemState()
print(microscope.getSetting(0))
print(microscope)
stages = mmc.getLoadedDevicesOfType(DeviceType.XYStage)
print(stages)