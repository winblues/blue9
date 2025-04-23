#!/bin/bash
set -ouex pipefail

systemctl --global preset-all
dnf5 -y config-manager setopt "terra*".enabled=false
