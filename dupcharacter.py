# hash_table = {}


# def find_duplicate(str):
# 	for i in range(len(str)):
# 		if str[i] not in hash_table:
# 			hash_table.update({str[i]:1})
# 		else:
# 			hash_table[str[i]] = hash_table[str[i]] + 1

# str = "Thang Tran khong biet chi het"
# find_duplicate(str);

# for key in hash_table:
# 	if hash_table[key] >1:
# 		print(key,hash_table[key])
# print(hash_table)



a = ["Asdfasdf","asdfasdf","Asdfasdf"]

if any("s" in str for str in a):
	print("t")
else:
	print("k")
