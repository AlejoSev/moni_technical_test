#!/bin/bash

echo "📦 Buildeando contenedores..."
docker-compose down --volumes --remove-orphans

echo "🚀 Levantando contenedores..."
docker-compose up -d --build

echo "✅ Deploy terminado."