#!/bin/bash

FILE1=$1

pdftotext $FILE1.pdf

strings -e S $FILE1.txt > $FILE1.2.txt

vim $FILE1.2.txt '+%s/\n/ /g' +wq
vim $FILE1.2.txt '+%s/\. /.\r/g' +wq

split $FILE1.txt -a 4 --numeric-suffix=1000  -C 4400 -d --additional-suffix=.txt
