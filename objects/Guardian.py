from Defines import EquipmentType
from Defines import StatisticType
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

        self.collectionEffectAtk = collectionEffectAtk or 0
        self.collectionEffectDef = collectionEffectDef or 0
        self.collectionEffectPincerAtk = collectionEffectPincerAtk or 0
        self.collectionEffectHp = collectionEffectHp or 0
        self.collectionEffectCrtRate = collectionEffectCrtRate or 0
        self.collectionEffectCrtDmg = collectionEffectCrtDmg or 0
        self.collectionEffectAcc = collectionEffectAcc or 0
        self.collectionEffectRes = collectionEffectRes or 0
        self.equipmentSets = {}
    
    def Equip(self, equipment, equipmentType):
        self.equipments[equipmentType] = equipment
        self.AddEquipmentSet(equipment.set)

    def AddEquipmentSet(self, equipmentSet):
        if self.equipmentSets.has_key(equipmentSet):
            self.equipmentSets[equipmentSet] += 1
        else:
            self.equipmentSets[equipmentSet] = 1

    def GetFinalStats(self):
        finalStats = {}

        for statisticType in len(StatisticType):
            finalStats[statisticType] = self.statistics[statisticType]
            for equipmentType in len(EquipmentType):
                # TODO: Add collect effect
                finalStats[statisticType] += self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)

    def ToString(self):
        thisString = "Guardian #" + str(self.id) + "\n"
        thisString += "  Name             : " + str(self.name) + "\n"

        thisString += "  Equipment IDs    : "
        for equipmentType in range(len(EquipmentType)):
            if self.equipments.has_key(equipmentType):
                thisString += str(self.equipments[equipmentType].id) + " "
        thisString += "\n"
        
        thisString += "                           ATK       DEF    PINCER        HP   CRTRATE    CRTDMG       ACC       RES\n"

        thisString += "  Base Statistic   :" 
        for statisticType in StatisticType:
            thisString += str(self.statistics[statisticType]).rjust(10)
        thisString += "\n"

        thisString += "  Collection Effect:"
        thisString += str(self.collectionEffectAtk).rjust(10)
        thisString += str(self.collectionEffectDef).rjust(10)
        thisString += str(self.collectionEffectPincerAtk).rjust(10)
        thisString += str(self.collectionEffectHp).rjust(10)
        thisString += str(self.collectionEffectCrtRate).rjust(10)
        thisString += str(self.collectionEffectCrtDmg).rjust(10)
        thisString += str(self.collectionEffectAcc).rjust(10)
        thisString += str(self.collectionEffectRes).rjust(10) + "\n"

        for equipmentType in EquipmentType:
            thisString += (equipmentType.name + " Buff:").rjust(20)
            for statisticType in StatisticType:
                thisString += str(self.equipments[equipmentType].GetBuffedStatistic(statisticType, self)).rjust(10)
            thisString += "\n"
        
        for key in self.equipmentSets.keys():
            if self.equipmentSets[key] >= 2:
                thisString += "  " + key + " Set Buff  :"
                setBuffPercent = Equipment.GetSetBuff(key, self)
                thisString += str(setBuffPercent.get("atk", 0)).rjust(10)
                thisString += str(setBuffPercent.get("def", 0)).rjust(10)
                thisString += str(setBuffPercent.get("pincerAtk", 0)).rjust(10)
                thisString += str(setBuffPercent.get("hp", 0)).rjust(10)
                thisString += str(setBuffPercent.get("crtRate", 0)).rjust(10)
                thisString += str(setBuffPercent.get("crtDmg", 0)).rjust(10)
                thisString += str(setBuffPercent.get("acc", 0)).rjust(10)
                thisString += str(setBuffPercent.get("res", 0)).rjust(10) + "   "
                thisString += str(setBuffPercent.get("CounterAtk", "")) + "   "
                thisString += str(setBuffPercent.get("LifeDrain", "")) + "   "
                thisString += str(setBuffPercent.get("ReduceTargetMaxHP", "")) + "   "
                thisString += str(setBuffPercent.get("Stun", "")) + "   "
                thisString += "\n"
        thisString += "\n"
        return thisString