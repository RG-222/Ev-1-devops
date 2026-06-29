# 🚀 Microservicio Flask - Evaluación Parcial 3 (DevOps)

**Integrante:** Renata Antonia González Agurto  
**Asignatura:** Ingeniería DevOps 006V - Duoc UC  
**Fecha de Entrega:** 28 de Junio de 2026  

---

## 🏗️ 1. Arquitectura del Entorno Orquestado (IE1 / IE2 / IE5)

En cumplimiento con las directrices institucionales (descarte de Kubernetes), se implementó un entorno orquestado avanzado utilizando Docker Compose que simula un entorno productivo seguro, robusto y auto-monitoreado.

El stack se compone de dos servicios principales interconectados en una red privada aislada:
* web_app (Microservicio Flask): Construido mediante una estrategia Multi-Stage para optimizar el peso de la capa final. Opera bajo un usuario seguro no-root (devopsuser), cuenta con un archivo .dockerignore para evitar la filtración de contexto y expone un endpoint de salud /health.
* prometheus (Monitoreo): Servidor de observabilidad nativo que realiza un raspado (scrape) de métricas de rendimiento cada 5 segundos apuntando al endpoint /metrics del microservicio. Cuenta con persistencia de datos mediante un volumen dedicado.

---

## 🛡️ 2. Políticas de Cumplimiento Normativo y SAST (IE5)

Para garantizar la gobernanza del código y la seguridad de la cadena de suministro de software, se integraron tres ejes de validación automatizada:

* Análisis SAST (Static Application Security Testing): Se incorporó Bandit en el pipeline CI/CD. Este motor audita el código fuente ante vulnerabilidades (como hardcoded binds). Se documenta el uso de excepciones controladas mediante tags # nosec únicamente en entornos de contenedores declarados.
* Análisis SCA (Software Composition Analysis): Se mantiene la gobernanza de librerías de terceros mediante Snyk y alertas automatizadas de Dependabot en la ruta .github/dependabot.yml.
* Branch Protection: Se configuró una regla de protección de ramas sobre main en GitHub que exige la aprobación obligatoria de un Pull Request y el paso exitoso del pipeline antes de cualquier fusión, garantizando la trazabilidad.

---

## 📊 3. Observabilidad y Dashboard de Métricas (IE3 / IE4)

El pipeline CI/CD genera dinámicamente un reporte de métricas clave (Dashboard) guardado como artefacto de ejecución tras cada despliegue simulado exitoso. Las métricas críticas observadas para la toma de decisiones técnicas son:

* Disponibilidad del Sistema (Healthcheck): Monitoreo continuo mediante urllib nativo que valida el estado healthy del contenedor. Si la app arroja errores, el pipeline se interrumpe de inmediato (Mecanismo de Ruptura - IE6).
* Cobertura de Código (Code Coverage): Evaluado con pytest-cov, alcanzando un 86% de cobertura analizada sobre las rutas críticas y de negocio del microservicio web.

---

## 🤖 4. Declaración de Uso de IA Institucional

* Herramienta Utilizada: Gemini AI.
* Ámbito de Aplicación: Apoyo en la optimización de sintaxis para flujos de trabajo de GitHub Actions, refactorización del Healthcheck nativo de Python para Docker Compose, y estructuración técnica del presente reporte. Toda la validación, ejecución del pipeline en verde y pruebas en el repositorio fueron controladas por el alumno.