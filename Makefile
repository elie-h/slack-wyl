.PHONY: lint

lint: lint-ruff lint-black
checks: lint typecheck

lint-ruff:
	@ruff --format=github --target-version=py311 ./api

lint-black:
	@black --check ./api

typecheck:
	@pyright ./api
