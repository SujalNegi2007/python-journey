#!/bin/bash

Project_Name={1:-"Project File"}

mkdir -p "$Project_Name/src"
mkdir -p "$Project_Name/docs"
mkdir -p "$Project_Name/tests"

cd "$Project_Name" || exit

git init

echo "# Requirements" > requirement.txt
echo "pyyaml" >> requirement.txt

echo "# $Project_Name" > README.md
echo "## Overview" >> README.md
echo "This is created using bash" >> README.md
echo "" >> README.md
echo "## Installation" >> README.md
echo "Run this to install respective commands" >> README.md
echo "pip install -r requirement.txt"
echo "" >> README.md
echo " Today's Date: $(date)" >> README.md

echo "Project File Created Successfully!"
