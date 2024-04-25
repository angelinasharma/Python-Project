import random

logic_gates = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "XOR": lambda x, y: x ^ y,
    "NOT": lambda x: not x
}

def generate_truth_table(logic_gate):
    if logic_gate == "NOT":
        return [(x, logic_gates[logic_gate](x)) for x in (0, 1)]
    else:
        return [(x, y, logic_gates[logic_gate](x, y)) for x in (0, 1) for y in (0, 1)]

def display_truth_table(truth_table):
    if len(truth_table[0]) == 2:
        print("Input | Output")
        print("-" * 13)
        for input_val, output_val in truth_table:
            print(f"  {input_val}   |   {output_val}")
    else:
        print("Input1 | Input2 | Output")
        print("-" * 20)
        for input1_val, input2_val, output_val in truth_table:
            print(f"   {input1_val}   |   {input2_val}    |   {output_val}")

def get_user_input():
    while True:
        user_input = input("\nGuess the logic gate (AND, OR, XOR, NOT): ").strip().upper()
        if user_input in logic_gates:
            return user_input
        else:
            print("Invalid input. Please enter a valid logic gate.")

def learn_about_logic_gates():
    print("\nLogic gates are the building blocks of digital circuits.")
    print("They perform logical operations on one or more binary inputs and produce a binary output.")

    while True:
        print("\nWhich logic gate would you like to learn about? (AND, OR, XOR, NOT, NAND, NOR, XNOR)")
        user_input = input("Enter the name of the logic gate or type 'exit' to quit: ").strip().upper()

        if user_input == "AND":
            print("\nThe AND gate produces a high output (1) only if all of its inputs are high (1).")
            print("Here is the truth table for the AND gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   0")
            print("   0    |    1     |   0")
            print("   1    |    0     |   0")
            print("   1    |    1     |   1")

        elif user_input == "OR":
            print("\nThe OR gate produces a high output (1) if any of its inputs are high (1).")
            print("Here is the truth table for the OR gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   0")
            print("   0    |    1     |   1")
            print("   1    |    0     |   1")
            print("   1    |    1     |   1")

        elif user_input == "XOR":
            print("\nThe XOR gate produces a high output (1) if one, and only one, of its inputs is high (1).")
            print("Here is the truth table for the XOR gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   0")
            print("   0    |    1     |   1")
            print("   1    |    0     |   1")
            print("   1    |    1     |   0")

        elif user_input == "NOT":
            print("\nThe NOT gate, also known as an inverter, produces the opposite output of its input.")
            print("Here is the truth table for the NOT gate:")
            print("Input A | Output")
            print("--------|--------")
            print("   0    |   1")
            print("   1    |   0")

        elif user_input == "NAND":
            print("\nThe NAND gate, also known as a shepherd's gate, produces the inverse of the AND operation.")
            print("Here is the truth table for the NAND gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   1")
            print("   0    |    1     |   1")
            print("   1    |    0     |   1")
            print("   1    |    1     |   0")

        elif user_input == "NOR":
            print("\nThe NOR gate, also known as a bubbled OR gate, produces the inverse of the OR operation.")
            print("Here is the truth table for the NOR gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   1")
            print("   0    |    1     |   0")
            print("   1    |    0     |   0")
            print("   1    |    1     |   0")

        elif user_input == "XNOR":
            print("\nThe XNOR gate, also known as the exclusive NOR gate, produces the inverse of the XOR operation.")
            print("Here is the truth table for the XNOR gate:")
            print("Input A | Input B | Output")
            print("--------|----------|--------")
            print("   0    |    0     |   1")
            print("   0    |    1     |   0")
            print("   1    |    0     |   0")
            print("   1    |    1     |   1")

        elif user_input == "EXIT":
            break

        else:
            print("Invalid input. Please enter the name of a logic gate or type 'exit' to quit.")


def main():
    print("Welcome to the Logic Gate Identification Game!")
    print("You will be shown a truth table, and you have to guess the corresponding logic gate.\n")

    while True:
        print("\nSelect an option:")
        print("1. Play the game")
        print("2. Learn about logic gates")
        print("3. Exit")

        user_choice = input("Enter your choice (1/2/3): ").strip()

        if user_choice == "1":
            while True:
                random_gate = random.choice(list(logic_gates.keys()))
                truth_table = generate_truth_table(random_gate)
                display_truth_table(truth_table)

                user_guess = get_user_input()

                if user_guess == random_gate:
                    print("Congratulations! You guessed correctly.")
                else:
                    print(f"Sorry, the correct answer is {random_gate}.")

                play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
                if play_again != "yes":
                    break

        elif user_choice == "2":
            learn_about_logic_gates()

        elif user_choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
