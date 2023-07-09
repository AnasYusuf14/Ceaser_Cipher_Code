print('''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')

direction = input("Enter 'encode' if you want to do encrypt , Enter 'decode' if you want to do 'decrypt' \n ").lower()
text = input("Your message:\n").lower()
shift_number = int(input("Enter the shift number: \n"))
#########################################################
#Encrypt Function:
def encrypt_fun(str,shift):
    cipher_text = ''.join(chr((ord(letter) - 97 + shift) % 26 + 97) for letter in str)
    print(f"Encrypted text is {cipher_text}")  
###########################################################  
#Decrypt Function:
def decrypt_fun(str,shift):
    for letter in str:
        decrypted_text = ''.join(chr((ord(letter) - 97 - shift) % 26 + 97) for letter in str)
    print(f"Decrypted text is {decrypted_text}")
#############################################################  
if direction == "encode":
    encrypt_fun(str = text,shift = shift_number)
elif direction == "decode":
    decrypt_fun(str = text , shift = shift_number)
else:
    print("Enter only 'encode' or 'decode' !!")    


