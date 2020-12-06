run:
	bin/aoc

test:
	tests/test_aoc.py --verbose

init:
	pip install -r requirements.txt

.PHONY: run
