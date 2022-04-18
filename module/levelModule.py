from module.sqlManager import SQLManager
from module.toolModule import ToolModule
from module.table import *

LOG_GROUPS = ["overrideLogLevels", "CamxLogDebug", "CamxLogError", "CamxLogWarning", "CamxLogConfig", "CamxLogInfo", "CamxLogVerbose", "CamxLogCoreCfg"]
OVERRIDE_LOG_MASK = ["Error", "Warning", "Config", "Info", "Dump", "Verbose", "Log", "Core Config"]

class LogMaskSelectionListener(object):
    @abstractmethod
    def onLogGroupSelectionChanged(self, isEmpty):
        pass

class LevelModule(ToolModule):

    def __init__(self):
        super().__init__()
        self.__camxLogMasks = None
        self.__selection = {}
        self.__listener = None

    def SetListener(self, listener):
        self.__listener = listener

    def Update(self):
        self.__camxLogMasks = self.__getMaskFromDb()
        self.__selection = {}
        pass

    def SelectGroup(self, group):
        if len(self.__selection) > 0 and group in self.__selection.keys():
            if self.__listener is not None:
                self.__listener.onLogGroupSelectionChanged(False)
            return False
        self.__selection[group] = []
        if self.__listener is not None:
            self.__listener.onLogGroupSelectionChanged(False)
        return True

    def DropGroup(self, group):
        if len(self.__selection) == 0:
            if self.__listener is not None:
                self.__listener.onLogGroupSelectionChanged(True)
            return False
        if group in self.__selection:
            self.__selection.pop(group)
            if self.__listener is not None:
                self.__listener.onLogGroupSelectionChanged(len(self.__selection) == 0)
            return True
        else:
            if self.__listener is not None:
                self.__listener.onLogGroupSelectionChanged(len(self.__selection) == 0)
            return False

    def SelectMask(self, group, mask):
        if len(self.__selection[group]) > 0 and mask in self.__selection[group]:
            return
        self.__selection[group].append(mask)

    def DropMask(self, group, mask):
        self.__selection[group].remove(mask)
        if self.__selection[group] == None:
            self.__selection[group] = []

    def GetGroups(self):
        return LOG_GROUPS

    def GetMasksForGroup(self, group):
        if group == LOG_GROUPS[0]:
            return OVERRIDE_LOG_MASK
        else:
            if self.__camxLogMasks is None:
                return None
            return self.__camxLogMasks[0]

    def GetSelectedMaskForGroup(self, group):
        return self.__selection[group]

    def GetSelected(self):
        selected = []
        for group in LOG_GROUPS:
            try:
                masks = self.__selection[group]
                selected.append("%s=%#x" % (group, self.__calculate(group == LOG_GROUPS[0], masks)))
            except:
                pass
        return selected

    def GetSelectedGroup(self, text):
        group = text[:text.find("=")]
        return LOG_GROUPS.index(group)

    def SearchMask(self, group, mask):
        if group == LOG_GROUPS[0]:
            try:
                return OVERRIDE_LOG_MASK.index(mask)
            except:
                return -1
        else:
            try:
                return self.__camxLogMasks[0].index(mask)
            except:
                return -1


    def __getMaskFromDb(self):
        info = SQLManager.QueryInfo()
        info.Table = maskTable.Table
        info.Columns = [maskTable.Mask, maskTable.Value]
        cursor = self._qsl_manager.Select(info)
        if cursor is not None:
            masks = []
            values = []
            for row in cursor:
                masks.append(row[0])
                values.append(row[1])
            return masks, values
        return None

    def __calculate(self, isOverride, masks):
        value = 0
        for mask in masks:
            if isOverride:
                maskValue = OVERRIDE_LOG_MASK.index(mask)
            else:
                maskValue = self.__camxLogMasks[1][self.__camxLogMasks[0].index(mask)]
            value |= 1 << maskValue
        return value

