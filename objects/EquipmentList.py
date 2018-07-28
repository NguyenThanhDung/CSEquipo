import json
from Equipment import Equipment

class EquipmentList:

    def __init__(self, fileName):
        self.equipments = self.Load(fileName)

    def Load(self, fileName):
        with open(fileName) as fileData:
            jsonData = json.load(fileData)
        equipments = []
        for quipSon in jsonData["Equipments"]:
            equipment = Equipment(quipSon["ID"], quipSon["Type"], quipSon["ATK %"], quipSon["ATK +"], quipSon["DEF %"], quipSon["DEF +"], quipSon["Pincer ATK %"], quipSon["Pincer ATK +"], quipSon["HP %"], quipSon["HP +"], quipSon["CRT Rate"], quipSon["CRT DMG"], quipSon["ACC"], quipSon["RES"], quipSon["Set"], quipSon["Stars"], quipSon["+"])
            equipments.append(equipment)
        return equipments
    
    def GetEquipmentAt(self, index):
        return self.equipments[index]
    
    def GetEquipmentById(self, id):
        for equipment in self.equipments:
            if equipment.id == id:
                return equipment
    
    def ToString(self):
        thisString = "EQUIPMENT LIST:\n\n"
        for equipment in self.equipments:
            thisString += equipment.ToString() + "\n"
        return thisString