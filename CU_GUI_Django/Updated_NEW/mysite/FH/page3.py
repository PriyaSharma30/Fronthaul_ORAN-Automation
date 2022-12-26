# from django.http import HttpResponse
# from django.shortcuts import render

# # Create your views here.
# def index(request):
#     # value = request.GET.get('FH/index.html')
#     # print(value)
#     return render(request ,'FH/index.html')


from django.shortcuts import render

import requests
import configparser

config = configparser.ConfigParser()



# def home(request):
#     data = request.POST.get('name1')
#     if data == None:
#         data = ""
#     print(data)
#     sound = data
#     filename = '/home/vvdn/Videos/ini_file/mysite/settings.conf'
#     file_write = configparser.ConfigParser() 
#     file_write.read(filename)
#     try:
#         file_write.add_section("DEFAULT")
#     except Exception as e:
#         print(e)
#         pass
#     file_write.set("DEFAULT","DL Frequency",sound)
#     with open(filename,"w") as cfgfile:
#         file_write.write(cfgfile)
#     cfgfile.close
#     return render(request,'FH/page2.html',{'data':data})
    






    
    
def home(request):
    data = request.POST.get('name1')
    data1 = request.POST.get('chk')
    if data == None:
        data = ""
    if data1 == None:  
        data1 = ""
    print(data)
    print(data1)
    filename = '/home/vvdn/Videos/ini_file/mysite/settings.conf'
    file_write = configparser.ConfigParser() 
    file_write.read(filename)
    try:
        file_write.add_section("DEFAULT")
    except Exception as e:
        print(e)
        pass
    file_write.set("DEFAULT","DL Frequency",data)
    file_write.set("DEFAULT","eaxid",data1)
    with open(filename,"w") as cfgfile:
        file_write.write(cfgfile)
    cfgfile.close
#     config['DEFAULT'] = {"DL" : "1", "music" : "1",
# "volume" : "0.8", "resolution" : "1920x1080"}
#     with open('settings.conf', 'w') as configfile:
#         config.write(configfile
    
    return render(request,'FH/page2.html',{'data':data,'data1': data1})
    

