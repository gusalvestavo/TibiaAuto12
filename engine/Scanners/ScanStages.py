from core.HookWindow import PixelMatchesColor


class ScanStages:
    def __init__(self, name):
        self.stage = 0
        self.name = name

    def ScanStages(self, Localization, color, colorFull):
        if PixelMatchesColor(Localization[0] + 100, Localization[1],
                             (colorFull[0], colorFull[1], colorFull[2])):
            return 100

        for i in range(95, 5, -5):
            if PixelMatchesColor(Localization[0] + i, Localization[1], (color[0], color[1], color[2])):
                return i

        return 0
