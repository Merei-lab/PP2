#1
def a(b):
    ounces = 28.3495231 * b
    return ounces
print(a(int(input("Enter grams: "))))

#2
def s(c):
    f= (c * 9/5) + 32
    return f
print(s(int(input("Enter celsius: "))))

#3
def solve(heads, legs):
 
  for rabbits in range(heads + 1): 
    chickens = heads - rabbits 
    total_legs = rabbits * 4 + chickens * 2  
    if total_legs == legs:
      return chickens, rabbits  

  return None, None 
print(solve(35, 94))
#4
def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers_string):
    
    numbers = [int(x) for x in numbers_string.split()]  
    prime_numbers = [number for number in numbers if is_prime(number)]  
    return prime_numbers



numbers_string = "2 3 4 5 6 7 8 9 10 11 12 13"
prime_numbers = filter_prime(numbers_string)
print(prime_numbers)  # Вывод: [2, 3, 5, 7, 11, 13]

numbers_string = "15 20 25 30 35"
prime_numbers = filter_prime(numbers_string)
print(prime_numbers) 

numbers_string = "2 3 5 7 11 13 17 19"
prime_numbers = filter_prime(numbers_string)
print(prime_numbers) 
#5
import itertools

def print_string_permutations(input_string):
  
    permutations = itertools.permutations(input_string) 
    for permutation in permutations:
        print(''.join(permutation))  

input_string = input("Введите строку: ")


print_string_permutations(input_string)
#6
def reverse_words(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

input_string = input("Введите строку: ")
reversed_string = reverse_words(input_string)
print(reversed_string)
#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
#8
def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
#9
import math

def sphere_volume(radius):
  
  return (4/3) * math.pi * (radius**3)
a=int(input("Enter radius: "))
print(sphere_volume(a))
#10
def unique_list(input_list):
  unique_elements = []
  for item in input_list:
    if item not in unique_elements:
      unique_elements.append(item)
  return unique_elements

input_string = input("Введите числа, разделенные пробелами: ")
numbers = [int(x) for x in input_string.split()] 
unique_numbers = unique_list(numbers)
print(f"Список уникальных элементов: {unique_numbers}")
#11
def is_palindrome(text):

  processed_text = ''.join(text.lower().split())  
  return processed_text == processed_text[::-1]  
print(is_palindrome("aappaa"))
#12
def histogram(data):
  
  for value in data:
    print('*' * value)
histogram([1,2,3])
#13
import random

def guess_the_number():
    """Plays the 'Guess the number' game."""

    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        try:
            guess = int(input("Take a guess.\n"))
            guesses_taken += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
                break  

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")

guess_the_number()