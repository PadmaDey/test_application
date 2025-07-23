.PHONY: run test

run:
	cd backend && uvicorn main:app --reload

test:
	pytest



