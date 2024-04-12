import os
import solution

# Set input and output directories to the current directory
INPUT_DIR = 'PL-RESOLUTION\source\input'
OUTPUT_DIR = 'PL-RESOLUTION\source\output'

def readKB(filename):
    content = []
    with open(filename, 'r') as f:
        # Skip the first line
        next(f)
        content = f.read().splitlines()

    alpha_size = len(content)
    query_string = content[:alpha_size]
    query = []
    for cnf in query_string:
        clause = cnf.split()
        clause = list(filter(lambda x: x != 'OR', clause))
        query.append(clause)

    KB = solution.KnowledgeBase()
    KB_size = 0  # No need to read this value anymore
    KB_string = content[alpha_size + 1:]
    for cnf in KB_string:
        clause = cnf.split()
        clause = list(filter(lambda x: x != 'OR', clause))
        KB.addClause(clause)

    return KB, query

# No changes needed in the writeOutput function
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
# Get list of input files in the current directory
inputs = os.listdir(INPUT_DIR)

for filename in inputs:
    # Read KB and query from input file
    KB, query = readKB(INPUT_DIR +'\\' + filename)
    # Perform PL resolution and get result
    result, check = KB.PL_Resolution(query)
    # Write output to a file in the same directory
    writeOutput(result, check, OUTPUT_DIR + '\\' + filename)
