from Building import Building

class Room:
    def __init__(self, room_id, room_name, building: Building):
        self.__room_id = room_id          
        self.__room_name = room_name        
        self.__building = building         

    def __str__(self) -> str:
        return f"ห้อง {self.room_id} ({self.room_name})  {self.building}"
    
    @property
    def room_id(self):
        return self.__room_id
    @room_id.setter
    def room_id(self, value):
        self.__room_id = value
 
    @property
    def room_name(self):
        return self.__room_name
    @room_name.setter
    def room_name(self, value):
        self.__room_name = value

    @property
    def building(self):
        return self.__building
    @building.setter
    def building(self, value):
        self.__building = value