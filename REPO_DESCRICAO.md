# 🛡️ IDOR Tester — Ferramenta para exploração ética de IDORs

![banner](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)  
Ferramenta para **testes controlados de vulnerabilidades IDOR (Insecure Direct Object Reference)** em aplicações web, voltada para CTFs, laboratórios de segurança e pentests com autorização.

Ideal para profissionais de cibersegurança que desejam realizar varreduras simples e eficazes em endpoints baseados em:
- UUIDs
- IDs numéricos
- IDs codificados em Base64
- IDs criptografados (MD5, SHA1, SHA256)

---

## ⚙️ Funcionalidades

- Interface via terminal com entradas guiadas (ex: URL base, UUID inicial, SID).
- Destaque em tempo real para **possível sucesso baseado em palavras-chave**.
- Registro de **logs completos** em arquivos `.txt`.
- ASCII Art 🐂 no terminal para motivação hacker.

---

## 🧪 Testes Suportados

- `main.py`: modo interativo (UUIDs via terminal).
- `idor_tester.py`: UUIDs diretamente no código.
- `idor_numeric.py`: sequência de IDs inteiros.
- `idor_base64.py`: IDs codificados com Base64.
- `idor_hash.py`: IDs com hash MD5, SHA1 ou SHA256.

---

## 🚀 Como rodar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/idor-tester.git
cd idor-tester
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o modo interativo
```bash
python main.py
```

Você será guiado para inserir a URL, UUID base e o SID. O script testará variações próximas ao UUID fornecido.

### 4. Verifique os resultados
Os resultados são exibidos no terminal e salvos no arquivo:
```
idor_log_from_console.txt
```

---

## 📝 Requisitos

- Python 3.7+
- Biblioteca `requests`

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** – consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribua!

Pull requests são bem-vindos! Sinta-se à vontade para:
- Sugerir melhorias de segurança ou eficiência.
- Adicionar suporte a outros formatos de ID.
- Criar uma interface gráfica ou versão web do tester.
