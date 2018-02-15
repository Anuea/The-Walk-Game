import sys
import RoomInformation

RoomData = {}

def StartGame():
    RoomData["Room1"].Enter()

class Room(object):
    Name = "Undetermined"
    Type = "Undetermined"
    Introduction = "Undetermined"
    Options = {}
    def Enter(self):
        print(self.Options.Introduction)
        for i,v in self.Options.iteritems():
            print(i,v)

def CreateRoom(roomType,intro,options):
    Iteration = 0
    Iteration = Iteration + len(RoomData)
    if Iteration == 0:
        Iteration = 1
    IterationName = "Room%s" % Iteration
    AssignedName = "Room %s" % Iteration
    NewRoom = Room()
    NewRoom.Name = AssignedName
    NewRoom.Type = roomType
    NewRoom.Options = options
    RoomData[str(IterationName)] = NewRoom

def CreateAllRooms():
    RoomsToCreate = RoomInformation.GetAllRoomData()
    for i,v in RoomsToCreate.iteritems():
        roomType = v["Type"]
        options = v["Options"]
        intro = v["Introduction"]
        CreateRoom(roomType,intro,options)
CreateAllRooms()
print("Okay")

StartGame()
