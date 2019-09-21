#!/bin/bash
FILE=$1
NAME=$2
N=$(( ${#FILE}-6 ))
STEM=${FILE:0:N}

jupyter nbconvert --to latex $FILE
python addauthor.py "${STEM}.tex" "$NAME"
pdflatex "${STEM}.tex"
rm "${STEM}.aux"
rm "${STEM}.out"
rm "${STEM}.log"
rm "${STEM}.tex"
