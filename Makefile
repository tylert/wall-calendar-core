# Tools required:  make, remind, sed, ghostscript, pdftk, inkscape

SHELL := /bin/bash

TOP_CALENDAR ?= source/top.rem
SOURCE_FILES ?= $(TOP_CALENDAR) $(wildcard source/*.rem)
BUILD_DIR ?= build

MEDIA ?= legal
YEAR ?= $(shell date +%Y)
DATE ?= jan 1 $(YEAR)

MONTHS ?= 12
RANGE = $(shell seq --format "%02g" $(MONTHS))
EN_PDFS = $(addprefix $(BUILD_DIR)/,$(addsuffix .pdf,$(addprefix en,$(RANGE))))
FR_PDFS = $(addprefix $(BUILD_DIR)/,$(addsuffix .pdf,$(addprefix fr,$(RANGE))))
EN_SVGS = $(EN_PDFS:.pdf=.svg)
FR_SVGS = $(FR_PDFS:.pdf=.svg)

GENERATED_FILES = \
  $(wildcard $(BUILD_DIR)/*.ps) \
  $(wildcard $(BUILD_DIR)/*.pdf) \
  $(wildcard $(BUILD_DIR)/*.svg) \
  doc_data.txt


.PHONY : all
all : $(BUILD_DIR)/en.pdf $(BUILD_DIR)/fr.pdf

.PHONY : more
more : $(EN_SVGS) $(FR_SVGS)

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)


# Remind -> Postscript

$(BUILD_DIR)/en.ps : $(SOURCE_FILES) Makefile
	@remind.en -p$(MONTHS) -b1 -gdaad $(TOP_CALENDAR) $(DATE) \
    | rem2ps.en -l -c3 -i -e -m Letter -sthed 8 -b 6 -t 1 -olrtb 1 \
    | sed \
      -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
      -e 's/\xc3\x83\|\xc2\x89/\d201/g' \
      -e 's/\d195\d162/\d226/g' \
      -e 's/\d195\d168/\d232/g' \
      -e 's/\d195\d169/\d233/g' \
      -e 's/\d195\d170/\d234/g' \
      -e 's/\d195\d171/\d235/g' \
      -e 's/\d195\d180/\d244/g' \
    | gs -sstdout=/dev/null -dQUIET -dNOPAUSE -dSAFER -sDEVICE=ps2write \
      -sPAPERSIZE=$(MEDIA) -dFIXEDMEDIA -sOutputFile=$@ \
      -c '<</BeginPage{0.9 0.9 scale 29.75 42.1 translate}>> setpagedevice'

$(BUILD_DIR)/fr.ps : $(SOURCE_FILES) Makefile
	@remind.fr -p$(MONTHS) -b1 -gdaad $(TOP_CALENDAR) $(DATE) \
    | rem2ps.fr -l -c3 -i -e -m Letter -sthed 8 -b 6 -t 1 -olrtb 1 \
    | sed \
      -e 's/\xc3\c82\|\xc2\xae/\d174/g' \
      -e 's/\xc3\x83\|\xc2\x89/\d201/g' \
      -e 's/\d195\d162/\d226/g' \
      -e 's/\d195\d168/\d232/g' \
      -e 's/\d195\d169/\d233/g' \
      -e 's/\d195\d170/\d234/g' \
      -e 's/\d195\d171/\d235/g' \
      -e 's/\d195\d180/\d244/g' \
    | gs -sstdout=/dev/null -dQUIET -dNOPAUSE -dSAFER -sDEVICE=ps2write \
      -sPAPERSIZE=$(MEDIA) -dFIXEDMEDIA -sOutputFile=$@ \
      -c '<</BeginPage{0.9 0.9 scale 29.75 42.1 translate}>> setpagedevice'

# http://ma.juii.net/blog/scale-page-content-of-pdf-files
# http://stackoverflow.com/questions/3351967/prevent-ghostscript-from-writing-errors-to-standard-output

# man iso_8859-1
#   ® -> Â® -> \303\202\302\256 -> \xc3\x82\|\xc2\xae -> \d174
#   É -> Ã -> \303\203\302\211 -> \xc3\x83\|\xc2\x89 -> \d201
#   â -> Ã¢ -> \d195\d162 -> \d226
#   è -> Ã¨ -> \d195\d168 -> \d232
#   é -> Ã© -> \d195\d169 -> \d233
#   ê -> Ãª -> \d195\d170 -> \d234
#   ë -> Ã« -> \d195\d171 -> \d235
#   ô -> Ã´ -> \d195\d180 -> \d244


# Postscript -> Portable Document Format

$(BUILD_DIR)/%.pdf : $(BUILD_DIR)/%.ps
	@ps2pdf14 -sPAPERSIZE=$(MEDIA) $< - \
    | pdftk - output $@ uncompress
#   | pdftk - background watermark_rac.pdf output $@ uncompress


# Multi-page -> Single-page Portable Document Format

$(EN_PDFS) : $(BUILD_DIR)/en.pdf
	@pdftk $^ burst output $(BUILD_DIR)/en%02d.pdf uncompress

$(FR_PDFS) : $(BUILD_DIR)/fr.pdf
	@pdftk $^ burst output $(BUILD_DIR)/fr%02d.pdf uncompress


# Portable Document Format -> Scalable Vector Graphic

$(BUILD_DIR)/%.svg : $(BUILD_DIR)/%.pdf
	@inkscape --export-plain-svg $@ $^


#$(BUILD_DIR)/%.pdf : svg/%.svg
#	@inkscape --export-text-to-path --export-pdf=$@ $<

#%.pdf : %.odt
#	@libreoffice --headless --convert-to pdf $^
