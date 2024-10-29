import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def maclaurin_approximation():
    st.title("Aproximación de Funciones con Series de MacLaurin")

    # Entrada de la función y grado del polinomio
    func_input = st.text_input("Introduce la función a aproximar (en términos de x):", "sin(x)")
    n = st.number_input("Grado del polinomio de MacLaurin:", min_value=1, max_value=10, value=3)

    if func_input:
        x = sp.symbols('x')
        f = sp.sympify(func_input)

        # Cálculo de la serie de MacLaurin
        maclaurin_series = sum([f.diff(x, i).subs(x, 0) / sp.factorial(i) * x**i for i in range(n + 1)])
        
        # Mostrar la serie resultante
        st.subheader("Aproximación de MacLaurin:")
        st.latex(sp.latex(maclaurin_series))

        # Calcular el error en un rango de valores
        x_values = np.linspace(-2, 2, 100)
        real_values = [float(f.evalf(subs={x: val})) for val in x_values]
        approx_values = [float(maclaurin_series.evalf(subs={x: val})) for val in x_values]
        errors = [abs(real - approx) for real, approx in zip(real_values, approx_values)]

        # Calcular error de truncación
        truncation_errors = []
        for val in x_values:
            term = (f.diff(x, n + 1).subs(x, val) / sp.factorial(n + 1)) * (val ** (n + 1))
            truncation_errors.append(float(abs(term)))

        # Gráfica de comparación
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Gráfico de la función real y la aproximación
        ax1.plot(x_values, real_values, label='Función Real', color='blue')
        ax1.plot(x_values, approx_values, '--', label='Aproximación de MacLaurin', color='red')
        ax1.set_title('Comparación: Función Real vs Aproximación')
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.legend()
        ax1.grid(True)

        # Gráfico del error
        ax2.plot(x_values, errors, label='Error de Aproximación', color='green', linestyle='--')
        ax2.plot(x_values, truncation_errors, label='Error de Truncación', color='orange')
        ax2.set_title('Errores de Aproximación y Truncación')
        ax2.set_xlabel('x')
        ax2.set_ylabel('Error')
        ax2.legend()
        ax2.grid(True)

        st.pyplot(fig)

maclaurin_approximation()
