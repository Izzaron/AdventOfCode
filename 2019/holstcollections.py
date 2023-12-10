from sortedcontainers import SortedKeyList
from typing import TypeVar, Generic

T = TypeVar('T')

class ValueSortedDict(Generic[T]):
    
    def __init__(self,tuple_list: list[tuple[T,int]]) -> None:
        self.sorted_list = SortedKeyList(tuple_list,lambda x: x[1])
        self.dict = dict(self.sorted_list)
    
    def __str__(self) -> str:
        return '{' + ', '.join('{}: {}'.format(k.__repr__(),v.__repr__()) for k,v in self.sorted_list) + '}'
    
    def __contains__(self,key: T) -> bool:
        return key in self.dict

    def __setitem__(self,key: T, newvalue: int) -> None:
        if key in self:
            self.sorted_list.remove((key,self.dict[key]))
        self.dict[key] = newvalue
        self.sorted_list.add((key,newvalue))
    
    def __getitem__(self,key: T) -> int:
        return self.dict[key]

    def __len__(self) -> int:
        return self.dict.__len__()
    
    def pop(self,i: int = -1) -> tuple[T,int]:
        item = self.sorted_list.pop(i)
        del self.dict[item[0]]
        return item
    
    def peek(self,i: int) -> tuple[T,int]:
        return self.sorted_list[i]
    
if __name__ == '__main__':
    d = ValueSortedDict([('a',3),('b',5),('c',2)])
    print('a' in d)
    d['z'] = -5
    print('z' in d)
    print(d)
    while(d):
        print(d.pop())