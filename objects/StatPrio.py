from objects.Defines import StatisticType

class StatPrio:

    def __init__(self, guardianID, priority, prioStat):
        self.guardianID = guardianID
        self.priority = priority
        self.prioStat = self.StatNameToStatType(prioStat)

    def StatNameToStatType(self, statName):
        if statName == "ATK":
            return StatisticType.Attack
        elif statName == "DEF":
            return StatisticType.Defend
        elif statName == "PincerATK":
            return StatisticType.PincerAttack
        elif statName == "HP":
            return StatisticType.HP
        elif statName == "CRT Rate":
            return StatisticType.CrtRate
        elif statName == "CRT Dmg":
            return StatisticType.CrtDmg
        elif statName == "ACC":
            return StatisticType.Accuracy
        elif statName == "RES":
            return StatisticType.Resistance

    def ToString(self):
        return self.guardianID.ljust(15) + ": " + str(self.prioStat)