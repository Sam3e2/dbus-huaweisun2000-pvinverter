#!/bin/bash

. /opt/victronenergy/serial-starter/run-service.sh

app=$(dirname $0)/dbus-huaweisun2000-pvinverter.py
args="/dev/$tty"
start $args
