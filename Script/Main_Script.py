#################################################################################################
#-----------------------------------------------------------------------------------------------#
#              VVDN CONFIDENTIAL                                                                #
#-----------------------------------------------------------------------------------------------#
# Copyright (c) 2016 - 2022 VVDN Technologies Pvt Ltd.                                          #
# All rights reserved                                                                           #
#-----------------------------------------------------------------------------------------------#
#                                                                                               #
# @file   : Main_Script.py                                                                      #
# @brief  : This script will call the corresponding functions and operations related to Duplex Types TDD/FDD. #
# @author : Umamaheswari E, VVDN Technologies Pvt. Ltd (e.umamaheswari@vvdntech.in)             #
# @Supervision : Sebu Mathew , VVDN Technologies Pvt. Ltd (sebu.mathew@vvdntech.in)             #
# @Support Given : Hariharan R, VVDN Technologies Pvt. Ltd (hariharan.r@vvdntech.in)            #
# @Support Given : Muhammed Siyaf E K, VVDN Technologies Pvt. Ltd (muhammed.siyaf@vvdntech.in)  #
# @Support Given : Athulya Saju, VVDN Technologies Pvt. Ltd (athulya.saju@vvdntech.in)          #
#################################################################################################


import re 

import FDD_Config
import TDD_Config

from FDD_Config import FDD
from TDD_Config import TDD

# opening the requirement text file in read mode
req = open("C:\ORAN_AUTOMATION1\Requirement\Requirement.txt", "r")

# reading the file data
data = req.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
#Assign the requirement to each variables

dup_type = re.sub(' +', '', str(data_into_list[0].split("-")[1]))
#print(dup_type)
band_count = int(data_into_list[1].split("-")[1])
bands = list(data_into_list[2].split("-")[1].split("/"))
phase_comp = data_into_list[3].split("-")[1]
eAxID = re.sub(' +', '', str(data_into_list[4].split("-")[1]))
Base_Folder_Path = re.sub(' +', '', str(data_into_list[5].split("-")[1]))
DL_Center_Freq = data_into_list[6].split("-")[1]
UL_Center_Freq = data_into_list[7].split("-")[1]
Power_Value = int(data_into_list[8].split("-")[1])*(-1)
VXT_Add = str(data_into_list[9].split("-")[1])
Ext_Gain = int(data_into_list[10].split("-")[1])*(-1)
print(Ext_Gain)

#close the file
req.close()

#Check for the Duplex type. If matches the requirement, then calls corresponding functions else shows the error
if (dup_type == 'FDD'):
    FDD_Config.FDD(band_count, bands, eAxID, phase_comp, Base_Folder_Path, DL_Center_Freq, UL_Center_Freq, Power_Value, VXT_Add, Ext_Gain)
elif (dup_type == 'TDD'):
    TDD_Config.TDD(band_count, bands, eAxID, phase_comp, Base_Folder_Path, DL_Center_Freq, UL_Center_Freq, Power_Value, VXT_Add, Ext_Gain)
else:
    print("Please check the Duplex Type given in the requirement")