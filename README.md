# Parcial de Calidad de Software Avanzado

Este proyecto implementa un pipeline de CI completo utilizando GitHub Actions para una aplicación en Python.

## Estrategia de CI (Parte 1)

### Herramientas seleccionadas
* **Lenguaje:** Python (versátil y estándar en la industria para scripting y backend).
* **Linter:** `flake8`. Es ligero, rápido y verifica el cumplimiento de PEP 8 sin configuración excesiva.
* **Pruebas/Cobertura:** `pytest` y `pytest-cov`. Pytest es el framework más moderno para python y su plugin de cobertura se integra nativamente.

### Umbral de Cobertura
Se ha definido un **umbral del 80%**.
*Justificación:* El 100% suele ser costoso de mantener y ofrece rendimientos decrecientes. Un 80% asegura que la lógica crítica está probada sin obligar a probar getters/setters triviales o configuraciones.

## Ejecución Local con nektos/act (Parte 3)

**¿Qué es act?**
`act` es una herramienta que permite ejecutar workflows de GitHub Actions localmente usando contenedores Docker. Simula el entorno de GitHub para detectar errores antes de hacer push.

**Requisitos:**
* Docker Desktop instalado y corriendo.
* `act` instalado (vía Chocolatey, Brew o binario).

**Comando de ejecución:**
Para correr el pipeline completo en tu máquina:

```bash
act push