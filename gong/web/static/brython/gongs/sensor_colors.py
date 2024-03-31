class SensorColor:
    def __init__(self, type_="default"):
        self.type = type_
        self.color_ranks = [
            (0, 15, "#00BFFF"),
            (15, 25, "#01DF3A"),
            (25, 37.5, "#FFE319"),
            (37.5, 75, "#FF8000"),
            (75, 1_000_000, "#FF0000"),
        ]

    def get_color(self, value):
        for min_value, max_value, color in self.color_ranks:
            if min_value <= value <= max_value:
                return color
        return "#808080"


class PM01Color(SensorColor):
    def __init__(self):
        super().__init__("pm_0_1")


class PM1Color(SensorColor):
    def __init__(self):
        super().__init__("pm_1")


class PM25Color(SensorColor):
    def __init__(self):
        super().__init__("pm_2_5")


class WindSpeedColor(SensorColor):
    def __init__(self):
        super().__init__("wind_speed")


class PM10Color(SensorColor):
    def __init__(self, type_="pm_10"):
        super().__init__(type_)

        self.color_ranks = [
            (0, 50, "#00BFFF"),
            (50, 80, "#01DF3A"),
            (80, 120, "#FFE319"),
            (120, 180, "#FF8000"),
            (180, 1_000_000, "#FF0000"),
        ]


class PM100Color(PM10Color):
    def __init__(self):
        super().__init__("pm_100")


class TemperatureColor(SensorColor):
    def __init__(self):
        super().__init__("temperature")

        self.color_ranks = [
            (0, 15, "#FE2EF7"),
            (15, 20, "#8904B1"),
            (20, 25, "#0040FF"),
            (25, 30, "#00BFFF"),
            (30, 35, "#FFE319"),
            (35, 40, "#FF8000"),
            (40, 1_000_000, "#FF0000"),
        ]


class HumidityColor(SensorColor):
    def __init__(self):
        super().__init__("humidity")

        self.color_ranks = [
            (0, 30, "#FE2EF7"),
            (30, 60, "#53B06E"),
            (60, 90, "#1CD2C7"),
            (90, 1_000_000, "#000080"),
        ]


class VOCColor(SensorColor):
    def __init__(self):
        super().__init__("voc")

        self.color_ranks = [
            (0, 66, "#00BFFF"),
            (66, 221, "#01DF3A"),
            (221, 661, "#FFE319"),
            (661, 2201, "#FF8000"),
            (2201, 1_000_000, "#FF0000"),
        ]


class CO2Color(SensorColor):
    def __init__(self):
        super().__init__("co2")

        self.color_ranks = [
            (0, 601, "#00BFFF"),
            (601, 1001, "#01DF3A"),
            (1001, 1501, "#FFE319"),
            (1501, 2001, "#FF8000"),
            (2001, 1_000_000, "#FF0000"),
        ]


SENSOR_COLORS = [
    PM01Color(),
    PM25Color(),
    PM10Color(),
    PM100Color(),
    TemperatureColor(),
    HumidityColor(),
    VOCColor(),
    CO2Color(),
]


def get_sensor_color_rank(type_):
    type_ = type_.lower()
    for sensor_color in SENSOR_COLORS:
        if type_ == sensor_color.type:
            return sensor_color.color_ranks

    return []


def get_sensor_color(type_, value):
    type_ = type_.lower()
    for sensor_color in SENSOR_COLORS:
        if type_ == sensor_color.type:
            return sensor_color.get_color(value)

    grey = "#808080"
    return grey
