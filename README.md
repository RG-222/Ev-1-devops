# Ev-1-devops
Entrega Evaluación Parcial 1 - DevOps
1. Estrategia de Ramificación
Se implementó el modelo GitFlow.

Justificación: Elegimos GitFlow porque permite un desarrollo organizado. La rama develop sirve para integrar funcionalidades, mientras que main se reserva para versiones estables. Las ramas hotfix/ permiten corregir errores críticos en producción sin detener el desarrollo de nuevas características.

2. Convenciones de Trabajo
Commits: Usamos prefijos claros como feat: para nuevas funciones y fix: para correcciones.

Ramas: Nombres descriptivos, por ejemplo feature/nueva-suma.

Revisiones: Se requiere un Pull Request para pasar código de una rama a otra, asegurando la trazabilidad.

3. Automatización - GitHub Actions
Se configuró un flujo de CI (Integración Continua) que se dispara con cada push. Esto asegura que el microservicio mantenga su calidad antes de ser mezclado.

4. Declaración de Uso de IA
Se utilizó Gemini (Google) como apoyo para la estructuración de comandos Git, diseño del flujo de trabajo y redacción técnica de este documento.

Para cumplir con los objetivos de la asignatura, diseñé un entorno de trabajo que garantiza la trazabilidad y la automatización mediante los siguientes pasos:

Configuración de GitFlow: No se trabajó directamente sobre la rama main. Se estableció la rama develop como el eje central de integración. Esto permite que el código en producción (main) nunca se vea afectado por errores durante el desarrollo.

Ciclo de Vida de Funcionalidades (Features): Cada mejora se desarrolló en una rama independiente (feature/). Esto facilita el trabajo en paralelo y permite que cada cambio sea revisado individualmente antes de ser mezclado.

Gestión de Errores Críticos (Hotfixes): Implementé una rama de hotfix/ que nace de main. Esto simula un entorno real donde, si ocurre un error en producción, se puede corregir y desplegar rápidamente sin esperar a que las otras funcionalidades en desarrollo estén listas.

Validación mediante Pull Requests: Utilicé los Pull Requests como un mecanismo de control de calidad. Cada integración requirió una revisión manual de los cambios, lo que asegura que solo el código validado llegue a las ramas principales.

Integración Continua (CI) con GitHub Actions: Configuré un archivo de automatización (.yml) que actúa como un "vigilante". Cada vez que se sube código, el sistema intenta ejecutar el proyecto. Si algo falla, el equipo es notificado de inmediato, cumpliendo con los estándares de CI/CD para una entrega de software confiable.

Reflexión Personal
Al realizar esta entrega sola por ingreso tardío decidí hacer uso de la IA como mi guía para entender a detalle cada movimiento que hacía, en especial cómo GitFlow ayuda al orden simulando estar trabajando de forma colaborativa o incluso como filtro de calidad, ademas utilicé una app muy simple según los requerimientos dandole más importancia a lo que hice en Github.
