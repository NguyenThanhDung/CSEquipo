from objects.Defines import EquipmentType
from objects.EquipmentList import EquipmentList
from objects.GuardianList import GuardianList
from objects.StatPrioMap import StatPrioMap
from objects.EquipmentSet import EquipmentSet
from objects.Guardian import Guardian

def main():
    equipmentList = EquipmentList("data/equipments.json")
    guardianList = GuardianList("data/guardians.json")
    statPrioMap = StatPrioMap("data/stat_prio_map.json")

    for guardian in guardianList.guardians:
        print("Find best equipment for " + guardian.name + ":")
        print("Generate equipment sets")
        equipmentSets = equipmentList.GenerateEquipmentSet()
        maxStatValue = 0
        maxEquipmentSet = None
        for equipmentSet in equipmentSets:
            print("Try set " + equipmentSet.ToString())
            guardian.Equip(equipmentSet.weapon)
            guardian.Equip(equipmentSet.armor)
            guardian.Equip(equipmentSet.shield)
            guardian.Equip(equipmentSet.gloves)
            guardian.Equip(equipmentSet.necklace)
            guardian.Equip(equipmentSet.ring)
            finalStats = guardian.GetFinalStats()
            desireStat = statPrioMap.GetDesireStat(guardian)
            print("Desire stat value: " + str(finalStats[desireStat]))
            if finalStats[desireStat] > maxStatValue:
                maxStatValue = finalStats[desireStat]
                maxEquipmentSet = equipmentSet
            print("Current best stat: " + str(maxStatValue))
        guardian.Equip(maxEquipmentSet)
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
