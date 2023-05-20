
SRC=hw
EXE=$(SRC)


do: console

all: console postscript troff clean

console: lua \
	 clean


lua: $(SRC).lua
	@echo "Hello world en $@..."
	lua $<


clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class
