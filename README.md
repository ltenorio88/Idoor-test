# IDOR Tester

Ferramenta simples para testar vulnerabilidades do tipo IDOR (Insecure Direct Object Reference) em ambientes autorizados, CTFs ou laboratórios de pentest.

## 🚨 Aviso Legal

Esta ferramenta **só deve ser usada em ambientes com permissão expressa** (como CTFs, pentests autorizados ou ambientes de teste controlado). Uso não autorizado pode ser considerado crime conforme a legislação local.

## ⚙️ Requisitos

- Python 3.7+
- `requests` (`pip install requests`)

## ▶️ Como usar

1. Edite o arquivo `idor_tester.py` com:
   - `base_uuid`: o UUID base a partir do qual serão feitas tentativas.
   - `base_url`: URL real do endpoint de teste.
   - `sid` e outros parâmetros conforme seu cenário.

2. Execute:

```bash
python idor_tester.py
```

3. Veja o terminal para respostas e o arquivo `idor_test_log.txt` para logs detalhados.

## 💡 Funcionalidades

- Testa UUIDs próximos ao fornecido (`±10` por padrão)
- Exibe no terminal códigos HTTP e detecta palavras-chave na resposta
- Salva log completo das tentativas

## 🔧 Melhorias Futuras

- Suporte a IDs numéricos, base64 ou hash
- Interface gráfica ou web
- Suporte a autenticação via cookie/token

## 🧑‍💻 Contribuições

Sinta-se livre para abrir issues, forks ou PRs para melhorias!

---

**Criado para fins educacionais e éticos.**


## 🧪 Outros tipos de testes incluídos

- `idor_numeric.py` – Testa URLs com IDs numéricos sequenciais.
- `idor_base64.py` – Testa URLs onde o ID é codificado em Base64.
- `idor_hash.py` – Testa URLs com IDs hashed (MD5 por padrão, mas pode ser SHA1 ou SHA256).

Edite os arquivos para configurar o endpoint e ID base, e execute da mesma forma:

```bash
python idor_numeric.py
python idor_base64.py
python idor_hash.py
```


## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔰 Logo ASCII

```
 _____ _____  _____   _____         _             
|_   _|  _  ||  _  | |  _  |_ _ ___| |_ ___ ___ ___ 
  | | |     ||     | |   __| | |   | '_| -_|_ -|_ -|
  |_| |__|__||__|__| |__|  |___|_|_|_,_|___|___|___|

          IDOR TESTER - by Tenorio (2025)
```