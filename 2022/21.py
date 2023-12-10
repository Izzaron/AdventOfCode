input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

def is_dependent_on(key,dep,commands):
    if key == dep:
        return True
    command = commands[key]
    if isinstance(command,int):
        return False
    elif isinstance(command,list):
        return is_dependent_on(command[0],dep,commands) or is_dependent_on(command[2],dep,commands)
    else:
        raise ValueError('key not int or list')

def set_value(key,value,changee,commands):
    if key == changee:
        commands[key] = value
    command = commands[key]
    if isinstance(command,int):
        return
    elif isinstance(command,float):
        return
    elif isinstance(command,list):
        change_left = True if is_dependent_on(command[0],changee,commands) else False
        op1 = command[0]
        operator = command[1]
        op2 = command[2]
        if operator == '+':
            # get_value(op1,commands) + get_value(op2,commands)
            if change_left:
                set_value(op1,value - get_value(op2,commands),changee,commands)
            else:
                set_value(op2,value - get_value(op1,commands),changee,commands)
        elif operator == '-':
            # get_value(op1,commands) - get_value(op2,commands)
            if change_left:
                set_value(op1,value + get_value(op2,commands),changee,commands)
            else:
                set_value(op2,get_value(op1,commands) - value,changee,commands)
        elif operator == '*':
            # get_value(op1,commands) * get_value(op2,commands)
            if change_left:
                set_value(op1,value / get_value(op2,commands),changee,commands)
            else:
                set_value(op2,value / get_value(op1,commands),changee,commands)
        elif operator == '/':
            # get_value(op1,commands) / get_value(op2,commands)
            if change_left:
                set_value(op1,value * get_value(op2,commands),changee,commands)
            else:
                set_value(op2,get_value(op1,commands) / value,changee,commands)
        else:
            raise ValueError('operator != +-*/')
    else:
        raise ValueError('key not int,float or list',type(command))

def get_value(key: str, commands: dict()):
    command = commands[key]
    if isinstance(command,int):
        return command
    elif isinstance(command,list):
        if command[1] == '+':
            return get_value(command[0],commands) + get_value(command[2],commands)
        elif command[1] == '-':
            return get_value(command[0],commands) - get_value(command[2],commands)
        elif command[1] == '*':
            return get_value(command[0],commands) * get_value(command[2],commands)
        elif command[1] == '/':
            return get_value(command[0],commands) / get_value(command[2],commands)
        else:
            raise ValueError('operator != +-*/')
    else:
        raise ValueError('key not int or list')

if __name__ == "__main__":

    commands = dict()

    with open(input_file) as puzzle_input:

        for line in puzzle_input:
            split_line = line.split()
            split_line[0] = split_line[0].replace(':','')
            if len(split_line) == 2:
                commands[split_line[0]] = int(split_line[1])
            elif len(split_line) == 4:
                commands[split_line[0]] = split_line[1:]
            else:
                raise ValueError('split_line len != 2 or 4')
    # part 1
    print(int(get_value('root',commands)))

    # part 2
    changee,fixed = (commands['root'][0],commands['root'][2]) if is_dependent_on(commands['root'][0],'humn',commands) else (commands['root'][1],commands['root'][0])
    set_value(changee,get_value(fixed,commands),'humn',commands)
    print(int(commands['humn']))