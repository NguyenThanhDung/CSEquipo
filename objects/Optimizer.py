from objects.Defines import EquipmentType

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


    def GetCombinedStatisticValue(self, priorityStatistic, equipmentSet):
        # TODO: Implement
        return None


    def FindBestEquipmentSet(self, equipmentsWithType, priorityStatistic):
        maxStatisticValue = 0
        bestEquipmentSet = None
        for weapon in equipmentsWithType[EquipmentType.Weapon]:
            for armor in equipmentsWithType[EquipmentType.Armor]:
                for shield in equipmentsWithType[EquipmentType.Shield]:
                    for gloves in equipmentsWithType[EquipmentType.Gloves]:
                        for necklace in equipmentsWithType[EquipmentType.Necklace]:
                            for ring in equipmentsWithType[EquipmentType.Ring]:
                                currentEquipmentSet = [weapon, armor, shield, gloves, necklace, ring]
                                currentStatisticValue = GetCombinedStatisticValue(priorityStatistic, currentEquipmentSet)
                                if maxStatisticValue < currentStatisticValue:
                                    print("Found max set of " + priorityStatistic + " with value " + str(currentStatisticValue))
                                    maxStatisticValue = currentStatisticValue
                                    bestEquipmentSet = currentEquipmentSet
        return bestEquipmentSet


    def RemoveEquipmentSet(self, equipmentsWithType, equipmentSet):
        for equipmentType in EquipmentType:
            equipmentsWithType[equipmentType].remove(equipmentSet[equipmentType])
        return None


    def Optimize(guardians, equipments):
        equipmentsWithType = GetEquipmentsByType(equipments)
        for guardian in guardians:
            print("Finding best equipment set for #" + guardian.id + " " + guardian.name)
            bestEquipmentSet = FindBestEquipmentSet(equipmentsWithType, guardian.priorityStatistic)
            guardian.Equipment(bestEquipmentSet)
            equipmentsWithType = RemoveEquipmentSet(equipmentsWithType, bestEquipmentSet)
        return guardians