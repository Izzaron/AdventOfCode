import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input6.txt')) as puzzle_input:

        puzzle_data = puzzle_input.readlines()[0]
    
    marker = 14
    packet_size = marker
    while True:

        if(len(set(puzzle_data[marker-packet_size:marker]))==packet_size):
            print(marker)
            break
        
        marker += 1