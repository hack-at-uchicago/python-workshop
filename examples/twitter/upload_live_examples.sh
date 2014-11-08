#!/bin/bash

FILE=$1

while true;
do
    date;
    ipython nbconvert --to html --quiet --output workshop "$1"
    scp -p workshop.html linux.cs.uchicago.edu:~/html/pyworkshop/
    sleep 10
done
