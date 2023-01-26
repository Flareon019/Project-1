result = ""

choice = input("\nEnter 1 to Encrypt or 2 to Decrypt:\n>>")

if choice == "1":
    msg = input("\nEnter the message to encrypt:\n>>")

    for i in range(0, len(msg)):
         result = result + chr(ord(msg[i]) - 4)
    print(result)

elif choice == "2":
    msg = input("\nEnter the message to decrypt:\n>>")

    for i in range(0, len(msg)):
        result = result + chr(ord(msg[i]) + 4)
    print(result)

else:
    print ("Use only numbers 1 or 2. Please try again.\n")
