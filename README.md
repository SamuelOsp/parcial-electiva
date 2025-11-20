# Parcial de Calidad de Software - CI/CD Pipeline

Este repositorio contiene la implementación de un pipeline de Integración Continua (CI) para una aplicación de calculadora en Python, enfocada en asegurar la calidad del código mediante análisis estático y pruebas automatizadas.

## Parte 1: Estrategia de Calidad

### Herramientas Seleccionadas
* **Lenguaje:** Python 3.9. Elegido por su simplicidad y robustez en herramientas de testing.
* **Linter:** `flake8`. Utilizado para garantizar el cumplimiento de los estándares PEP-8. Se configuró para ser estricto con errores de sintaxis (E9, F63) pero flexible con detalles de formato no críticos.
* **Pruebas y Cobertura:** `pytest` y `pytest-cov`. Permiten una ejecución rápida de pruebas unitarias y generan reportes claros de cobertura.

### Umbral de Cobertura
Se definió un **umbral mínimo del 80%**.
* **Justificación:** Este porcentaje asegura que la lógica de negocio crítica está probada, manteniendo un equilibrio costo-beneficio. Buscar el 100% a menudo implica probar código trivial, lo cual no añade valor significativo al producto final.

## Parte 2: Workflow CI/CD

El pipeline definido en `.github/workflows/ci-quality.yml` se ejecuta automáticamente en cada `push` y `pull_request` a la rama `main`.

**Etapas del Pipeline:**
1.  **Checkout & Setup:** Prepara el entorno con Python 3.9.
2.  **Dependencias:** Instala los paquetes listados en `requirements.txt`.
3.  **Linting:** Ejecuta `flake8`.
    * *Nota de configuración:* Se ignoraron explícitamente los errores de formato `W292`, `W293`, `E302` y `W391` para evitar fallos por espacios en blanco irrelevantes, priorizando la lógica del código.
4.  **Tests:** Ejecuta las pruebas y valida que la cobertura no sea inferior al 80%. Si esto no se cumple, el pipeline falla y detiene el proceso.

## Parte 3: Uso de nektos/act

`act` es una herramienta que permite ejecutar workflows de GitHub Actions localmente utilizando contenedores Docker.

* **Requisitos:** Docker Desktop instalado y el binario de `act`.
* **Comando de ejecución local:**
    ```bash
    act push
    ```
* **Nota de ejecución:** Para este parcial, la validación principal y las capturas de evidencia se realizaron directamente en los runners de GitHub (en la nube) para garantizar un entorno limpio y logs accesibles.