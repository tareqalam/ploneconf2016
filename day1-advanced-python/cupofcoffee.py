import datetime


class CupOfCoffee:
    def __init__(self, temp, k, vol):
        self._temp = temp
        self.k = k
        self.vol = vol
        self.init_time = datetime.datetime.now()
    @property
    def temp(self):
        return 100000 * self.k * self.vol - (datetime.datetime.now() - self.init_time).total_seconds()

    @temp.setter
    def update_temp(self, vol):
        pass

cup = CupOfCoffee(80, 0.0008, 0.200)

cup.temp = 220
