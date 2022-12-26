import os
import paramiko

def take_ssh(host,username,password,command):
    #if response == 0:
        
        # ('Ping Successful')
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        _stdin, _stdout,_stderr = client.exec_command(command)
        print(_stdout.read().decode())
        client.close()
    #else:
        #print ('Ping Failed')

# host= input("enter hostname: ")
# username =input("enter username: ")
# password=input("enter passwd: ")
# command = input("Enter the command to run (Eg. ifconfig): ")
host = "172.17.166.37"
username="vvdn"
password="priya6863"
command="Documents"
response = os.system("sudo /etc/init.d/isc-dhcp-server restart")
response1 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response2 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response3 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response4 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response1 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response2 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response3 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response4 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response1 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response2 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response3 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response4 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response1 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response2 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response3 = os.system("sudo /etc/init.d/isc-dhcp-server status")
response4 = os.system("sudo /etc/init.d/isc-dhcp-server status")
print(response)
print(response1)


res=take_ssh(host,username,password,command)
print(res)


