from dotenv import load_dotenv
from supabase import create_client
import os
import requests

load_dotenv()

# supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Z-API
instance_id = os.getenv("ZAPI_INSTANCE_ID")
token = os.getenv("ZAPI_TOKEN")

# busca contatos
response = (
    supabase
    .table("contatos")
    .select("*")
    .limit(1) # alterar valor para enviar para mais contatos
    .execute()
)

contatos = response.data

for contato in contatos:
    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    url = (
        f"https://api.z-api.io/instances/"
        f"{instance_id}/token/{token}/send-text"
    )

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    resposta = requests.post(url, json=payload)

    print(f"Mensagem enviada para {nome}")
    print(resposta.text)