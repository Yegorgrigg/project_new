import json
from ugen import line_split, read_file, create_username, put_answer, main_function

class LenError(Exception):
    ...


def get_data(testname):
    with open('test_data.json') as data:
        data_dict = json.load(data)
        input_list = data_dict[testname]['inputs']
        output_list = data_dict[testname]['outputs']
    return input_list, output_list

print(get_data('linesplit'))


def test_line_split():
    input_list,output_list = get_data('linesplit')
    if len(input_list) == len(output_list):
        for i in range(0, len(input_list)):
            assert line_split(input_list[i]) == output_list[i]
    else:
        raise LenError('длинна инпут и аутпут данных не совпадает')

def test_read_file():
    input_list,output_list = get_data('readfile')
    if len(input_list) == len(output_list):
        for i in range(0, len(input_list)):
            assert read_file(input_list[i]) == output_list[i]
    else:
        raise LenError('длинна инпут и аутпут данных не совпадает')

def test_creat_username():
    input_list,output_list = get_data('createusername')
    if len(input_list) == len(output_list):
        for i in range(0, len(input_list)):
            assert create_username(input_list[i]) == output_list[i]
    else:
        raise LenError('длинна инпут и аутпут данных не совпадает')

def test_put_answer():
    input_list,output_list = get_data('putanswer')
    for i in range(0, len(input_list)):
         put_answer(input_list[i][0], input_list[i][1])

def test_main_function():
    input_list,output_list = get_data('mainfunction')
    main_function(*input_list)
    with open(input_list[0]) as res:
        text = res.readlines()
        assert text == output_list
    open(input_list[0], 'w').close()