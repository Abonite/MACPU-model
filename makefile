CC = cl.exe

build:
	$(CC) -o cup.exe ./src/main.c ./src/Decoder/decoder.c