#!/bin/bash
set -exuo pipefail

[[ -n "${WINBLUES_CHEZMOI_ORIGINAL_ENV_FILE-}" ]] && source "${WINBLUES_CHEZMOI_ORIGINAL_ENV_FILE}"

# TODO: check user's config to see if they don't want us to manage wallpapers

function set_tiled_background {
  workspace_id=$1
  image=$2
  xfconf-query --channel xfce4-desktop --list |
    grep "workspace${workspace_id}/color-style" |
    xargs -I{} xfconf-query --create -c 'xfce4-desktop' -p {} --type 'int' --set 0

  xfconf-query --channel xfce4-desktop --list |
    grep "workspace${workspace_id}/image-style" |
    xargs -I{} xfconf-query --create -c 'xfce4-desktop' -p {} --type 'int' --set 2

  xfconf-query --channel xfce4-desktop --list |
    grep "workspace${workspace_id}/last-image" |
    xargs -I{} xfconf-query --create -c 'xfce4-desktop' -p {} --type 'string' --set "$image"
}

# Allow setting a different wallpaper per workspace
xfconf-query --create -c 'xfce4-desktop' -p '/backdrop/single-workspace-mode' --type 'bool' --set 'false'

set_tiled_background 0 "/usr/share/backgrounds/Platinum9/Finder/OS9_Default.png"
set_tiled_background 1 "/usr/share/backgrounds/Platinum9/Finder/OS8_Default.png"
set_tiled_background 2 "/usr/share/backgrounds/Platinum9/Finder/CD_OS8.png"
set_tiled_background 3 "/usr/share/backgrounds/Platinum9/Finder/CD_OS9.png"
