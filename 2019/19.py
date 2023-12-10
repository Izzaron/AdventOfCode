from intcodeprogram import IntcodeProgram

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

cache = dict()

def at(x:int,y:int,icp: IntcodeProgram) -> bool:
    coord = (x,y)
    if coord in cache:
        return cache[coord]
    else:
        affected = icp.run(x,y)[0]
        cache[coord] = affected
        return affected

def fits_ship(x:int,y:int,size:int,icp: IntcodeProgram) -> bool:
    # return all(all(at(xx,yy,icp) for xx in range(x,x+size)) for yy in range(y,y+size))
    return at(x,y,icp) and at(x+size,y,icp) and at(x,y+size,icp) and at(x+size,y+size,icp)

if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        source_code = [int(i) for i in puzzle_input.read().split(',')]

    icp = IntcodeProgram(source_code)

    # for x in range(55):
    #     for y in range(55):
    #         if x == 46 and y==47:
    #             print('O',end='')
    #             continue
    #         print('#' if icp.run(x,y)[0] else '.',end='')
    #     print()
    # exit()
    x,y = 5,6
    size = 99
    
    while(not fits_ship(x,y,size,icp)):
        x += 1
        print(x,y,at(x,y,icp))
        if not at(x+size,y,icp):
            y += 1
            print(x,y,at(x,y,icp))
            while(not at(x,y,icp)):
                x += 1
                print(x,y,at(x,y,icp))
            x-=1
    print(x,y,'=',x*10000+y)

# 1127 1254 = 11271254 is too high
# 1132 1259 = 11321259 is too high
