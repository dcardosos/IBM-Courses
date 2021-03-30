# write a file, mod "w"

lines = ['eu sou o douglas \n', 'a raissa \n', 'não, o guibs \n']

with open('example_text1.txt', 'w', encoding='UTF-8') as file1:
    for line in lines:
        file1.write(line)

    file1.close()

# append a file, mod 'a'
with open('example_text1.txt', 'a') as file1:
    file1.write('hahahaha vdd')
    file1.close()

# read a file, mod 'r'
with open('example_text1.txt', 'r') as file1:
    file_stuff = file1.read()
    print(file_stuff)

print(file_stuff)

# method readlines, serve para ler cada linha, podendo especificar quantas strings
with open('example_text1.txt', 'r') as file1:
    # coloca todas as linhas em uma lista
    file_line = file1.readlines()
    print(file_line)

    # printando todas as linhas
    for line in file1.readlines():
        print(line)

    # le apenas as 4 primeiras letras da, no caso, terceira linha
    file_line = file1.readlines(4)
    print(file_line)

# copy a file

with open('example_text1.txt', 'r') as readfile:
    with open('example2', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

        writefile.close()
    readfile.close()
