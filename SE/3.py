import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)

    a1, b1, c1 = 0.1, -1, 30
    temperature1 = quadratic_model(time_values, a1, b1, c1)

    a2 = float(input("Enter the value of a: "))
    b2 = float(input("Enter the value of b: "))
    c2 = float(input("Enter the value of c: "))
    temperature2 = quadratic_model(time_values, a2, b2, c2)

    plt.plot(time_values, temperature1, label=f'Set 1: a={a1}, b={b1}, c={c1}')
    plt.plot(time_values, temperature2, label=f'Set 2: a={a2}, b={b2}, c={c2}')
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Two Sets of Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
