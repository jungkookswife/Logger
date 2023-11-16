import random
import logging

logging.basicConfig(filename='logi_file.log', level=logging.INFO)

def get_user_input():
    while True:
        try:
            n = int(input("Enter a natural number: "))
            if n <= 0:
                print("Please enter a positive number!")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_random_sequence(n):
    sequence = list(range(1, n+1))
    random.shuffle(sequence)
    return sequence

def main():
    n = get_user_input()
    sequence = generate_random_sequence(n)
    
    print("Press any key to draw a barrel...")
    logging.info("Sequence: " + str(sequence))
    
    for i in range(n):
        input()
        barrel = sequence.pop(0)
        print("Barrel ", barrel, " is drawn")
        logging.info("Barrel " + str(barrel) + " is drawn")
    
    print("All the barrels have been drawn!")

if __name__ == '__main__':
    main()