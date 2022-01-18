# В файле `input.txt` будет содержаться текст, переверните каждое слово (непробельные символы)
# задом наперёд и запишите в этот же файл.
#
# Вы можете открыть файл на чтение-и-запись, читать построчно и сразу же записывать обработанную
# строку на исходное место; для этого пригодятся функции `file.tell()` и `file.seek()` - чтения
# и установки текущего положения.
#
# Или же сперва прочитать весь файл, обработать, и перезаписать.


def reverse_string(s):
    words = s.split(' ')
    reversed_words = []
    n = ''
    for word in words:
        if word.endswith('\n'):
            word = word.replace('\n', '')
            n = word[::-1] + '\n'
            reversed_words.append(n)
            continue
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 2


num_lines = file_len('text.txt')
f2 = open("text1.txt", "w")
with open("text.txt", "r") as myfile:
    for _ in range(num_lines - 1):
        data = myfile.readline()
        data_2 = reverse_string(data)
        f2.writelines(data_2)
f2.close()
