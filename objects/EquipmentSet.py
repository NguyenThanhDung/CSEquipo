
class EquipmentSet:

    def __init__(self, weapon, armor, shield, gloves, necklace, ring):
        self.weapon = weapon
        self.armor = armor
        self.shield = shield
        self.gloves = gloves
        self.necklace = necklace
        self.ring = ring

    def ToString(self):
        return "(" + str(self.weapon.id).rjust(3) + ","  \
            + str(self.armor.id).rjust(3) + ","          \
            + str(self.shield.id).rjust(3) + ","         \
            + str(self.gloves.id).rjust(3) + ","         \
            + str(self.necklace.id).rjust(3) + ","       \
            + str(self.ring.id).rjust(3) + ","