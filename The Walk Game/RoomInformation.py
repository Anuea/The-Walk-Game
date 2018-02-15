import sys

Information = {}
Information["Room1"] = {
    "Type":"Entry",
    "Options":{
        1:{"|Enter the tall door|","MY RESPONSE"},
        2:{"|Enter the small door|","MY RESPONSE"},
    },
    "Introduction":"""
        You have awoken in a strange room. Your look around and notice the room is surprisingly clean.
        A desk sits in the corner with papers and pens spread out and the dim light of a candle half melted.
        You look around the room. It must be some sort of office. Adjacent from you there are two doors.
        One is blue, tall, and has a white border. The other is short, red, and a black border.
        Upon further inspection of the doors, you see an engraving on the top between them. It states
        'Enter a door and exit a door. The Walk is over when you meet the start and the end.'
    """,
}
Information["Room2"] = {
    "Type":"Riddle",
    "Options":{
        1:"|Option1|",
        2:"|Option2|",
    },
}

def GetRoomData(RoomName):
    if Information[str(RoomName)]:
        return Information[str(RoomName)]
    else:
        return "Unable to find data for the room: %s" % str(RoomName)

def GetAllRoomData():
    return Information
