# data_pointer stores where the program is pointing to in memory
data_pointer = 0
# instruction_pointer stores where the program is pointing to in the instructions
instruction_pointer = 0
# program stores the instructions of the program
program = ""
# memory stores the memory of the program as an infititely long list of 1 byte numbers
memory = [0]

def increment_data_pointer():
    # If the data_pointer is at the end of currently used memory then it needs to create a new value in the list
    if data_pointer == len(memory)-1:
        memory.append(0)
        data_pointer += 1
    else:
        data_pointer += 1

def decrement_data_pointer():
    # If the data_pointer is at the first index then it doesn't go further because the index starts at 0 and has an undefined length
    if data_pointer != 0:
        data_pointer -= 1

def increment_data():
    # Increment the data at the current data_pointer by 1 and overflow if it goes above 255, has to be done manually because python doesn't have UINT8 variables
    if memory[data_pointer] == 255:
        memory[data_pointer] = 0
    else:
        memory[data_pointer] += 1

def decrement_data():
    # Decrement the data at the current data_pointer by 1 and overflow if it goes below 0, has to be doen manually because python doesn't have UINT8 variables
    if memory[data_pointer] == 0:
        memory[data_pointer] = 255
    else:
        memory[data_pointer] -= 1

def output_character():
    # Prints the ascii representation of the current value at the data_pointer
    character = chr(memory[data_pointer])
    print(character)

def input_character():
    # Stores the ascii representation of the inputted value at the data_pointer
    character = ord(input())
    memory[data_pointer] = character

def increment_instruction_pointer():
    if instruction_pointer == len(program)-1:
        print("End of File")
    else:
        instruction_pointer += 1

def decrement_instruction_pointer():
    if instruction_pointer == 0:
        print("Start of File")
    else:
        instruction_pointer -= 1

def jump_forward():
    if memory[data_pointer] == 0:
        bracket_pairs = 0
        increment_instruction_pointer()
        while not(bracket_pairs == 0 and program[instruction_pointer] == "]"):
            if program[instruction_pointer] == "[":
                bracket_pairs += 1
            elif program[instruction_pointer] == "]":
                bracket_pairs -= 1
            increment_instruction_pointer()

def jump_back():
    if memory[data_pointer] != 0:
        bracket_pairs = 0
        decrement_instruction_pointer()
        while not(bracket_pairs == 0 and program[instruction_pointer] == "["):
            if program[instruction_pointer] == "]":
                bracket_pairs += 1
            elif program[instruction_pointer] == "[":
                bracket_pairs -= 1
            decrement_instruction_pointer()

# the program needs to increment the pointer at the end of *everything* including jumping
# i also need to do global stuff