# from django.http import HttpResponse
# from django.shortcuts import render

from asyncio.subprocess import PIPE
from sys import stdout
from build import sys
from django.http import HttpResponse
from django.shortcuts import render

import requests
import configparser

config = configparser.ConfigParser()
from subprocess import run, PIPE


###### for SUBMIT Configuration Window  #########################
def home(request):
    data = request.POST.get('test_m')
    data1 = request.POST.get('sub_c')
    data2 = request.POST.get('du_t')
    data3 = request.POST.get('name1')
    data4 = request.POST.get('name2')
    data5 = request.POST.get('name3')
    data6 = request.POST.get('band_w')
    data7 = request.POST.get('Ph_a')
    data8 = request.POST.get('name4')
    data9 = request.POST.get('chk')
    if data == None:
        data = ""
    if data1 == None:  
        data1 = ""
    if data2 == None:  
        data2 = "" 
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
    print(data)
    print(data1)
    print(data2)
    print(data3)
    print(data4)
    print(data5)
    print(data6)
    print(data7)
    print(data8)
    print(data9)   
    # filename = '/home/vvdn/Videos/Project/ini_file/mysite/settings.conf'
    filename = '/home/vvdn/Videos/Project/r.txt'
    file_write = configparser.ConfigParser() 
    file_write.read(filename)
    try:
        file_write.add_section("DEFAULT")
    except Exception as e:
        print(e)
        pass
    file_write.set("DEFAULT","Test Model",data)
    file_write.set("DEFAULT","SubCarrier Spacing",data1)
    file_write.set("DEFAULT","Duplex Type",data2)
    file_write.set("DEFAULT","DL Frequency",data3)
    file_write.set("DEFAULT","UL Frequency",data4)
    file_write.set("DEFAULT","Power",data5)
    file_write.set("DEFAULT","Bandwidths",data6)
    file_write.set("DEFAULT","Phase Compensation",data7)
    file_write.set("DEFAULT","VXT Address",data8)
    file_write.set("DEFAULT","eAxID",data9)
    
    with open(filename,"w") as cfgfile:
        file_write.write(cfgfile)
    cfgfile.close
   
    # return render(request,'FH/index.html',{'data8':data8,'data9': data9})

    return render(request,'FH/index.html',{'data':data,'data1': data1,'data2': data2,'data3': data3,'data4': data4,'data5': data5,'data6': data6,'data7': data7,'data8': data8,'data9': data9})



# def about(request):
#     return render(request,'FH/base_dl.html')


###### for DL BASE page to Run BASE page #########################

def about(request):
    return render(request,'FH/base_dl.html')


###### for RUN DOWNLINK BASE FILE #########################
def base(request):
    return render(request,'FH/base_dl.html')    

###### Configuration page submit button #########################

def button(request):
    return render(request,'FH/index.html')

# def output(request):
#     # data = requests.get('/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/python/Main_Script.py')
#     #      "exec('/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/python Main_Script.py
#     data10 = requests.get("https://home/vvdn/Videos/Project/a.py")
#     # data10='/home/vvdn/Videos/Project/a.py'
#     print(data10)
#     # data=data.text
#     return render(request,'FH/test_base.html',{'data10':data10}) 
# run='/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/python Main_Script.py'
# def output(request):
#     # data = requests.post.get('param')
#     #      "exec('/home/vvdn/ORAN_AUTOMATION/ORAN_AUTOMATION/Script/python Main_Script.py
#     # data = requests.get("https://reqres.in/api/users")
#     out=run([sys.executable,run], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/test_base',{'out':out.stdout})        


# def external(request):
#     inp = request.POST.get('param')
#     out=run([sys.executable,'/home/vvdn/Videos/Project/z.py',inp], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/execute.html',{'data10':out.stdout})




###### for RUN DOWNLINK BASE FILE #########################
def external(request):
    # inp = request.POST.get('param')
    out=run([sys.executable,'/home/vvdn/Videos/Project/pinging.py'], shell = False, stdout= PIPE)
    print(out)
    return render(request,'FH/base_dl.html',{'data10':out.stdout})    


# def external(request):
#     # inp = request.POST.get('param')
#     out=run([sys.executable,'/home/vvdn/Videos/Project/pinging.py'], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/base_dl.html',{'data10':out.stdout})    

# def external(request):
#     # inp = request.POST.get('param')
#     out=run([sys.executable,'/home/vvdn/Videos/Project/pinging.py'], shell = False, stdout= PIPE)
#     print(out)
#     return render(request,'FH/execute.html',{'data10':out.stdout})  