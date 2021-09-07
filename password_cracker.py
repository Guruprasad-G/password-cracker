import hashlib

def write_passwords(password_list):
    fhand = open("password_decoded.csv","w")
    fhand.write("User name, Password hash, Password decoded?, Password\n")
    for item in password_list:
        try:
            fhand.write(f"{item[0]},{item[1]},{item[2]},{item[3]}\n")
        except:
            fhand.write(f"{item[0]},{item[1]},{item[2]}, \n")
    print("Passwords CSV file generated")

def generate_passwords(hashing_algorithm,fhand1,password_list):
    count = 0
    for password in fhand1:
        password = password.strip()
        for i in range(len(password_list[1:])):
            if hashing_algorithm == "md5" and not password_list[i][2] and hashlib.md5(password.encode()).hexdigest() == password_list[i][1]:
                password_list[i][2] = True
                password_list[i].append(password)
                print(password_list[i])
            elif hashing_algorithm == "sha1" and not password_list[i][2] and hashlib.md5(password.encode()).hexdigest() == password_list[i][1]:
                password_list[i][2] = True
                password_list[i].append(password)
                print(password_list[i])
            elif hashing_algorithm == "sha256" and not password_list[i][2] and hashlib.md5(password.encode()).hexdigest() == password_list[i][1]:
                password_list[i][2] = True
                password_list[i].append(password)
                print(password_list[i])
        count+=1
        if count%100000 == 0:
            print(f"Passwords checked so far = {count} ")
    print("Final password list = ",password_list)
    write_passwords(password_list)

def algorithm_checker(fhand1,fhand2):
    '''This function checks if md5,sha1,sha256 algorithm is used in the hash dump by checking it for the first password'''
    password_list = []
    for sentence in fhand2:
        temp_list = sentence.split(":")
        password_list.append([temp_list[0],temp_list[1].strip(),False])
    #print(password_list)
    first_password_hash = password_list[1][1]
    hashing_algorithm = ""
    for password in fhand1:
        password = password.strip()
        if hashlib.md5(password.encode()).hexdigest() == first_password_hash:
            hashing_algorithm = "md5"
            print("Hashing Algorithm =",hashing_algorithm)
            print("First password =",password)
            password_list[0][2] = True
            password_list[0].append(password)
            break
        elif hashlib.sha1(password.encode()).hexdigest() == first_password_hash:
            hashing_algorithm  = "sha1"
            print("Hashing Algorithm =",hashing_algorithm)
            print("First password =",password)
            password_list[0][2] = True
            password_list[0].append(password)
            break
        elif hashlib.sha256(password.encode()).hexdigest() == first_password_hash:
            hashing_algorithm  = "sha256"
            print("Hashing Algorithm =",hashing_algorithm)
            print("First password =",password)
            password_list[0][2] = True
            password_list[0].append(password)
            break
    if hashing_algorithm == "":
        print("Either password was not found in common password list or wrong algorithm")
        exit()
    else:
        generate_passwords(hashing_algorithm,fhand1,password_list)

def file_opener():
    '''This function opens the has dump file and the possible passwords file'''
    try:
        password_list_file = input("Enter the common/possible passwords file : ")
        #password_list_file = "rockyou.txt"
        password_dump_file = input("Enter the password dump file : ")
        #password_dump_file = "passwd_dump.txt"
        fhand1 = open(password_list_file,encoding="latin-1")
        #Had to use latin-1 encoding since utf8 encoding raised an encoding error near line number 600000 in the rockyou.txt
        fhand2 = open(password_dump_file,encoding="utf8")
        algorithm_checker(fhand1,fhand2)
    except:
        print("Error")
        exit()

if __name__ == "__main__":
    file_opener()












