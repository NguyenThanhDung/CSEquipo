from objects.Defines import EquipmentType
from objects.Defines import StatisticType

class Optimizer:

    def GetEquipmentsByType(self, equipments):
        indexes = {}
        indexes[EquipmentType.Weapon] = []
        indexes[EquipmentType.Armor] = []
        indexes[EquipmentType.Shield] = []
        indexes[EquipmentType.Gloves] = []
        indexes[EquipmentType.Necklace] = []
        indexes[EquipmentType.Ring] = []
        for equipment in equipments:
            equipmentType = equipment.type
            indexes[equipmentType].append(equipment)
        return indexes


    def RemoveEquipmentSet(self, equipmentsWithType, equipmentSet):
        for equipmentType in EquipmentType:
            equipmentsWithType[equipmentType].remove(equipmentSet[equipmentType])
        return equipmentsWithType


    def Optimize(self, guardians, equipments):
        equipmentsWithType = self.GetEquipmentsByType(equipments)
        for guardian in guardians:
            print("Finding best equipment set for #" + str(guardian.id) + " " + guardian.name)
            maxStatisticValue = 0
            for weapon in equipmentsWithType[EquipmentType.Weapon]:
                for armor in equipmentsWithType[EquipmentType.Armor]:
                    for shield in equipmentsWithType[EquipmentType.Shield]:
                        for gloves in equipmentsWithType[EquipmentType.Gloves]:
                            for necklace in equipmentsWithType[EquipmentType.Necklace]:
                                for ring in equipmentsWithType[EquipmentType.Ring]:
                                    currentEquipmentSet = [weapon, armor, shield, gloves, necklace, ring]
                                    guardian.Equip(currentEquipmentSet)
                                    currentStatisticValue = guardian.GetPriorityStatisticValue()
                                    if maxStatisticValue < currentStatisticValue:
                                        print("Found max set with value " + str(currentStatisticValue))
                                        maxStatisticValue = currentStatisticValue
            equipmentsWithType = self.RemoveEquipmentSet(equipmentsWithType, guardian.GetEquipments())
        return guardians