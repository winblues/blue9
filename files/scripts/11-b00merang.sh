#!/bin/bash

set -xeuo pipefail

cd /tmp
rm -f master.zip
wget https://github.com/B00merang-Project/Mac-OS-9/archive/refs/heads/master.zip
unzip master.zip
mv Mac-OS-9-master /usr/share/themes/Mac-OS-9
