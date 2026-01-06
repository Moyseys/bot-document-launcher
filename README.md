# Sienge Title Automation Bot

https://github.com/user-attachments/assets/d8156576-15c5-4000-b8a5-6c97711c6ecd

Este bot em Python automatiza o processo de lançamento de títulos no sistema Sienge, utilizando a biblioteca PyAutoGUI para interação com a interface gráfica do usuário. Ele permite que os usuários realizem lançamentos de forma eficiente e sem intervenção manual constante.

## Funcionalidades

- **Automação de Lançamentos**: Automatiza o processo de lançamento de títulos no sistema Sienge, economizando tempo e minimizando erros manuais.
- **Interação com o Usuário**: Permite que o usuário escolha a linha do relatório de onde iniciar o lançamento e verifica periodicamente se o processo deve continuar.
- **Ponto de Segurança**: Após um número configurável de lançamentos, o bot pausa para confirmar se o usuário deseja continuar, evitando lançamentos indesejados.
- **Logs de Lançamento**: A cada lançamento feito pelo bot é registrado na raiz do projeto um arquivo `.json` com os logs, contendo o título, número do documento, uma mesagem e a linha da plainlha que foi lançada.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `PyAutoGUI`
  - `pandas` (se o bot utilizar planilhas Excel)
  
## Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone https://github.com/Moyseys/bot-document-launcher.git

2. Instale as dependencias:
   ```bash
      pip install

3. Prepare os dados necessários, como a planilha de títulos a serem lançados.

4. Execute o script principal:
   ```bash
      python main.py

5. Siga as instruções na tela para selecionar a linha de início e responder às solicitações de confirmação.


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias ou novas funcionalidades.
