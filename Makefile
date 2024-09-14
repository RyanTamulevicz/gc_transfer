all: run

run:
	uv run src/main.py

install: 
	pyinstaller --name gc-transfer --onefile --add-data "images;images" src/main.py
