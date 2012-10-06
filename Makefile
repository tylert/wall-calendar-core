SHELL := /bin/bash

GENERATED_FILES = yearly.ps yearly.fr.ps rulers.pdf calendar.pdf

.PHONY : all
all : $(GENERATED_FILES)

yearly.ps : $(wildcard *.rem)
	@remind -p12 -b1 -gdddd top.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

yearly.fr.ps : $(wildcard *.rem)
	@remind.fr -p12 -b1 -gdddd rac.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

# Ã© -> é
# Ã ̈ -> è
# Ã« -> ë
# Ãa -> ê
# Ã¢ -> â
# Ã ́ -> ô

rulers.pdf : rulers.svg
	@inkscape -T -A $@ $<

calendar.pdf : yearly.ps rulers.pdf
	@a2ps -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
