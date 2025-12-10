import math
import numpy as np
import matplotlib.pyplot as plt

class FuncionTrigonometrica:
    def __init__(self, tipo_funcion, amplitud=1.0, periodo=2 * math.pi):
        # Atributos [cite: 22, 23]
        self.tipo_funcion = tipo_funcion.lower()
        self.amplitud = amplitud
        self.periodo = periodo
        self.validar_tipo()

    def validar_tipo(self):
        if self.tipo_funcion not in ['seno', 'coseno', 'tangente']:
            raise ValueError("Tipo de función no soportado. Use 'seno', 'coseno', o 'tangente'.")

    def __str__(self):
        omega = 2 * math.pi / self.periodo
        # Representación de texto de la función trigonométrica [cite: 29]
        return f"f(x) = {self.amplitud} * {self.tipo_funcion}({omega:.2f} * x)"

    def evaluar(self, x_radianes):
        # Método para evaluar la función trigonométrica en un valor x [cite: 25]
        omega = 2 * math.pi / self.periodo
        argumento = omega * x_radianes
        
        if self.tipo_funcion == 'seno':
            return self.amplitud * math.sin(argumento)
        elif self.tipo_funcion == 'coseno':
            return self.amplitud * math.cos(argumento)
        elif self.tipo_funcion == 'tangente':
            return self.amplitud * math.tan(argumento)
        
    def valor_critico(self):
        # Método para devolver un valor crítico de la función [cite: 30]
        if self.tipo_funcion in ['seno', 'coseno']:
            # El valor máximo para seno y coseno es la amplitud.
            return f"Máximo Absoluto: {self.amplitud}"
        elif self.tipo_funcion == 'tangente':
            return "La función tangente no tiene un máximo o mínimo absoluto."
        
    def graficar(self, x_min=-2*math.pi, x_max=2*math.pi, num_puntos=400):
        
        # Método para graficar la función en un intervalo de valores [cite: 28]
        
        X = np.linspace(x_min, x_max, num_puntos)
        Y = np.array([self.evaluar(x) for x in X])
        
        plt.figure(figsize=(10, 5))
        plt.plot(X, Y, label=str(self), color='blue')
        
        # Demostración gráfica de la periodicidad y el efecto de amplitud/periodo [cite: 33]
        plt.title(f'Gráfico de la función: {self.tipo_funcion.capitalize()} | A={self.amplitud}, P={self.periodo:.2f}')
        plt.xlabel('x (radianes)')
        plt.ylabel('f(x)')
        plt.axhline(0, color='gray', linewidth=0.5)
        plt.axvline(0, color='gray', linewidth=0.5)
        
        # Marcar periodo en el eje X
        for i in range(-3, 4):
            period_mark = self.periodo * i
            if x_min < period_mark < x_max:
                plt.axvline(period_mark, color='red', linestyle='--', linewidth=0.7, alpha=0.5)
        
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()
        plt.show()


# Ejemplo de Uso:
if __name__ == "__main__":
    print("--- 1. Función Seno Estándar ---")
    f_seno = FuncionTrigonometrica(tipo_funcion='seno')
    print(f_seno) 
    print(f"Valor en pi/2: {f_seno.evaluar(math.pi / 2):.4f}")
    print(f_seno.valor_critico())
    # f_seno.graficar() 
    print("\n--- 2. Función Coseno Modificada (Amplitud y Periodo) ---")
    f_coseno_mod = FuncionTrigonometrica(tipo_funcion='coseno', amplitud=3.0, periodo=math.pi)
    print(f_coseno_mod) 
    print(f"Valor en pi: {f_coseno_mod.evaluar(math.pi):.4f}")
    print(f_coseno_mod.valor_critico())
    # f_coseno_mod.graficar()     
    print("\n--- 3. Función Tangente ---")
    f_tangente = FuncionTrigonometrica(tipo_funcion='tangente', amplitud=0.5)
    print(f_tangente)
    print(f"Valor en pi/4: {f_tangente.evaluar(math.pi / 4):.4f}")
    print(f_tangente.valor_critico())
    # f_tangente.graficar(x_min=-3*math.pi/2, x_max=3*math.pi/2) ```
