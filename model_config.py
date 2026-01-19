#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model Configuration for AskForHelp Chatbot

This file contains the AI model configuration settings.
Admin can change the model here without modifying the main application code.
"""

# Ollama Model Configuration
# Default model: qwen3:4b (2.5 GB, good balance of performance and quality)
# Available models (examples):
# - qwen3:4b (default, recommended)
# - llama2:7b (Meta's Llama 2, 7B parameters)
# - llama2:13b (Meta's Llama 2, 13B parameters)
# - mistral:7b (Mistral AI, 7B parameters)
# - codellama:7b (Code-focused model)
# - phi:2.7b (Microsoft's Phi, smaller but efficient)

# To use a different model:
# 1. Make sure the model is downloaded: ollama pull <model_name>
# 2. Update the MODEL_NAME variable below
# 3. Restart the application

# MODEL_NAME = "qwen3:4b"
MODEL_NAME = "phi:2.7b"

# Ollama API Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"

# Model Options (advanced settings)
MODEL_OPTIONS = {
    "temperature": 0.7,  # Controls randomness (0.0-1.0, lower = more focused)
    "top_p": 0.9,        # Nucleus sampling (0.0-1.0, lower = more diverse)
    "max_tokens": 1024,  # Maximum tokens in response
}

# Notes:
# - The model name is NOT displayed to end users
# - Only administrators should modify this file
# - Changes take effect after restarting the application
# - For LAN deployment, update OLLAMA_URL to point to your server
