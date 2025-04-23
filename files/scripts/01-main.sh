#!/bin/bash

set -exuo pipefail

dnf5 -y config-manager setopt "terra*".enabled=true
rpm-ostree install -y xfce4-vala-panel-appmenu-plugin vala-panel-appmenu-gtk-module
