#!/bin/bash
echo "Starting Termux AI assistant setup..."

pkg update -y
pkg upgrade -y
pkg install -y python git termux-api

pip install --no-cache-dir keyboard

termux-setup-storage

echo "✅ Termux setup complete!"
echo "Run: python main.py"
