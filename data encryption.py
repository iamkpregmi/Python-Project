import hashlib
# prints all available algorithms
# print ("The available algorithms are : ", end ="")
# print (hashlib.algorithms_guaranteed)

str = input("Enter an text you want to encrypt: ")
result = hashlib.md5(str.encode())
print("md5:",result.hexdigest())

result = hashlib.sha256(str.encode())
result = hashlib.sha256(str.encode())
print("sha256:",result.hexdigest())

result = hashlib.sha512(str.encode())
print("sha512:",result.hexdigest())
