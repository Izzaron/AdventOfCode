import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class FileSystem:
    def __init__(self) -> None:
        self.filesystem = dict()
        self.folders = set()

    def build(self,commands):

        current_dir = ''
        l = 0
        while(l<len(commands)):
            
            command = commands[l].strip().split()
            
            if command[0] != '$':
                raise ValueError('Unexpected not $: \"' + commands[l].strip() + "\"")

            if command[1] == 'cd':
                if command[2] == '..':
                    current_dir = '/'.join(current_dir.split('/')[:-1])
                else:
                    if command[2] == '/':
                        current_dir = '/'
                    else:
                        self.create_folder(current_dir,command[2])
                        current_dir += '/'+command[2]
                l += 1
            elif command[1] == 'ls':
                l += 1
                while(l<len(commands) and commands[l][0] != '$'):
                    item = commands[l].strip().split()
                    if item[0] == '$':
                        continue
                    if item[0] == 'dir':
                        self.create_folder(current_dir,item[1])
                    else:
                        self.create_file(current_dir,item[1],int(item[0]))
                    l += 1
            else:
                raise ValueError('Unexpected command: ',command[1])
    
    def get_item(self,path: str):
        current_item = self.filesystem
        for item_name in path.split('/'):
            if item_name == '':
                continue
            current_item = current_item[item_name]
        return current_item

    def create_folder(self,path: str,name:str) -> None:
        current_directory = self.filesystem
        for folder_name in path.split('/'):
            if folder_name == '':
                continue
            if not folder_name in current_directory:
                current_directory[folder_name] = dict()
            current_directory = current_directory[folder_name]
        current_directory[name] = dict()
        self.folders.add(path+'/'+name)
    
    def create_file(self,path: str,name: str,size: int) -> None:
        self.get_item(path)[name] = size

    def print_folders(self,path='/',pre=''):
        if path == '/':
            print('/')
        else:
            print(pre,path.split('/')[-1])
        for name,item in self.get_item(path).items():
            if isinstance(item,dict):
                self.print_folders(path+'/'+name,pre+'-')
    
    def print(self,path='/',pre=''):
        if path == '/':
            print('/','(dir)')
        else:
            print(pre,path.split('/')[-1],'(dir)')
        for name,item in self.get_item(path).items():
            if isinstance(item,dict):
                self.print(path+'/'+name,pre+'-')
            else:
                print(pre+'-',name,'(file, size=',item,')')

    def size_of(self,path: str = '/'):

        item = self.get_item(path)

        if isinstance(item,int):
            return item

        if len(item) == 0:
            return 0
        
        total_size = 0
        for item_name in item:
            total_size += self.size_of(path+'/'+item_name)
        return total_size
    
    def part1(self):
        return sum(self.size_of(folder_path) for folder_path in self.folders if self.size_of(folder_path)<=100000)
    
    def part2(self):
        sizes = [self.size_of(folder_path) for folder_path in self.folders]

        sizes.sort()

        total = 70000000
        used = self.size_of()
        free = total - used

        for folder_size in sizes:
            if free + folder_size > 30000000:
                return folder_size

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input7.txt')) as puzzle_input:

        commands = puzzle_input.readlines()

    filesystem = FileSystem()
    filesystem.build(commands)

    # print(filesystem.part1())
    print(filesystem.part2())