import os

def check_ping(hostname):
    response = os.system("ping -c 2 " + hostname)
    if response == 0:
    
    
        print ('Ping Successful')
    else:
        print ('Ping Failed')

if __name__ == "__main__":
    hostname = "172.17.166.36" 
    res=check_ping(hostname)
