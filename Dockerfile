# 1. Imagen base oficial de Python
FROM python:3.10-slim

# 2. Directorio de trabajo
WORKDIR /app

# 3. Copiar las dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar todo el código del proyecto
COPY . .

# 5. Exponer el puerto de Flask
EXPOSE 5000

# 6. Comando de arranque
CMD ["python", "app.py"]