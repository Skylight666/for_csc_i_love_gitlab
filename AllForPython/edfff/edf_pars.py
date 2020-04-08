import os
import re

inp = input()
onlyfiles = [f for f in os.listdir(inp) if os.path.isfile(os.path.join(inp, f)) and '.edf' == os.path.splitext(f)[1]]

pattern = r'(dp)(\s+(|\-)\d+\.\d+){3}'

for fl in onlyfiles:
    array_of_correct_lines = []
    number_of_lines_in_block = []
    flag = False
    counter = 0
    incr = 1
    with open(os.path.join(inp, fl), 'r') as f:
        for line in f:
            mb = re.match(pattern, line)
            if (mb and not flag):
                flag = True
                if (number_of_lines_in_block):
                    number_of_lines_in_block.append(1+number_of_lines_in_block[counter-1])
                else:
                    number_of_lines_in_block.append(1)
                counter += 1
                array_of_correct_lines.append(mb.group(0))
            elif (not mb):
                flag = False
            elif (mb):
                number_of_lines_in_block[counter-1] += 1
                array_of_correct_lines.append(mb.group(0))

    name_txt = os.path.splitext(fl)[0]+'.txt'
    path_txt = os.path.join(inp, name_txt)

    #print(counter)

    # for i in range(counter):
    #     print(number_of_lines_in_block[i])

    new_counter = 0

    for n, line in enumerate(array_of_correct_lines):
        if (new_counter < counter and n < number_of_lines_in_block[new_counter]):
            array_of_correct_lines[n] = str(new_counter+1) + line[2:]
        else:
            new_counter += 1
            array_of_correct_lines[n] = str(new_counter+1) + line[2:]

    with open(path_txt, 'w') as f:
        for line in array_of_correct_lines:
          f.write(f"{line}\n")
