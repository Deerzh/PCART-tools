import scipy.sparse as sp
adjacency_matrix = sp.csr_matrix([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
laplacian = sp.csgraph.laplacian(adjacency_matrix, normed=False, return_diag=False, use_out_degree=False, copy=True, form='array', dtype=None, symmetrized=False)
print(laplacian.toarray())
