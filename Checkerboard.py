sym = '*'
ncols = 8
nrows = 8
def row(rownum):
	parity = rownum % 2
	syms = [sym, ' ']
	j = parity
	rowstr = ''
	for i in range(ncols):
		rowstr += syms[j]
		j = 1 - j
	return rowstr

for rownum in range(nrows):
	print row(rownum)
