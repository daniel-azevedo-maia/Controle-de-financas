
# Controle de Finanças

Um sistema para gerenciamento simples de receitas e despesas, desenvolvido em Django. Permite que o usuário controle suas finanças pessoais de maneira prática e organizada.

## Funcionalidades

- Cadastro de receitas e despesas.
- Classificação por categorias.
- Upload de comprovantes.
- Exibição de balanço financeiro (receitas, despesas e saldo).
- Exportação de dados para Excel.
- Sistema de autenticação (login, logout e cadastro de usuários).

## Tecnologias Utilizadas

- **Django**: Framework principal para o desenvolvimento.
- **OpenPyXL**: Biblioteca para exportação de dados em arquivos Excel.
- **Pandas**: Manipulação de dados para relatórios e exportações.
- **Bootstrap 4**: Estilização de templates.
- **Python Dotenv**: Gerenciamento de variáveis de ambiente.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/controle-financas.git
   cd controle-financas
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env`:
   Crie um arquivo `.env` na raiz do projeto com a seguinte estrutura:
   ```
   SECRET_KEY=sua-chave-secreta
   DEBUG=True
   ```

5. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

7. Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Como Usar

1. Acesse o sistema e faça login ou crie uma nova conta.
2. Cadastre receitas e despesas no menu "Cadastrar".
3. Visualize o balanço financeiro no menu "Listar".
4. Exporte seus dados para Excel no menu "Exportar Excel".

## Estrutura do Projeto

- **admin.py**: Configurações do Django Admin para os modelos.
- **models.py**: Definições dos modelos `Receita` e `Despesa`.
- **views.py**: Funções que implementam a lógica de negócios.
- **urls.py**: Rotas do sistema.
- **templates/**: Arquivos HTML para a interface do usuário.
- **static/**: Arquivos estáticos (CSS, JS, imagens).

## Dependências

- Django
- OpenPyXL
- Pandas
- Python Dotenv
- Bootstrap 4
