import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))

    time_values = np.linspace(0, 10, 50)
    temperature_user_input = quadratic_model(time_values, a, b, c)

    plt.plot(time_values, temperature_user_input, label='User-input Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (User-input Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
