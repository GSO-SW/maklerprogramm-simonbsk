roomSize = []
roomName = []
room = []
tempContinue = 0

while tempContinue == 0:
    tempIn = int(input("1: Neuen Raum hinzufügen \n2: Liste ausgeben\n3: exit"))
    if tempIn == 1:
        raumName = input("Welchen Raum möchten Sie hinzufügen")
        room.append(raumName)
        tempIn = str(input("Ist der Raum ein Viereck? [j/n]"))
        if tempIn == "j":
            tempIn = str(input("Ist der Raum ein Quadrat? [j/n]"))
            if tempIn == "j":
                wallA = float(input("Wandlänge in m?"))
                raumGroesse = float(wallA * 4)
                roomSize.append(raumGroesse)
                room.append(raumGroesse)
                print(raumGroesse)
            elif tempIn == "n":
                wallA = float(input("Raumlänge?"))
                wallB = float(input("Raumbreite?"))
                raumGroesse = float(wallA * wallB)
                roomSize.append(raumGroesse)
                room.append(raumGroesse)
                print(raumGroesse)
        elif tempIn == "n":
            wallA = float(input("Längste Wand? (Raumbreite)"))
            wallB = float(input("Längste Wand? (Raumlänge)"))
            minusWallC = float(input("Kürzeste Wand? (Raumbreite)"))
            minusWallD = float(input("Kürzeste Wand? (Raumlänge)"))
            raumGroesse = float(wallA * wallB - minusWallC * minusWallD)
            roomSize.append(raumGroesse)
            room.append(raumGroesse)
    elif tempIn == 2:
        print(room)
        print(str(float(sum(roomSize))) + "m^2 beträgt die Gesamtfläche")
        #for x in roomName and roomSize:
        #    print("Raum: " + str(x))
        #    print("Größe: " + str(x) + "\n")

    elif tempIn == 3:
        print("end")
        break

