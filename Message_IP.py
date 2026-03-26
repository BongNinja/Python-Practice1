#Message Pop File to multiple users on this LAN 
import os
i = 100
while i<=150:
    command = f'msg * /server:192.168.0.{i} /time:10 "System Breach Detected"'
    os.system(command)