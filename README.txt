# Smoke-automation

THESE CODE ARE FOR JUPITER SMOKE TEST CASES ONLY

PLS USE AN IDE (eg: pycharm) TO RUN THE CODE

USAGE OF THE SCRIPTS :
*Remember to change the printer's pin in "PIN_detection.py"
*Remember to change printer's IP in "config.json"
===========================================================
1. Auto_putty_connection.py
To establish maia > dune telnet connection

2. EWS_LDAP.py
To automate LDAP configuration on EWS 
If this script runs successfully, you may mark the test case [EWS - LDAP server settings management] as PASSED
*Remember to change the printer's IP in the code

3. ManangeDeviceUserAccount.py
To automate user creation, edit, and delete on EWS
If this script runs successfully, you may mark the test case [Managing the Device User Accounts - EWS] as PASSED
*Remember to change the printer's IP in the code

4. VNC_viewer_connection.py
To establish VNC connection, after running this script, wait for few seconds (4-5 sec) then open vnc viewer and connect the specific printer

5. certificate_management.py
To automate self-signed certificate creation and deletion on EWS
If this script runs successfully, you may mark the test case [EWS - certificate management] as PASSED
*Remember to change the printer's IP in the code

6. configure_network_folder.py
To automate network folder configuration on EWS
If this script runs successfully, you may mark the test case [EWS - Network folder setup (configuration stored.)] as PASSED
*Remember to change the printer's IP in the code
*Remember to change the display name (if needed) & network folder path to your own network folder path in the code

7. fix_printheads.py (ENSURE YOU ARE FAMILIAR WITH OOBE SKIPPING BEFORE EXECUTING THIS!)
To fix the printheads automatically after skipping OOBE

8. send_print_job.py
To send a printjob through 9100 port
This can be used in test case SMOKE 2 when it asked to send print job after the printer enters sleeps mode

9. smoke_printjobs.py
To send all printjobs required in smoke test
After printing, pls check the printouts are ok before marking the test cases as PASSED
[PDLs RasterICF Print Port 9100 Single Page Job]
[PDLs RasterICF Print Port 9100 Multi Pages Job]
[PDLs URF Print Port 9100 Single Page Job]
[PDLs PCL3Gui Print Port 9100 Single Page Graphic Job]
[PDLs PCL3Gui Print Port 9100 Single Page Vectorial Job]
[PDLs JPEG Print Port 9100 Jobs]
[PDLs TIFF Print Port 9100 Jobs]
[PDLs PWG Print Port 9100 Single Page Job]
[Print a RasterICF job through port 9100 with Collate On/Off]
[Print a RasterICF job through port 9100 with Multiple job copies]
[Print a RasterICF job through port 9100 with Multiple page copies]

*Remember to change the file path of the print job files' to the path the files save in ur PC
