# Conectar el formulario a Google Sheets

El formulario de la landing envía cada solicitud a un **Google Apps Script**
publicado como aplicación web, que agrega una fila en una planilla. Sin backend
propio; funciona con el sitio estático en Vercel.

## Pasos (una sola vez, ~5 minutos)

1. **Cree la planilla**
   Vaya a [sheets.new](https://sheets.new) y cree una hoja de cálculo nueva
   (por ejemplo, "Oversia — Solicitudes"). No hace falta agregar encabezados: el
   script los crea solo.

2. **Abra el editor de Apps Script**
   En la planilla: menú **Extensiones → Apps Script**.

3. **Pegue el código**
   Borre el contenido de `Code.gs` en el editor y pegue el contenido de
   [`Code.gs`](./Code.gs) de esta carpeta.
   - (Opcional) Para recibir un email por cada solicitud, complete
     `NOTIFY_EMAIL` con su correo.
   - Guarde (ícono de disquete).

4. **Publique como aplicación web**
   Botón **Implementar → Nueva implementación** → engranaje → **Aplicación web**.
   - *Ejecutar como*: **Yo (su cuenta)**.
   - *Quién tiene acceso*: **Cualquier persona**.
   - Clic en **Implementar** y autorice los permisos que pida Google.

5. **Copie la URL**
   Google le da una URL que termina en `/exec`, por ejemplo:
   `https://script.google.com/macros/s/AKfy.../exec`

6. **Péguela en la landing**
   En [`js/script.js`](../../js/script.js), reemplace el valor de la constante
   `FORM_ENDPOINT` (arriba del todo) por esa URL.

7. **Pruebe**
   Abra la landing, envíe una solicitud de prueba y verifique que aparece una
   fila nueva en la hoja **Solicitudes** de la planilla.

## Notas

- **Columnas que se guardan:** Fecha, Nombre, Empresa, Email, País, Rubro, Tipo
  (Demostración / Informe de muestra).
- **Anti-spam:** el formulario incluye un campo oculto (*honeypot*). Si un bot lo
  completa, el script descarta el envío.
- **Actualizar el código:** si cambia `Code.gs`, en Apps Script haga
  **Implementar → Gestionar implementaciones → editar → Nueva versión**. La URL
  `/exec` se mantiene.
- **Migrar a Supabase más adelante:** solo habría que cambiar `FORM_ENDPOINT` y
  el destino; el formulario no requiere otros cambios.
