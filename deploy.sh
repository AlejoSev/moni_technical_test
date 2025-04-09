#!/bin/bash

echo "📦 Buildeando contenedores..."
docker-compose down --remove-orphans #--volumes

echo "🚀 Levantando contenedores..."
docker-compose up -d --build

echo "✅ Deploy terminado."