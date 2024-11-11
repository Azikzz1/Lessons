from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, features, price):
        self._features = features
        self.__price = price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_features(self):
        pass


class StandardRoom(Room):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features


class WiFiService:
    def get_wifi_description(self):
        return "WiFi Service available"


class BreakfastService:
    def get_breakfast_description(self):
        return "Breakfast Service available"


class LuxuryRoom(Room, WiFiService, BreakfastService):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description(), self.get_breakfast_description()]


class FamilyRoom(Room, WiFiService):
    def __init__(self, features, price):
        super().__init__(features, price)

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features + [self.get_wifi_description()]


# Пример использования

standard_room = StandardRoom(["Basic bed", "Shower"], 100)
luxury_room = LuxuryRoom(["King-size bed", "Jacuzzi"], 300)
family_room = FamilyRoom(["Two queen-size beds", "Mini fridge"], 200)

rooms = [standard_room, luxury_room, family_room]

for room in rooms:
    print(f"Цена: {room.get_price()}")
    print(f"Удобства: {room.get_features()}")
    print()
