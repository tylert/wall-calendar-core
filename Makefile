# Tools required:  make, remind, sed, ghostscript, pdftk, inkscape

SHELL := /bin/bash

SOURCE ?= source
BUILD ?= build
TOP_CALENDAR ?= $(SOURCE)/top.rem
CALENDARS ?= $(TOP_CALENDAR) $(wildcard $(SOURCE)/*.rem)

MEDIA ?= legal

YEAR ?= $(shell expr 1 + $(shell date +%Y))
DATE ?= $(YEAR)-01-01

MONTHS ?= 12
RANGE = $(shell seq --format "%02g" $(MONTHS))
EN_PDFS = $(addprefix $(BUILD)/,$(addsuffix .pdf,$(addprefix en,$(RANGE))))
FR_PDFS = $(addprefix $(BUILD)/,$(addsuffix .pdf,$(addprefix fr,$(RANGE))))
EN_SVGS = $(EN_PDFS:.pdf=.svg)
FR_SVGS = $(FR_PDFS:.pdf=.svg)

GENERATED_FILES = \
  $(wildcard $(BUILD)/*.ps) \
  $(wildcard $(BUILD)/*.pdf) \
  $(wildcard $(BUILD)/*.svg) \
  doc_data.txt


.PHONY : all
all : $(BUILD)/$(YEAR)_calendar.pdf $(BUILD)/$(YEAR)_calendrier.pdf

.PHONY : svgs
svgs : $(EN_SVGS) $(FR_SVGS)

.PHONY : clean
clean :
	@rm -f $(GENERATED_FILES)


# Remind -> Postscript

$(BUILD)/en.ps : $(CALENDARS) Makefile
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

$(BUILD)/fr.ps : $(CALENDARS) Makefile
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

$(BUILD)/%.pdf : $(BUILD)/%.ps
	@ps2pdf14 -sPAPERSIZE=$(MEDIA) $< - \
    | pdftk - output $@ uncompress

$(BUILD)/$(YEAR)_calendar.pdf : $(BUILD)/en.pdf $(BUILD)/watermark_rac.pdf
	@pdftk $< background $(BUILD)/watermark_rac.pdf output $@ uncompress

$(BUILD)/$(YEAR)_calendrier.pdf : $(BUILD)/fr.pdf $(BUILD)/watermark_rac.pdf
	@pdftk $< background $(BUILD)/watermark_rac.pdf output $@ uncompress


# Multi-page -> Single-page Portable Document Format

$(EN_PDFS) : $(BUILD)/en.pdf
	@pdftk $^ burst output $(BUILD)/en%02d.pdf uncompress

$(FR_PDFS) : $(BUILD)/fr.pdf
	@pdftk $^ burst output $(BUILD)/fr%02d.pdf uncompress


# Portable Document Format -> Scalable Vector Graphic

$(BUILD)/%.svg : $(BUILD)/%.pdf
	@inkscape --export-plain-svg $@ $^


$(BUILD)/%.pdf : $(SOURCE)/%.svg
	@inkscape --export-text-to-path --export-pdf=$@ $<

#%.pdf : %.odt
#	@libreoffice --headless --convert-to pdf $^
