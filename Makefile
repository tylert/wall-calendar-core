SHELL := /bin/bash

YEAR ?= $(shell date +%Y)
MONTHS ?= 13

SOURCE_DIR := source
BUILD_DIR := build

GENERATED_FILES = \
  $(wildcard $(BUILD_DIR)/*.ps) \
  $(wildcard $(BUILD_DIR)/*.pdf) \
  $(wildcard $(BUILD_DIR)/*.svg) \
  doc_data.txt


.PHONY : all
all : burst

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)


# Remind to PS

$(BUILD_DIR)/en.ps : $(wildcard source/*.rem) Makefile
	@remind.en -p$(MONTHS) -b1 -gdaad source/top.rem $(DATE) \
    | rem2ps.en -l -c3 -i -e -m Letter -sthed 8 -b 6 -t 1 -olrtb 1 > $@

$(BUILD_DIR)/fr.ps : $(wildcard source/*.rem) Makefile
	@remind.fr -p$(MONTHS) -b1 -gdaad source/top.rem $(DATE) \
    | rem2ps.fr -l -c3 -i -e -m Letter -sthed 8 -b 6 -t 1 -olrtb 1 > $@


# PS to PDF

$(BUILD_DIR)/%.pdf : $(BUILD_DIR)/%.ps
	@cat $< | sed \
    -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
    -e 's/\xc3\x83\|\xc2\x89/\d201/g' \
    -e 's/\d195\d162/\d226/g' \
    -e 's/\d195\d168/\d232/g' \
    -e 's/\d195\d169/\d233/g' \
    -e 's/\d195\d170/\d234/g' \
    -e 's/\d195\d171/\d235/g' \
    -e 's/\d195\d180/\d244/g' \
    | ps2pdf - - \
    | pdftk - output $@ uncompress
# XXX ps2pdf -sPAPERSIZE=legal - -
# XXX pdftk - background watermark_rac.pdf output $@ uncompress

# man iso_8859-1
#   ® -> Â® -> \303\202\302\256 -> \xc3\x82\|\xc2\xae -> \d174
#   É -> Ã -> \303\203\302\211 -> \xc3\x83\|\xc2\x89 -> \d201
#   â -> Ã¢ -> \d195\d162 -> \d226
#   è -> Ã¨ -> \d195\d168 -> \d232
#   é -> Ã© -> \d195\d169 -> \d233
#   ê -> Ãª -> \d195\d170 -> \d234
#   ë -> Ã« -> \d195\d171 -> \d235
#   ô -> Ã´ -> \d195\d180 -> \d244


# multi-page PDF to single-page PDF

.PHONY : burst
burst : burst_en burst_fr

.PHONY : burst_en
burst_en : $(BUILD_DIR)/en.pdf
	@pdftk $^ burst output $(BUILD_DIR)/en%02d.pdf uncompress

.PHONY : burst_fr
burst_fr : $(BUILD_DIR)/fr.pdf
	@pdftk $^ burst output $(BUILD_DIR)/fr%02d.pdf uncompress


# PDF to SVG

$(BUILD_DIR)/%.svg : $(BUILD_DIR)/%.pdf
	@inkscape --export-plain-svg $@ $^


#$(BUILD_DIR)/%.pdf : svg/%.svg
#	@inkscape --export-text-to-path --export-pdf=$@ $<

#%.pdf : %.odt
#	@libreoffice --headless --convert-to pdf $^
