import os
hostname = "10.1.14.1"
response = os.system("ping -c 1 " + hostname)

if response == 0:
    pingstatus = "Network Active"
else:
    pingstatus = "Network Error"