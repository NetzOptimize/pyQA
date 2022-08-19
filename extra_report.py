from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML, CSS
import datetime


# def generate_content():
#     templates_dir = "templates"
#     env = Environment(loader=FileSystemLoader(templates_dir))
#     template = env.get_template('template.html')
#     filename = "Extended Reports/content.html"
#     with open(filename, 'w') as fh:
#         fh.write(template.render(
#             var1=5,
#             var2=7,
#             h1="Hello Jinja2"
#         ))
#
#     pdf_template = env.get_template('pdf_template.html')
#
#     filename = "archive/pdf_content.html"
#     with open(filename, 'w') as fh:
#         fh.write(pdf_template.render(
#             h1="REPORT",
#             h3="report data: ",
#             date=datetime.datetime.now().strftime("%d-%m-%Y"),
#         ))
#
#     css = CSS(
#         string='''
#         @page {size:A4; margin:1cm;}
#         '''
#     )
#     HTML('archive/pdf_content.html').write_pdf('Extended Reports/content.pdf', stylesheets=[css])
