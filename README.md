# 💰 Controle de Finanças Pessoais

Este projeto é um sistema em Python + FastAPI para gerenciar gastos mensais.
Ele permite adicionar, excluir e visualizar gastos, salvando os dados em um arquivo JSON para persistência, além de oferecer uma interface web simples para interação, podendo ser utlizado via terminal também.


---

Funcionalidades
- Adicionar gastos por mês (formato MM/YYYY).
- Excluir gastos específicos de um mês.
- Visualizar o total de gastos por mês.
- Gerar relatório anual com totais por mês e soma geral.
- Interface web (index.html) para interação com a API.
- Persistência dos dados em arquivo gastos.json.

---

Tecnologias utilizadas
- Python 3.10+
- FastAPI → criação da API.
- Uvicorn → servidor para rodar a API.
- HTML + CSS + JavaScript → interface web.
- Módulos padrão:
- datetime → validação de datas.
- json → salvar e carregar os dados.

Para rodar o API, instale as bibliotecas continda no requirements.txt.
Rode o comando no terminal python:

uvicorn main:app --reload

documentação: http://127.0.0.1:8000/docs



---
