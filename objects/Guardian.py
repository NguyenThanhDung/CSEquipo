from Defines import EquipmentType
from Defines import StatisticType
from Defines import SpecialAbility
from Equipment import Equipment

class Guardian:

    def __init__(self, id, name, atk, defend, pincerAtk, hp, crtRate, crtDmg, acc, res, collectionEffectAtk, collectionEffectDef, collectionEffectPincerAtk, collectionEffectHp, collectionEffectCrtRate, collectionEffectCrtDmg, collectionEffectAcc, collectionEffectRes):
        self.id = int(id)
        self.name = name

        self.equipments = {}
        self.equipments[EquipmentType.Weapon] = None
        self.equipments[EquipmentType.Armor] = None
        self.equipments[EquipmentType.Shield] = None
        self.equipments[EquipmentType.Gloves] = None
        self.equipments[EquipmentType.Necklace] = None
        self.equipments[EquipmentType.Ring] = None

        self.statistics = {}
        self.statistics[StatisticType.Attack] = atk
        self.statistics[StatisticType.Defend] = defend
        self.statistics[StatisticType.PincerAttack] = pincerAtk
        self.statistics[StatisticType.HP] = hp
        self.statistics[StatisticType.CrtRate] = crtRate
        self.statistics[StatisticType.CrtDmg] = crtDmg
        self.statistics[StatisticType.Accuracy] = acc
        self.statistics[StatisticType.Resistance] = res

        self.collectionEffects = {}
        self.collectionEffects[StatisticType.Attack] = collectionEffectAtk or 0
        self.collectionEffects[StatisticType.Defend] = collectionEffectDef or 0
        self.collectionEffects[StatisticType.PincerAttack] = collectionEffectPincerAtk or 0
        self.collectionEffects[StatisticType.HP] = collectionEffectHp or 0
        self.collectionEffects[StatisticType.CrtRate] = collectionEffectCrtRate or 0
        self.collectionEffects[StatisticType.CrtDmg] = collectionEffectCrtDmg or 0
        self.collectionEffects[StatisticType.Accuracy] = collectionEffectAcc or 0
        self.collectionEffects[StatisticType.Resistance] = collectionEffectRes or 0
    
    def Equip(self, equipment):
        if equipment is not None:
            self.equipments[equipment.type] = equipment

    def UnequipAll(self):
        self.equipments.clear()

    def GetEquipmentSet(self):
        setCount = {}
        if len(self.equipments) > 0:
            for equipmentType in EquipmentType:
                if self.equipments.has_key(equipmentType):
                    equipmentSet = self.equipments[equipmentType].set
                    if setCount.has_key(equipmentSet):
                        setCount[equipmentSet] = setCount[equipmentSet] + 1
                    else:
                        setCount[equipmentSet] = 1
        set = []
        for key in setCount.keys():
            while setCount[key] >= 2:
                set.append(key)
                setCount[key] = setCount[key] - 2
        return set

    def CalculateFinalStats(self):
        finalStats = {}
        for statisticType in StatisticType:
            finalStats[statisticType] = self.statistics[statisticType]
            finalStats[statisticType] += self.collectionEffects[statisticType]
            if len(self.equipments) > 0:
                for equipmentType in EquipmentType:
                    if self.equipments.has_key(equipmentType):
                        finalStats[statisticType] += self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)
        equipmentSet = self.GetEquipmentSet()
        for set in equipmentSet:
            setBuffPercent = Equipment.GetSetBuff(set, self)
            for statisticType in StatisticType:
                finalStats[statisticType] += setBuffPercent.get(statisticType, 0)
        return finalStats

    @staticmethod
    def GetAverageAttack(finalStats):
        atk = finalStats[StatisticType.Attack]
        crtRate = finalStats[StatisticType.CrtRate]
        crtDmg = finalStats[StatisticType.CrtDmg]
        return atk + crtRate * (atk + crtDmg) / 100

    def ToString(self):
        thisString = "Guardian #" + str(self.id) + "\n"
        thisString += self.GetAlignedText(2, "Name", True, ":") + str(self.name) + "\n"

        thisString += self.GetAlignedText(2, "Equipment IDs", True, ":")
        for equipmentType in EquipmentType:
            if self.equipments.has_key(equipmentType):
                thisString += str(self.equipments[equipmentType].id) + " "
            else:
                thisString += "0 "
        thisString += "\n"
        
        thisString += self.GetAlignedText(2, " ", True, " ") + "       ATK       DEF    PINCER        HP   CRTRATE    CRTDMG       ACC       RES\n"

        thisString += self.GetAlignedText(2, "Base Statistic", True, ":")
        for statisticType in StatisticType:
            thisString += str(self.statistics[statisticType]).rjust(10)
        thisString += "\n"

        thisString += self.GetAlignedText(2, "Collection Effect", True, ":")
        for statisticType in StatisticType:
            thisString += str(self.collectionEffects[statisticType]).rjust(10)
        thisString += "\n"

        for equipmentType in EquipmentType:
            thisString += self.GetAlignedText(2, equipmentType.name + " Buff ", False, ":")
            for statisticType in StatisticType:
                if self.equipments.has_key(equipmentType):
                    thisString += str(self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)).rjust(10)
            thisString += "\n"
        
        equipmentSet = self.GetEquipmentSet()
        for set in equipmentSet:
            thisString += self.GetAlignedText(2, str(set), True, ":")
            setBuffPercent = Equipment.GetSetBuff(set, self)
            for statisticType in StatisticType:
                thisString += str(setBuffPercent.get(statisticType, 0)).rjust(10)
            for specialAbility in SpecialAbility:
                thisString += "    " + str(setBuffPercent.get(specialAbility, ""))
            thisString += "\n"

        finalStats = self.CalculateFinalStats()
        thisString += self.GetAlignedText(2, "Final Statistic", True, ":")
        for statisticType in StatisticType:
            thisString += str(finalStats[statisticType]).rjust(10)
        thisString += "\n"

        thisString += self.GetAlignedText(2, "Average ATK", True, ":") + str(Guardian.GetAverageAttack(finalStats)).rjust(10)

        return thisString

    def GetAlignedText(self, indent, text, alignLeft = True, suffixText = ""):
        width = 33
        alignedText = ""
        for i in range(indent):
            alignedText += " "
        if alignLeft:
            alignedText += text.ljust(width)
        else:
            alignedText += text.rjust(width)
        alignedText += suffixText
        return alignedText