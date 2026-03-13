# 🛡️ Project Hydra: Educational Ransomware Challenge

[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security: Educational](https://img.shields.io/badge/Security-Educational-green.svg)]()

Este projeto é uma implementação avançada do desafio de Ransomware da **DIO (Digital Innovation One)**. O objetivo é demonstrar, de forma prática e segura, como funciona a criptografia simétrica em ataques cibernéticos, utilizando Python e a biblioteca `pyaes`.

---

## ⚠️ AVISO LEGAL (DISCLAIMER)

Este software foi desenvolvido exclusivamente para fins **educacionais e de pesquisa**. 

* O uso desta ferramenta para criptografar dados sem autorização é **ilegal**.
* O autor não se responsabiliza por quaisquer danos causados pelo uso indevido deste código.
* **Sempre** utilize ambientes controlados (VMs ou pastas de teste) para executar scripts de segurança.

---

## 🚀 Diferenciais desta Versão

Diferente da versão básica, este projeto foi estruturado com foco em **escalabilidade** e **segurança**:

* **Arquitetura em Camadas:** Lógica separada entre `engine` (core), `utils` (interface) e `main` (execução).
* **Criptografia AES-128 CTR:** Utilização do modo *Counter (CTR)*, garantindo que o arquivo não mude de tamanho após a criptografia.
* **Interface Colorida (CLI):** Feedback visual no terminal para indicar sucessos e erros.
* **Proteção de Ambiente:** Uso de Ambientes Virtuais (`venv`) e gestão de dependências via `requirements.txt`.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **pyaes:** Implementação pura de Python para o algoritmo AES.
* **colorama:** Para estilização do terminal.

---

## 📋 Como Executar

### 1. Clonar e Configurar

# Clone o repositório

git clone [https://github.com/dgsilvino/cibersecurity-desafio-ransomware](https://github.com/dgsilvino/cibersecurity-desafio-ransomware)

# Entre na pasta

cd cibersecurity-desafio-ransomware

# Crie e ative o ambiente virtual

python -m venv venv
source venv/Scripts/activate  # No Windows (Git Bash)

# Instale as dependências

pip install -r requirements.txt



### 2 . Rodar o Desafio

python main.py



Siga as instruções no terminal para **Encriptar** ou **Decriptar** o arquivo de teste localizado em `tests/alvo.txt`.



🧠 Conceitos Aprendidos
-----------------------

Durante o desenvolvimento, foram aplicados conceitos fundamentais de cibersegurança e desenvolvimento:

* **Criptografia Simétrica:** Uso da mesma chave (AES-128) para trancar e destrancar dados.

* **Manipulação de Binários:** Leitura e escrita de arquivos em modo `rb` (read binary) e `wb` (write binary) para garantir a integridade total dos dados.

* **Tratamento de Exceções:** Implementação de barreiras contra erros comuns, como arquivos inexistentes ou chaves de tamanho inválido.

* **Arquitetura de Software:** Organização de código em módulos (`src/`) e classes para maior clareza, profissionalismo e manutenção.



**Desenvolvido por [Diego Silvino]** _Conecte-se comigo no [LinkedIn](https://www.google.com/search?q=https://linkedin.com/in/dg-silvino)_


