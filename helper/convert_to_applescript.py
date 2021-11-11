main_arr = []
build = '''on run {input, parameters}

    delay 5'''

with open("chess_model.py", "r") as f:

    for i in f.readlines():
        if len(i) > 0 and i[0] != "#":
            main_arr.append(list(i))
        else:
            main_arr.append(i)

for n, arr_build in enumerate(main_arr):

    if arr_build != "":

        if arr_build[0] == "#":
            single_list = '"#---------------------"}'

        else:
            single_list = ''
            for x in arr_build:
                if x == '"':
                    single_list += f'"\{x}",'
                elif x == "\\":
                    single_list += f'"{x}{x}",'
                else:
                    single_list += f'"{x}",' if x != '"' else f'"\{x}",'
        
        build += f'''
    
    set list{n} to {{ {single_list[:-1]} }}

    repeat with a from 1 to length of list{n}
        set theCurrentListItem to item a of list{n}
        tell application "System Events" to keystroke theCurrentListItem
        delay 0.03
    end repeat

    tell application "System Events" to keystroke (key code 76)
    delay 0.1'''
        
    else:

        build += f'''
    tell application "System Events" to keystroke (key code 76)'''

build += '''

    return input

end run'''

with open('helper/applescript.scpt', 'w') as f:
    f.write(build)
