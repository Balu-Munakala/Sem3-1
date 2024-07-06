import matplotlib.pyplot as plt
import numpy as np

def quadratic_model_hardcoded(time):
    a = 0.1
    b = -1
    c = 30
    temperature = a * (time ** 2) + b * time + c
    return temperature

def quadratic_model_user_input(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def quadratic_model_multiple_sets(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def quadratic_model_file_input(time, coefficients_file):
    with open(coefficients_file, 'r') as file:
        lines = file.readlines()
        a = float(lines[0].strip())
        b = float(lines[1].strip())
        c = float(lines[2].strip())
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    # Code 1: Hard-coded coefficients
    time_values = np.linspace(0, 10, 50)
    temperature_hardcoded = quadratic_model_hardcoded(time_values)
    plt.figure()
    plt.plot(time_values, temperature_hardcoded, label='Hard-coded Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Hard-coded Coefficients)')
    plt.show()

    # Code 2: User input coefficients
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    temperature_user_input = quadratic_model_user_input(time_values, a, b, c)
    plt.figure()
    plt.plot(time_values, temperature_user_input, label='User-input Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (User-input Coefficients)')
    plt.show()

    # Code 3: Multiple sets of coefficients
    coefficients_sets = [
        (0.1, -1, 30),
        (0.2, -0.5, 25),
        (0.05, -0.3, 28)
    ]
    plt.figure()
    for i, (a, b, c) in enumerate(coefficients_sets, start=1):
        temperature = quadratic_model_multiple_sets(time_values, a, b, c)
        plt.plot(time_values, temperature, label=f'Set {i}: a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Multiple Sets of Coefficients)')
    plt.show()

    # Code 4: File input coefficients
    coefficients_file = '5.txt'
    temperature_file_input = quadratic_model_file_input(time_values, coefficients_file)
    plt.figure()
    plt.plot(time_values, temperature_file_input, label='File Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (File Coefficients)')
    plt.show()

    # Code 5: Multiple sets of coefficients from file
    coefficients_file_multiple = '6.txt'
    with open(coefficients_file_multiple, 'r') as file:
        lines = file.readlines()
    plt.figure()
    for i, line in enumerate(lines, start=1):
        a, b, c = map(float, line.strip().split())
        temperature = quadratic_model_multiple_sets(time_values, a, b, c)
        plt.plot(time_values, temperature, label=f'Set {i}: a={a}, b={b}, c={c}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Multiple Sets of Coefficients from File)')
    plt.show()

    # Code 6: Both hard-coded and user input coefficients
    temperature1_hardcoded = quadratic_model_hardcoded(time_values)
    x = float(input("Enter the value of a: "))
    y = float(input("Enter the value of b: "))
    z = float(input("Enter the value of c: "))
    temperature2_user_input = quadratic_model_user_input(time_values, x, y, z)
    plt.plot(time_values, temperature1_hardcoded, label='Hard-Coded Coefficients: a=0.1, b=-1, c=30')
    plt.plot(time_values, temperature2_user_input, label=f'User-input Coefficients: a={x}, b={y}, c={z}')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Both User-input and Hard-coded Coefficients from File)')
    plt.show()


if __name__ == "__main__":
    main()
