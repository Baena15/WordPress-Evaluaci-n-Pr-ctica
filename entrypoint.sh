#!/bin/bash
set -e

# Asegurar que solo esté cargado el MPM prefork.
a2dismod mpm_event || true
a2enmod mpm_prefork || true

# Lanzar el entrypoint oficial de WordPress en segundo plano; hará la copia
# inicial del core, creará wp-config.php y finalmente ejecutará apache2-foreground.
/usr/local/bin/docker-entrypoint.sh apache2-foreground &
APACHE_PID=$!

# Esperar a que WordPress esté realmente instalado y accesible.
MAX_WAIT=180
WAITED=0
until wp core is-installed --allow-root >/dev/null 2>&1; do
    if [ "$WAITED" -ge "$MAX_WAIT" ]; then
        echo "WARN: WordPress no estuvo listo después de ${MAX_WAIT}s; continuando sin reconfigurar."
        break
    fi
    echo "Esperando a que WordPress esté listo... (${WAITED}s)"
    sleep 2
    WAITED=$((WAITED + 2))
done

# Si WordPress está instalado y detectamos un dominio de Railway, normalizar URLs.
if wp core is-installed --allow-root >/dev/null 2>&1 && [ -n "${RAILWAY_PUBLIC_DOMAIN:-}" ]; then
    SITE_URL="https://${RAILWAY_PUBLIC_DOMAIN}"

    echo "Actualizando siteurl/home a ${SITE_URL}"
    wp option update home "$SITE_URL" --allow-root
    wp option update siteurl "$SITE_URL" --allow-root

    echo "Reemplazando URLs locales por ${SITE_URL}"
    wp search-replace 'http://localhost:8080' "$SITE_URL" --allow-root
    wp search-replace 'https://localhost:8080' "$SITE_URL" --allow-root
    wp search-replace 'http://localhost' "$SITE_URL" --allow-root

    echo "Refrescando permalinks y caché"
    wp rewrite flush --allow-root
    wp cache flush --allow-root
fi

# Mantiene Apache en primer plano para que el contenedor siga vivo.
wait "$APACHE_PID"
