from Defines import StatisticType
from Defines import SetType
from Defines import SpecialAbility
from Defines import ValueType

class Equipment:

    def __init__(self, id, equipmentType, atkPercent, atkPlus, defPercent, defPlus, \
        pincerAtkPercent, pincerAtkPlus, hpPercent, hpPlus, crtRate, crtDmg, accuracy, resistance,  \
        set, starCount, level):

        self.id = id
        self.type = equipmentType

        self.statistics = {}

        self.statistics[StatisticType.Attack] = {}
        self.statistics[StatisticType.Attack][ValueType.Percent] = atkPercent or 0
        self.statistics[StatisticType.Attack][ValueType.Plus] = atkPlus or 0

        self.statistics[StatisticType.Defend] = {}
        self.statistics[StatisticType.Defend][ValueType.Percent] = defPercent or 0
        self.statistics[StatisticType.Defend][ValueType.Plus] = defPlus or 0

        self.statistics[StatisticType.PincerAttack] = {}
        self.statistics[StatisticType.PincerAttack][ValueType.Percent] = pincerAtkPercent or 0
        self.statistics[StatisticType.PincerAttack][ValueType.Plus] = pincerAtkPlus or 0

        self.statistics[StatisticType.HP] = {}
        self.statistics[StatisticType.HP][ValueType.Percent] = hpPercent or 0
        self.statistics[StatisticType.HP][ValueType.Plus] = hpPlus or 0
        
        self.statistics[StatisticType.CrtRate] = crtRate or 0
        self.statistics[StatisticType.CrtDmg] = crtDmg or 0
        self.statistics[StatisticType.Accuracy] = accuracy or 0
        self.statistics[StatisticType.Resistance] = resistance or 0

        self.set = self.SetNameToSetType(set)
        self.starCount = starCount
        self.level = level

    def SetNameToSetType(self, setName):
        if setName == "Strike":
            return SetType.Strike
        elif setName == "Guard":
            return SetType.Guard
        elif setName == "Pincer":
            return SetType.Pincer
        elif setName == "Energy":
            return SetType.Energy
        elif setName == "Blade":
            return SetType.Blade
        elif setName == "Violent":
            return SetType.Violent
        elif setName == "Focus":
            return SetType.Focus
        elif setName == "Endure":
            return SetType.Endure
        elif setName == "Revenge":
            return SpecialAbility.CounterAttack
        elif setName == "Vampire":
            return SpecialAbility.LifeDrain
        elif setName == "Pulverize":
            return SpecialAbility.ReduceTargetMaxHP
        elif setName == "Stun":
            return SpecialAbility.Stun
    
    def GetStatistic(self, statisticType):
        return self.statistics[statisticType]
    
    def GetBuffedStatistic(self, statisticType, guardian):
        if statisticType.value <= StatisticType.HP.value:
            return guardian.statistics[statisticType] * self.statistics[statisticType][ValueType.Percent] / 100 + self.statistics[statisticType][ValueType.Plus]
        else:
            return self.statistics[statisticType]

    def ToString(self):
        thisString = "Equipment #" + str(self.id) + "\n"
        thisString += "  Type      : " + self.type + "\n"
        thisString += "  ATK       : " + str(self.statistics[StatisticType.Attack][ValueType.Percent]) + "% +" + str(self.statistics[StatisticType.Attack][ValueType.Plus]) + "\n"
        thisString += "  DEF       : " + str(self.statistics[StatisticType.Defend][ValueType.Percent]) + "% +" + str(self.statistics[StatisticType.Defend][ValueType.Plus]) + "\n"
        thisString += "  Pincer ATK: " + str(self.statistics[StatisticType.PincerAttack][ValueType.Percent]) + "% +" + str(self.statistics[StatisticType.PincerAttack][ValueType.Plus]) + "\n"
        thisString += "  HP        : " + str(self.statistics[StatisticType.HP][ValueType.Percent]) + "% +" + str(self.statistics[StatisticType.HP][ValueType.Plus]) + "\n"
        thisString += "  CRT Rate  : " + str(self.statistics[StatisticType.CrtRate]) + "%\n"
        thisString += "  CRT Dmg   : " + str(self.statistics[StatisticType.CrtDmg]) + "%\n"
        thisString += "  Accuracy  : " + str(self.statistics[StatisticType.Accuracy]) + "%\n"
        thisString += "  Resistance: " + str(self.statistics[StatisticType.Resistance]) + "%\n"
        thisString += "  Set       : " + self.set + "\n"
        thisString += "  Star Count: " + str(self.starCount) + "\n"
        thisString += "  Level     : " + str(self.level) + "\n"
        return thisString
    
    @staticmethod
    def GetSetBuff(setType, guardian):
        setBuff = {}
        if setType == SetType.Strike:
            setBuff[StatisticType.Attack] = guardian.statistics[StatisticType.Attack] * 0.1
        elif setType == SetType.Guard:
            setBuff[StatisticType.Defend] = guardian.statistics[StatisticType.Defend] * 0.1
        elif setType == SetType.Pincer:
            setBuff[StatisticType.PincerAttack] = guardian.statistics[StatisticType.PincerAttack] * 0.1
        elif setType == SetType.Energy:
            setBuff[StatisticType.HP] = guardian.statistics[StatisticType.HP] * 0.1
        elif setType == SetType.Blade:
            setBuff[StatisticType.CrtRate] = 8
        elif setType == SetType.Violent:
            setBuff[StatisticType.CrtDmg] = 0
        elif setType == SetType.Focus:
            setBuff[StatisticType.Accuracy] =15
        elif setType == SetType.Endure:
            setBuff[StatisticType.Resistance] = 15
        elif setType == SetType.Revenge:
            setBuff[SpecialAbility.CounterAttack] = 10
        elif setType == SetType.Vampire:
            setBuff[SpecialAbility.LifeDrain] = 20
        elif setType == SetType.Pulverize:
            setBuff[SpecialAbility.ReduceTargetMaxHP] = 3
        elif setType == SetType.Stun:
            setBuff[SpecialAbility.Stun] = 20
        return setBuff
