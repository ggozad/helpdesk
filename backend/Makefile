include ${PWD}/../.env
include ${PWD}/etc/.env
include ${PWD}/../config/mail.env
export

dev-image:
	docker build -t helpdesk.backend:dev .

dev-config:
	POSTGRES_HOST=localhost \
	POSTGRES_PORT="5432" \
	POSTGRES_DATABASE=helpdesk \
	POSTGRES_USER=${SQL_BACKEND_USER} \
	POSTGRES_PASSWORD=${SQL_BACKEND_PASSWORD} \
	MAIL_HOSTNAME=mail.helpdesk.local.dev \
	MAIL_PORT=mail.helpdesk.local.dev \
	envsubst < ./etc/env.in > ./etc/.env

init-dev: dev-config
	python3 -m venv .venv
	( \
		source .venv/bin/activate; \
		pip install poetry; \
		poetry install; \
	)
dev:
	alembic upgrade head
	uvicorn backend.main:app

alembic-init:
	alembic revision --autogenerate -m 'initial'

