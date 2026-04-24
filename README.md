# 🚀 Inter Task

Sistema web desenvolvido para gerenciamento de tarefas, permitindo organização, controle e acompanhamento de atividades de forma simples e eficiente.

---

## 📖 Sobre o Projeto

O **Inter Task** é uma aplicação web voltada para gerenciamento de tarefas (tasks), ideal para uso pessoal ou em equipe.  
O sistema permite criar, visualizar, editar e remover tarefas, facilitando o controle do fluxo de trabalho.

Este projeto foi desenvolvido utilizando boas práticas de desenvolvimento web, com foco em organização de código, escalabilidade e facilidade de uso.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Django
- SQLite (ou outro banco configurado)
- HTML5
- CSS3
- JavaScript (opcional)
- Bootstrap (opcional)

---

## ⚙️ Funcionalidades

- ✅ Cadastro de tarefas  
- 📋 Listagem de tarefas  
- ✏️ Edição de tarefas  
- ❌ Exclusão de tarefas  
- 🔍 Visualização detalhada  
- 📅 Organização por status/data  

---

## 📂 Estrutura do Projeto

```bash
inter-task/
│
├── tasks/               # App principal (lógica de tarefas)
├── templates/           # Arquivos HTML
├── static/              # CSS, JS e imagens
├── db.sqlite3           # Banco de dados
├── manage.py            # Gerenciador do Django
└── README.md
🚀 Como Executar o Projeto
🔧 Pré-requisitos

Antes de começar, você precisa ter instalado:

Python 3.x
pip
virtualenv (opcional, mas recomendado)
📥 Clonar o repositório
git clone https://github.com/VITINHUS29/inter-task.git
cd inter-task
🧪 Criar ambiente virtual
python -m venv venv

Ativar:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
📦 Instalar dependências
pip install -r requirements.txt

Caso não exista o requirements.txt:

pip install django
🗄️ Aplicar migrações
python manage.py makemigrations
python manage.py migrate
▶️ Rodar o servidor
python manage.py runserver

Acesse no navegador:

http://127.0.0.1:8000/
👤 Acesso ao Admin (Opcional)

Criar superusuário:

python manage.py createsuperuser

Acesse:

http://127.0.0.1:8000/admin/
🧠 Conceitos Aplicados
Arquitetura MTV (Model-Template-View)
CRUD completo
Organização modular com Django Apps
Separação de responsabilidades
Boas práticas de versionamento com Git
📌 Melhorias Futuras
🔐 Sistema de autenticação de usuários
📊 Dashboard com estatísticas
🏷️ Filtros e categorias de tarefas
🌐 API REST com Django REST Framework
📱 Interface responsiva aprimorada
🤝 Contribuição

Contribuições são bem-vindas!

Faça um fork do projeto
Crie uma branch
git checkout -b minha-feature
Commit suas alterações
git commit -m "feat: minha nova feature"
Push para o repositório
git push origin minha-feature
Abra um Pull Request
📄 Licença

Este projeto está sob a licença MIT.

👨‍💻 Autor

Desenvolvido por Vitor

GitHub: https://github.com/VITINHUS29
