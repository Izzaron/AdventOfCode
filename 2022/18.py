input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

def neighbour_count(pixel,points,shadow):
    neighbours = 0
    i,j,k = 0,0,0
    for i in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in points:
            neighbours += 1
    i,j,k = 0,0,0
    for j in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in points:
            neighbours += 1
    i,j,k = 0,0,0
    for k in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in points:
            neighbours += 1
    i,j,k = 0,0,0
    for i in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in shadow:
            neighbours += 1
    i,j,k = 0,0,0
    for j in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in shadow:
            neighbours += 1
    i,j,k = 0,0,0
    for k in [-1,1]:
        if (point[0]+i,point[1]+j,point[2]+k) in shadow:
            neighbours += 1
    return neighbours

def surface_area(points):
    surface = 0
    counted = set()
    for point in points:
        surface += 6
        i,j,k = 0,0,0
        for i in [-1,1]:
            if (point[0]+i,point[1]+j,point[2]+k) in counted:
                surface -= 2
        i,j,k = 0,0,0
        for j in [-1,1]:
            if (point[0]+i,point[1]+j,point[2]+k) in counted:
                surface -= 2
        i,j,k = 0,0,0
        for k in [-1,1]:
            if (point[0]+i,point[1]+j,point[2]+k) in counted:
                surface -= 2
        counted.add(point)
    return surface

if __name__ == "__main__":
    points = set()
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    with open(test_file) as puzzle_input:

        for line in puzzle_input:
            point = eval(line)
            points.add(point)
            
            min_x = min(min_x,point[0])
            max_x = max(max_x,point[0])
            min_y = min(min_y,point[1])
            max_y = max(max_y,point[1])
            min_z = min(min_z,point[2])
            max_z = max(max_z,point[2])
    
    #part 1
    print(surface_area(points))

    #part 2
    shadow = set([(i,j,k) for i in range(min_x,max_x+1) for j in range(min_y,max_y+1) for k in range(min_z,max_z+1)])
    shadow -= points
    points_removed = True
    while(points_removed):
        points_removed = False
        for point in shadow:
            if neighbour_count(point,points,shadow) <6:
                shadow.remove(point)
                points_removed = True
                break
    print(surface_area(points.union(shadow)))