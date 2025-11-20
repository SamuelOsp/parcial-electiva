# Parcial de Calidad de Software – Respuestas Teóricas y Análisis

## Parte 1: Conceptos de CI/CD

### 1. Diferencia entre CI y CD

**CI (Continuous Integration):**  
Es la práctica de integrar cambios en el repositorio de forma frecuente. Cada push activa pruebas automáticas, linters y validaciones para detectar errores lo antes posible.  
En este parcial, el CI corresponde al workflow que ejecuta los tests de Python y el linter Flake8 cada vez que hago push.

**CD (Continuous Delivery/Deployment):**  
Es la etapa posterior al CI.  
- **Delivery:** El software queda listo para ser desplegado manualmente.  
- **Deployment:** Se despliega automáticamente a producción sin intervención humana.

---

## Parte 4: Validación y Análisis de Logs

### Identificación de fallos

Para encontrar un fallo en GitHub Actions, se revisa el paso que aparece con una cruz roja. Ahí se ve el error exacto.

**Tipos de fallos:**

- **Errores de Linter (Flake8):**  
  Aparecen como códigos E o W, indicando el tipo de error y la línea.  
  Ejemplo: `line 16:1`.

- **Errores de Pruebas (Pytest):**  
  Una prueba fallida se marca con una F roja. Al final aparece la sección **FAILURES** con el detalle de la aserción.

- **Errores de Cobertura:**  
  Se muestran al final si el porcentaje queda por debajo del umbral (80%).

---

## Análisis de mis ejecuciones

### 1. Run Fallido (Linter)

**Causa:**  
El pipeline falló en la etapa de análisis con Flake8.

**Detalles:**  
El código funcionaba, pero el linter aplicó reglas estrictas. En los logs aparecieron:

- `W292`: faltaba un salto de línea al final del archivo.  
- `W391`: sobraba una línea vacía.  
- `E302`: faltaban líneas en blanco entre funciones.

**Consecuencia:**  
El pipeline se detuvo antes de ejecutar los tests (Exit code 1).

---

### 2. Run Exitoso

**Solución:**  
Corregí el formato del archivo `calculadora.py` y configuré Flake8 para ignorar errores menores de espacios en blanco:

**Resultado:**  
El pipeline completó todas las fases exitosamente (check verde ✅) y la cobertura alcanzó el 80% requerido.

---