from objects.EquipmentList import EquipmentList
from objects.GuardianList import GuardianList
from objects.Defines import EquipmentType

def main():
    equipmentList = EquipmentList("data/equipments.json")
    guardianList = GuardianList("data/guardians.json")

    guardian = guardianList.GetGuardianAt(0)

    equipment = equipmentList.GetEquipmentById(14)
    guardian.Equip(equipment, EquipmentType.Weapon)
    equipment = equipmentList.GetEquipmentById(15)
    guardian.Equip(equipment, EquipmentType.Armor)
    equipment = equipmentList.GetEquipmentById(16)
    guardian.Equip(equipment, EquipmentType.Shield)
    equipment = equipmentList.GetEquipmentById(17)
    guardian.Equip(equipment, EquipmentType.Gloves)
    equipment = equipmentList.GetEquipmentById(18)
    guardian.Equip(equipment, EquipmentType.Necklace)
    equipment = equipmentList.GetEquipmentById(19)
    guardian.Equip(equipment, EquipmentType.Ring)

    print(guardian.ToString())

if __name__ == "__main__":
    main()
