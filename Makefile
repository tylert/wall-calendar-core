SHELL := /bin/bash

YEAR ?= $(shell date +%Y)

GENERATED_FILES = calendar.ps calendar.pdf \
  calendar_mrow.ps calendar_mrow.pdf floral_border.pdf \
  rac_calendar_en.ps rac_calendar_en.pdf \
  rac_calendar_fr.ps rac_calendar_fr.pdf rac_watermark.pdf

.PHONY : all
all : $(GENERATED_FILES)

# Personal calendars

calendar.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd calendar.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar.pdf : calendar.ps
	@a2ps -Xiso1 -2B --borders=no $< -o - | ps2pdf - |\
    pdftk - cat 1-endS output $@ uncompress

calendar_mrow.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd calendar_mrow.rem $(DATE) |\
    rem2ps -l -e -olrtb 1 -sthed 8 > $@

calendar_mrow.pdf : calendar_mrow.ps floral_border.pdf
	@ps2pdf $< - |\
    pdftk - background floral_border.pdf output $@ uncompress

# Public calendars

rac_calendar_en.ps : $(wildcard *.rem) Makefile
	@remind -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps -i -l -e -olrtb 1 -sthed 8 > $@

rac_calendar_fr.ps : $(wildcard *.rem) Makefile
	@remind.fr -p12 -b1 -gdddd rac_calendar.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

rac_calendar_en.pdf : rac_calendar_en.ps rac_watermark.pdf
	@cat $< | sed \
    -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
	    | ps2pdf - - | pdftk - background rac_watermark.pdf output $@ uncompress

rac_calendar_fr.pdf : rac_calendar_fr.ps rac_watermark.pdf
	@cat $< | sed \
    -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
    -e 's/\xc3\x83\|\xc2\x89/\d201/g' \
    -e 's/\d195\d162/\d226/g' \
    -e 's/\d195\d168/\d232/g' \
    -e 's/\d195\d169/\d233/g' \
    -e 's/\d195\d170/\d234/g' \
    -e 's/\d195\d171/\d235/g' \
    -e 's/\d195\d180/\d244/g' \
	     | ps2pdf - - | pdftk - background rac_watermark.pdf output $@ uncompress

# man iso_8859-1
#   ® -> Â® -> \303\202\302\256 -> \xc3\x82\|\xc2\xae -> \d174
#   É -> Ã -> \303\203\302\211 -> \xc3\x83\|\xc2\x89 -> \d201
#   â -> Ã¢ -> \d195\d162 -> \d226
#   è -> Ã¨ -> \d195\d168 -> \d232
#   é -> Ã© -> \d195\d169 -> \d233
#   ê -> Ãª -> \d195\d170 -> \d234
#   ë -> Ã« -> \d195\d171 -> \d235
#   ô -> Ã´ -> \d195\d180 -> \d244

.PHONY : burst
burst :
	@pdftk rac_calendar_en.pdf burst output en%02d.pdf uncompress
	@pdftk rac_calendar_fr.pdf burst output fr%02d.pdf uncompress

%.pdf : %.svg
	@inkscape -T -A $@ $<

%.pdf : %.odt
	@libreoffice --headless --convert-to pdf $^

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)


# (c) 2008 - 2013 7601999 Canada, Inc.  All rights reserved.
