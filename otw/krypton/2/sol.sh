#!/usr/bin/env bash

# I wish I had a pizza, because CEASERISEASY

# make working dir
tmp_dir=/tmp/$(cat /dev/urandom| tr -dc 'a-zA-Z0-9' | fold -w 128| head -n 1 | sha256sum | awk '{ print $1 }' )
mkdir $tmp_dir
cd $tmp_dir

cp /krypton/krypton2/krypton3 .
ln -s /krypton/krypton2/keyfile.dat keyfile.dat
password=""
for i in {1..13}; do
    for x in {A..Z}; do
        echo $x > ciphertext_tmp
        /krypton/krypton2/encrypt ciphertext_tmp
        if [[ $(cat ciphertext) = $(cat krypton3 | cut -c$i) ]]; then
            password=$password$x
        fi
    done
done

echo $password

# clean up
cd $HOME
rm -r $tmp_dir
