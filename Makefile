.PHONY: install deps clean deploy

install:
	@echo "Installing dependencies..."
	@pip install -r src/backend/requirements.txt
	# @pnpm install --prefix src/frontend/app

deps:
	@echo "generating dependencies..."
	@pip-compile -v src/backend/requirements.in

clean:
	@echo "Cleaning up..."

deploy:
	@okteto context use "https://cloud.okteto.com"
	@okteto deploy -n varun-dhruv --build




