FROM wordpress:php8.3-apache

# Forzar el MPM prefork para evitar el conflicto "More than one MPM loaded"
RUN a2dismod mpm_event && a2enmod mpm_prefork

# Herramientas necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

# Instalar el tema padre y los plugins directamente en /usr/src/wordpress para
# que el entrypoint oficial de WordPress los copie junto con el core.
RUN set -e; \
    mkdir -p /usr/src/wordpress/wp-content/themes /usr/src/wordpress/wp-content/plugins; \
    \
    curl -L -o /tmp/hello-elementor.zip https://downloads.wordpress.org/theme/hello-elementor.zip && \
    unzip -q /tmp/hello-elementor.zip -d /usr/src/wordpress/wp-content/themes/ && \
    rm /tmp/hello-elementor.zip; \
    \
    for plugin in elementor contact-form-7 wordpress-seo; do \
        echo "Installing plugin: ${plugin}"; \
        curl -L -o /tmp/${plugin}.zip https://downloads.wordpress.org/plugin/${plugin}.zip && \
        unzip -q /tmp/${plugin}.zip -d /usr/src/wordpress/wp-content/plugins/ && \
        rm /tmp/${plugin}.zip; \
    done

# Copiar tema hijo, assets y uploads al origen de WordPress
COPY wp-content/themes/urbanfit-child /usr/src/wordpress/wp-content/themes/urbanfit-child
COPY assets /usr/src/wordpress/assets
COPY wp-content/uploads /usr/src/wordpress/wp-content/uploads

# Entrypoint personalizado
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]
EXPOSE 80
