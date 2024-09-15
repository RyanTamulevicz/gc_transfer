all: run

run:
	uv run src/main.py

install: 
	pyinstaller --name gc-transfer --onefile --add-data "images;images" --add-data "src/data.csv;src" src/main.py

build:
	pyinstaller gc-transfer.spec