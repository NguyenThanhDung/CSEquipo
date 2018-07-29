
class StatPrio:

    def __init__(self, guardian, prioStat):
        self.guardian = guardian
        self.prioStat = prioStat

    def ToString(self):
        return self.guardian.ljust(15) + ": " + str(self.prioStat)