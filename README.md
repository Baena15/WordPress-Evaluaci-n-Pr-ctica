# UrbanFit Gym — Sitio corporativo en WordPress

Sitio web corporativo para un gimnasio ficticio, construido con WordPress + Elementor.

## Entorno local con Docker

### Requisitos

- Docker Desktop
- Docker Compose

### Iniciar el proyecto

```bash
cd urbanfit-gym
docker compose up -d
```

### Acceder al sitio

- WordPress: http://localhost:8080
- phpMyAdmin: http://localhost:8081

### Credenciales por defecto (local)

- Base de datos: `urbanfit_db`
- Usuario BD: `urbanfit_user`
- Password BD: `urbanfit_password`
- Root BD: `root_password_urbanfit`

## Despliegue en Railway

1. Sube este repositorio a GitHub.
2. Crea un nuevo proyecto en Railway y conecta el repositorio.
3. Añade un servicio de MySQL/MariaDB en Railway.
4. Configura las variables de entorno en Railway:
   - `WORDPRESS_DB_HOST`
   - `WORDPRESS_DB_NAME`
   - `WORDPRESS_DB_USER`
   - `WORDPRESS_DB_PASSWORD`
   - `WORDPRESS_TABLE_PREFIX`
5. Railway usará el `Dockerfile` para construir y desplegar WordPress.

## Estructura del proyecto

```
urbanfit-gym/
├── docker-compose.yml    # Entorno local
├── Dockerfile            # Imagen para Railway
├── .env.example          # Plantilla de variables
├── .gitignore
└── README.md
```
