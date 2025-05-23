#!/bin/bash

set -xeuo pipefail

cd /tmp
wget https://github.com/timnetworks/Platinum9/archive/refs/heads/master.zip
unzip *.zip
cd Platinum9-master

mv NineIcons /usr/share/icons
mv Charcoal.ttf MONACO.TTF /usr/share/fonts

mv OS9-wallpaper /usr/share/backgrounds/Platinum9

# Greeter background
montage /usr/share/backgrounds/Platinum9/Finder/OS9_Default.png -tile 10x10 -geometry +0+0 /usr/share/backgrounds/Platinum9/greeter.png

cd boot
unzip System8-master.zip
cd System8-master
mv System8 /usr/share/plymouth/themes

plymouth-set-default-theme System8

update-mime-database /usr/share/mime
gdk-pixbuf-query-loaders-64 --update-cache
#gtk-update-icon-cache --force --ignore-theme-index /usr/share/icons/NineIcons

# Panel config
cd /usr/share/winblues/chezmoi/dot_local/share/xfce-panel-profile
tar cjf /usr/share/xfce4-panel-profiles/layouts/blue9.tar.bz2 config.txt
