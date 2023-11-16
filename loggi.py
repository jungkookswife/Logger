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

