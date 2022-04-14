from utils.defines import *
from utils.Utils import *

class LogLevelParser(object):
    def __init__(self):
        self.__mask = {}
        pass

    def Parse(self, str):
        self.__mask = {}
        lines = str.rsplit("\n")
        for line in lines:
            lineEnd = line.find(";")
            if lineEnd > 0:
                define = line[:lineEnd]
                # 1. find assignment
                # [DEF, VAL]
                # we may have a case that xxx = xxx, so that we will get
                # [DEF, DEFINED_VAR]
                l_def = define.rsplit("=")
                # 2. parse definition
                l_define = l_def[0].rsplit(" ")
                definition = l_define[3].replace(" ", "")
                # 3. parse value
                if not l_def[1].find("CamxLogGroup") == -1:
                    # we are in special case
                    var = l_def[1][l_def[1].find("CamxLogGroup"):]
                    if var.find(" "):
                        var = var.replace(" ", "")
                    self.__mask[definition] = self.__mask[var]
                else:
                    s_val = l_def[1][l_def[1].find("<<") + 2:]
                    s_val = s_val.replace(" ", "")
                    if s_val == "":
                        return ERROR_CODE_INVALID_PARAM
                    val = ""
                    for char in s_val:
                        if char.isdigit():
                            val += char
                    self.__mask[definition] = val

            elif line == "":
                continue
            else:
                return ERROR_CODE_INVALID_PARAM

        IF_Print(self.__mask)
        # 4. store the result into db