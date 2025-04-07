#!/bin/bash

set -exuo pipefail

dnf install --nogpgcheck --repofrompath 'terra,https://repos.fyralabs.com/terra$releasever' terra-release

rpm-ostree install vala-panel-appmenu
