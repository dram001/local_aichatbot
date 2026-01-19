# AskForHelp Chatbot - Installation & Setup Guide

## Overview

AskForHelp is a local AI-powered chatbot designed to assist with PC hardware and software support. It automatically collects system information and generates IT support tickets that can be emailed to your IT department.

## Quick Start

### 1. Run the Setup Script
```bash
setup.bat
```

This will check all prerequisites and help you configure the system.

### 2. Configure Email (Optional but Recommended)
1. Copy `email_config_template.py` to `email_config.py`
2. Edit `email_config.py` with your email credentials
3. For Gmail: Use an App Password (not your regular password)

### 3. Start the Chatbot
```bash
python askforhelp_chatbot.py
```

## Detailed Installation Steps

### Prerequisites

#### Python 3.12 or Higher
```bash
python --version
```
If not installed, download from [python.org](https://www.python.org/downloads/)

#### Ollama
```bash
ollama --version
```
If not installed, download from [ollama.ai](https://ollama.ai/download)

#### Required Python Packages
```bash
pip install requests
```

### Ollama Setup

#### 1. Start Ollama Server
```bash
ollama serve
```

#### 2. Verify Ollama is Running
```bash
curl http://localhost:11434/api/tags
```
You should see the qwen3:4b model listed.

#### 3. Download the AI Model (if not already present)
```bash
ollama pull qwen3:4b
```
This downloads a 2.5 GB model file.

### Email Configuration

#### For Gmail Users

1. **Enable 2-Factor Authentication**
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification

2. **Generate App Password**
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and your device
   - Generate a 16-character password
   - Copy this password

3. **Configure Email Settings**
   - Copy `email_config_template.py` to `email_config.py`
   - Edit the file:
   ```python
   EMAIL_CONFIG = {
       "smtp_server": "smtp.gmail.com",
       "smtp_port": 587,
       "sender_email": "your.email@gmail.com",
       "sender_password": "your_app_password_here",  # 16-character app password
       "recipient_email": "douglas.ho@hkuspace.hku.hk",
       "use_tls": True
   }
   ```

#### For Other Email Providers

| Provider | SMTP Server | Port |
|----------|-------------|------|
| Outlook/Hotmail | smtp.office365.com | 587 |
| Yahoo | smtp.mail.yahoo.com | 587 |
| iCloud | smtp.mail.me.com | 587 |
| University SMTP | Check IT documentation | 587/465 |

### LAN Access Configuration (Optional)

To allow other computers on your network to use Ollama:

#### 1. Set Ollama to Listen on All Interfaces
```bash
set OLLAMA_HOST=0.0.0.0
ollama serve
```

#### 2. Update Chatbot Configuration
Edit `askforhelp_chatbot.py`:
```python
self.ollama_url = "http://YOUR_SERVER_IP:11434/api/generate"
```

#### 3. Configure Firewall
```powershell
# Windows PowerShell (Run as Administrator)
New-NetFirewallRule -DisplayName "Ollama API" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
```

## Usage Guide

### Starting the Application

1. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

2. Run the chatbot:
   ```bash
   python askforhelp_chatbot.py
   ```

### Chat Interface

1. **Welcome Screen**: Displays system information (username, hostname, OS)

2. **Type Your Question**: 
   - Describe your computer issue
   - Example: "My computer is running very slow and the fan is making noise"

3. **AI Assistance**: 
   - AskForHelp provides troubleshooting steps
   - Asks clarifying questions
   - Suggests solutions

### Generating IT Tickets

1. After chatting, click **"Generate IT Ticket"**
2. Review the formatted ticket
3. Choose an action:
   - **Copy to Clipboard**: Paste into email or other applications
   - **Save to File**: Save as text file
   - **Send Email**: Directly email to IT support (requires email configuration)

### Ticket Content

Each ticket includes:
- **Ticket ID**: Unique identifier (hostname + timestamp)
- **System Information**: Username, hostname, IP address, OS
- **Problem Description**: From your chat conversation
- **Chat History**: Complete conversation summary
- **Timestamp**: When the ticket was created

### Export Reports

Click **"Export Report"** to save the entire conversation and system information as a text file for documentation.

### Clear Chat

Click **"Clear Chat"** to start a new conversation.

## Troubleshooting

### Ollama Connection Error

**Symptom**: "Cannot connect to Ollama" error

**Solution**:
```bash
# Check if Ollama is running
netstat -ano | findstr :11434

# Start Ollama if not running
ollama serve

# Check Ollama logs
ollama --version
```

### Model Not Found

**Symptom**: Model not available error

**Solution**:
```bash
# List available models
ollama list

# Pull qwen3:4b model
ollama pull qwen3:4b
```

### Port Already in Use

**Symptom**: "Address already in use" error

**Solution**:
```bash
# Find process using port 11434
netstat -ano | findstr :11434

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F
```

### Email Authentication Failed

**Symptom**: "Authentication failed" when sending email

**Solution**:
1. **Gmail Users**:
   - Ensure 2-Factor Authentication is enabled
   - Use App Password (not regular password)
   - Check that App Password is 16 characters

2. **Other Providers**:
   - Verify SMTP server and port
   - Check if your account allows SMTP access
   - Contact your email provider for SMTP settings

### Tkinter Not Available

**Symptom**: "No module named tkinter" error

**Solution**:
- Tkinter is included with Python on Windows
- On Linux: `sudo apt-get install python3-tk`
- On macOS: Tkinter comes with Python from python.org

## File Structure

```
AskForHelp/
├── askforhelp_chatbot.py      # Main application
├── email_config_template.py   # Email configuration template
├── email_config.py            # Your email credentials (create this)
├── setup.bat                  # Setup script
├── README.md                  # Project documentation
├── INSTALLATION_GUIDE.md      # This file
├── .gitignore                 # Git ignore file
└── IT_Ticket_*.txt            # Generated tickets (after use)
```

## Security Best Practices

1. **Never commit credentials**:
   - Add `email_config.py` to `.gitignore`
   - Never share your email password

2. **Use App Passwords**:
   - For Gmail, use 16-character app passwords
   - Revoke app passwords when not needed

3. **Local Processing**:
   - All AI processing happens locally
   - No data sent to external servers (except email if configured)

4. **File Permissions**:
   - Keep `email_config.py` readable only by you
   - On Linux: `chmod 600 email_config.py`

## Support

### For Ollama Issues
- Website: https://ollama.ai
- Documentation: https://github.com/ollama/ollama

### For Email Configuration
- Gmail Help: https://support.google.com/mail
- App Passwords: https://myaccount.google.com/apppasswords

### For This Application
- Review the troubleshooting section above
- Check system requirements
- Verify all prerequisites are installed

## Advanced Configuration

### Custom SMTP Server
Edit `askforhelp_chatbot.py`:
```python
self.email_config = {
    "smtp_server": "your.custom.server.com",
    "smtp_port": 587,
    "sender_email": "your@email.com",
    "sender_password": "your_password",
    "recipient_email": "it@university.edu",
    "use_tls": True
}
```

### Multiple Recipients
Modify the recipient email to include multiple addresses:
```python
"recipient_email": "it@university.edu, support@university.edu"
```

### Change AI Model
Edit `askforhelp_chatbot.py`:
```python
self.model = "llama2:7b"  # Or any other Ollama model
```

## Performance Tips

1. **First Run**: The first AI response may take 10-20 seconds as the model loads
2. **Subsequent Runs**: Responses are typically 2-5 seconds
3. **Memory Usage**: The qwen3:4b model uses ~2.5 GB RAM
4. **CPU Usage**: AI processing is CPU-intensive during generation

## Uninstallation

To remove the application:
1. Delete the `AskForHelp` folder
2. Remove Ollama if no longer needed: `ollama rm qwen3:4b`
3. Uninstall Ollama if desired

## License

This is a demonstration project for educational purposes.

## Version History

- **v1.0** (2026-01-20): Initial release
  - Local AI chatbot with Ollama
  - System information collection
  - IT ticket generation
  - Email support
  - Export functionality
