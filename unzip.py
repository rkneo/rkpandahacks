import subprocess

#Can be passed as parameters
secret_password = 'L@unceston20' 
file_name = "ziptest.zip"
out_file_name = 'ziptest.txt'
##################################

try:
    command = ["7z","x", "-aoa", "-p" + secret_password, file_name]
    rc = subprocess.call(command,stdout=subprocess.DEVNULL)
    with open(out_file_name,'r') as f:
        print(f.read())
    f.close
except:
    print(" Error Reading file")
    