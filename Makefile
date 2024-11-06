up:
	docker compose up -d

down:
	docker compose down && docker network prune --force


restart:
	docker compose down && docker compose up --build

logs:
	docker compose logs -f
