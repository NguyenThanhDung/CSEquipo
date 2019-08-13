from enum import Enum

class GuardianDirection(Enum):
    Rook = 0
    Knight = 1
    Bishop = 2
    Queen = 3
    King = 4

class EquipmentType(Enum):
    Weapon = 0
    Armor = 1
    Shield = 2
    Gloves = 3
    Necklace = 4
    Ring = 5

class StatisticType(Enum):
    Attack = 0
    Defend = 1
    PincerAttack = 2
    HP = 3
    CrtRate = 4
    CrtDmg = 5
    Accuracy = 6
    Resistance = 7

class SetType(Enum):
    Strike = 0
    Guard = 1
    Pincer = 2
    Energy = 3
    Blade = 4
    Violent = 5
    Focus = 6
    Endure = 7
    Revenge = 8
    Vampire = 9
    Pulverize = 10
    Stun = 11

class SpecialAbility(Enum):
    CounterAttack = 0
    LifeDrain = 1
    ReduceTargetMaxHP = 2
    Stun = 3

class ValueType(Enum):
    Percent = 0
    Plus = 1