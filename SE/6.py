import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)
    coefficients_file = '6.txt'

    with open(coefficients_file, 'r') as file:
        lines = file.readlines()
    
    a1, b1, c1 = map(float, lines[0].strip().split())
    temperature1 = quadratic_model(time_values, a1, b1, c1)

    a2, b2, c2 = map(float, lines[1].strip().split())
    temperature2 = quadratic_model(time_values, a2, b2, c2)

    a3, b3, c3 = map(float, lines[2].strip().split())
    temperature3 = quadratic_model(time_values, a3, b3, c3)

    plt.plot(time_values, temperature1, label=f'Set 1: a={a1}, b={b1}, c={c1}')
    plt.plot(time_values, temperature2, label=f'Set 2: a={a2}, b={b2}, c={c2}')
    plt.plot(time_values, temperature3, label=f'Set 3: a={a3}, b={b2}, c={c3}')
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Multiple Sets of Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
