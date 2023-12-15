import sympy as sp

lam, mu, rho = sp.symbols('lambda mu rho') 
A=sp.zeros(9,9)
A[0, 3],A[1, 4],A[2, 5] =-(1/rho), -(1/rho),-(1/rho)
A[3, 0],A[4, 1],A[5, 2]=-(lam+2*mu), -mu,-mu
A[6,0],A[8,0]=-lam,-lam
print(A.eigenvals())
