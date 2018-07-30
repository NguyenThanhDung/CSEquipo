import json
from Defines import EquipmentType
from Equipment import Equipment
from EquipmentSet import EquipmentSet

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

    def GenerateEquipmentSet(self):
        weapons = [None]
        armors = [None]
        shields = [None]
        glovesList = [None]
        necklaces = [None]
        rings = [None]
        for equipment in self.equipments:
            if equipment.type == EquipmentType.Weapon:
                weapons.append(equipment)
            elif equipment.type == EquipmentType.Armor:
                armors.append(equipment)
            elif equipment.type == EquipmentType.Shield:
                shields.append(equipment)
            elif equipment.type == EquipmentType.Gloves:
                glovesList.append(equipment)
            elif equipment.type == EquipmentType.Necklace:
                necklaces.append(equipment)
            elif equipment.type == EquipmentType.Ring:
                rings.append(equipment)
        equipmentSets = []
        for weapon in weapons:
            for armor in armors:
                for shield in shields:
                    for gloves in glovesList:
                        for necklace in necklaces:
                            for ring in rings:
                                equipmentSet = EquipmentSet(weapon, armor, shield, gloves, necklace, ring)
                                equipmentSets.append(equipmentSet)
        return equipmentSets

    def Remove(self, equipment):
        if equipment is not None:
            self.equipments.remove(equipment)
    
    def ToString(self):
        thisString = "EQUIPMENT LIST:\n\n"
        for equipment in self.equipments:
            thisString += equipment.ToString() + "\n"
        return thisString