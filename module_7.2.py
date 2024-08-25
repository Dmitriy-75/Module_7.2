info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

def custom_write(file_name, strings):

    num = 1
    string_position_list = []
    file = open(file_name, 'a', encoding='utf-8')
    pos = (file.tell())
    for i in strings:
        string_position_list.append(((num, pos), i))
        file.write(i + '\n')
        pos = (file.tell())
        num += 1
    file.close()
    string_position=dict(string_position_list)
    return string_position

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)















