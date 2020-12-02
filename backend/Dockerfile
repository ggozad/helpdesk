FROM python:3.8.5-buster
# ARG VERSION=99.0.0

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# Do not write .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Do not ever buffer console output
ENV PYTHONUNBUFFERED 1

# We need gettext to get the envsubst command
RUN \
    apt-get update && \
    apt-get install --no-install-recommends -y gettext && \
    rm -r /var/cache/apt /var/lib/apt

RUN pip install poetry==1.0.10

RUN mkdir -p /var/vault
VOLUME [ "/var/vault"]

COPY poetry.lock pyproject.toml /app/
COPY backend /app/backend/
COPY etc/env.in /app/etc/
WORKDIR /app
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY alembic.ini /app/
COPY alembic /app/alembic/
COPY docker/runner /usr/bin/runner

RUN \
    adduser --disabled-password --no-create-home --disabled-login --system backend
RUN chown -R backend /app

VOLUME ["/app/alembic/versions"]

USER backend
EXPOSE 8000

ENTRYPOINT ["/usr/bin/runner"]
CMD ["start"]
