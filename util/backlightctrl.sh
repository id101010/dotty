#!/bin/bash
#
# This script is used to control the backlight.
#

if [ "$1" == "up" ]; then
    xbacklight -inc 10
elif [ "$1" == "down" ]; then
    xbacklight -dec 10
elif [ "$1" == "min" ]; then
    xbacklight -set 10
elif [ "$1" == "max" ]; then
    xbacklight -set 100
fi
