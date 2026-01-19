# AskForHelp - PC Hardware & Software Support Chatbot

A local AI-powered chatbot specifically designed for PC hardware and software troubleshooting. It helps users with computer-related issues and automatically generates IT support tickets for further assistance.

## Features

- **Local AI Processing**: Uses Ollama with Qwen3-4B model for privacy and offline operation
- **Automatic System Information Collection**: Captures username, hostname, IP address, OS, and PC serial number
- **Screenshot Capture**: Automatically capture and save screenshots for visual documentation
- **IT Ticket Generation**: Creates formatted support tickets with all relevant information
- **Chat History**: Maintains conversation history for reference
- **Export Reports**: Save tickets and reports as text files
- **Email Integration**: Send tickets directly to IT support (douglas.ho@hkuspace.hku.hk) with automatic screenshot attachment
- **LAN API Access**: Ollama can be configured for network access
- **Admin Model Selection**: LLM model can be configured by admin in backend file (not visible to users)

## Prerequisites

### 1. Python 3.12 or higher
```bash
python --version
```

### 2. Ollama installed and running
```bash
ollama --version
```

### 3. Required Python packages
```bash
pip install requests
```

## Setup Instructions

### Step 1: Start Ollama (if not already running)
```bash
ollama serve
```

### Step 2: Verify Ollama is running
```bash
curl http://localhost:11434/api/tags
```

You should see the qwen3:4b model listed.

### Step 3: Run the Chatbot
```bash
python askforhelp_chatbot.py
```

## Configuration

### Ollama API URL
By default, the chatbot connects to `http://localhost:11434/api/generate`

### For LAN Access
To allow other computers on the network to access Ollama:

1. **Set Ollama to listen on all interfaces:**
   ```bash
   set OLLAMA_HOST=0.0.0.0
   ollama serve
   ```

2. **Update the chatbot configuration** (edit `askforhelp_chatbot.py`):
   ```python
   # Change from localhost to your server IP
   self.ollama_url = "http://YOUR_SERVER_IP:11434/api/generate"
   ```

3. **Configure firewall** to allow port 11434:
   ```bash
   # Windows PowerShell (Run as Administrator)
   New-NetFirewallRule -DisplayName "Ollama API" -Direction Inbound -LocalPort 11434 -Protocol TCP -Action Allow
   ```

### Model Configuration (Admin Only)
To change the AI model, edit `model_config.py`:

```python
MODEL_NAME = "qwen3:4b"  # Change to any Ollama model you have installed
```

Available models:
- qwen3:4b (default, recommended)
- llama2:7b, llama2:13b
- mistral:7b
- codellama:7b
- phi:2.7b

**Note**: The model name is hidden from end users. Only administrators can change it.

### Email Configuration
To enable email sending for IT support tickets, configure the email settings in `askforhelp_chatbot.py`:

```python
# Email Configuration
self.email_config = {
    "smtp_server": "smtp.gmail.com",  # Change to your SMTP server
    "smtp_port": 587,
    "sender_email": "your.email@university.edu",  # Your email address
    "sender_password": "your_app_password",  # Your email password or app password
    "recipient_email": "douglas.ho@hkuspace.hku.hk",  # IT support email
    "use_tls": True
}
```

**For Gmail Users:**
1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password:
   - Go to Google Account > Security
   - Under "Signing in to Google" > "App passwords"
   - Generate a new app password for "Mail"
   - Use this 16-character password in the configuration

**For Other Email Providers:**
- Update `smtp_server` and `smtp_port` to match your provider
- Check your provider's documentation for SMTP settings
- Some providers may require different authentication methods

**Security Note:** Never commit your email password to version control. Consider using environment variables or a configuration file for sensitive credentials.

## Usage

### Starting the Application
1. Run `python askforhelp_chatbot.py`
2. The application will display a welcome message with system information
3. Type your question in the input field and press Enter or click "Send"

### Features

#### Chat Interface
- **Type questions**: Type your problem in the red text input box
- **Submit**: Click "Submit" button or press Enter to send
- **AI Assistance**: Get troubleshooting help and guidance
- **User Messages**: Displayed in red text for easy identification
- **System Info**: Automatically includes your username and hostname in responses

#### Generate IT Ticket
- Click "Generate IT Ticket" to create a formatted support report
- The ticket includes:
  - Unique Ticket ID (hostname + timestamp)
  - System information (username, hostname, IP, OS)
  - Problem description from chat
  - Chat history summary
- Options: Copy to clipboard or save as text file

#### Export Report
- Click "Export Report" to save the entire conversation and system info
- Useful for documentation and follow-up

#### Clear Chat
- Click "Clear Chat" to start a new conversation

## Example Workflow

1. **User**: "My computer is running very slow and the fan is making noise"
2. **AskForHelp**: Provides troubleshooting steps and asks clarifying questions
3. **User**: "It happens when I open multiple Chrome tabs"
4. **AskForHelp**: Suggests solutions and explains the issue
5. **User clicks "Generate IT Ticket"**
6. **Result**: A formatted ticket is created with:
   ```
   IT SUPPORT TICKET - AskForHelp System
   ======================================================================
   
   TICKET INFORMATION
   ------------------
   Ticket ID:      DESKTOP-ULB3G1P-20260120-011200
   Created:        2026-01-20 01:12:00
   Status:         NEW
   Priority:       To be determined
   
   SYSTEM INFORMATION
   ------------------
   Username:       doug
   Hostname:       DESKTOP-ULB3G1P
   IP Address:     192.168.1.100
   Operating System: Windows 11
   Python Version: 3.12.10
   
   PROBLEM DESCRIPTION
   ------------------
   User's initial description:
     - My computer is running very slow and the fan is making noise
     - It happens when I open multiple Chrome tabs
   
   CHAT HISTORY SUMMARY
   ------------------
   [01:12:00] You:
     My computer is running very slow and the fan is making noise
   
   [01:12:15] AskForHelp:
     I understand your computer is running slow with fan noise...
   ```

## System Information Collected

The application automatically collects and includes in reports:
- **Username**: Current logged-in user (e.g., "doug")
- **Hostname**: Computer name (e.g., "DESKTOP-ULB3G1P")
- **IP Address**: Local network IP address
- **Operating System**: Windows/Mac/Linux version
- **Python Version**: For troubleshooting compatibility
- **Timestamp**: When the ticket was created

## Security & Privacy

- **Local Processing**: All AI processing happens on your local machine
- **No Cloud Uploads**: No data is sent to external servers
- **LAN Access**: Can be configured for trusted network access only
- **File Export**: Tickets are saved locally as text files
- **Admin Rights Protection**: The bot will NEVER ask users to perform actions requiring admin rights or system modifications
- **Safe Troubleshooting**: Only provides non-invasive troubleshooting steps that don't require administrator privileges

## Troubleshooting

### Ollama Connection Error
```bash
# Check if Ollama is running
netstat -ano | findstr :11434

# Start Ollama if not running
ollama serve
```

### Model Not Found
```bash
# List available models
ollama list

# Pull qwen3:4b if missing
ollama pull qwen3:4b
```

### Port Already in Use
```bash
# Find process using port 11434
netstat -ano | findstr :11434

# Kill the process (replace PID with actual number)
taskkill /PID <PID> /F
```

## File Structure

```
askforhelp_chatbot.py    # Main application
README.md               # This file
IT_Ticket_*.txt         # Generated tickets (after use)
AskForHelp_Report_*.txt # Exported reports (after use)
```

## Requirements

- Python 3.12+
- Ollama 0.14.2+
- qwen3:4b model (2.5 GB)
- requests library

## License

This is a demonstration project for educational purposes.

## Support

For issues with:
- **Ollama**: Visit https://ollama.ai
- **Qwen3 Model**: Check Ollama model library
- **This Application**: Review the troubleshooting section above

## Future Enhancements

- [ ] Add screenshot capture for error documentation
- [ ] Support for multiple AI models
- [ ] Email integration for ticket submission
- [ ] Database storage for ticket history
- [ ] Web interface for remote access
- [ ] Hardware diagnostic tools integration
- [ ] Software inventory collection
- [ ] Multi-language support
