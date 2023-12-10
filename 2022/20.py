input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

class LinkedNode:
    def __init__(self,value: int) -> None:
        self.value      :int            = value
        self.previous   :'LinkedNode'   = None
        self.next       :'LinkedNode'   = None
    
    def __str__(self) -> str:
        return str(self.value)
    
    def __repr__(self) -> str:
        return self.__str__()

class LinkedList:
    def __init__(self, init_list: list[int],decryption_key: int = 1) -> None:
        self.links: list[LinkedNode] = [LinkedNode(val*decryption_key) for val in init_list]
        for i,link in enumerate(self.links):
            link.previous   = self.links[i-1]
            link.next       = self.links[(i+1)%len(self.links)]
        
    def __str__(self) -> str:
        return str(self.links)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def string(self) -> str:
        start = self.links[0]
        string = '[{}'.format(start.value)
        next_link = start.next
        while(next_link != start):
            string += ', {}'.format(next_link.value)
            next_link = next_link.next
        string += ']'
        return string

    def print(self,start: LinkedNode = None):
        if start == None:
            start = next((x for x in self.links if x.value == 0))
        print('[{}'.format(start.value),end='')
        next_link = start.next
        while(next_link != start):
            print(', {}'.format(next_link.value),end='')
            next_link = next_link.next
        print(']')
    
    def after(self, link: LinkedNode, steps: int) -> LinkedNode:
        target = link
        for _ in range(steps%len(self.links)):
            target = target.next
        return target
    
    def mix(self, times: int = 1):
        for i in range(times):
            # print('After {} round of mixing:'.format(i+1))
            for link in self.links:
                self.move(link)
            # self.print()
    
    def move(self, link: LinkedNode, steps: int = None) -> None:
        if steps == None:
            steps = link.value
        if steps%(len(self.links)-1) == 0:
            return
        link.previous.next = link.next
        link.next.previous = link.previous
        steps %= len(self.links)-1
        target = link
        for _ in range(steps):
            target = target.next
        
        link.previous = target
        link.next = target.next
        target.next.previous = link
        target.next = link

if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        links: list[int] = [int(line) for line in puzzle_input]
    
    # part 1
    linked_list = LinkedList(links)
    linked_list.mix()
    val0 = next((x for x in linked_list.links if x.value == 0), None)
    val1 = linked_list.after(val0,1000)
    val2 = linked_list.after(val0,2000)
    val3 = linked_list.after(val0,3000)
    print(val1.value+val2.value+val3.value)
    # part 2
    decryption_key = 811589153
    linked_list = LinkedList(links,decryption_key)
    linked_list.mix(10)
    val0 = next((x for x in linked_list.links if x.value == 0), None)
    val1 = linked_list.after(val0,1000)
    val2 = linked_list.after(val0,2000)
    val3 = linked_list.after(val0,3000)
    print(val1.value+val2.value+val3.value)