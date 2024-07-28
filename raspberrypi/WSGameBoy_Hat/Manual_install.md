# Raspberry Pi Game HAT

![Game HAT](Game-HAT-3.jpg) ---> i will put a pic of mine :) almost finshed --- adding 7/28

![GitHub stars](https://img.shields.io/github/stars/ailynux/pieceofpy?style=social)
![GitHub forks](https://img.shields.io/github/forks/ailynux/pieceofpy?style=social)
![GitHub issues](https://img.shields.io/github/issues/ailynux/pieceofpy)
![GitHub license](https://img.shields.io/github/license/ailynux/pieceofpy)

## Game HAT for Raspberry Pi - Make Your Own Retro Portable Games

### Note
Please focus on the direction of the battery. If you connect the battery in reverse, the charging circuit will be damaged. Pay attention to this when mounting the battery.

## Features
- 3.5inch IPS screen, 480 × 320 resolution.
- 60-frame experience, smooth display, no more frame loss.
- Compatible with Raspberry Pi A+/B+/2B/3B/3B+/4B (Raspberry Pi Zero/Zero W/Zero WH requires another HDMI cable).
- Integrates battery charge circuitry, powered from an 18650 lithium battery (NOT included), plays anywhere anytime.
- Battery capacity indicator.
- Onboard speaker and earphone jack, listen to the familiar BGM from the old days.

## User Guides

### Hardware Connection
1. Insert Raspberry Pi to Game HAT (GPIO pin headers).
2. Connect HDMI. Insert the HDMI connector into the screen and Raspberry Pi.
3. If you use Raspberry Pi Zero/Raspberry Pi Zero W, you need to use an HDMI cable.
4. Toggle the Battery switch of Game HAT to OFF, and mount the 18650 battery to it.

### Using RetroPie

#### Method 1: Use Pre-built Image
1. Download the appropriate Retropie image: from the waveshare wiki.

#### Method 2: Install Driver Manually
1. Download the Retropie image from the Retropie website according to your Raspberry Pi type.
2. Download and unzip to get a .img file.
3. Write the .img file to the TF card using Win32DiskImager.exe.
4. Copy the Game HAT driver to the root directory of the TF card.
5. Open the config.txt file on the root directory, and append the following statements:
   ```text
   hdmi_force_hotplug=1
   hdmi_group=2
   hdmi_mode=87
   hdmi_cvt=640 480 60 1 0 0 0
   ```

6. Inset the TF card and a USB keyboard to Raspberry Pi, and open the Battery switch to power on Raspberry Pi. After booting, press F4 to open Terminal.
7. Install the joystick driver according to the image version you are using.
<br>   **【Note】The GanmeHAT must be connected to the network, or else the driver won't be successfully installed.**
```bash
cd RetroPie-Setup/
sudo ./retropie_setup.sh
```
- Select Manage Packages > Manage Driver Packages > mkarcadejoystick > Install from source.
- Exit RetroPie-Setup.
```bash
sudo nano /etc/modprobe.d/mk_arcade_joystick_rpi.conf
```
- Modify the line to:
```bash
options mk_arcade_joystick_rpi map=5 gpio=5,6,13,19,21,4,26,12,23,20,16,18
```
- Save and reboot.
8. For retropie-v4.6 or earlier
```bash
sudo tar xzvf /boot/Game-HAT-*.tar.gz
cd Game-HAT/
sudo ./Game-HAT
```
## Using Recalbox
1. Download the newest Recalbox image from the official website.
2. Write the image to your TF card using Win32DiskImager.
3. Modify the config.txt file:
```text
hdmi_force_hotplug=1
hdmi_group=2
hdmi_mode=4
hdmi_drive=2
display_rotate=0
avoid_warnings=1
```
4. Insert the SD card into the Raspberry Pi, connect to Game HAT, and connect the HDMI adapter. Turn on the power switch.
5. Login via SSH (Raspberry Pi needs to be connected to the Internet:
```bash
mount -o remount,rw /
mount -o remount,rw /boot
nano /recalbox/share/system/recalbox.conf
```
- Change "controllers.gpio.enabled=0" to "controllers.gpio.enabled=1" and modify as follows:
```bash
##controller.gpio.args=map=1,2
controllers.gpio.args=map=5 gpio=5,6,13,19,21,4,26,12,23,20,16,18,-1
```
- Save and reboot.

# Adding New Games
1. Expand the filesystem first. Choose RASPI-CONFIG on the configure page.
```Text
Advanced Options -> A1 Expand Filesystem -> Enter -> Finish
```
2. Reboot
3. Download ROMs of your games.
4. Connect your Raspberry Pi to the network.
5. Use the IP address of your Raspberry Pi to access it from your PC.
6. Restart the emulator to see the added games.

## Setup WIFI

### In Retropie or Raspberry Pi OS
1. Download and unzip the `wpa_supplicant.conf` file.
2. Modify the SSID and password in the file and save.
3. Copy the file to the root directory of Raspberry Pi OS/Retropie and reboot.

### In Recalbox OS
1. Press START to enter the MENU.
2. Choose NETWORK SETTING.
3. Set ENABLE WIFI to ON.
4. Enter the SSID and password.

## Interfaces
| PIN | SYMBOL | Description       |
|-----|--------|-------------------|
| 1   | 3.3V   | 3.3V power input  |
| 2   | 5V     | 5V Power input    |
| ... | ...    | ...               |
| 40  | START  | BCM=21, WPI=29    |

## FAQ
**Q: How long could the Li-ion battery last for?**  
**A:** The battery could last for about 1~2 hours, depending on the game. It supports charging and playing.

**Q: What is the charging voltage and current of Game HAT?**  
**A:** Use a 5V/2A power adapter. If the voltage exceeds 7V, it will damage the charging circuit.

**Q: What is the default password of Recalbox?**  
**A:** Username: `reboot`, password: `recalboxroot`.

## Resources
- [User Manual](https://www.waveshare.com/wiki/Game_HAT)
- [Setting for Recalbox](https://www.waveshare.com/wiki/Game_HAT)
- [Images](https://www.waveshare.com/wiki/Game_HAT)
  - [Retropie for Pi 2/3B/3B+](https://www.waveshare.com/wiki/Game_HAT)
- [Driver](https://www.waveshare.com/wiki/Game_HAT)
- [3D Drawing](https://www.waveshare.com/wiki/Game_HAT)
  - [Game HAT 3D Drawing](https://www.waveshare.com/wiki/Game_HAT)

## Support
If you encounter any issues or have any questions, please open an issue in this repository or reach out through the following:

- [Waveshare Support](https://www.waveshare.com/wiki/Game_HAT#Support)
- Email: support@waveshare.com

I encourage you to check the [FAQ](#faq) section before reaching out for quicker resolutions to common problems. I strayed away a lot from the original documents due to aging and update but this is the guide I followed to manually install everything and get things up and running. HAPPY BUILDING! 

## Acknowledgments
A lot of this information was sourced from the [Waveshare Wiki](https://www.waveshare.com/wiki/Game_HAT).

Thank you for your support! If you like this project, please give it a star to help others find it.





