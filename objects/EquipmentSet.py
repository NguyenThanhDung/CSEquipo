
class EquipmentSet:

    def __init__(self, weapon, armor, shield, gloves, necklace, ring):
        self.weapon = weapon
        self.armor = armor
        self.shield = shield
        self.gloves = gloves
        self.necklace = necklace
        self.ring = ring

    def ToString(self):
        return "(" + str(self.weapon.id if self.weapon is not None else 0).rjust(3) + ","  \
            + str(self.armor.id if self.armor is not None else 0).rjust(3) + ","          \
            + str(self.shield.id if self.shield is not None else 0).rjust(3) + ","         \
            + str(self.gloves.id if self.gloves is not None else 0).rjust(3) + ","         \
            + str(self.necklace.id if self.necklace is not None else 0).rjust(3) + ","       \
            + str(self.ring.id if self.ring is not None else 0).rjust(3) + ")"