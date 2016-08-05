
li=[11,22,33,44,55,66,77,88]
dic = {}
 
for item in li:
	if item > 66:
		if 'k2' in dic.keys():
			dic['k2'].append(item)
		else:
			dic['k2'] = [item,]
	else:
		if 'k1' in dic.keys():
			dic['k1'].append(item)
		else:
			dic['k1'] = [item,]
