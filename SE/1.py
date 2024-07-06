import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time):
    a = 0.1
    b = -1
    c = 30

    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)

    temperature_hardcoded = quadratic_model(time_values)

    # print(temperature_hardcoded)
    # print(time_values)

    plt.plot(time_values, temperature_hardcoded, label = 'Hard-coded Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Hard-coded Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()