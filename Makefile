SHELL := /bin/bash

GENERATED_FILES = rac.en.pdf rac.fr.pdf watermark.pdf \
  yearly.ps calendar.pdf rulers.pdf

.PHONY : all
all : $(GENERATED_FILES)

yearly.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd top.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

rac.en.pdf : $(wildcard *.rem) watermark.pdf Makefile
	@remind -p12 -b1 -gdddd contest.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background watermark.pdf output $@

rac.fr.pdf : $(wildcard *.rem) watermark.pdf Makefile
	@remind.fr -p12 -b1 -gdddd contest.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background watermark.pdf output $@

# Ã© -> é
# Ã ̈ -> è
# Ã« -> ë
# Ãa -> ê
# Ã¢ -> â
# Ã ́ -> ô

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

calendar.pdf : yearly.ps rulers.pdf
	@a2ps -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
