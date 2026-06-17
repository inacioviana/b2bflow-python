# Desafio b2bflow

Projeto desenvolvido em Python para automação de envio de mensagens pelo WhatsApp utilizando integração com Supabase e Z-API.

## Estrutura da Tabela

Tabela: `contatos`

Campos:
- `id`
- `nome`
- `telefone`

## Variáveis de Ambiente

Crie um arquivo `.env`:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```