SHELL := /bin/bash

GENERATED_FILES = yearly.ps calendar.pdf rulers.pdf \
  contest.en.pdf contest.fr.pdf watermark.pdf

.PHONY : all
all : $(GENERATED_FILES)

yearly.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd top.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar.pdf : yearly.ps rulers.pdf
	@a2ps -Xiso1 -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@ uncompress

contest.en.pdf : $(wildcard *.rem) watermark.pdf Makefile
	@remind -p12 -b1 -gdddd contest.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background watermark.pdf output $@ uncompress

contest.fr.pdf : $(wildcard *.rem) watermark.pdf Makefile
	@remind.fr -p12 -b1 -gdddd contest.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background watermark.pdf output $@ uncompress

# Ã© -> é
# Ã¨ -> è
# Ã« -> ë
# Ãª -> ê
# Ã¢ -> â
# Ã ́ -> ô

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
