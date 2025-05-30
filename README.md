# Shadow user gui
A simple script to display logged users and perform Remote Desktop Shadow session locally on Windows Server.
* Displays the list of available users with TK
* Initiates shadow session with `C:\\Windows\\system32\\mstsc.exe /shadow:%sess_id% /noconsentprompt`
