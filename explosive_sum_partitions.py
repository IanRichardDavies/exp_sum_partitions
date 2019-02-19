def exp_sum(n):
	'''
	This functions finds the number of partitions of integer, n.
	It considers combinations not permutations.
	'''
	alg_num = n + 1
	import numpy as np
	partition_matrix = np.zeros((alg_num, alg_num), dtype = int)

	# first column is always 1
	partition_matrix[:,0] = 1

	for row in range(1, alg_num):
		for col in range(1, alg_num):
			if row > col:
				partition_matrix[row][col] = partition_matrix[row - 1][col]
			else:
				partition_matrix[row][col] = partition_matrix[row - 1][col] + partition_matrix[row][col - row]

	return partition_matrix[n][n] 