#!/bin/bash

echo "Bajando contenedores existentes..."
docker-compose down --remove-orphans

echo "Bajando front-ends existentes..."
pkill -f 'npm run dev'

echo "Buildeando y levantando nuevos contenedores..."
docker-compose up -d --build

echo "Levantando front-end del cliente..."
cd frontend-client
npm install
npm run dev > /dev/null 2>&1 &
cd ..

echo "Levantando front-end de admin..."
cd frontend-admin
npm install
npm run dev > /dev/null 2>&1 &
cd ..

echo "Deploy terminado."