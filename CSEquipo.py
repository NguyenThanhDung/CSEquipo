from objects.Defines import EquipmentType
from objects.Defines import StatisticType
from objects.EquipmentList import EquipmentList
from objects.GuardianList import GuardianList
from objects.StatPrioMap import StatPrioMap
from objects.EquipmentSet import EquipmentSet
from objects.Guardian import Guardian

def main():
    equipmentList = EquipmentList("data/equipments.json")
    guardianList = GuardianList("data/guardians.json")
    statPrioMap = StatPrioMap("data/stat_prio_map.json")

    for statPrio in statPrioMap.statPrioMap:
        guardian = guardianList.GetGuardianById(statPrio.guardianID)
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
    print("Final result:")
    for guardian in guardianList.guardians:
        print(guardian.ToString())

if __name__ == "__main__":
    main()
