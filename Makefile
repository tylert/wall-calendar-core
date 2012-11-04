SHELL := /bin/bash

GENERATED_FILES = calendar.ps calendar.pdf rulers.pdf \
  rac_calendar_en.pdf rac_calendar_fr.ps rac_calendar_fr.pdf rac_watermark.pdf

.PHONY : all
all : $(GENERATED_FILES)

calendar.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd top.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar.pdf : calendar.ps rulers.pdf Makefile
	@a2ps -Xiso1 -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@ uncompress

rac_calendar_en.pdf : $(wildcard *.rem) rac_watermark.pdf Makefile
	@remind -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 | ps2pdf - |\
      pdftk - background rac_watermark.pdf output $@ uncompress

rac_calendar_fr.ps : $(wildcard *.rem) rac_watermark.pdf Makefile
	@remind.fr -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

rac_calendar_fr.pdf : rac_calendar_fr.ps rac_watermark.pdf Makefile
	@cat $< | sed \
    -e 's/\d195\d162/\d226/g' \
    -e 's/\d195\d168/\d232/g' \
    -e 's/\d195\d169/\d233/g' \
    -e 's/\d195\d170/\d234/g' \
    -e 's/\d195\d171/\d235/g' \
    -e 's/\d195\d180/\d244/g' \
      | ps2pdf - - |\
        pdftk - background rac_watermark.pdf output $@ uncompress

# man iso_8859-1

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
