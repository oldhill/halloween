#!/bin/bash -ex

# Messing around w bash
# http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html

# basic variable assignment and accessing value with $
MYVAR="hi!"
echo $MYVAR
echo MYVAR  # echos the variable name :/

echo "Not gonna list contents of current directory..."
echo ls
echo "Gonna list the contents of current directory..."
echo $(ls)

# basic conditionals
M1="something"
M2="something"
if [ "$M1" = "$M2" ]; then
  echo "'yeah they're equal"
else
  echo "nah"
fi

# function with arguments
function echo_stuff {
  echo $1
  echo $2
}
echo_stuff 'hi' 'there'

# finally, shell out to openssl lol
my_hash=$(echo 0 | openssl dgst -sha1)
echo "SHA1 hash of 0: $my_hash"
echo "Length: ${#my_hash}"

my_hash=$(echo 0 | openssl dgst -sha256)
echo "SHA1 hash of 0: $my_hash"
echo "Length: ${#my_hash}"

