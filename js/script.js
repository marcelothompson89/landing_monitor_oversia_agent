// Endpoint del Web App de Google Apps Script (ver integrations/google-sheets/README.md).
// Pegue aquí la URL que le da Google al publicar el script como aplicación web.
const FORM_ENDPOINT = 'https://script.google.com/macros/s/AKfycbyP_ThzWoy2n0WpBAzrzDAvBAOh8cqXmv2uxe0kUvk4Ffov1eWsiR0QrIqJI4CARMZH9Q/exec';

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('contact-form');
  const status = document.getElementById('form-status');
  const submitBtn = document.getElementById('submit-btn');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    // Honeypot: si un bot completó el campo oculto, simulamos éxito y no enviamos.
    if (data.website) {
      form.reset();
      return;
    }

    const esInforme = data.tipo === 'informe';
    const nombre = data.nombre.split(' ')[0];

    submitBtn.disabled = true;
    submitBtn.textContent = 'Enviando...';
    status.className = 'form-status';
    status.textContent = '';

    try {
      await fetch(FORM_ENDPOINT, { method: 'POST', body: formData, mode: 'no-cors' });

      status.textContent = esInforme
        ? `Gracias, ${nombre}. Le enviaremos un informe de muestra a ${data.email} a la brevedad.`
        : `Gracias, ${nombre}. Nos pondremos en contacto con usted en ${data.email} para coordinar la demostración.`;
      status.classList.add('success');
      form.reset();
    } catch (err) {
      status.textContent = 'No pudimos enviar su solicitud. Vuelva a intentarlo o escríbanos a info@oversiasolutions.com.';
      status.classList.add('error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'Solicitar demostración';
    }
  });

  const sampleLink = document.getElementById('sample-link');
  sampleLink.addEventListener('click', (e) => {
    e.preventDefault();
    const informeRadio = document.querySelector('input[name="tipo"][value="informe"]');
    if (informeRadio) informeRadio.checked = true;
    document.getElementById('nombre').focus();
    status.textContent = 'Complete el formulario y le enviaremos un informe de muestra por correo.';
    status.className = 'form-status';
  });
});
