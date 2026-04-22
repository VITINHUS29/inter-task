# Inter Task

Sistema web de gerenciamento de tarefas desenvolvido com **Django + Django REST Framework**, com interface moderna inspirada no estilo do banco Inter.

---

##  Funcionalidades

✅ Cadastro e login de usuários  
✅ Dashboard com visão geral das tarefas  
✅ CRUD completo de tarefas (Criar, listar, editar, excluir)  
✅ Organização por categorias  
✅ Visualização em lista, kanban e calendário  
✅ API REST para integração externa   
✅ Painel administrativo do Django  
✅ Interface moderna (estilo Inter)

---

##  Tecnologias utilizadas

- Python 3.x
- Django
- Django REST Framework
- SQLite
- HTML5 + CSS3
- JavaScript

---

##  Estrutura do Projeto


inter-task/
│
├── manage.py
├── requirements.txt
├── .gitignore
│
├── taskmanager/ # Configurações do projeto
│
├── tasks/ # App principal
│ ├── models.py
│ ├── views.py
│ ├── api_views.py
│ ├── serializers.py
│ ├── urls.py
│ ├── api_urls.py
│ │
│ ├── templates/tasks/
│ ├── static/tasks/
│ └── migrations/
│
└── db.sqlite3


---

##  Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/VITINHUS29/inter-task.git
cd inter-task
2. Crie o ambiente virtual
python -m venv venv
3. Ative o ambiente virtual
Windows:
venv\Scripts\activate
Linux/Mac:
source venv/bin/activate
4. Instale as dependências
pip install -r requirements.txt
5. Rode as migrações
python manage.py makemigrations
python manage.py migrate
6. Crie um superusuário
python manage.py createsuperuser
7. Execute o servidor
python manage.py runserver
8. Acesse no navegador
http://127.0.0.1:8000/
 Acesso ao Admin
http://127.0.0.1:8000/admin/

Use o superusuário criado.

 API REST
Endpoint principal:
GET /api/tasks/
Exemplo de retorno:
[]

Você pode usar ferramentas como:

Postman
Insomnia
Thunder Client (VS Code)

 Interface

O layout foi inspirado em interfaces modernas como:

Dashboard limpo
Cores minimalistas
Botões intuitivos
UX focado em produtividade
 Melhorias futuras
Notificações em tempo real
Upload de arquivos
Compartilhamento de tarefas
Deploy em produção
Integração com apps mobile
 Licença

Este projeto é livre para uso acadêmico e aprendizado.

 Autor

Desenvolvido por Vitor

GitHub:
 https://github.com/VITINHUS29

⭐ Se curtir o projeto

Deixa uma ⭐ no repositório pra ajudar!
