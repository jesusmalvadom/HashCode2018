import numpy as np
import math

def dist(row_start, col_start, row_finish, col_finish):
	return math.fabs(row_start - row_finish) + math.fabs(col_start - col_finish)


# Open input file
infile = open('b_should_be_easy.in', 'r')


# Read header
rows, columns, vehicles, rides, bonus, steps = infile.readline().strip().split() # We read the first line with problem info

for line in infile:
	r_row_start, r_col_start, r_row_fin, r_col_fin, r_start, r_finish = line.strip().split()
	print dist(int(r_row_start), int(r_col_start), int(r_row_fin), int(r_col_fin))
