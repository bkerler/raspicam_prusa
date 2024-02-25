# raspicam_prusa
Use the raspberry pi zero w2 together with a raspi camera for PrusaConnect

# Get raspberry pi
- Install rpi_imager
- "Choose OS" -> Raspberry Pi for your Pi
- "Advanced options" -> "Set hostname" -> "raspicam"
- "Enable SSH" -> "Use password authentication"
- "Set username and password" -> "Username": "pi", "Password" : [your password here]
- "Configure wireless LAN" -> Your wifi settings here, make sure to select right country
- "Save"
- "Choose storage" : Select your sd card, then write
- Insert the written sdcard to your rpi zero w2

# Get your token and fingerprint from Prusa
- You need a PC with webcam for this step
- Make sure Prusa Connect is enabled and registered on your Prusa Printer
- Go to "connect.prusa3d.com", "Camera", "Add new web camera"
- Note down the token next to the qr code
- Click on the qr code
- Allow camera connection in browser
- On firefox, press ctrl-shift-i to get the developer menu, click on "Network". Now press "START CAMERA" 
- You should see a request with status "204", click on it. On the "Request Headers" Tab, you should see at the very end the "fingerprint" value, note this down as well

# Installation
- ssh to your raspberry pi: "ssh pi@raspicam", enter your password if asked
- "sudo raspi-config"
- In raspi-config, enable legacy camera support via "Interface -> legacy camera -> yes -> ok -> Finish"
- Reboot via "sudo reboot" and then reconnect via ssh "ssh pi@raspicam"
- "sudo apt update"
- "sudo apt dist-upgrade"
- "sudo apt install python git -y"
- "git clone https://github.com/bkerler/raspicam_prusa"
- "cd raspicam_prusa"
- Edit the raspicam_prusa.py and replace the token and fingerprint values with the ones you were writing down : "nano raspicam_prusa.py"
- Save and quit via ctrl-o, enter, ctrl-x
- "sudo cp raspicam.service /etc/systemd/system/raspicam.service"
- "sudo systemctl daemon-reload"
- "sudo systemctl enable raspicam"
- "sudo systemctl start raspicam"
- "sudo systemctl status raspicam"
- If you see no error, all is good and you should start to see pictures after a few seconds on prusa connect


