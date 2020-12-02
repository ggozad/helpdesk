# Local Helpdesk instance

## Prerequisites

You need to have installed:

- Docker (for example via [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/))
- mkcert (via `brew install mkcert`)

## One-time initialisation

First you need to generate some passwords for your environment:

```shell
./scripts/gen-secrets > .env
```

And generate a SSL certificate:

```shell
mkcert \
    -cert-file secrets/local.helpdesk.health.pem \
    -key-file secrets/local.helpdesk.health-key.pem \
    \*.local.helpdesk.health
```

You can now start all docker containers. Start by [creating a GitHub Personal Access Token](https://github.com/settings/tokens) with the `read:packages` scope. You must use that token as the password when logging in to GitHub Packages using docker. Please not that using your normal password will work with `docker login`, but will fail when you later try to pull images.

```shell
$ docker login docker.pkg.github.com/ggozad
Username: ggozad
Password:
Login Succeeded
```

You can run run `docker-compose`:

```shell
$ docker-compose up
...
```

or just

```shell
$ make
...
```

## Removing an install

Occasionally you want to start from a clean slate. To do this you need to remove the docker containers:

```shell
$ docker-compose rm -v
Going to remove postgresql...
Are you sure? [yN] y
Removing ejabberd    ... done
Removing postgresql  ... done
...
```

And remove the volumes:

```shell
$ docker volume prune
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
3954e6dd88003c69dec805ec394c8b0ad7816f7007dc8c84e8a732e3a266bcab
fe41e5e7fbaa84448db71c0024f21046a02db3508af88795216427f4e663ff75
...
```

Alternatively just run

```shell
$ make clean
...
```

After that start again.
