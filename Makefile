.PHONY: install start-frontend start-backend deps clean deploy

install:
	@echo "Installing dependencies..."
	@pip install -r src/backend/requirements.txt
	@pnpm install --prefix src/frontend/app
start-frontend:
	@echo "Starting frontend..."
	@cd src/frontend/app && pnpm run dev

start-backend:
	@echo "Starting backend..."
	@cd src/backend/app && python manage.py runserver

deps:
	@echo "generating dependencies..."
	@pip-compile -v src/backend/requirements.in


clean:
	@echo "Cleaning up..."

deploy:
	@okteto context use "https://cloud.okteto.com"
	@okteto deploy -n varun-dhruv --build




