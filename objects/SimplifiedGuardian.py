from objects.Defines import EquipmentType
from objects.Defines import GuardianDirection


class SimplifiedGuardian:
    def __init__(self, id, name, direction, baseStars, currentStars, level,
                 status, priorityStatistic, note):
        self.id = int(id)
        self.name = name
        self.direction = direction
        self.baseStars = baseStars
        self.currentStars = currentStars
        self.level = level
        self.status = status
        self.priorityStatistic = priorityStatistic
        self.note = note
        self.equipments = {
            EquipmentType.Weapon: 0,
            EquipmentType.Armor: 0,
            EquipmentType.Shield: 0,
            EquipmentType.Gloves: 0,
            EquipmentType.Necklace: 0,
            EquipmentType.Ring: 0
        }

    def ToString(self):
        text = "Guardian #" + str(self.id) + ": " + str(self.name).ljust(10) + "| "
        for equipmentID in self.equipments.values():
            text += str(equipmentID).rjust(3)
        text += "\n"
        return text
