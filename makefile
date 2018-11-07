# SHELL := '/bin/bash'

run:
	python manage.py runserver

migrate:
	python manage.py migrate

make-migrations:
	python manage.py makemigrations

static:
	python manage.py collectstatic

git-log:
	git log --graph --oneline --decorate -n 5

git-log+:
	git log --stat --graph --decorate

# Atualiza os pacotes instalados
pip-upgrade:
	pip install --upgrade $$(pip list --format=freeze | cut -d = -f 1);
	pip freeze > requirements.txt
	sed -i ':a;N;$$!ba;s/pkg-resources==0.0.0\n//g' requirements.txt

# Executa os testes do projeto e exibe saída simplificada no terminal
test:
	# python -m unittest discover
	python manage.py test

# Executa os testes do projeto e exibe informações detalhadas de cada "test case"
test-detailed:
	# python -m unittest discover -v
	python manage.py test -v 3

#Deleta arquivos com extensão pyc do módulo tests
delete-pyc:
	find ./tests -name "*.pyc" -delete

# Gera relatório de cobertura de testes em formato HTML
coverage-html:
	coverage run manage.py test
	coverage html
	firefox htmlcov/index.html 2> /dev/null

# Gera relatório de cobertura de testes simplificado no terminal
coverage:
	coverage run manage.py test
	coverage report
