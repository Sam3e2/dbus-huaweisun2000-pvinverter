#!/bin/bash

. /opt/victronenergy/serial-starter/run-service.sh

app="python /opt/victronenergy/dbus-huaweisun2000-pvinverter/dbus-huaweisun2000-pvinverter.py"
args="/dev/$tty"
start $args
