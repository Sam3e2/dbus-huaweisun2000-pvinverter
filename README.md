# dbus-huaweisun2000-pvinverter

dbus driver for victron cerbo gx / venus os for (old series) huawei sun 2000 inverter.

## Purpose

This script is intended to help integrate a Huawei Sun 2000 inverter into the Venus OS and thus also into the VRM portal.

The code is based on https://github.com/kcbam/dbus-huaweisun2000-pvinverter. That driver used the internal WiFi of the inverter. It seems, that older series doesn't have WiFi, so I rewrote the driver to support modbus RTU. 

The registers addresses are taken from https://www-file.huawei.com/~/media/CORPORATE/PDF/FusionSolar/HUAWEI_SUN2000_245KTL28KTL_MODBUS_Interface_Definitions_20150715_JP.pdf.

## Todo

The code is working, but is not clean and doesn't support all features of the inverter.

- [ ] alarm, state
- [ ] more values: temperature, efficiency
- [ ] clean code

## Hardware prequisites

- Venus OS device (e.g. Cerbo GX)
- (old) Huawei Sun 2000 inverter with modbus RTU interface
- USB to RS485 adapter

I assume that newer series of Huawei Sun 2000 use a different register mapping. So this driver probably won't work with newer inverters.

## Installation

1. Copy the full project directory to the /data/etc folder on your venus:

    - /data/dbus-huaweisun2000-pvinverter/

   Info: The /data directory persists data on venus os devices while updating the firmware

   Easy way:
   ```
   wget https://github.com/Sam3e2/dbus-huaweisun2000-pvinverter/archive/refs/heads/main.zip
   unzip main.zip -d /data
   mv /data/dbus-huaweisun2000-pvinverter-main /data/dbus-huaweisun2000-pvinverter
   chmod a+x /data/dbus-huaweisun2000-pvinverter/install.sh
   rm main.zip
   ```


2. Edit the config.py file

   `nano /data/dbus-huaweisun2000-pvinverter/config.py`

3. Check Modbus RTU Connection to gridinverter

   The driver can be tested standalone. To do this, disable serial-starter for the serial port you want to use. For example, to disable the serial port /dev/ttyUSB0, run the following commands:

   ```
   /opt/victronenergy/serial-starter/stop-tty.sh /dev/ttyUSB0
   python /data/dbus-huaweisun2000-pvinverter/dbus-huaweisun2000-pvinverter.py /dev/ttyUSB0
   ```

   To enable the serial port again, run:

   ```
   /opt/victronenergy/serial-starter/start-tty.sh /dev/ttyUSB0
   ```

4. Run install.sh

   `sh /data/dbus-huaweisun2000-pvinverter/install.sh`

### Debugging

If you have problems with the script, first try to run it standalone as described above. If the script runs without problems, but does not work as a service, check the serial starter log file:

`tail -F -n 100 /data/log/serial-starter/current | tai64nlocal`

If the service is started, you can check the log file:

`tail -F -n 100 /data/log/dbus-huaweisun2000.ttyUSB*/current | tai64nlocal`

If the service is not started, you can check the service binding of serial-starter:

`head /data/var/lib/serial-starter/*`

## Uninstall the script

Run

```
sh /data/dbus-huaweisun2000-pvinverter/uninstall.sh
rm -r /data/dbus-huaweisun2000-pvinverter/
```

# Thank you
## Contributers

DenkBrettl

## Used libraries

modified verion of https://github.com/olivergregorius/sun2000_modbus

## this project is inspired by

https://github.com/kcbam/dbus-huaweisun2000-pvinverter

https://github.com/RalfZim/venus.dbus-fronius-smartmeter

https://github.com/fabian-lauer/dbus-shelly-3em-smartmeter.git

https://github.com/victronenergy/velib_python.git