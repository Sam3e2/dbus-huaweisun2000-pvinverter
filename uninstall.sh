#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SERVICE_NAME=$(basename $SCRIPT_DIR)
filename=/data/rc.local
rm -r /opt/victronenergy/service-templates/dbus-huaweisun2000-pvinverter
rm -r /opt/victronenergy/dbus-huaweisun2000-pvinverter

serialstarter_path="/data/conf/serial-starter.d"
serialstarter_file="$serialstarter_path/dbus-huaewaisun2000-pvinverter.conf"
rm $serialstarter_file

kill $(pgrep -f 'supervise dbus-huaweisun2000-pvinverter')
chmod a-x $SCRIPT_DIR/service/run
$SCRIPT_DIR/restart.sh
STARTUP=$SCRIPT_DIR/install.sh
sed -i "\~$STARTUP~d" $filename
