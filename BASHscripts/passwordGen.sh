#!/bin/bash

#simple password Generator

echo "Password Generator - base64"
echo "Enter Length of password desired:"
read Paswdlen

# openssl rand to generate random bytes, which are then encoded to base64 

Password=$(openssl rand -base64 48 | tr -d '\n/+'| cut -c1-$Paswdlen) 

echo "$Password"