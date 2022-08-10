def array_from_text(text):
    index = 0
    array = text.lower().split()
    for i in range(len(array)):
        array[i] = array[i].strip('.,!?:;')
    for i in array:
        if i.isnumeric():
            array[index] = int(i)
        index += 1
    return array

def dictionary_of_arrays(key, array):
    dictionary = {}
    dictionary.update({key:array})
    return dictionary

def parse_input(game, text):
    array = array_from_text(text)
    dictionary = dictionary_of_arrays(game, array)
    return dictionary

def get_input(game, prompt):
    input_values = input(prompt)
    return parse_input(game, input_values)