import textwrap

def render(sifImage,width,height):
    idx = 0
    for _ in range(height):
        for _ in range(width):
            if sifImage[idx] == '0':
                print("  ",end='')
            elif sifImage[idx] == '1':
                print("■ ",end='')
            elif sifImage[idx] == '2':
                print("□ ",end='')
            else:
                print("\n Unknown color: {}".format(sifImage[idx]))
                return
            idx += 1
        print("")
    print(idx," tiles painted")


def main():

    #Part 1
    puzzleInput = open("input8.txt").read()
    width = 25
    height = 6
    
    layers = textwrap.wrap(puzzleInput, width*height)

    zeros = []
    for l in layers:
        zeros.append(l.count('0'))
    
    maxZeros = zeros.index(min(zeros))

    print(layers[maxZeros].count('1') * layers[maxZeros].count('2'))

    #Part 2
    decodedImage = ['x'] * (width*height)
    for pixel in range(width*height):
        for layer in layers:
            if layer[pixel] != '2':
                decodedImage[pixel] = layer[pixel]
                break

    render(decodedImage,width,height)

if __name__ == '__main__':
    main()