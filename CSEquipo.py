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
        equipmentSets = equipmentList.GenerateEquipmentSet()
        maxStatValue = 0
        maxEquipmentSet = None
        for equipmentSet in equipmentSets:
            guardian.Equip(equipmentSet.weapon)
            guardian.Equip(equipmentSet.armor)
            guardian.Equip(equipmentSet.shield)
            guardian.Equip(equipmentSet.gloves)
            guardian.Equip(equipmentSet.necklace)
            guardian.Equip(equipmentSet.ring)
            finalStats = guardian.GetFinalStats()
            desireStat = statPrioMap.GetDesireStat(guardian)
            if finalStats[desireStat] > maxStatValue:
                maxStatValue = finalStats[desireStat]
                maxEquipmentSet = equipmentSet
        guardian.Equip(maxEquipmentSet)
        equipmentList.Remove(maxEquipmentSet.weapon)
        equipmentList.Remove(maxEquipmentSet.armor)
        equipmentList.Remove(maxEquipmentSet.shield)
        equipmentList.Remove(maxEquipmentSet.gloves)
        equipmentList.Remove(maxEquipmentSet.necklace)
        equipmentList.Remove(maxEquipmentSet.ring)
        print(guardian.ToString())

if __name__ == "__main__":
    main()
