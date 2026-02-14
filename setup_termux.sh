#!/bin/bash
echo "Starting Termux AI assistant setup..."

# Update packages
pkg update -y
pkg upgrade -y

# Install Python, git, termux-api
pkg install -y python git termux-api

# Install Python packages safely (do not upgrade pip!)
pip install --no-cache-dir keyboard

# Grant storage permission
termux-setup-storage

echo "✅ Termux setup complete!"
echo "Run the assistant with: python main.py"
