#!/bin/bash
echo "Starting Translator..."
echo "----------------------------------------"

if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 was not found. Download and configure Python."
    exit
fi

python3 __main__.py
