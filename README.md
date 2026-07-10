# Projeto Interdisciplinar

Sistema acadêmico desenvolvido em **Python/Django** para integração de disciplinas.

## Sobre

Projeto de conclusão de curso com foco em gestão de cursos, alunos, professores e notas. Inclui funcionalidades de cadastro, relatórios e painel administrativo.

## Tecnologias

- Python 3
- Django
- SQLite
- HTML/CSS

## Configuração

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Copie `.env.example` para `.env` e configure a senha do banco.

4. Execute as migrations:

```bash
python manage.py migrate
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

## Próximos passos

- Atualizar para Django LTS.
- Migrar para PostgreSQL.
- Adicionar testes automatizados.
