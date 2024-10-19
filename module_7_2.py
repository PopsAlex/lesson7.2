def custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as file:
        string_position = {}
        index = 0
        for i in strings:
            index += 1
            tell = file.tell()
            file.write(f'{i}\n')
            _key = (index, tell)
            string_position[_key] = i
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)