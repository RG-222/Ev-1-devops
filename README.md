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

5. Reflexión Personal
Al realizar esta entrega sola por ingreso tardío decidí hacer uso de la IA como mi guía para entender a detalle cada movimiento que hacía, en especial cómo GitFlow ayuda al orden simulando estar trabajando de forma colaborativa o incluso como filtro de calidad, ademas utilicé una app muy simple según los requerimientos dandole más importancia a lo que hice en Github.
