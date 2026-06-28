up:
	docker compose up -d

build:
	docker compose up --build -d

down:
	docker compose down

logs:
	docker compose logs -f

test:
	docker compose exec mediabridge python -m pytest -v

shell:
	docker compose exec mediabridge bash
	
	