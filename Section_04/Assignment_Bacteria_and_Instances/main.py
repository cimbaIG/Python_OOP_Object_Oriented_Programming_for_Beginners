class Bacterium():

    def __init__(self, x, y, shape, isHarmful, antibioticsResistant):
        self.x = x
        self.y = y
        self.shape = shape
        self.isHarmful = isHarmful,
        self.antibioticsResistant = antibioticsResistant



bacterium1 = Bacterium(2, 2, 'Bacilli',True,False)
bacterium2 = Bacterium(5, 3, 'Cocci', True, True)
bacterium3 = Bacterium(0, 0, 'Spirilli', True, False)
