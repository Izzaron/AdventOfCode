import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Forest:
    def __init__(self,puzzle_input) -> None:
        self.trees = [[int(i) for i in line.strip()] for line in puzzle_input.readlines()]
    
    def no_higher_than(self,this_tree,trees):
        return not any([tree>=this_tree for tree in trees])

    def trees_north_of(self,i,j):
        return [row[i] for row in reversed(self.trees[:j])]

    def trees_south_of(self,i,j):
        return [row[i] for row in self.trees[j+1:]]

    def trees_east_of(self,i,j):
        return self.trees[j][i+1:]

    def trees_west_of(self,i,j):
        return list(reversed(self.trees[j][:i]))

    def get_visibility_map(self):

        visible = [[0 for _ in line] for line in self.trees]

        for j in range(len(self.trees)):
            for i in range(len(self.trees[j])):
                if j == 0 or j == len(self.trees)-1:
                    visible[j] = [1 for _ in range(len(self.trees[j]))]
                elif i == 0 or i == len(self.trees[j])-1:
                    visible[j][i] = 1
                else:
                    this_tree = self.trees[j][i]
                    trees_north = self.trees_north_of(i,j)
                    trees_west = self.trees_west_of(i,j)
                    trees_south = self.trees_south_of(i,j)
                    trees_east = self.trees_east_of(i,j)
                    directions = [trees_north,trees_west,trees_south,trees_east]
                    if any([self.no_higher_than(this_tree,direction) for direction in directions]):
                        visible[j][i] = 1
        
        return visible

    def print(self):
        for row in self.trees:
            print(row)

    def part_1(self):

        visible = self.get_visibility_map()

        return sum(i for row in visible for i in row)

    def viewing_distance(self,this_tree,trees):
        distance = len(trees)
        if distance == 0:
            return 0
        for s,tree in enumerate(trees):
            if tree>=this_tree:
                return s+1
        return distance
    
    def part_2(self):

        max_vd = 0

        for j in range(len(self.trees)):
            for i in range(len(self.trees[j])):
                
                this_tree = self.trees[j][i]
                north_vd = self.viewing_distance(this_tree,self.trees_north_of(i,j))
                west_vd = self.viewing_distance(this_tree,self.trees_west_of(i,j))
                south_vd = self.viewing_distance(this_tree,self.trees_south_of(i,j))
                east_vd = self.viewing_distance(this_tree,self.trees_east_of(i,j))
                vd = north_vd * west_vd * south_vd * east_vd

                max_vd = max(max_vd,vd)

        return max_vd

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input8.txt')) as puzzle_input:

        forest = Forest(puzzle_input)
    
    print(forest.part_1())
    print(forest.part_2())
