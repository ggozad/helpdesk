image:
	docker build -t helpdesk.frontend:dev .

prod-image:
	docker build -t helpdesk.frontend:prod -f Dockerfile.production .

dev:
	docker run \
		-it \
		--rm \
		-v ${PWD}:/app \
		-v /app/node_modules \
		-p 3000:3000 \
		-e CHOKIDAR_USEPOLLING=true \
		helpdesk.frontend:dev
