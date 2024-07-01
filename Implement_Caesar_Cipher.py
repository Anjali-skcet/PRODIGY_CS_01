print ("Enter the number for required ciphering method\n1 - Encryption\n2 - Decryption\n")
method = int(input())
print("\nEnter the text : ")
text = str(input())
print("\nEnter the shift value : ")
shiftvalue=int(input())

if method == 1:
    answer=""
    for i in text:
        if i.isalpha():
            value=(ord(i) + shiftvalue)
            if i.isupper():
                if(value>ord('Z')):
                    value-=26
            elif i.islower():
                if(value>ord('z')):
                    value-=26
            answer+=chr(value)
    print("\nEncrypted text : ",answer)

elif method == 2:
    answer = ""
    for i in text:
        if i.isalpha():
            value=ord(i)-shiftvalue
            if i.isupper():
                if value<ord('A'):
                    value+=26
            elif i.islower():
                if value<ord('a'):
                    value+=26
            answer += chr(value)
    print("\nDecrypted text : ",answer,"\n")