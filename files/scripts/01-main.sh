#!/bin/bash

set -exuo pipefail

dnf install -y --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' terra-release

rpm-ostree install -y xfce4-vala-panel-appmenu-plugin vala-panel-appmenu-gtk-module
