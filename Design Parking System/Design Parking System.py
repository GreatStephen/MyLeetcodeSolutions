class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.one = big
        self.two = medium
        self.three = small

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.one>0:
            self.one -= 1
            return True
        if carType==2 and self.two>0:
            self.two -= 1
            return True
        if carType==3 and self.three>0:
            self.three -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)