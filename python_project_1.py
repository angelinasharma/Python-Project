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

def main():
    print("Welcome to the Logic Gate Identification Game!")
    print("You will be shown a truth table, and you have to guess the corresponding logic gate.\n")

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

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
