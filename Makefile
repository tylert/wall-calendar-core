# Tools required:  make, bash, remind, sed, ghostscript, psutils, pdftk,
#   inkscape

SHELL := /bin/bash

SOURCE ?= source
BUILD ?= build
TOP_CALENDAR ?= $(SOURCE)/top.rem
CALENDARS ?= $(TOP_CALENDAR) $(wildcard $(SOURCE)/*.rem)

GEN_LANG ?= fr
MEDIA ?= legal

#YEAR ?= $(shell expr 1 + $(shell date +%Y))
YEAR ?= $(shell date +%Y)
DATE ?= $(YEAR)-01-01
MONTHS ?= 12

SVGS = $(PDFS:.pdf=.svg)

GENERATED_FILES = \
  $(wildcard $(BUILD)/*.ps) \
  $(wildcard $(BUILD)/*.pdf) \
  $(wildcard $(BUILD)/*.svg) \
  doc_data.txt


.PHONY : all
all : calendar

.PHONY : calendar
calendar : $(BUILD)/$(MEDIA)_$(YEAR)_$(GEN_LANG).pdf

.PHONY : svgs
svgs : $(SVGS)

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)


# Remind -> Postscript

$(BUILD)/$(MEDIA)_$(GEN_LANG).ps : $(CALENDARS) Makefile
	@remind.$(GEN_LANG) -p$(MONTHS) -b1 -gdaad $(TOP_CALENDAR) $(DATE) \
    | rem2ps.$(GEN_LANG) -l -c3 -i -e -m Letter -sthed 8 -b 6 -t 1 -olrtb 1 \
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

$(BUILD)/%.pdf : $(BUILD)/%.ps
	@ps2pdf14 -sPAPERSIZE=$(MEDIA) $< - | pdftk - output $@ uncompress

$(BUILD)/$(MEDIA)_$(YEAR)_$(GEN_LANG).pdf : $(BUILD)/$(MEDIA)_$(GEN_LANG).pdf $(BUILD)/$(MEDIA)_border.pdf
	@pdftk $< background $(BUILD)/$(MEDIA)_border.pdf output $@ uncompress


# Single-page -> 2-up Portable Document Format

$(BUILD)/junior_$(YEAR)_$(GEN_LANG).pdf : $(BUILD)/letter_$(YEAR)_$(GEN_LANG).pdf
	@pdf2ps $< - | psnup -2 -c -f | ps2pdf - $@


# Multi-page -> Single-page Portable Document Format

# XXX If n < 100 months, otherwise use different padding
RANGE = $(shell seq --format "%02g" $(MONTHS))
PDFS = $(addprefix $(BUILD)/, $(addsuffix .pdf, $(addprefix $(GEN_LANG), \
  $(RANGE))))

# XXX If n < 100 months, otherwise use different padding
$(PDFS) : $(BUILD)/$(MEDIA)_$(GEN_LANG).pdf
	@pdftk $^ burst output $(BUILD)/$(GEN_LANG)%02d.pdf uncompress


# Portable Document Format -> Scalable Vector Graphic

$(BUILD)/%.svg : $(BUILD)/%.pdf
	@inkscape --export-plain-svg $@ $^


$(BUILD)/%.pdf : $(SOURCE)/%.svg
	@inkscape --export-text-to-path --export-pdf=$@ $<
