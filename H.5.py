def caesar_encryption(plaintext,key):
  encryption_str = ''
  for a in plaintext:
    if a.isupper():
      temp = 65 + ((ord(a) - 65 + key) % 26) 
      encryption_str = encryption_str + chr(temp)                              
    elif a.islower():
      temp = 97 + ((ord(a) - 97 + key) % 26)
      encryption_str = encryption_str + chr(temp)
    else:
      encryption_str = encryption_str + a  
 
  print("The ciphertext is:",encryption_str)
 
plaintext = input("Enter the plaintext:")
key = int(input("Enter the key:"))
caesar_encryption(plaintext,key)