.PHONY: run test

run:
	uvicorn backend.main:app --reload

test:
	pytest
