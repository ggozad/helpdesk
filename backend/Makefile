include ${PWD}/../.env
include ${PWD}/../config/hosts.env
include ${PWD}/../config/mail.env
export
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=helpdesk
POSTGRES_USER=${SQL_BACKEND_USER}
POSTGRES_PASSWORD=${SQL_BACKEND_PASSWORD}
AUTH_SECRET=${BACKEND_AUTH_SECRET}

dev-image:
	docker build -t helpdesk.backend:dev .

init-dev:
	python3 -m venv .venv
	( \
		source .venv/bin/activate; \
		pip install poetry; \
		poetry install; \
	)
dev:
	alembic upgrade head
	uvicorn backend.main:app --reload

alembic-rev:
	alembic revision --autogenerate -m "$(msg)"

