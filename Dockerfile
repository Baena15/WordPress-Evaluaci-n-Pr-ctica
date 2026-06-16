FROM wordpress:php8.3-apache

# Instalar WP-CLI para gestión automatizada de plugins/temas
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

# Copiar tema hijo personalizado y assets
COPY wp-content/themes/urbanfit-child /var/www/html/wp-content/themes/urbanfit-child
COPY assets /var/www/html/assets

# Exponer el puerto 80 (Railway detectará esto automáticamente)
EXPOSE 80
