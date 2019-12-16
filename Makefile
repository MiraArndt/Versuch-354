all: build/main.pdf

# hier Python-Skripte:
build/plot1.pdf: Plots/plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot1.py

build/plot2.pdf: Plots/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot2.py

build/plot3.pdf: Plots/plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot3.py

build/plot4.pdf: Plots/plot4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot4.py

build/plot5.pdf: Plots/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot5.py

build/plot1-1.pdf: Plots/plot1-1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python Plots/plot1-1.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1.pdf	build/plot2.pdf build/plot3.pdf build/plot4.pdf build/plot5.pdf build/plot1-1.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
