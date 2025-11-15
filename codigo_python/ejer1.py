import numpy as np

# --- 1. Definición de la Función y su Derivada ---

def f(x):
    """Función: f(x) = x^3 - exp(0.8x) - 20"""
    return x**3 - np.exp(0.8 * x) - 20

def df(x):
    """Derivada: f'(x) = 3x^2 - 0.8 * exp(0.8x)"""
    return 3 * x**2 - 0.8 * np.exp(0.8 * x)

# Tolerancia de error absoluto
TOL = 0.0001

# --- 2. Método de Bisección ---

def biseccion(a, b, tol, raiz_id):
    print(f"\n--- Bisección (Raíz {raiz_id}) ---")
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb > 0:
        return f"Error: El intervalo [{a}, {b}] no encierra la raíz (no hay cambio de signo)."
    
    p = 0
    
    for i in range(50): # Límite de iteraciones
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

def newton_raphson(x0, tol, raiz_id):
    print(f"\n--- Newton-Raphson (Raíz {raiz_id}) ---")
    x_k = x0
    
    for i in range(50): # Límite de iteraciones
        fx = f(x_k)
        dfx = df(x_k)
        
        if np.abs(dfx) < 1e-10: # Evitar división por cero
            return "División por cero (derivada cercana a cero)."
            
        x_k_nuevo = x_k - fx / dfx
        
        # Criterio de parada: Error Absoluto |x_k_nuevo - x_k|
        if np.abs(x_k_nuevo - x_k) < tol:
            return f"Raíz encontrada: {x_k_nuevo:.6f} en {i+1} iteraciones."
            
        x_k = x_k_nuevo
        
    return f"Convergencia lenta. Última aproximación: {x_k:.6f}"

# --- 4. Método de la Secante ---

def secante(x_menos_1, x0, tol, raiz_id):
    print(f"\n--- Método de la Secante (Raíz {raiz_id}) ---")
    x_k_menos_1 = x_menos_1
    x_k = x0
    
    for i in range(50): # Límite de iteraciones
        fx_menos_1 = f(x_k_menos_1)
        fx_k = f(x_k)
        
        if np.abs(fx_k - fx_menos_1) < 1e-10: # Evitar división por cero
            return "División por cero (denominador nulo)."
            
        x_k_mas_1 = x_k - fx_k * (x_k_menos_1 - x_k) / (fx_menos_1 - fx_k)
        
        # Criterio de parada: Error Absoluto |x_k_mas_1 - x_k|
        if np.abs(x_k_mas_1 - x_k) < tol:
            return f"Raíz encontrada: {x_k_mas_1:.6f} en {i+1} iteraciones."
            
        x_k_menos_1 = x_k
        x_k = x_k_mas_1
        
    return f"Convergencia lenta. Última aproximación: {x_k:.6f}"

# --- 5. Ejecución para las dos raíces ---

print("--- SOLUCIONES PARA f(x) = x^3 - exp(0.8x) - 20 ---")

# --- Raíz 1 (cercana a 3.229) ---
print("# Búsqueda de la Primera Raíz (x1)")
print(biseccion(3.0, 4.0, TOL, 1))
print(newton_raphson(3.5, TOL, 1))
print(secante(3.0, 4.0, TOL, 1))


