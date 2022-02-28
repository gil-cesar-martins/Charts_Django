# Charts_Django
Projeto que exibe um gráfico de acesso aos 6 cursos de uma suposta Escola de Programação durante um ano.

### Deploy local 
Instale as seguinte bibliotecas com o comando pip:

`pip install django django-bootstrap4 django-chartjs`

Instale as dependências no **requirements.txt**:
 
`pip freeze > requirements.txt`
 
migre os **models** para o banco de dados:
 
`python manage.py migrate`
 
Execute sua aplicação:
 
`python manage.py runserver`
 
Para acessar vá no seu navegador e  digite [http://localhost:8000](http://localhost:8000)
