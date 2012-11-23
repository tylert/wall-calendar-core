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
    rem2ps -i -l -e -olrtb 1 -sthed 8 > $@

calendar_rac_en.pdf : calendar_rac_en.ps watermark_rac.pdf Makefile
	@cat $< | sed \
    -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
	    | ps2pdf - - | pdftk - background watermark_rac.pdf output $@ uncompress

calendar_rac_fr.ps : $(wildcard *.rem) Makefile
	@remind.fr -p12 -b1 -gdddd calendar_rac.rem $(DATE) |\
    rem2ps.fr -i -l -e -olrtb 1 -sthed 8 > $@

calendar_rac_fr.pdf : calendar_rac_fr.ps watermark_rac.pdf Makefile
	@cat $< | sed \
    -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
    -e 's/\xc3\x83\|\xc2\x89/\d201/g' \
    -e 's/\d195\d162/\d226/g' \
    -e 's/\d195\d168/\d232/g' \
    -e 's/\d195\d169/\d233/g' \
    -e 's/\d195\d170/\d234/g' \
    -e 's/\d195\d171/\d235/g' \
    -e 's/\d195\d180/\d244/g' \
      | ps2pdf - - | pdftk - background watermark_rac.pdf output $@ uncompress

# man iso_8859-1
#   ® -> Â®    -> \303\202\302\256 -> \xc3\x82\|\xc2\xae -> \d174
#   É -> Ã -> \303\203\302\211 -> \xc3\x83\|\xc2\x89 -> \d201
#   â -> Ã¢    -> \d195\d162 -> \d226
#   è -> Ã¨    -> \d195\d168 -> \d232
#   é -> Ã©    -> \d195\d169 -> \d233
#   ê -> Ãª    -> \d195\d170 -> \d234
#   ë -> Ã«    -> \d195\d171 -> \d235
#   ô -> Ã´    -> \d195\d180 -> \d244

%.pdf : %.ps
	@ps2pdf $< $@

%.pdf : %.svg
	@inkscape -T -A $@ $<

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)
