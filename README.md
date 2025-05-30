# Shadow user gui
Want to preview other user's desktop on Remote desktop server? A simple script to display logged users and perform Remote Desktop Shadow session locally on Windows Server.
* Displays the list of available users with TKInter
* Initiates shadow session with `C:\\Windows\\system32\\mstsc.exe /shadow:%sess_id% /noconsentprompt`

  
# Remark
* To perform shadow session the user has to be administrator and Remote Desktop Services must be configured with Shadow session enabled in Group Policy.

* The file is manually written without LLM tool.
