import os
import solution

INPUT_DIR = 'PL-RESOLUTION\input'
OUTPUT_DIR = 'PL-RESOLUTION\output'

def readKB(filename):
    content = []
    with open(filename, 'r') as f:
        content = f.read().splitlines()

    alpha_size = 1  #
    query = [content[0].split()]  
    KB = solution.KnowledgeBase()

    KB_string = content[2:]  #
    for cnf in KB_string:
        clause = cnf.split()
        clause = list(filter(lambda x: x != 'OR', clause))
        KB.addClause(clause)

    return KB, query


def writeOutput(result, check, filename):
    with open(filename, 'w') as f:
        for loop_res in result:
            f.write(str(len(loop_res)) + '\n')
            for clause in loop_res:
                string = ''
                for c in clause:
                    string += c
                    if c != clause[-1]:
                        string += ' OR '
                f.write(string + '\n')
        if check:
            f.write('YES')
        else:
            f.write('NO')

inputs = os.listdir(INPUT_DIR)

for filename in inputs:
    KB, query = readKB(INPUT_DIR +'\\' + filename)
    result, check = KB.PL_Resolution(query)
    writeOutput(result, check, OUTPUT_DIR + '\\' 'output-' + filename)
