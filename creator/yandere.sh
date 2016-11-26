#!/bin/bash

cd /home/janhenrik/Druckschnubbel/app/uploads/

TAG="$1"
[ -z "$TAG" ] && exit 1

POST=$(wget -q -O- "https://yande.re/post?tags=${TAG}+order%3Arandom+rating%3Asafe+score%3A20.." | grep -E -o 'href="/post/show/[0-9]+' | head -n1 | cut -d '/' -f4)
URL=$(wget -q -O- "https://yande.re/post/show/${POST}" | grep 'Post.register_resp(' | grep '"id":'$POST | grep -o -E '"file_url":"http[^"]+"' | cut -d'"' -f4)
wget -O $(date +%N) "$URL"
exit $?
