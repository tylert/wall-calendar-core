SHELL := /bin/bash

GENERATED_FILES = yearly.ps calendar.pdf rulers.pdf \
  rac_calendar_en.pdf rac_calendar_fr.ps rac_calendar_fr.pdf watermark.pdf

.PHONY : all
all : $(GENERATED_FILES)

yearly.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd top.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar.pdf : yearly.ps rulers.pdf
	@a2ps -Xiso1 -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@ uncompress

rac_calendar_en.pdf : $(wildcard *.rem) watermark.pdf Makefile
	@remind -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background watermark.pdf output $@ uncompress

rac_calendar_fr.ps : $(wildcard *.rem) watermark.pdf Makefile
	@remind.fr -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

rac_calendar_fr.pdf : rac_calendar_fr.ps watermark.pdf
	@ps2pdf $< - |\
    pdftk - background watermark.pdf output $@ uncompress

# 's/Ã©/é/g'
# 's/Ã¨/è/g'
# 's/Ã«/ë/g'
# 's/Ãª/ê/g'
# 's/Ã¢/â/g'
# 's/Ã´/ô/g'

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
