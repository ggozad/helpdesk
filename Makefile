all:
	docker-compose up

dev:
	docker-compose -f docker-compose.yml -f dev-backend.yml up

clean:
	 docker-compose rm -v -f && docker volume prune -f