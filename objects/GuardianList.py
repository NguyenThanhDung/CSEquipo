import json
from objects.Guardian import Guardian
from objects.SimplifiedGuardian import SimplifiedGuardian

class GuardianList:

    def __init__(self, fileName, isSimplified):
        self.guardians = self.Load(fileName, isSimplified)

    def Load(self, fileName, isSimplified):
        with open(fileName) as fileData:
            jsonData = json.load(fileData)
        guardians = []
        
        if isSimplified:
            for guarSon in jsonData["GuardianList"]:
                guardian = SimplifiedGuardian(guarSon["ID"], guarSon["Name"], guarSon["Direction"], guarSon["Base stars"], guarSon["Current stars"], 
                guarSon["Level"], guarSon["Status"], guarSon["Prior Statistic"], guarSon["Note"])
                guardians.append(guardian)
        else:
            for guarSon in jsonData["GuardianList"]:
                guardian = Guardian(guarSon["ID"], guarSon["Guardian"], guarSon["Base ATK"], guarSon["Base DEF"], 
                guarSon["Base Pincer"], guarSon["Base HP"], guarSon["Base CRT Rate"], guarSon["Base CRT DMG"], 
                guarSon["Base ACC"], guarSon["Base RES"], guarSon["Collection Effect ATK"], guarSon["Collection Effect DEF"],
                guarSon["Collection Effect Pincer ATK"], guarSon["Collection Effect HP"], guarSon["Collection Effect CRT Rate"],
                guarSon["Collection Effect CRT DMG"], guarSon["Collection Effect ACC"], guarSon["Collection Effect RES"], guarSon["Prior Statistic"])
                guardians.append(guardian)
        return guardians

    def GetGuardianAt(self, index):
        return self.guardians[index]
    
    def GetGuardianById(self, id):
        for guardian in self.guardians:
            if guardian.id == id:
                return guardian

    def ToString(self):
        thisString = "GUARDIAN LIST:\n\n"
        for guardian in self.guardians:
            thisString += guardian.ToString() + "\n"
        return thisString