import hashlib

while(True):
    hash_string = str(input("Input string: "))
    if hash_string == '-1':
        break
    hash_string = hash_string.encode() 
    hash = hashlib.sha1(hash_string)    
    hash_hex = hash.hexdigest()
    print(hash_hex)