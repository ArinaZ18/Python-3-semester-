import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#sympy
x = sp.symbols('x')
y = sp.Function('y')

eq = syp.Eq(syp.Derivative(y(x), x), -2 * y(x))

sol_sympy = syp.lambdify(x, syp.dsolve(eq, ics={y(0): syp.sqrt(2)}).rhs, 'numpy')


#scipy
def exponential_decay(t, y): return -2 * y
sol_scipy = solve_ivp(exponential_decay, [0, 10], [sp.sqrt(2)])


plt.figure(figsize=(16, 16))
x=np.linspace(1,10,100)
plt.subplot(211)
plt.plot(x,sol_sympy(x),label='sympy')
plt.plot(sol_scipy.t,  sol_scipy.y[0],label='scipy')
plt.grid()
plt.title("SymPy and SciPy diff eq solution")
plt.legend()

len(sol_sympy(sol_sympy(x)))
plt.subplot(212)
plt.plot(sol_scipy.t, np.abs(sol_sympy(sol_scipy.t)-sol.y[0]))
plt.title("Difference in solutions")
plt.grid()

plt.savefig('Sympy_Scipy.png')
