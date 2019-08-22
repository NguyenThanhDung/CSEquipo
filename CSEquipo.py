from objects.Defines import EquipmentType
from objects.Defines import StatisticType
from objects.EquipmentList import EquipmentList
from objects.GuardianList import GuardianList
from objects.StatPrioMap import StatPrioMap
from objects.EquipmentSet import EquipmentSet
from objects.Guardian import Guardian


def Optimize1(guardianList, equipmentList):
    for guardian in guardianList:
        print("Find best equipment for " + guardian.name + ":")
        print("Generate equipment sets")
        equipmentSets = equipmentList.GenerateEquipmentSet()
        maxStatValue = 0
        maxEquipmentSet = None
        for equipmentSet in equipmentSets:
            print("Try set " + equipmentSet.ToString())
            guardian.UnequipAll()
            guardian.Equip(equipmentSet.weapon)
            guardian.Equip(equipmentSet.armor)
            guardian.Equip(equipmentSet.shield)
            guardian.Equip(equipmentSet.gloves)
            guardian.Equip(equipmentSet.necklace)
            guardian.Equip(equipmentSet.ring)
            finalStats = guardian.CalculateFinalStats()
            desireStat = statPrioMap.GetDesireStat(guardian)
            if desireStat == StatisticType.Attack:
                averageAttack = Guardian.GetAverageAttack(finalStats)
                print("Desire stat value: " + str(averageAttack))
                if averageAttack > maxStatValue:
                    maxStatValue = averageAttack
                    maxEquipmentSet = equipmentSet
            else:
                print("Desire stat value: " + str(finalStats[desireStat]))
                if finalStats[desireStat] > maxStatValue:
                    maxStatValue = finalStats[desireStat]
                    maxEquipmentSet = equipmentSet
            print("Current best stat: " + str(maxStatValue))
        guardian.UnequipAll()
        guardian.Equip(maxEquipmentSet.weapon)
        guardian.Equip(maxEquipmentSet.armor)
        guardian.Equip(maxEquipmentSet.shield)
        guardian.Equip(maxEquipmentSet.gloves)
        guardian.Equip(maxEquipmentSet.necklace)
        guardian.Equip(maxEquipmentSet.ring)
        equipmentList.Remove(maxEquipmentSet.weapon)
        equipmentList.Remove(maxEquipmentSet.armor)
        equipmentList.Remove(maxEquipmentSet.shield)
        equipmentList.Remove(maxEquipmentSet.gloves)
        equipmentList.Remove(maxEquipmentSet.necklace)
        equipmentList.Remove(maxEquipmentSet.ring)
    return None


def GetEquipmentsByType(equipments):
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


def GetCombinedStatisticValue(priorityStatistic, equipmentSet):
    # TODO: Implement
    return None


def FindBestEquipmentSet(equipmentsWithType, priorityStatistic):
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


def RemoveEquipmentSet(equipmentsWithType, equipmentSet):
    for equipmentType in EquipmentType:
        equipmentsWithType[equipmentType].remove(equipmentSet[equipmentType])
    return None


def Optimize2(guardians, equipments):
    equipmentsWithType = GetEquipmentsByType(equipments)
    for guardian in guardians:
        print("Finding best equipment set for #" + guardian.id + " " + guardian.name)
        bestEquipmentSet = FindBestEquipmentSet(equipmentsWithType, guardian.priorityStatistic)
        guardian.Equipment(bestEquipmentSet)
        equipmentsWithType = RemoveEquipmentSet(equipmentsWithType, bestEquipmentSet)
    return None


def main():
    equipmentList = EquipmentList("data/equipments.json")
    guardianList = GuardianList("data/simplifiedGuardians.json", True)
    Optimize2(guardianList.guardians, equipmentList.equipments)
    return None

if __name__ == "__main__":
    main()
