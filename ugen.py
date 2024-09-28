import argparse

def read_file(filename):
    """function to open file

    Args:
        filename(_str_): name of file, that need to be open

    Returns:
        text(_list_): list of lines from file
    """    
    try:
        if isinstance(filename, str) and filename[-4:] == '.txt':
            #file= open(filename)
            with open(filename) as file:
                text = file.readlines()
                return text
        else:
            print(f'Непрваильно указано название файла {filename} !')
    except FileNotFoundError as e:
        print(e)
        


def line_split(line):
    """spliting line

    Args:
        line (_str_): text, that need to be splited

    Returns:
        list(_list_): list of objects from line
    """        
    if isinstance(line, str) and ':' in line:
        list = line.split(':')
        if len(list) == 5:
            return list
    
def create_username(list):
    """creating username from name, second name(if it is), surname

    Args:
        list (_list_): list of information

    Returns:
        username(_str_): username
    """       
    if list is not None and len(list)>0:
        username = list[1][0]
        username += list[2][:1]
        username += list[3]
        username = username.lower()[:8] 
    else:
        username = 'incorrect_data'         
    # else:
    #     username += list[3][0:7]
    return username

def put_answer(file_name, answer):
    """putin result into new file

    Args:
        file_name (_str_): name of file, that need to get answer
        answer (_str_): thing, that need to be puted
    """    
    try:
        if isinstance(file_name, str) and file_name[-4:] == '.txt' and isinstance(answer, str):
            file = open(file_name, 'a')
            file.write(answer)
            file.close()
        else:
            print(f'Непрваильно указано название файла {file_name} или ответ {answer} не является текстом !')
    except FileNotFoundError as e:
        print(e)

def main_function(output_file_name, *input_file_name):
    """function for recreating line from one file, and puting result to another file

    Args:
        output_file_name (_str_): name of output file
        input_file_name (_str_): name of input file
    """      
    username_list = {}
    
    for i in input_file_name:
        text = read_file(i)
        for x in text:
            line = line_split(x) 
            username = create_username(line)
            if username in username_list:
                username += str(username_list[username])
                username_list[username[:-1]] += 1
            else:
                username_list[username] = 1
            if line is not None:
                line.insert(1, username)
                text_line = ':'.join(line)
            else:
                text_line = username + '\n'
            put_answer(output_file_name,text_line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        prog='ugen.py',
                        description='recraet line< make username',
                        epilog='Text at the bottom of help'
    )

    parser.add_argument('input_file', nargs="+", help='write your input file')
    parser.add_argument('-o', '--output_file', help = 'write your output file')

    args = parser.parse_args()

    main_function(args.output_file, *args.input_file)
