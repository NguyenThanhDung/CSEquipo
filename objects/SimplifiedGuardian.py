from objects.Defines import GuardianDirection

class SimplifiedGuardian:

    def __init__(self, id, name, direction, baseStars, currentStars, level, status, priorityStatistic, note):
        self.id = int(id)
        self.name = name
        self.direction = direction
        self.baseStars = baseStars
        self.currentStars = currentStars
        self.level = level
        self.status = status
        self.priorityStatistic = priorityStatistic
        self.note = note

    def ToString(self):
        return "Guardian #" + str(self.id) + ": " + str(self.name) + "\n"
