# from django.http import HttpResponse
# from django.shortcuts import render

# from asyncio.subprocess import PIPE
from asyncio.subprocess import STDOUT
from sys import stderr, stdout
from build import sys
from django.http import HttpResponse
from django.shortcuts import render


import requests
import configparser

config = configparser.ConfigParser()
from subprocess import run, PIPE



###### for SUBMIT Configuration Window  #########################
def home(request):
    data2 = request.POST.get('du_t')
    data1 = request.POST.get('sub_c')
    data = request.POST.get('test_m')
    data3 = request.POST.get('name1')
    data4 = request.POST.get('name2')
    data5 = request.POST.get('name3')
    data6 = request.POST.get('band_w')
    data7 = request.POST.get('Ph_a')
    data8 = request.POST.get('name4')
    data30 = request.POST.get('name10')
    data9 = request.POST.get('chk')
    data15= request.POST.get('name5')
    data16= request.POST.get('name6')
    data17= request.POST.get('name7')
    data20= request.POST.get('C_P')
    data21= request.POST.get('name9')
    if data2 == None:
        data2 = ""
    if data1 == None:  
        data1 = ""
    if data == None:  
        data = "" 
    if data3 == None:  
        data3 = "" 
    if data4 == None:  
        data4 = "" 
    if data5 == None:  
        data5 = ""     
    if data6 == None:  
        data6 = "" 
    if data7 == None:  
        data7 = "" 
    if data8 == None:  
        data8 = "" 
    if data9 == None:  
        data9 = ""            
    if data15 == None:  
        data15 = "" 
    if data16 == None:  
        data16 = ""
    if data17 == None:  
        data17 = ""
    if data20 == None:  
        data20 = ""   
    if data21 == None:  
        data21 = "" 
    if data30 == None:  
        data30 = ""                                 
    print(data2)
    print(data1)
    print(data)
    print(data3)
    print(data4)
    print(data5)
    print(data6)
    print(data7)
    print(data8)
    print(data9) 
    print(data15)
    print(data16)
    print(data17)
    print(data20)
    print(data21)
    print(data30)
    # filename = '/home/vvdn/Videos/Project/ini_file/mysite/settings.conf'
    filename = '/home/vvdn/Videos/Project/Updated_NEW/requirement.txt'
    file_write = configparser.ConfigParser() 
    file_write.read(filename)
    try:
        file_write.add_section("DEFAULT")
    except Exception as e:
        print(e)
        pass
    file_write.set("DEFAULT","Duplex Type",data2)
    file_write.set("DEFAULT","number of bandwidths to test","1")
    file_write.set("DEFAULT","SubCarrier Spacing",data1)
    file_write.set("DEFAULT","Test Model",data)
    file_write.set("DEFAULT","Downlink Center Frequency in GHz",data3)
    file_write.set("DEFAULT","Uplink Center Frequency in GHz",data4)
    file_write.set("DEFAULT","Power in dBm",data5)
    file_write.set("DEFAULT","Bandwidths (Split with '/')",data6)
    file_write.set("DEFAULT","Phase Compensation",data7)
    file_write.set("DEFAULT","VXT Address","TCPIP::"+data8+"::hislip"+data30+"::INSTR")
    file_write.set("DEFAULT","eAxID",data9)
    # file_write.set("DEFAULT","eAxID_all","1,2,3,4")
    file_write.set("DEFAULT","Folder path to save results",data15)
    file_write.set("DEFAULT","DL C-Plane Time",data16)
    file_write.set("DEFAULT","DL U-Plane Time",data17)
    file_write.set("DEFAULT","Cyclic Prefix",data20)
    file_write.set("DEFAULT","External Gain",data21)
    with open(filename,"w") as cfgfile:
        file_write.write(cfgfile)
    cfgfile.close
    return render(request,'FH/index.html',{'data2':data2,'data1': data1,'data': data,'data3': data3,'data4': data4,'data5': data5,'data6': data6,'data7': data7,'data8': data8,'data9': data9,'data15': data15,'data16': data16,'data17': data17,'data20': data20,'data21': data21,'data30': data30})





###### for rct configuration  page base click  #########################


def about(request):
        return render(request,'FH/base_dl.html')

###### for DL configuration  page base click  #########################
def about1(request):
        return render(request,'FH/cu_base_dl.html')



###### for rct configuration page extended click  #########################
def extended(request):
    return render(request,'FH/extended_dl.html')

###### for DL configuration page extended click  #########################
def extended1(request):
    return render(request,'FH/CU_extended_dl.html')

###### for RUN DOWNLINK BASE FILE #########################
def base(request):
    return render(request,'FH/base_dl.html')  

###### for RUN DOWNLINK BASE FILE #########################
def base1(request):
    return render(request,'FH/cu_base_dl.html')  

##### for RUN RCT extended FILE #########################
def extended_run(request):
    return render(request,'FH/extended_dl.html')       


##### for RUN DOWNLINK extended FILE #########################
def extended_run1(request):
    return render(request,'FH/CU_extended_dl.html')  
###### Configuration page submit button #########################

def button(request):
    return render(request,'FH/index.html')
    


# ###### for RUN DOWNLINK BASE FILE python file #########################

# def external(request):
#     # inp = request.POST.get('param')
#     out=run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/ssh.py'], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/base_dl.html',{'data10':out.stdout}) 


###### for RCT DOWNLINK BASE FILE python file #########################
def external(request):
    # inp = request.POST.get('param')
    out=run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/pinging.py'], shell = False, stdout= PIPE)
    return render(request,'FH/base_dl.html',{'data10':out.stdout.decode()})    

###### for RUN DOWNLINK BASE FILE python file #########################
def cu_base_dl(request):
    # inp = request.POST.get('param')
    out=run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/pinging.py'], shell = False, stdout= PIPE)
    return render(request,'FH/cu_base_dl.html',{'data10':out.stdout.decode()}) 


# ###### for RUN DOWNLINK BASE FILE python file #########################
# def external(request):
#     # inp = request.POST.get('param')
#     out=run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/pinging.py'], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/base_dl.html',{'data10':out.stdout})    



###### for RCT DOWNLINK BASE FILE python file #########################
def cu(request):
    # inp = request.POST.get('param')
    # out = ping.check_ping('192.168.1.10')
    out=run([sys.executable,'/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/Main_Script.py'], shell = False,stdout= PIPE, stderr = STDOUT)
    print(out)
    return render(request,'FH/extended_dl.html',{'data11':out.stdout.decode()})  
    # return render(request,'FH/extended_dl.html',{'data11':run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/ping.py'], shell = False, stdout= PIPE, stderr = STDOUT).stdout.decode()})  
    

    

###### for RUN DOWNLINK BASE FILE python file #########################
def CU_extended_dl(request):
    # inp = request.POST.get('param')
    # out = ping.check_ping('192.168.1.10')
    out=run([sys.executable,'/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/Main_Script.py'], shell = False,stdout= PIPE, stderr = STDOUT)
    print(out)
    return render(request,'FH/CU_extended_dl.html',{'data11':out.stdout.decode()})  
    # return render(request,'FH/extended_dl.html',{'data11':run([sys.executable,'/home/vvdn/Videos/Project/Updated_NEW/ping.py'], shell = False, stdout= PIPE, stderr = STDOUT).stdout.decode()})  
    

# def run_script(filename):
#     print(filename)
#     out=run([sys.executable,filename], shell = False, stdout= PIPE)
#     print(out)
#     # print(out.stdout.decode())
#     error = handle_stdout(out)
#     print(bool(error), True)
#     if error:
#         return error
#     else:
#         return handle_stderr(out)


# def handle_stderr(out):
#     return out.stderr.decode()

# def handle_stdout(out):
#     return out.stdout.decode()