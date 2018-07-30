import json
import os
from StatPrio import StatPrio

class StatPrioMap:

    def __init__(self, fileName):
        self.statPrioMap = self.Load(fileName)

    def Load(self, fileName):
        filePath = os.path.abspath(fileName)
        with open(filePath) as fileData:
            jsonData = json.load(fileData)
        statPrioMap = []
        for node in jsonData["StatPrioMap"]:
            statPrio = StatPrio(node["Guardian ID"], node["Prio"], node["Stat"])
            statPrioMap.append(statPrio)
        statPrioMap.sort(key=StatPrioMap.GetPriorityOfElement)
        return statPrioMap

    @staticmethod
    def GetPriorityOfElement(element):
        return element.priority

    def GetDesireStat(self, guardian):
        for item in self.statPrioMap:
            if item.guardianID == guardian.id:
                return item.prioStat

    def ToString(self):
        thisString = "STAT PRIO MAP:\n\n"
        for statPrio in self.statPrioMap:
            thisString += statPrio.ToString() + "\n"
        return thisString