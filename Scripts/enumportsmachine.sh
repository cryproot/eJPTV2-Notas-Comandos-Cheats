#!/bin/bash

ip="XX.XX.XX.XX"  # Dirección IP a escanear

echo "Escaneo de puertos abiertos en curso..."
echo " "

# Realiza un bucle a través de todos los puertos y verifica si están abiertos
for port in $(seq 0 65535); do
    (echo >/dev/tcp/$ip/$port) >/dev/null 2>&1 && echo "Puerto $port abierto"
done
