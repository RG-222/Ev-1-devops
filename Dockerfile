# Capa de compilación y dependencias (Multi-stage simulado para optimizar)
FROM python:3.10-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Capa final de producción
FROM python:3.10-slim

WORKDIR /app

# Copiar dependencias instaladas desde la capa anterior
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar código de la app
COPY app.py .
COPY test_app.py .

# Seguridad: Crear usuario no-root para no correr con privilegios de administrador
RUN useradd -m devopsuser && chown -R devopsuser:devopsuser /app
USER devopsuser

# Exponer puerto del microservicio
EXPOSE 5000

# Ejecutar aplicación
CMD ["python", "app.py"]