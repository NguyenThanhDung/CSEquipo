from objects.Defines import EquipmentType
from objects.EquipmentList import EquipmentList
from objects.GuardianList import GuardianList
from objects.StatPrioMap import StatPrioMap
from objects.EquipmentSet import EquipmentSet

def main():
    equipmentList = EquipmentList("data/equipments.json")
    guardianList = GuardianList("data/guardians.json")
    statPrioMap = StatPrioMap("data/stat_prio_map.json")

    equipmentSets = equipmentList.GenerateEquipmentSet()
    for equipmentSet in equipmentSets:
        print(equipmentSet.ToString())

if __name__ == "__main__":
    main()
