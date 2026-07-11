# 🚀 Microservicio Flask - Evaluación Final (DevOps)

**Integrante:** Renata Antonia González Agurto  
**Asignatura:** Ingeniería DevOps 006V - Duoc UC  
**Fecha de Entrega:** 11 de Julio de 2026  

---

## 🏗️ 1. Arquitectura del Entorno Orquestado (IE1 / IE2 / IE5)

En cumplimiento con las directrices institucionales (descarte de Kubernetes en entornos locales restringidos), se implementó un entorno orquestado avanzado utilizando **Docker Compose** que simula un entorno productivo seguro, robusto y auto-monitoreado, complementado con el diseño declarativo de manifiestos para la escalabilidad empresarial.

El stack se compone de servicios interconectados en una red privada aislada:
* **web_app (Microservicio Flask):** Construido mediante una estrategia Multi-Stage para optimizar el peso de la capa final. Opera bajo un usuario seguro no-root (`devopsuser`), cuenta con un archivo `.dockerignore` para evitar la filtración de contexto y expone un endpoint de salud `/health`.
* **prometheus (Monitoreo - IE11):** Servidor de observabilidad nativo que realiza un raspado (*scrape*) de métricas de rendimiento cada 5 segundos apuntando al endpoint `/metrics` del microservicio. Cuenta con persistencia de datos mediante un volumen dedicado.
* **Manifiestos de Alta Disponibilidad (Carpeta `/k8s` - IE10):** Se incluye la arquitectura declarativa para el despliegue a gran escala en Kubernetes, configurando un deployment de **3 réplicas** con políticas de auto-reparación (*Self-Healing*), mallas de servicio mediante **Istio** (`Gateway` y `VirtualService`) y centralización conceptual de logs hacia **AWS CloudWatch** (IE12).

---

## 🛡️ 2. Políticas de Cumplimiento Normativo y SAST (IE8 / IE13)

Para garantizar la gobernanza del código y la seguridad de la cadena de suministro de software, se integraron cuatro ejes de validación automatizada dentro del ciclo de vida (DevSecOps):

* **Análisis SAST (Static Application Security Testing):** Se incorporó **Bandit** en el pipeline CI/CD para auditar el código fuente ante vulnerabilidades (como hardcoded binds).
* **Análisis SCA (Software Composition Analysis):** Se mantiene la gobernanza de librerías de terceros mediante **Snyk** y alertas automatizadas de Dependabot.
* **Calidad de Código y Gobernanza:** Integración con la nube de **SonarCloud** para evaluar el cumplimiento de Quality Gates antes del despliegue masivo.
* **Branch Protection & GitFlow (IE3):** Se ejecutó el flujo bajo la metodología **GitFlow**. El repositorio cuenta con reglas de protección que exigen la validación del pipeline y auditoría mediante *Pull Requests* para la fusión de ramas hacia `main`.

---

## 📊 3. Observabilidad y Dashboard de Métricas (IE11 / IE14)

El pipeline CI/CD genera dinámicamente un reporte de métricas clave (Dashboard) guardado como artefacto de ejecución tras cada despliegue automatizado exitoso. Las métricas críticas observadas para la toma de decisiones técnicas son:

* **Disponibilidad del Sistema (Healthcheck):** Monitoreo continuo mediante urllib nativo que valida el estado healthy del contenedor. Si la app arroja errores, el pipeline se interrumpe de inmediato (Mecanismo de Ruptura - IE6).
* **Cobertura de Código (Code Coverage):** Evaluado con `pytest-cov`, alcanzando un **86% de cobertura** analizada sobre las rutas críticas y de negocio del microservicio web.

---

## 🔑 4. Enlaces, Credenciales y Accesos para Revisión

Para facilitar la evaluación del entorno orquestado y la gobernanza del código, se declaran los siguientes accesos oficiales:
* **Estado del Repositorio:** El ciclo de desarrollo ha finalizado exitosamente. El código auditado se encuentra unificado y disponible en la rama de producción **`main`**, manteniendo la trazabilidad histórica del Pull Request desde `develop`.
* **Registro de Contenedores (Docker Hub - IE6):** La imagen final inmutable ha sido empaquetada y distribuida automáticamente a la nube. Está disponible públicamente en: `rg222/ev1-devops:latest` (etiquetada adicionalmente con su respectivo `github.sha` para control de versiones).
* **Acceso y Visibilidad:** Al tratarse de un repositorio de carácter **público**, el evaluador tiene acceso irrestricto de lectura para auditar el código fuente, el historial de GitHub Actions, los logs de SonarCloud y los flujos de trabajo de CI/CD de forma directa.
* **Dashboard como Artefacto:** El reporte de métricas y cobertura se genera automáticamente tras la ejecución exitosa del pipeline y queda guardado como el artefacto descargable `dashboard_report.md` en la pestaña **Actions** de GitHub.

---

## 🤖 5. Declaración de Uso de IA Institucional

* **Herramienta Utilizada:** Gemini AI.
* **Ámbito de Aplicación:** Apoyo en la optimización de sintaxis para flujos de trabajo de GitHub Actions, refactorización del Healthcheck nativo de Python para Docker Compose, diseño conceptual de la arquitectura en Kubernetes/Istio, y estructuración técnica del presente reporte. Toda la validación, ejecución del pipeline en verde y pruebas en el repositorio fueron controladas y ejecutadas por el alumno.
