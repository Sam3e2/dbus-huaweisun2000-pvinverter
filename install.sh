#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo "SCRIPT_DIR: $SCRIPT_DIR"
SERVICE_NAME=$(basename $SCRIPT_DIR)
echo "SERVICE_NAME: $SERVICE_NAME"
# set permissions for script files
chmod +x $SCRIPT_DIR/*.sh
chmod +x $SCRIPT_DIR/*.py

chmod a+x $SCRIPT_DIR/restart.sh
chmod 744 $SCRIPT_DIR/restart.sh

chmod a+x $SCRIPT_DIR/uninstall.sh
chmod 744 $SCRIPT_DIR/uninstall.sh

chmod a+x $SCRIPT_DIR/service/run
chmod 755 $SCRIPT_DIR/service/run

chmod a+x $SCRIPT_DIR/service/log/run

chmod a+x $SCRIPT_DIR/start.sh
chmod 755 $SCRIPT_DIR/start.sh

# create sym-link for serial starter
cp -rf $SCRIPT_DIR /opt/victronenergy/
cp -rf $SCRIPT_DIR/service /opt/victronenergy/service-templates/dbus-huaweisun2000-pvinverter

# add service to serial-starter
# check if serial-starter.d was deleted
serialstarter_path="/data/conf/serial-starter.d"
serialstarter_file="$serialstarter_path/dbus-huaewaisun2000-pvinverter.conf"

# check if folder exists
if [ ! -d "$serialstarter_path" ]; then
    mkdir "$serialstarter_path"
fi

# check if file exists
#if [ ! -f "$serialstarter_file" ]; then
#    {
#        echo "service pvinvsun dbus-huaweisun2000-pvinverter"
#        echo "alias default gps:vedirect:pvinvsun"
#        echo "alias rs485 cgwacs:fzsonick:imt:modbus:sbattery:pvinvsun"
#    } > "$serialstarter_file"
#fi

# add install-script to rc.local to be ready for firmware update
filename=/data/rc.local
if [ ! -f $filename ]
then
    touch $filename
    chmod 755 $filename
    echo "#!/bin/bash" >> $filename
    echo >> $filename
fi

grep -qxF "$SCRIPT_DIR/install.sh" $filename || echo "$SCRIPT_DIR/install.sh" >> $filename

# The "PV inverters" page in Settings is somewhat specific for Fronius. Let's change that.
invertersSettingsFile="/opt/victronenergy/gui/qml/PageSettingsFronius.qml"

if (( $(grep -c "PageSettingsHuaweiSUN2000" $invertersSettingsFile) > 0)); then
    echo "INFO: $invertersSettingsFile seems already modified for HuaweiSUN2000 -- skipping modification"
else
    echo "INFO: Adding menu entry to $invertersSettingsFile"
    sed -i "/model: VisibleItemModel/ r $SCRIPT_DIR/gui/menu_item.txt" $invertersSettingsFile
fi

cp -av $SCRIPT_DIR/gui/*.qml /opt/victronenergy/gui/qml/

# As we've modified the GUI, we need to restart it
svc -t /service/gui

