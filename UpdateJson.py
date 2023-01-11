from pathlib import Path
import sys
import glob
import json, os
from pprint import pprint

ctmenv = sys.argv[1]
JSON_FName = sys.argv[2]
old_CTM_FolderName = sys.argv[3]
#new_CTM_FolderName = sys.argv[4]

envLen = len(old_CTM_FolderName.split("_")[0])
#print(envLen)

new_CTM_FolderName = ctmenv + old_CTM_FolderName[envLen:]
#print(new_CTM_FolderName)

oldCTMenv = (old_CTM_FolderName.split("_")[0])
#print(oldCTMenv)

#sys.exit(9)

with open(str(JSON_FName), 'r') as f:
    json_data = json.load(f)
    json_data[new_CTM_FolderName] = json_data.pop(old_CTM_FolderName)
    json_data[new_CTM_FolderName]['INIT_PP_PROCESS']['SubApplication'] = ctmenv + (json_data[new_CTM_FolderName]['INIT_PP_PROCESS']['SubApplication'])[envLen:]
    json_data[new_CTM_FolderName]['SAY_HELLO']['SubApplication'] = ctmenv + (json_data[new_CTM_FolderName]['SAY_HELLO']['SubApplication'])[envLen:]
    json_data[new_CTM_FolderName]['PUT_PP_FILE']['SubApplication'] = ctmenv + (json_data[new_CTM_FolderName]['PUT_PP_FILE']['SubApplication'])[envLen:]
    json_data[new_CTM_FolderName]['GET_GD_FILE']['SubApplication'] = ctmenv + (json_data[new_CTM_FolderName]['GET_GD_FILE']['SubApplication'])[envLen:]
    json_data[new_CTM_FolderName]['END_PP_PROCESS']['SubApplication'] = ctmenv + (json_data[new_CTM_FolderName]['END_PP_PROCESS']['SubApplication'])[envLen:]		
    if (ctmenv.upper() == 'DEV'):	
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\DEV\\OUT\\PpTestfile01.txt'
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\DEV\\IN\\GDTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'QA'):	
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\QA\\OUT\\PpTestfile01.txt'
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\QA\\IN\\GDTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'PREPROD'):
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\PREPROD\\OUT\\PpTestfile01.txt'
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\PREPROD\\IN\\GDTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'PROD'):
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\PROD\\OUT\\PpTestfile01.txt'
        json_data[new_CTM_FolderName]['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\PROD\\IN\\GDTestfile01.txt'
        json_data[new_CTM_FolderName]['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    else :
        print("Something is wrong!")
        sys.exit(9)

json_object = json.dumps(json_data, indent=4)

with open(".\\" + str(ctmenv) + "_Descriptor.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
f.close()
