# KeyWhisperer
Welcome to the "KeyWhisperer: Keylogger with Python" tutorial. In this tutorial, I will demonstrate how to create a Python-based keylogger. A keylogger is a tool that monitors and records keyboard strokes on a victim machine and forwards them to the server, which can be useful for various purposes such as network security testing and system administration.

In this tutorial, we will cover the following topics:

1. Setting up the project environment and required libraries
2. Creating a server-side script to receive keyboard strokes
3. Developing a client-side script to be executed on the victim machine
4. Setting up the tool to run automatically on system startup on victim machine
5. Run the script on the victim machine
<br>

## Installation
Install the source code:
```
git clone https://github.com/BlurryFace04/KeyWhisperer.git
cd KeyWhisperer
```

Setup virtual environment in Windows (optional):
```
python -m venv venv
call venv\Scripts\activate
```

Setup virtual environment in Linux (optional):
```
python3 -m venv venv
source venv/bin/activate
```

Install libraries:
```
pip install -r requirements.txt
```
<br>

## Server
It is highly recommended to consider renting a dedicated/shared server or a virtual private server (VPS) for hosting your keylogger server script. By utilizing a rented server, you can gain remote access and control over your keylogger from any location, rather than being limited to a local area network (LAN) when using a home PC or laptop. This approach significantly enhances the flexibility and reach of your keylogger, enabling more efficient monitoring and management across various network environments. 

For this tutorial, we will be using an Ubuntu Server.

Once you have set up your server environment, ensure that your server script is uploaded to the server. Then, initiate the server script by executing the following command:
```
python3 server.py
```
Upon successful execution, your server will be up and running, actively listening for incoming connections from your keylogger clients.
<br><br><br>


## Client
To prepare the client-side script for execution on the target machine, you'll need to convert it into an executable (.exe) file using PyInstaller. This process makes it easier to run the script on the target system without even requiring a separate Python installation on the target machine.
The client script provided can be executed on both Windows and Linux operating systems.

Run the following command to convert your script into a standalone executable:
```
pyinstaller --onefile --noconsole client.py

```
<br>

## Run script on startup
In order to ensure that the keylogger runs automatically every time the target system starts, you can use the startup script.

Run the following command to convert your script into a standalone executable:
```
pyinstaller --onefile --noconsole startup.py
```

This will copy the client.exe file to any derired location which can be edited in the startup.py file and create a shortcut to the client.exe file in the Windows Startup folder, ensuring that the keylogger runs every time the system starts.
<br><br><br>

## Execution:
After generating the executable files, you will find the client.exe and startup.exe files within the dist folder created by PyInstaller.

To deploy the keylogger on the target machine, transfer both files using an appropriate method, such as a USB flash drive, a Rubber Ducky, or another suitable technique.

Once connected to the target system, execute the startup.exe file to initiate the keylogging process.

### USB Flash Drive:
If using a USB flash drive, simply run the startup.exe file. This will copy the client.exe file to the pre-defined location on the target system and create a shortcut in the Windows Startup folder, ensuring the keylogger is launched each time the system starts.

### Rubber Ducky:
You can create a script for Rubber Ducky using the following steps:

1. Use the payload.txt provided in the source code and create a inject.bin (binary payload file) from here: https://payloadstudio.hak5.org/community/
2. Copy the inject.bin file to the root of the Rubber Ducky's microSD card.
3. Insert the Rubber Ducky into the target system and the payload script will automatically execute the startup.exe file. 
<br>

## Conclusion:
As you embark on this journey of mastering the art of keylogging, remember that knowledge is power, but with great power comes great responsibility. Use this knowledge wisely to create a safer and more secure digital world. Happy keylogging!



