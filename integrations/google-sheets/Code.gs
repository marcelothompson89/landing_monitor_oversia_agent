/**
 * Oversia — Recepción de solicitudes del formulario de contacto en Google Sheets.
 *
 * Este script se pega en el editor de Apps Script de una Google Sheet y se
 * publica como "Aplicación web". Recibe los POST del formulario de la landing
 * y agrega una fila por cada solicitud.
 *
 * Instrucciones completas en el README.md de esta carpeta.
 */

// (Opcional) Correo que recibe un aviso por cada nueva solicitud. Deje '' para desactivar.
const NOTIFY_EMAIL = '';

const SHEET_NAME = 'Solicitudes';
const HEADERS = ['Fecha', 'Nombre', 'Empresa', 'Email', 'País', 'Rubro', 'Tipo'];

function doPost(e) {
  try {
    const p = (e && e.parameter) || {};

    // Honeypot anti-spam: si el campo oculto viene completo, es un bot. Ignorar.
    if (p.website) {
      return jsonOutput({ ok: true, ignored: true });
    }

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    let sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
    }
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
    }

    const tipo = p.tipo === 'informe' ? 'Informe de muestra' : 'Demostración';
    sheet.appendRow([
      new Date(),
      p.nombre || '',
      p.empresa || '',
      p.email || '',
      p.pais || '',
      p.rubro || '',
      tipo
    ]);

    if (NOTIFY_EMAIL) {
      MailApp.sendEmail({
        to: NOTIFY_EMAIL,
        subject: `Nueva solicitud (${tipo}) — ${p.empresa || 'sin empresa'}`,
        body: [
          `Tipo: ${tipo}`,
          `Nombre: ${p.nombre || ''}`,
          `Empresa: ${p.empresa || ''}`,
          `Email: ${p.email || ''}`,
          `País: ${p.pais || ''}`,
          `Rubro: ${p.rubro || ''}`
        ].join('\n')
      });
    }

    return jsonOutput({ ok: true });
  } catch (err) {
    return jsonOutput({ ok: false, error: String(err) });
  }
}

function jsonOutput(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}
