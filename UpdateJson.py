from pathlib import Path
import sys
import glob
import json, os
from pprint import pprint

ctmenv = sys.argv[1]

with open(".\example001.json", 'r') as f:
    json_data = json.load(f)
    if (ctmenv.upper() == 'DEV'):
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\DEV\\OUT\\PpTestfile01.txt'
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\DEV\\IN\\GDTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'QA'):
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\QA\\OUT\\PpTestfile01.txt'
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\QA\\IN\\GDTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'PREPROD'):
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\PREPROD\\OUT\\PpTestfile01.txt'
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\PREPROD\\IN\\GDTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    elif (ctmenv.upper() == 'PROD'):
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Src'] = 'C:\\Partner_Portal\\PROD\\OUT\\PpTestfile01.txt'
        json_data['DEV_ABC123']['PUT_PP_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Inbound/PpTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Src'] = 'C:\\Member_Portal\\PROD\\IN\\GDTestfile01.txt'
        json_data['DEV_ABC123']['GET_GD_FILE']['FileTransfers'][0]['Dest'] = '/ctm/ctmagent/Outbound/GDTestfile01.txt'
    else :
        print("Something is wrong!")
        sys.exit(9)

#print(json_data)

json_object = json.dumps(json_data, indent=4)

with open(".\\" + str(ctmenv) + "_Descriptor.json", "w") as outfile:
    outfile.write(json_object)

# Closing file
f.close()