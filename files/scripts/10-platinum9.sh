#!/bin/bash

set -xeuo pipefail

cd /tmp
wget https://github.com/timnetworks/Platinum9/archive/refs/heads/master.zip
unzip *.zip
cd Platinum9-master

mv NineIcons /usr/share/icons
mv Charcoal.ttf MONACO.TTF /usr/share/fonts

mv OS9-wallpaper /usr/share/backgrounds/Platinum9

cd boot
unzip System8-master.zip
cd System8-master
mv System8 /usr/share/plymouth/themes

plymouth-set-default-theme System8

update-mime-database /usr/share/mime
gdk-pixbuf-query-loaders-64 --update-cache
#gtk-update-icon-cache --force --ignore-theme-index /usr/share/icons/NineIcons
