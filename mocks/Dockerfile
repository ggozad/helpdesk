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

RUN mkdir -p /var/mail
RUN pip install behaving
VOLUME [ "/var/mail"]

RUN \
    adduser --disabled-password --no-create-home --disabled-login --system mocker
RUN chown -R mocker /var/mail

USER mocker
EXPOSE 8081

# ENTRYPOINT ["/usr/bin/runner"]
CMD ["mailmock", "-p", "8081", "-o", "/var/mail"]
