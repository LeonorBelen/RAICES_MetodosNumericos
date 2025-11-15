import numpy as np

# --- 1. Definición de la Función y su Derivada ---

def f(x):
    """Función: f(x) = x^3 - 0.5x^2 + 4x - 1"""
    return x**3 - 0.5 * x**2 + 4 * x - 1

def df(x):
    """Derivada: f'(x) = 3x^2 - x + 4"""
    return 3 * x**2 - x + 4

# Tolerancia de error absoluto: |x_nuevo - x_viejo| < 0.0001
TOL = 0.0001

# --- 2. Método de Bisección ---

def biseccion(a, b, tol):
    print("\n=== Método de Bisección ===")
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        return "El intervalo inicial no encierra la raíz (no hay cambio de signo)."
    
    p = 0
    
    for i in range(50): # Límite de iteraciones
        p_anterior = p
        p = (a + b) / 2
        
        # Criterio de parada: Ancho del intervalo (Error Absoluto)
        if np.abs(b - a) / 2 < tol:
            return f"Raíz encontrada: {p:.6f} en {i} iteraciones."
        
        fp = f(p)
        
        if fp == 0:
            return f"Raíz exacta: {p:.6f} en {i+1} iteraciones."
        
        if fa * fp < 0:
            b = p
        else:
            a = p
            
    return f"Convergencia lenta. Última aproximación: {p:.6f}"

# --- 3. Método de Newton-Raphson ---

def newton_raphson(x0, tol):
    print("\n=== Método de Newton-Raphson ===")
    x_k = x0
    
    for i in range(50): # Límite de iteraciones
        fx = f(x_k)
        dfx = df(x_k)
        
        if dfx == 0:
            return "División por cero (derivada nula)."
            
        x_k_nuevo = x_k - fx / dfx
        
        # Criterio de parada: Error Absoluto |x_k_nuevo - x_k|
        if np.abs(x_k_nuevo - x_k) < tol:
            return f"Raíz encontrada: {x_k_nuevo:.6f} en {i+1} iteraciones."
            
        x_k = x_k_nuevo
        
    return f"Convergencia lenta. Última aproximación: {x_k:.6f}"

# --- 4. Método de la Secante ---

def secante(x_menos_1, x0, tol):
    print("\n=== Método de la Secante ===")
    x_k_menos_1 = x_menos_1
    x_k = x0
    
    for i in range(50): # Límite de iteraciones
        fx_menos_1 = f(x_k_menos_1)
        fx_k = f(x_k)
        
        if fx_k - fx_menos_1 == 0:
            return "División por cero (denominador nulo)."
            
        x_k_mas_1 = x_k - fx_k * (x_k_menos_1 - x_k) / (fx_menos_1 - fx_k)
        
        # Criterio de parada: Error Absoluto |x_k_mas_1 - x_k|
        if np.abs(x_k_mas_1 - x_k) < tol:
            return f"Raíz encontrada: {x_k_mas_1:.6f} en {i+1} iteraciones."
            
        x_k_menos_1 = x_k
        x_k = x_k_mas_1
        
    return f"Convergencia lenta. Última aproximación: {x_k:.6f}"

# --- 5. Ejecución ---

print("--- PROBLEMA: f(x) = x^3 - 0.5x^2 + 4x - 1 ---")
# Bisección: Intervalo [0, 1]
print(biseccion(0, 1, TOL))
# Newton-Raphson: Valor inicial x0 = 0.2
print(newton_raphson(0.2, TOL))
# Secante: Valores iniciales x_-1 = 0.3, x_0 = 0.2 (como en el análisis previo)
print(secante(0.3, 0.2, TOL))