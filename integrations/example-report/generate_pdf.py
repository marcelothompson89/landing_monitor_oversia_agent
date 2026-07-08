"""
Genera el informe de ejemplo en PDF (assets/informe-ejemplo-oversia.pdf).

Datos de ejemplo basados en un informe semanal real, anonimizados (sin nombrar
a ningún cliente; se usa "Laboratorios Ejemplo S.A."). Regenerar con:

    python integrations/example-report/generate_pdf.py

Requiere: pip install fpdf2
"""
import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO = os.path.join(BASE, "assets", "oversia-logo.png")
OUT = os.path.join(BASE, "assets", "informe-ejemplo-oversia.pdf")

NAVY = (11, 24, 48)
ACCENT = (37, 99, 235)
MUTED = (86, 97, 121)
BORDER = (228, 233, 242)
BGALT = (245, 247, 251)
ALTA = (192, 57, 43)
MEDIA = (183, 121, 31)
BAJA = (21, 115, 71)
PCOLOR = {"Alta": ALTA, "Media": MEDIA, "Baja": BAJA}

EXEC = ("Se analizaron 26 alertas regulatorias y sanitarias de Latinoamérica; 18 resultaron "
        "relevantes para su operación. Los focos de la semana son el uso responsable de "
        "medicamentos de venta libre (Brasil y Perú) y la cooperación regulatoria regional, "
        "que podría agilizar el acceso a productos. Dos alertas se marcaron para revisión humana.")

# (país, [alertas]) — cada alerta: titulo, fuente, fecha, prioridad, impacto, accion, url
DATA = [
 ("Argentina", [
   ("Actualización del listado de sustancias sujetas a fiscalización especial",
    "ANMAT Argentina", "29/06/2026", "Alta",
    "Mediante la Disposición 3943/26, ANMAT actualiza las listas de estupefacientes y psicotrópicos sujetos a fiscalización, lo que puede requerir ajustes de cumplimiento en productos que contengan esas sustancias.",
    "Revisar el nuevo listado y evaluar su impacto en el portfolio; involucrar al área de Asuntos Regulatorios.",
    "https://www.argentina.gob.ar/noticias/anmat-actualiza-el-listado-de-sustancias-sujetas-fiscalizacion-especial"),
   ("Nueva convocatoria de la Revista Científica ANMAT",
    "ANMAT Argentina", "01/07/2026", "Media",
    "ANMAT convoca a presentar artículos en producción y control de medicamentos y productos médicos, con impacto en la agenda científica y regulatoria del sector.",
    "Evaluar oportunidades de participación y dar seguimiento a las líneas de investigación priorizadas.",
    "https://www.argentina.gob.ar/noticias/nueva-convocatoria-de-la-revista-cientifica-anmat-0"),
   ("Acuerdo para fortalecer el acceso a medicamentos e insumos",
    "Ministerio de Salud Argentina", "30/06/2026", "Media",
    "El Ministerio firma un acuerdo para canalizar donaciones de insumos y medicamentos al sistema público con foco en calidad y trazabilidad, lo que puede incidir en la disponibilidad y el acceso a productos.",
    "Monitorear la implementación y su efecto sobre la disponibilidad de productos OTC y suplementos.",
    "https://www.argentina.gob.ar/noticias/salud-y-bnai-brith-firman-acuerdo-para-fortalecer-el-acceso-medicamentos-e-insumos"),
 ]),
 ("Brasil", [
   ("Advertencia sobre riesgos de medicamentos vendidos sin receta",
    "ANVISA Brasil", "02/07/2026", "Alta",
    "ANVISA advierte sobre los riesgos de los medicamentos de venta libre y refuerza la orientación médica en su uso, con impacto en la percepción pública y la regulación de los productos OTC.",
    "Preparar campañas de educación al consumidor sobre el uso seguro de OTC y monitorear posibles consultas públicas.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/medicamento-vendido-sem-receita-oferece-risco"),
   ("Anvisa suspende un medicamento y prohíbe productos irregulares",
    "ANVISA Brasil", "02/07/2026", "Alta",
    "ANVISA suspende el Clorhidrato de Dobutamina y prohíbe productos sin registro adecuado, lo que afecta la disponibilidad de productos en el mercado.",
    "Verificar el estado de registro del portfolio y reforzar los controles de cumplimiento.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/anvisa-suspende-medicamento-e-proibe-produtos-irregulares"),
   ("Revisión de prospecto estándar: más de 350 peticiones",
    "ANVISA Brasil", "30/06/2026", "Alta",
    "ANVISA concluye una etapa de la revisión de prospectos estándar (353 peticiones), lo que puede modificar la información obligatoria de los medicamentos.",
    "Seguir las publicaciones en el DOU y anticipar ajustes en prospectos y etiquetado.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/revisao-de-bula-padrao-anvisa-conclui-etapa-do-chamamento-e-define-encaminhamento-de-mais-de-350-peticoes"),
   ("Documentación técnica para la prescripción electrónica (SNCR)",
    "ANVISA Brasil", "30/06/2026", "Alta",
    "ANVISA publica los requisitos técnicos para integrar la prescripción electrónica al SNCR, lo que afecta la emisión digital de recetas de medicamentos controlados.",
    "Evaluar la preparación tecnológica para cumplir con los nuevos requisitos de integración.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/anvisa-publica-documentacao-tecnica-para-integracao-de-sistemas-de-prescricao-eletronica-ao-sncr"),
   ("Actualización de peticiones para IFAs agonistas del GLP-1 importados",
    "ANVISA Brasil", "30/06/2026", "Media",
    "ANVISA crea nuevos temas de petición para IFAs agonistas del GLP-1 importados, cambiando el procedimiento de protocolo según el tipo de ingreso.",
    "Actualizar los procedimientos de importación y capacitar a los equipos en la nueva clasificación.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/atualizacao-de-assuntos-de-peticao-para-ifas-agonistas-do-glp-1-importados"),
   ("Aclaración sanitaria: el ajo no es un antibiótico",
    "ANVISA Brasil", "02/07/2026", "Media",
    "ANVISA aclara que el ajo no es un antibiótico y advierte sobre el riesgo de usarlo como sustituto de tratamientos, con impacto en la percepción de los productos naturales.",
    "Considerar comunicación educativa para evitar desinformación sobre productos de autocuidado.",
    "https://www.gov.br/anvisa/pt-br/assuntos/noticias-anvisa/2026/checamos-alho-nao-e-antibiotico-saiba-quais-sao-os-perigos-para-a-sua-saude"),
 ]),
 ("Colombia", [
   ("El Invima y Anvisa fortalecen la cooperación regulatoria",
    "INVIMA Colombia", "01/07/2026", "Alta",
    "Invima y Anvisa firman un memorando para intercambiar decisiones regulatorias y agilizar la evaluación de medicamentos, con potencial de acelerar el acceso a productos en la región.",
    "Seguir la implementación e identificar oportunidades de registro más ágil en Colombia y Brasil.",
    "https://www.invima.gov.co/blog/sala-de-prensa-13/el-invima-y-anvisa-fortalecen-la-cooperacion-regulatoria-para-agilizar-el-acceso-a-tecnologias-sanitarias-525"),
   ("Alerta por comercialización fraudulenta de un producto",
    "INVIMA Colombia", "02/07/2026", "Alta",
    "Invima alerta por un producto con registro sanitario falso e incumplimientos de rotulado, lo que afecta la confianza del consumidor y refuerza la vigilancia sobre productos similares.",
    "Verificar la vigencia y el correcto uso de los registros sanitarios propios.",
    "https://www.invima.gov.co/blog/sala-de-prensa-13/invima-alerta-sobre-la-comercializacion-fraudulenta-del-agua-marca-refresk-530"),
   ("El Invima fortalece la cooperación regulatoria regional",
    "INVIMA Colombia", "01/07/2026", "Alta",
    "En la reunión de autoridades reguladoras de referencia se reafirma el compromiso de convergencia de estándares en las Américas, orientado a optimizar los procesos regulatorios.",
    "Monitorear los avances de armonización que puedan simplificar los trámites regionales.",
    "https://www.invima.gov.co/blog/sala-de-prensa-13/el-invima-fortalece-la-cooperacion-regulatoria-regional-durante-la-reunion-de-autoridades-reguladoras-nacionales-de-referencia-524"),
 ]),
 ("Perú", [
   ("Semana por el Uso Racional de Medicamentos",
    "Ministerio de Salud Perú", "02/07/2026", "Alta",
    "El Minsa, a través de Digemid, lanza una campaña con ferias y capacitaciones sobre el uso seguro de medicamentos y la prevención de la automedicación.",
    "Evaluar sumarse a la difusión y alinear la comunicación de producto con el mensaje de uso responsable.",
    "https://www.gob.pe/institucion/minsa/noticias/1414107-digemid-impulsa-semana-por-el-uso-racional-de-medicamentos-y-promover-su-uso-seguro-y-responsable"),
   ("Digemid consolida alianzas con autoridades regulatorias de las Américas",
    "Ministerio de Salud Perú", "01/07/2026", "Alta",
    "Digemid participa en la reunión de autoridades de referencia de las Américas (OPS), impulsando la cooperación y la armonización regulatoria en la región.",
    "Seguir las definiciones de armonización que puedan afectar registros y requisitos.",
    "https://www.gob.pe/institucion/minsa/noticias/1413423-digemid-fortalece-su-liderazgo-internacional-y-consolida-alianzas-estrategicas-con-autoridades-regulatorias-de-las-americas"),
   ("Feria informativa y Observatorio de Precios de Medicamentos",
    "Ministerio de Salud Perú", "30/06/2026", "Media",
    "Se presenta el Observatorio de Precios de Medicamentos, que permite comparar precios y puede influir en las decisiones de compra del consumidor.",
    "Monitorear el Observatorio y su efecto sobre la transparencia y la competitividad de precios.",
    "https://www.gob.pe/institucion/minsa/noticias/1412721-digemid-desarrolla-feria-informativa-sobre-la-promocion-y-acceso-a-medicamentos-de-calidad-a-precios-accesibles"),
 ]),
 ("Honduras", [
   ("ARSA juramenta un comité nacional de expertos en asuntos regulatorios",
    "Latam ReguNews", "29/06/2026", "Media",
    "ARSA conforma un comité de expertos que podría influir en la regulación de productos de autocuidado y OTC en el país. La fuente aporta información básica sin detalles de funciones ni plazos.",
    "Marcada para revisión humana: dar seguimiento a las funciones y recomendaciones del comité.",
    "https://latamregunews.com/honduras/arsa-juramenta-al-comite-nacional-de-expertos-en-asuntos-regulatorios/"),
 ]),
 ("México", [
   ("Capacitación en farmacología y farmacovigilancia",
    "Ministerio de Salud México", "01/07/2026", "Media",
    "Se anuncia un curso de farmacología y farmacovigilancia para profesionales de la salud, alineado con el uso seguro de medicamentos.",
    "Considerar difundir la capacitación y seguir iniciativas similares de farmacovigilancia.",
    "https://www.gob.mx/salud/prensa/165-con-capacitacion-especializada-hospital-juarez-del-centro-fortalece-innovacion-y-uso-seguro-en-medicamentos"),
 ]),
]

REVIEW = [
 ("Colombia", "Cobertura de prensa sobre la cooperación regulatoria del Invima, sin detalles normativos ni plazos concretos; confirmar alcance con la fuente oficial."),
 ("Honduras", "Juramentación de un comité de expertos con información básica; se requiere más detalle para evaluar el impacto en la regulación de productos."),
]

DISCLAIMER = ("Oversia ayuda a detectar, filtrar y priorizar información; cada alerta enlaza a la fuente "
              "oficial. La interpretación final corresponde a su equipo regulatorio y las acciones "
              "sugeridas son orientativas. No reemplaza asesoramiento jurídico, técnico ni regulatorio.")


class Report(FPDF):
    def header(self):
        if self.page_no() == 1:
            self.image(LOGO, x=15, y=11, w=38)
        else:
            self.image(LOGO, x=15, y=10, w=26)
        self.set_xy(120, 12)
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*NAVY)
        self.cell(75, 4, "OVS-2026-W27", align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_xy(120, 16)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*MUTED)
        self.cell(75, 4, "29 jun - 03 jul 2026  ·  Semana 27", align="R")
        self.set_draw_color(*BORDER)
        self.set_line_width(0.3)
        y = 24 if self.page_no() == 1 else 20
        self.line(15, y, 195, y)
        # fpdf no reposiciona el cursor tras header(): fijarlo para el cuerpo.
        self.set_xy(15, 29 if self.page_no() == 1 else 25)

    def footer(self):
        self.set_y(-16)
        self.set_draw_color(*BORDER)
        self.line(15, self.get_y(), 195, self.get_y())
        self.ln(1.5)
        self.set_font("Helvetica", "", 6.5)
        self.set_text_color(*MUTED)
        self.multi_cell(150, 3, DISCLAIMER, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_xy(-40, self.get_y())
        self.set_font("Helvetica", "B", 7)
        self.cell(25, 3, f"Página {self.page_no()}", align="R")


def label_block(pdf, label, text):
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(*NAVY)
    lw = pdf.get_string_width(label) + 1.5
    pdf.cell(lw, 4.6, label, new_x=XPos.RIGHT, new_y=YPos.TOP)
    x = pdf.get_x()
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    old = pdf.l_margin
    pdf.set_left_margin(x)
    pdf.set_x(x)
    pdf.multi_cell(195 - x, 4.6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_left_margin(old)
    pdf.set_x(old)


def alert(pdf, a):
    title, source, date, prio, impacto, accion, url = a
    if pdf.will_page_break(34):
        pdf.add_page()
    y0 = pdf.get_y()
    indent = 20
    old = pdf.l_margin
    pdf.set_left_margin(indent)
    pdf.set_x(indent)
    # título
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*NAVY)
    pdf.multi_cell(195 - indent, 5, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_x(indent)
    # meta
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*MUTED)
    meta = f"{source}   ·   {date}   ·   "
    pdf.cell(pdf.get_string_width(meta), 5, meta, new_x=XPos.RIGHT, new_y=YPos.TOP)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*PCOLOR[prio])
    pdf.cell(0, 5, f"Prioridad {prio}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1)
    pdf.set_x(indent)
    label_block(pdf, "Impacto", impacto)
    pdf.set_x(indent)
    label_block(pdf, "Acción recomendada", accion)
    pdf.set_x(indent)
    pdf.set_font("Helvetica", "U", 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 4.6, "Ver fuente oficial", link=url, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_left_margin(old)
    pdf.set_x(old)
    y1 = pdf.get_y()
    # barra de color de prioridad
    pdf.set_fill_color(*PCOLOR[prio])
    pdf.rect(15, y0, 1.4, y1 - y0, "F")
    pdf.ln(3)
    pdf.set_draw_color(*BORDER)
    pdf.line(20, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(3)


def kpi_row(pdf, items):
    gap = 4
    n = len(items)
    w = (180 - gap * (n - 1)) / n
    x = 15
    y = pdf.get_y()
    for num, lbl in items:
        pdf.set_fill_color(*BGALT)
        pdf.set_draw_color(*BORDER)
        pdf.rect(x, y, w, 18, "DF")
        pdf.set_xy(x, y + 3)
        pdf.set_font("Helvetica", "B", 17)
        pdf.set_text_color(*ACCENT)
        pdf.cell(w, 8, num, align="C", new_x=XPos.LMARGIN, new_y=YPos.TOP)
        pdf.set_xy(x, y + 12)
        pdf.set_font("Helvetica", "B", 6.5)
        pdf.set_text_color(*MUTED)
        pdf.cell(w, 3, lbl.upper(), align="C")
        x += w + gap
    pdf.set_y(y + 18)


def section_title(pdf, text):
    if pdf.will_page_break(16):
        pdf.add_page()
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 12.5)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 7, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.4)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.set_line_width(0.3)
    pdf.ln(4)


def country_title(pdf, text):
    if pdf.will_page_break(30):
        pdf.add_page()
    pdf.ln(1)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(1.5)


def build():
    pdf = Report(format="A4")
    pdf.set_auto_page_break(True, margin=20)
    pdf.set_margins(15, 28, 15)
    pdf.add_page()

    # Portada
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 5, "MONITOREO REGULATORIO Y SANITARIO  ·  LATAM", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "B", 21)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 11, "Informe regulatorio semanal", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 6, "Preparado para Laboratorios Ejemplo S.A.  ·  Semana 27  ·  2026", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(5)

    kpi_row(pdf, [("26", "Analizadas"), ("18", "Relevantes"), ("10", "Prioridad alta"), ("2", "Revisión humana")])
    pdf.ln(6)

    # Resumen ejecutivo
    y = pdf.get_y()
    pdf.set_fill_color(*BGALT)
    pdf.rect(15, y, 180, 26, "F")
    pdf.set_fill_color(*ACCENT)
    pdf.rect(15, y, 1.5, 26, "F")
    pdf.set_xy(20, y + 3)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 4, "RESUMEN EJECUTIVO", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_xy(20, y + 8)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.set_left_margin(20)
    pdf.multi_cell(172, 4.4, EXEC, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_left_margin(15)
    pdf.set_y(y + 26)
    pdf.ln(3)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, "Relevantes por prioridad:  Alta 10   ·   Media 6   ·   Baja 2", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Novedades por país
    section_title(pdf, "Novedades por país")
    for country, alerts in DATA:
        country_title(pdf, country)
        for a in alerts:
            alert(pdf, a)

    # Revisión humana
    section_title(pdf, "Temas que requieren revisión humana")
    for country, note in REVIEW:
        if pdf.will_page_break(16):
            pdf.add_page()
        y = pdf.get_y()
        pdf.set_fill_color(255, 244, 229)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_left_margin(20)
        pdf.set_x(20)
        pdf.set_text_color(*NAVY)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(0, 5, country, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_x(20)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*MUTED)
        pdf.multi_cell(175, 4.4, note, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_left_margin(15)
        pdf.set_fill_color(*MEDIA)
        pdf.rect(15, y, 1.4, pdf.get_y() - y, "F")
        pdf.ln(4)

    pdf.output(OUT)
    print("PDF generado:", OUT, "-", pdf.page_no(), "páginas")


if __name__ == "__main__":
    build()
