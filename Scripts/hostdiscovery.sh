#!/bin/bash
for i in $(seq 1 254); do
        timeout 1 bash -c "ping -c 1 10.185.10.$i" &>/dev/null && echo "[+] Host 10.185.10.$i - active" &
done; wait
