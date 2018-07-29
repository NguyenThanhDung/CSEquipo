from Defines import EquipmentType
from Defines import StatisticType
from Defines import SpecialAbility
from Equipment import Equipment

class Guardian:

    def __init__(self, id, name, atk, defend, pincerAtk, hp, crtRate, crtDmg, acc, res, collectionEffectAtk, collectionEffectDef, collectionEffectPincerAtk, collectionEffectHp, collectionEffectCrtRate, collectionEffectCrtDmg, collectionEffectAcc, collectionEffectRes):
        self.id = id
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

        self.equipmentSets = {}
    
    def Equip(self, equipment):
        self.equipments[equipment.type] = equipment
        self.AddEquipmentSet(equipment.set)

    def AddEquipmentSet(self, equipmentSet):
        if self.equipmentSets.has_key(equipmentSet):
            self.equipmentSets[equipmentSet] += 1
        else:
            self.equipmentSets[equipmentSet] = 1

    def GetFinalStats(self):
        finalStats = {}
        for statisticType in StatisticType:
            finalStats[statisticType] = self.statistics[statisticType]
            finalStats[statisticType] += self.collectionEffects[statisticType]
            for equipmentType in EquipmentType:
                finalStats[statisticType] += self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)
            for key in self.equipmentSets.keys():
                if self.equipmentSets[key] >= 2:
                    setBuffPercent = Equipment.GetSetBuff(key, self)
                    finalStats[statisticType] += setBuffPercent.get(statisticType, 0)
        return finalStats

    def ToString(self):
        thisString = "Guardian #" + str(self.id) + "\n"
        thisString += "  Name             : " + str(self.name) + "\n"

        thisString += "  Equipment IDs    : "
        for equipmentType in EquipmentType:
            if self.equipments.has_key(equipmentType):
                thisString += str(self.equipments[equipmentType].id) + " "
        thisString += "\n"
        
        thisString += "                           ATK       DEF    PINCER        HP   CRTRATE    CRTDMG       ACC       RES\n"

        thisString += "  Base Statistic   :" 
        for statisticType in StatisticType:
            thisString += str(self.statistics[statisticType]).rjust(10)
        thisString += "\n"

        thisString += "  Collection Effect:"
        for statisticType in StatisticType:
            thisString += str(self.collectionEffects[statisticType]).rjust(10)
        thisString += "\n"

        for equipmentType in EquipmentType:
            thisString += (equipmentType.name + " Buff:").rjust(20)
            for statisticType in StatisticType:
                thisString += str(self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)).rjust(10)
            thisString += "\n"
        
        for key in self.equipmentSets.keys():
            if self.equipmentSets[key] >= 2:
                thisString += "  " + str(key).ljust(16) + " :"
                setBuffPercent = Equipment.GetSetBuff(key, self)
                for statisticType in StatisticType:
                    thisString += str(setBuffPercent.get(statisticType, 0)).rjust(10)
                for specialAbility in SpecialAbility:
                    thisString += "    " + str(setBuffPercent.get(specialAbility, ""))
                thisString += "\n"

        finalStats = self.GetFinalStats()
        thisString += "  Final Statistic  :"
        for statisticType in StatisticType:
            thisString += str(finalStats[statisticType]).rjust(10)

        return thisString