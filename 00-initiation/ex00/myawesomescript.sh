#!/bin/sh

if [ -z "$1" ]; then
    echo "Usage: $0 <bit.ly URL>"
    exit 1
fi

curl -sI "$1" | grep -i "^location:" | cut -d '' -f2