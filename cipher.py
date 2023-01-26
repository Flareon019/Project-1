def caesar_encryption(plaintext,key):
  encryption_str = ''
  for i in plaintext:
    if i.isupper():
      temp = 65 + ((ord(i) - 65 + key) % 26) 
      encryption_str = encryption_str + chr(temp)                              
    elif i.islower():
      temp = 97 + ((ord(i) - 97 + key) % 26)
      encryption_str = encryption_str + chr(temp)
    else:
      encryption_str = encryption_str + i  
 
  print("The ciphertext is:",encryption_str)
 
plaintext = input("Enter the plaintext:")
key = int(input("Enter the key:"))
caesar_encryption(plaintext,key)


#Decryption using Cipher text
def caesar_decryption(ciphertext,key):
  decryption_str = ''
  for i in ciphertext:
    if i.isupper():
      if ((ord(i) - 65 - key) < 0):
        temp = 65 + ((ord(i) - 65 - key + 26) % 26) 
      else:
        temp = 65 + ((ord(i) - 65 - key) % 26) 
decryption_str = decryption_str + chr(temp)                              
    elif i.islower():
      if ((ord(i) - 97 - key) < 0):
        temp = 97 + ((ord(i) - 97 - key + 26) % 26) 
      else:
        temp = 97 + ((ord(i) - 97 - key) % 26) 
      decryption_str = decryption_str + chr(temp)
    else:
      decryption_str = decryption_str + i  
 
  print("The plaintext is:",decryption_str)
 
ciphertext = input("Enter the ciphertext:")
key = int(input("Enter the key:"))
caesar_decryption(ciphertext,key)
