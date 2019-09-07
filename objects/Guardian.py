from objects.Defines import EquipmentType
from objects.Defines import StatisticType
from objects.Defines import SpecialAbility
from objects.Equipment import Equipment


class Guardian:
    def __init__(self, id, name, atk, defend, pincerAtk, hp, crtRate, crtDmg,
                 acc, res, collectionEffectAtk, collectionEffectDef,
                 collectionEffectPincerAtk, collectionEffectHp,
                 collectionEffectCrtRate, collectionEffectCrtDmg,
                 collectionEffectAcc, collectionEffectRes,
                 priorityStatisticType):
        self.id = int(id)
        self.name = name

        self.equipments = {}
        self.equipments[EquipmentType.Weapon] = None
        self.equipments[EquipmentType.Armor] = None
        self.equipments[EquipmentType.Shield] = None
        self.equipments[EquipmentType.Gloves] = None
        self.equipments[EquipmentType.Necklace] = None
        self.equipments[EquipmentType.Ring] = None

        self.baseStatistics = {}
        self.baseStatistics[StatisticType.Attack] = atk
        self.baseStatistics[StatisticType.Defend] = defend
        self.baseStatistics[StatisticType.PincerAttack] = pincerAtk
        self.baseStatistics[StatisticType.HP] = hp
        self.baseStatistics[StatisticType.CrtRate] = crtRate
        self.baseStatistics[StatisticType.CrtDmg] = crtDmg
        self.baseStatistics[StatisticType.Accuracy] = acc
        self.baseStatistics[StatisticType.Resistance] = res

        self.collectionEffects = {}
        self.collectionEffects[StatisticType.Attack] = collectionEffectAtk or 0
        self.collectionEffects[StatisticType.Defend] = collectionEffectDef or 0
        self.collectionEffects[
            StatisticType.PincerAttack] = collectionEffectPincerAtk or 0
        self.collectionEffects[StatisticType.HP] = collectionEffectHp or 0
        self.collectionEffects[
            StatisticType.CrtRate] = collectionEffectCrtRate or 0
        self.collectionEffects[
            StatisticType.CrtDmg] = collectionEffectCrtDmg or 0
        self.collectionEffects[
            StatisticType.Accuracy] = collectionEffectAcc or 0
        self.collectionEffects[
            StatisticType.Resistance] = collectionEffectRes or 0

        self.finalStatistics = {}
        self.finalStatistics[StatisticType.Attack] = 0
        self.finalStatistics[StatisticType.Defend] = 0
        self.finalStatistics[StatisticType.PincerAttack] = 0
        self.finalStatistics[StatisticType.HP] = 0
        self.finalStatistics[StatisticType.CrtRate] = 0
        self.finalStatistics[StatisticType.CrtDmg] = 0
        self.finalStatistics[StatisticType.Accuracy] = 0
        self.finalStatistics[StatisticType.Resistance] = 0

        self.priorityStatisticType = self.StringToStatType(
            priorityStatisticType)

    def StringToStatType(self, statString):
        if statString == "ATK":
            return StatisticType.Attack
        if statString == "DEF":
            return StatisticType.Defend
        if statString == "Pincer ATK":
            return StatisticType.PincerAttack
        if statString == "HP":
            return StatisticType.HP
        if statString == "CRT Rate":
            return StatisticType.CrtRate
        if statString == "CRT DMG":
            return StatisticType.CrtDmg
        if statString == "ACC":
            return StatisticType.Accuracy
        if statString == "RES":
            return StatisticType.Resistance
        return None

    def EquipSingle(self, newEquipment):
        for equipmentType in EquipmentType:
            if equipmentType == newEquipment.type:
                self.equipments[equipmentType] = newEquipment
            else:
                self.equipments[equipmentType] = None
        self.CalculateFinalStats()

    def EquipWholeSet(self, equipments):
        for equipment in equipments:
            self.equipments[equipment.type] = equipment
        self.CalculateFinalStats()

    def UnequipAll(self):
        self.equipments.clear()

    def GetEquipments(self):
        return self.equipments

    def GetEquipmentSet(self):
        setCount = {}
        for equipmentType in EquipmentType:
            if self.equipments[equipmentType] == None:
                continue
            equipmentSet = self.equipments[equipmentType].set
            if equipmentSet in setCount:
                setCount[equipmentSet] = setCount[equipmentSet] + 1
            else:
                setCount[equipmentSet] = 1
        equipmentSets = []
        for key in setCount.keys():
            while setCount[key] >= 2:
                equipmentSets.append(key)
                setCount[key] = setCount[key] - 2
        return equipmentSets

    def CalculateFinalStats(self):
        for statisticType in StatisticType:
            self.finalStatistics[statisticType] = self.baseStatistics[
                statisticType]
            self.finalStatistics[statisticType] += self.collectionEffects[
                statisticType]
            for equipmentType in EquipmentType:
                if self.equipments[equipmentType] != None:
                    self.finalStatistics[statisticType] += self.equipments[
                        equipmentType].GetBuffedStatistic(statisticType, self)
        equipmentSets = self.GetEquipmentSet()
        for equipmentSet in equipmentSets:
            setBuffPercent = Equipment.GetSetBuff(equipmentSet, self)
            for statisticType in StatisticType:
                self.finalStatistics[statisticType] += setBuffPercent.get(
                    statisticType, 0)

    def GetAverageAttack(self):
        atk = self.finalStatistics[StatisticType.Attack]
        crtRate = self.finalStatistics[StatisticType.CrtRate]
        crtDmg = self.finalStatistics[StatisticType.CrtDmg]
        return atk * (1 + crtRate * crtDmg * 0.0001)

    def GetPriorityStatisticValue(self):
        if self.priorityStatisticType == StatisticType.Attack:
            return self.GetAverageAttack()
        else:
            return self.finalStatistics[self.priorityStatisticType]

    def ToString(self):
        thisString = "Guardian #" + str(self.id) + "\n"
        thisString += self.GetAlignedText(2, "Name", True, ": ") + str(
            self.name) + "\n"

        thisString += self.GetAlignedText(2, "Equipment IDs", True, ": ")
        for equipmentType in EquipmentType:
            if equipmentType in self.equipments:
                thisString += str(self.equipments[equipmentType].id) + " "
            else:
                thisString += "0 "
        thisString += "\n"

        thisString += self.GetAlignedText(
            2, " ", True, " "
        ) + "       ATK       DEF    PINCER        HP   CRTRATE    CRTDMG       ACC       RES\n"

        thisString += self.GetAlignedText(2, "Base Statistic", True, ":")
        for statisticType in StatisticType:
            thisString += str(self.baseStatistics[statisticType]).rjust(10)
        thisString += "\n"

        thisString += self.GetAlignedText(2, "Collection Effect", True, ":")
        for statisticType in StatisticType:
            thisString += str(self.collectionEffects[statisticType]).rjust(10)
        thisString += "\n"

        for equipmentType in EquipmentType:
            thisString += self.GetAlignedText(4, equipmentType.name + " Buff ",
                                              True, ":")
            for statisticType in StatisticType:
                if equipmentType in self.equipments:
                    thisString += str(
                        round(
                            self.equipments[equipmentType].GetBuffedStatistic(
                                statisticType, self))).rjust(10)
            thisString += "\n"

        equipmentSets = self.GetEquipmentSet()
        for equipmentSet in equipmentSets:
            thisString += self.GetAlignedText(2, str(equipmentSet), True, ":")
            setBuffPercent = Equipment.GetSetBuff(equipmentSet, self)
            for statisticType in StatisticType:
                thisString += str(round(setBuffPercent.get(statisticType,
                                                           0))).rjust(10)
            for specialAbility in SpecialAbility:
                thisString += "    " + str(
                    setBuffPercent.get(specialAbility, ""))
            thisString += "\n"

        thisString += self.GetAlignedText(2, "Final Statistic", True, ":")
        for statisticType in StatisticType:
            thisString += str(round(
                self.finalStatistics[statisticType])).rjust(10)
        thisString += "\n"

        thisString += self.GetAlignedText(2, "Average ATK", True, ":") + str(
            round(self.GetAverageAttack())).rjust(10)

        return thisString

    def GetAlignedText(self, indent, text, alignLeft=True, suffixText=""):
        width = 33
        alignedText = ""
        for i in range(indent):
            alignedText += " "
        if alignLeft:
            alignedText += text.ljust(width - indent)
        else:
            alignedText += text.rjust(width - indent)
        alignedText += suffixText
        return alignedText