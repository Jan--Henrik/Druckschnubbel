#!/bin/bash

cd ../app/uploads/

TAG="$1"
TAG="${TAG/ /_}"
TAG="${TAG/\"/}"
[ -z "$TAG" ] && exit 1

URL=$(wget -q -O- "https://yande.re/post.json?limit=1&tags=${TAG}+order%3Arandom+rating%3Asafe+score%3A20.." | grep -o -E '"file_url":"http[^"]+"' | cut -d'"' -f4)
wget -O $(date +%N) "$URL"
exit $?
