#!/bin/sh
# sass --sourcemap=none /Bitpoll/_static/scss/main.scss /Bitpoll/_static/COMPILED/scss/main.css
# python3 -m scss  /Bitpoll/_static/scss/main.scss -o  /Bitpoll/_static/COMPILED/scss/main.css

python3 -m scss $2 -o $3