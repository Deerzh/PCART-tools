from sympy import symbols, itermonomials
(x, y) = symbols('x y')
monomials = itermonomials([x, y], max_degree=2, min_degree=0)