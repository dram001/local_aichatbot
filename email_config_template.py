#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Configuration Template for AskForHelp Chatbot

Copy this file to email_config.py and fill in your credentials.
"""

# Email Configuration
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",  # Gmail SMTP server
    "smtp_port": 587,                  # TLS port
    "sender_email": "your.email@university.edu",  # Your email address
    "sender_password": "your_app_password",       # Your email password or app password
    "recipient_email": "douglas.ho@hkuspace.hku.hk",  # IT support email
    "use_tls": True
}

# For Gmail Users:
# 1. Enable 2-Factor Authentication on your Google account
# 2. Generate an App Password:
#    - Go to Google Account > Security
#    - Under "Signing in to Google" > "App passwords"
#    - Generate a new app password for "Mail"
#    - Use this 16-character password in the configuration

# For Other Email Providers:
# - Update smtp_server and smtp_port to match your provider
# - Common SMTP servers:
#   - Outlook/Hotmail: smtp.office365.com, port 587
#   - Yahoo: smtp.mail.yahoo.com, port 587
#   - iCloud: smtp.mail.me.com, port 587
#   - University SMTP: Check your university's IT documentation

# Security Notes:
# - Never commit email_config.py to version control
# - Add email_config.py to .gitignore
# - Consider using environment variables for production use
# - Use app passwords instead of regular passwords when possible
