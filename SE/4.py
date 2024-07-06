import matplotlib.pyplot as plt
import numpy as np

def quadratic_model(time, a, b, c):
    temperature = a * (time ** 2) + b * time + c
    return temperature

def main():
    time_values = np.linspace(0, 10, 50)

    coefficients_sets = [
        (0.1, -1, 30),  
        (0.2, -0.5, 25), 
        (0.05, -0.3, 28) 
    ]
    
    for i, (a, b, c) in enumerate(coefficients_sets, start=1):
        temperature = quadratic_model(time_values, a, b, c)
        plt.plot(time_values, temperature, label=f'Set {i}: a={a}, b={b}, c={c}')
    
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.title('Weather Modeling with Quadratic Equation (Multiple Sets of Coefficients)')
    plt.show()

if __name__ == "__main__":
    main()
