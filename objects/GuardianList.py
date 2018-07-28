import json
from Guardian import Guardian

class GuardianList:

    def __init__(self, fileName):
        self.guardians = self.Load(fileName)

    def Load(self, fileName):
        with open(fileName) as fileData:
            jsonData = json.load(fileData)
        guardians = []
        id = 0
        for guarSon in jsonData["GuardianList"]:
            guardian = Guardian(id, guarSon["Guardian"], guarSon["Base ATK"], guarSon["Base DEF"], 
            guarSon["Base Pincer"], guarSon["Base HP"], guarSon["Base CRT Rate"], guarSon["Base CRT DMG"], 
            guarSon["Base ACC"], guarSon["Base RES"], guarSon["Collection Effect ATK"], guarSon["Collection Effect DEF"],
            guarSon["Collection Effect Pincer ATK"], guarSon["Collection Effect HP"], guarSon["Collection Effect CRT Rate"],
            guarSon["Collection Effect CRT DMG"], guarSon["Collection Effect ACC"], guarSon["Collection Effect RES"])
            guardians.append(guardian)
            id += 1
        return guardians

    def GetGuardianAt(self, index):
        return self.guardians[index]

    def ToString(self):
        thisString = "GUARDIAN LIST:\n\n"
        for guardian in self.guardians:
            thisString += guardian.ToString() + "\n"
        return thisString