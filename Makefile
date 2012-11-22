SHELL := /bin/bash

GENERATED_FILES = calendar.ps calendar.pdf rulers.pdf \
  calendar_rac_en.ps calendar_rac_en.pdf \
  calendar_rac_fr.ps calendar_rac_fr.pdf watermark_rac.pdf

.PHONY : all
all : $(GENERATED_FILES)

calendar.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd calendar.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar.pdf : calendar.ps rulers.pdf Makefile
	@a2ps -Xiso1 -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-2S output - uncompress |\
      pdftk - background rulers.pdf output $@ uncompress

calendar_rac_en.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd calendar_rac.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar_rac_en.pdf : calendar_rac_en.ps watermark_rac.pdf Makefile
	@ps2pdf $< - | pdftk - background watermark_rac.pdf output $@ uncompress

calendar_rac_fr.ps : $(wildcard *.rem) Makefile
	@remind.fr -p12 -b1 -gdddd calendar_rac.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

calendar_rac_fr.pdf : calendar_rac_fr.ps watermark_rac.pdf Makefile
	@cat $< | sed \
    -e 's/\d195\d162/\d226/g' \
    -e 's/\d195\d168/\d232/g' \
    -e 's/\d195\d169/\d233/g' \
    -e 's/\d195\d170/\d234/g' \
    -e 's/\d195\d171/\d235/g' \
    -e 's/\d195\d180/\d244/g' \
      | ps2pdf - - | pdftk - background watermark_rac.pdf output $@ uncompress
# man iso_8859-1
# Ã<89>
#   -e 's/\d195\d089/\d201/g' \

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
