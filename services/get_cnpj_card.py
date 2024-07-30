import requests
import os
import json
import re
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def formatar_cnpj(cnpj):
    cnpj_formatado = re.sub(r'\D', '', cnpj)
    if len(cnpj_formatado) == 14:
        return cnpj_formatado
    else:
        raise ValueError("CNPJ deve conter 14 dígitos.")

def get_cnpj_card(cnpj, filename):
    url = f'https://www.receitaws.com.br/v1/cnpj/{formatar_cnpj(cnpj)}'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        

        doc = SimpleDocTemplate(os.path.join(os.getcwd(), "py", "static", "pdf", f"{filename}.pdf"), pagesize=letter)
        styles = getSampleStyleSheet()

        # Cabeçalho
        header = Paragraph('<b>Informações da Empresa</b>', styles['Heading1'])

        # Informações básicas
        data = [
            ('Abertura:', dados['abertura']),
            ('Situação:', dados['situacao']),
            ('Tipo:', dados['tipo']),
            ('Nome:', dados['nome']),
            ('Fantasia:', dados['fantasia']),
            ('Porte:', dados['porte']),
            ('Natureza Jurídica:', dados['natureza_juridica']),
        ]

        info_basicas = []
        for label, value in data:
            info_basicas.append(Paragraph(f'<b>{label}</b> {value}', styles['Normal']))

        # Atividades
        atividades_principal = dados['atividade_principal'][0]['text']
        atividades_secundarias = [act['text'] for act in dados['atividades_secundarias']]
        atividades = [
            ('Atividade Principal:', atividades_principal),
            ('Atividades Secundárias:', ', '.join(atividades_secundarias)),
        ]

        info_atividades = []
        for label, value in atividades:
            info_atividades.append(Paragraph(f'<b>{label}</b> {value}', styles['Normal']))

        # Quadro de Sócios e Administradores (QSA)
        qsa = ['{} - {}'.format(member['nome'], member['qual']) for member in dados['qsa']]
        qsa_text = ', '.join(qsa)
        qsa_info = Paragraph(f'<b>Quadro de Sócios e Administradores:</b> {qsa_text}', styles['Normal'])

        # Endereço e Contato
        endereco = dados['logradouro'] + ', ' + dados['numero'] + ' - ' + dados['bairro'] + ', ' + dados['municipio'] + ' - ' + dados['uf'] + ', CEP: ' + dados['cep']
        contato = f'Email: {dados["email"]} | Telefone: {dados["telefone"]}'
        end_contato = Paragraph(f'<b>Endereço:</b> {endereco}<br/><b>Contato:</b> {contato}', styles['Normal'])

        # Capital Social
        capital_social = f'Capital Social: R$ {float(dados["capital_social"]):,.2f}'
        capital = Paragraph(f'<b>{capital_social}</b>', styles['Normal'])

        # Adicionando todos os elementos ao conteúdo do PDF
        content = [header, Spacer(1, 12)]
        content.extend(info_basicas)
        content.append(Spacer(1, 12))
        content.extend(info_atividades)
        content.append(Spacer(1, 12))
        content.append(qsa_info)
        content.append(Spacer(1, 12))
        content.append(end_contato)
        content.append(Spacer(1, 12))
        content.append(capital)

        # Construir o PDF
        doc.build(content)
        return os.path.join(os.getcwd(), "py", "static", "pdf", f"{filename}.pdf")
    else:
        return None
    