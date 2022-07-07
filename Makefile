
LINKY  := python ./scripts/linky.py
MD_SRC := $(shell find . -name '*.md')

.DEFAULT_GOAL: help

.PHONY: help
help :
	@echo "Makefile for TerraFirmaCraft/Documentation"
	@echo "  help      : Show this information"
	@echo "  deploy    : Build and host the documentation"
	@echo "  test      : Run validations and sanitize"
	@echo "  dos2unix  : Run dos2unix on all .md files"
	@echo "  setup-wsl : Setup script for WSL"


.PHONY: deploy
deploy: test
	bundle exec jekyll serve

.PHONY: test
test:
	$(LINKY) validate
	$(LINKY) sanitize

.PHONY: dos2unix
dos2unix:
	@dos2unix $(MD_SRC)

.PHONY: setup-wsl
setup-wsl:
	sudo apt install make gcc g++
	sudo apt-get install glib1g-dev liblzma-dev patch
	sudo apt install ruby-full
	sudo gem install jekyll bundler
	sudo bundle install
