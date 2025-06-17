#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <hostname_or_ip>"
  exit 1
fi

host="$1"

# Ping the host 4 times
ping -c 4 "$host" 