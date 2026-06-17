# Desafio b2bflow

Projeto desenvolvido em Python que realiza:

- Leitura de contatos cadastrados no Supabase;
- Busca de até 3 contatos;
- Personalização de mensagens;
- Envio de mensagens via WhatsApp utilizando a Z-API.

## Estrutura da tabela

Tabela: contatos

Campos:
- id
- nome
- telefone

## Variáveis de ambiente

Crie um arquivo `.env`:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/inacioviana/b2bflow-python.git
cd b2bflow-python
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` baseado no `.env.example` e preencha:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Execução

```bash
python main.py
```