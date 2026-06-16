#!/bin/bash
set -e

# Railway/V2 runtime sometimes enables mpm_event in addition to mpm_prefork.
# Ensure only mpm_prefork is active before starting Apache.
if [ -L /etc/apache2/mods-enabled/mpm_event.load ] || [ -e /etc/apache2/mods-enabled/mpm_event.load ]; then
    a2dismod mpm_event || true
fi
if [ ! -L /etc/apache2/mods-enabled/mpm_prefork.load ] && [ ! -e /etc/apache2/mods-enabled/mpm_prefork.load ]; then
    a2enmod mpm_prefork || true
fi

# Execute the original WordPress entrypoint
exec docker-entrypoint.sh apache2-foreground "$@"
