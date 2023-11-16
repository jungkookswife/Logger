import random
import logging

logging.basicConfig(filename='logi_file.log', level=logging.INFO)

def get_user_input():
    while True:
        try:
            n = int(input("Введите натуральное число: "))
            if n <= 0:
                print("Введите положительное число!")
            else:
                return n
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")

def generate_random_sequence(n):
    sequence = list(range(1, n+1))
    random.shuffle(sequence)
    return sequence

def main():
    n = get_user_input()
    sequence = generate_random_sequence(n)
    
    print("Нажмите клавишу Enter, чтобы вытащить бочонок...")
    logging.info("Последовательность: " + str(sequence))
    
    for i in range(n):
        input()
        barrel = sequence.pop(0)
        print("Бочонок ", barrel, " вытащен")
        logging.info("Бочонок " + str(barrel) + " вытащен")
    
    print("Все бочонки вытащены!")

if __name__ == '__main__':
    main()