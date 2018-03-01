import numpy as np

# Open input file
infile = open('b_should_be_easy.in', 'r')


# Read header
rows, columns, vehicles, rides, bonus, steps = infile.readline().strip().split() # We read the first line with problem info

for line in infile:
	r_row_start, r_col_start, r_row_fin, r_col_fin, r_start, r_finish = line.strip().split()

print r_row_start, r_col_start, r_row_fin, r_col_fin, r_start, r_finish
