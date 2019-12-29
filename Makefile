setup-pre-commit-hook:
	@if [ -d ".git/hooks" ]; then \
		cp hooks/pre-commit .git/hooks/pre-commit; \
	fi

clean:
	@find . -name '*.pyc' -delete
	@find . -name __pycache__  -type d | xargs rm -rf
	@echo clean done

install:
	CFLAGS='-std=c99' && pip install -i http://pypi.douban.com/simple -r requirements.txt --trusted-host pypi.douban.com

mysql:
	mysql -uroot --password="aixocm" -h 127.0.0.1 -e "CREATE DATABASE if not exists HBlog DEFAULT CHARACTER SET utf8"
	python manage.py makemigrations && python manage.py migrate

migrate:
	python manage.py makemigrations && python manage.py migrate

depend:
	@pip freeze > requirements.txt

pylint: setup-pre-commit-hook
	pylint -j 0 --rcfile=pylintrc apps

run:
	python manage.py runserver 0.0.0.0:8000

start:
	docker-compose start

stop:
	docker-compose stop

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

dmigrate:
	docker-compose exec api sh -c "cd /src && make migrate"

load:
	docker-compose exec api sh -c "cd /src && make load"
