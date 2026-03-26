# Provide Network statistics like Ping
import os
os.system('start cmd /k"ipconfig /all && echo  type exit to continue further"')
print("Would You like to know network latency \"ping test\" \n")
s = input("Enter Y or N: ")
if s == "Y":
    os.system('start cmd /k "echo Enter the Ping command wih your IP address e.g. Ping IP-address -t and exit after done"')
    print("Network Stat Check : Complete")
elif s == "N":
    print("Network Stat Check: Denied \n")