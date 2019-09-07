import datetime
from objects.Defines import EquipmentType
from objects.Defines import StatisticType


class Optimizer:

    def __init__(self):
        self.startTime = None
        self.optimizeTime = None

    def RemoveEquipmentSet(self, equipments, equipmentSet):
        for equipmentType in EquipmentType:
            equipments[equipmentType].remove(
                equipmentSet[equipmentType])
        return equipments

    def Ordering(self, equipments, guardian):
        for equipmentType in EquipmentType:
            for equipment in equipments[equipmentType]:
                guardian.EquipSingle(equipment)
                score = guardian.GetPriorityStatisticValue()
                equipment.score = score
            for i in range(len(equipments[equipmentType])):
                for j in range(i+1, len(equipments[equipmentType])):
                    if equipments[equipmentType][i].score < equipments[equipmentType][j].score:
                        temp = equipments[equipmentType][j]
                        equipments[equipmentType][j] = equipments[equipmentType][i]
                        equipments[equipmentType][i] = temp
        return equipments

    def Optimize(self, guardians, equipments):
        self.startTime = datetime.datetime.now()
        for guardian in guardians:
            print("Finding best equipment set for #" +
                  str(guardian.id) + " " + guardian.name)
            equipments = self.Ordering(equipments, guardian)
            bestEquipmentSet = [equipments[EquipmentType.Weapon][0], equipments[EquipmentType.Armor][0], equipments[EquipmentType.Shield]
                                [0], equipments[EquipmentType.Gloves][0], equipments[EquipmentType.Necklace][0], equipments[EquipmentType.Ring][0]]
            guardian.EquipWholeSet(bestEquipmentSet)
            equipments = self.RemoveEquipmentSet(
                equipments, guardian.GetEquipments())
        now = datetime.datetime.now()
        self.optimizeTime = now - self.startTime
        return guardians

    def GetOptimizeTime(self):
        return str(self.optimizeTime)
