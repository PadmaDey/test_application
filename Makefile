.PHONY: run test

run:
	cd backend && uvicorn main:app --reload

test:
	cd backend && pytest


