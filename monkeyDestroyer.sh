#!/bin/bash

var=$(adb shell ps | grep monkey | awk '{print $2}')
echo $var
adb shell kill -9 $var