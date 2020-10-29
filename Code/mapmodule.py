class Map:
    def __init__(self, lknown, laccess):
        self.known = lknown
        self.access = laccess
        
    def unlockarea(self, area, accessible = 0):
        self.known.add(area)
        if accessible:
            self.access.add(area)