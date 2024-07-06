import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, coefficients_file):
    with open(coefficients_file, 'r') as file:
        lines = file.readlines()
        a = float(lines[0].strip())
        b = float(lines[1].strip())
        c = float(lines[2].strip())

    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)
    coefficients_file = '5.txt' 

    temperature = quadratic_model(time_values, coefficients_file)

    plt.plot(time_values, temperature, label='File Coefficients')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (File Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
