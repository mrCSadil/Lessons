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

class WifiService():
    def get_wifi_description(self):
        return "It has Wifi access"

class BreakfastService():
    def get_breakfast_description(self):
        return "It has Breakfast service everymorning"


class StandartRoom(Room):

    def get_price(self):
        return self._Room__price

    def get_features(self):
        return self._features

class FamilyRoom(Room, WifiService):

    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.append(self.get_wifi_description())
        return features

class LuxuryRoom(Room , WifiService , BreakfastService):

    def get_price(self):
        return self._Room__price

    def get_features(self):
        features = self._features.copy()
        features.extend([self.get_wifi_description() , self.get_breakfast_description()])
        return features

def AllInfo(room):
    print("Features: ", room.get_features())
    print(f"Price: {room.get_price()} \n")

standard_room = StandartRoom(features=["no bed" , "In room 20 people", "No windows and no toilet, no bathroom, no food", "your room under luxury's  toilet" ], price="12 pennies")
luxury_room = LuxuryRoom(features=["Alaska King size bed " , "teleportator", "Your own Jet" , "infinite number of food"], price="1 life")
family_room = FamilyRoom(features=["one crib size bed , concrete floor only", "No lights", "no access to fresh air"], price="60 dollars")

AllInfo(standard_room)
AllInfo(family_room)
AllInfo(luxury_room)
