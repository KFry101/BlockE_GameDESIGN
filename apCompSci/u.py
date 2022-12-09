distance= {1:10, 2:20, 3:30, 4:40, 5:50}

paths= {1:[distance[1],distance[2],distance[3]], 2:[distance[2],distance[3],distance[4]], 3:[distance[5],distance[4],distance[3]]}

def driveToDistance(Distance):
    print(Distance)

def followPath(paths):
    print(paths)

driveToDistance(distance[1])
driveToDistance(distance[2])
followPath(paths[1])
followPath(paths[2])