# data_pointer stores where the program is pointing to in memory
data_pointer = 0
# instruction_pointer stores where the program is pointing to in the instructions
instruction_pointer = 0
# program stores the instructions of the program
program = """++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."""
# memory stores the memory of the program as an infititely long list of 1 byte numbers
memory = [0]
# output_memory saves what needs to be outputted
output_memory = ""

def increment_data_pointer():
    global data_pointer, memory
    # If the data_pointer is at the end of currently used memory then it needs to create a new value in the list
    if data_pointer == len(memory)-1:
        memory.append(0)
        data_pointer += 1
    else:
        data_pointer += 1

def decrement_data_pointer():
    global data_pointer
    # If the data_pointer is at the first index then it doesn't go further because the index starts at 0 and has an undefined length
    if data_pointer != 0:
        data_pointer -= 1

def increment_data():
    global memory
    # Increment the data at the current data_pointer by 1 and overflow if it goes above 255, has to be done manually because python doesn't have UINT8 variables
    if memory[data_pointer] == 255:
        memory[data_pointer] = 0
    else:
        memory[data_pointer] += 1

def decrement_data():
    global memory
    # Decrement the data at the current data_pointer by 1 and overflow if it goes below 0, has to be doen manually because python doesn't have UINT8 variables
    if memory[data_pointer] == 0:
        memory[data_pointer] = 255
    else:
        memory[data_pointer] -= 1

def output_character():
    global output_memory
    # Prints the ascii representation of the current value at the data_pointer

    if memory[data_pointer] == 10:
        print(output_memory)
        output_memory = ""
    else:
        character = chr(memory[data_pointer])
        output_memory += character

def input_character():
    global memory, output_memory
    # Stores the ascii representation of the inputted value at the data_pointer
    print(output_memory)
    output_memory = ""
    character = ord(input())
    memory[data_pointer] = character

def increment_instruction_pointer():
    global instruction_pointer
    if instruction_pointer == len(program)-1:
        print("EOF")
        quit()
    else:
        instruction_pointer += 1

def decrement_instruction_pointer():
    global instruction_pointer
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

def main():
    while True:
        if program[instruction_pointer] == ">":
            increment_data_pointer()
        elif program[instruction_pointer] == "<":
            decrement_data_pointer()
        elif program[instruction_pointer] == "+":
            increment_data()
        elif program[instruction_pointer] == "-":
            decrement_data()
        elif program[instruction_pointer] == ".":
            output_character()
        elif program[instruction_pointer] == ",":
            input_character()
        elif program[instruction_pointer] == "[":
            jump_forward()
        elif program[instruction_pointer] == "]":
            jump_back()
        increment_instruction_pointer()

main()