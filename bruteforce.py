password='passwords.txt'
brute=open("Ppass.txt","w")
with open(password)as pwd:
    line=pwd.readline()
    while line:
        brute.write("\"")
        brute.write(line.strip())
        brute.write("\",")
        line=pwd.readline()
    brute.close()