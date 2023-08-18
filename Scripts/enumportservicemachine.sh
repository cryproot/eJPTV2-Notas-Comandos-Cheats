#!/bin/bash

ip="xx.xx.xx.xx"  # Dirección IP a escanear

echo "Escaneo de puertos abiertos en curso..."
echo " "

# Realiza un bucle a través de todos los puertos y verifica si están abiertos
for port in $(seq 0 65535); do
    (echo >/dev/tcp/$ip/$port) >/dev/null 2>&1 && {
        service=$(echo "$(sudo lsof -i :$port)" | awk 'NR==2{print $1}')
        [ -n "$service" ] && echo "Puerto $port abierto - Servicio: $service"
    }
done
