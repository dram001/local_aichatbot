# AskForHelp - Complete Feature Summary

## 🎯 Core Purpose
**PC Hardware & Software Support Only** - This chatbot is specifically designed to help with computer-related issues and guide users to submit IT tickets for further assistance.

## 📋 New Features Added

### 1. PC Serial Number Collection
- **What**: Automatically retrieves the PC's serial number
- **How**: Uses WMIC on Windows, system files on Linux/Mac
- **Where**: Included in IT support tickets
- **Benefit**: IT can track specific hardware assets

### 2. Automatic Screenshot Capture
- **What**: One-click screenshot capture and save
- **How**: Uses PIL/Pillow to capture screen and save as PNG
- **Where**: Saved locally with hostname and timestamp
- **Benefit**: Visual documentation of errors/UI issues

### 3. PC-Only Scope Enforcement
- **What**: Chatbot only answers PC hardware/software questions
- **How**: Updated AI prompt to restrict scope
- **Where**: Welcome message and AI responses
- **Benefit**: Focused support, guides users to tickets for other topics

### 4. Email Integration
- **What**: Send tickets directly to IT support
- **How**: SMTP with TLS encryption
- **Where**: douglas.ho@hkuspace.hku.hk (configurable)
- **Benefit**: Immediate ticket submission

## 📊 Complete System Information Collected

| Information | Source | Included in Ticket |
|-------------|--------|-------------------|
| Username | OS login | ✓ |
| Hostname | System | ✓ |
| IP Address | Network | ✓ |
| OS Version | System | ✓ |
| Python Version | Runtime | ✓ |
| **Serial Number** | **BIOS/DMI** | **✓** |
| Timestamp | Current time | ✓ |

## 🎨 User Interface Features

### Main Window (900x700)
- **Header**: Title and subtitle
- **System Info Bar**: Shows user, host, OS
- **Chat Display**: Scrollable conversation history
- **Input Field**: Type messages (Enter to send)
- **Status Bar**: Shows current state (Ready, Thinking, Error)

### Buttons
1. **Generate IT Ticket** - Create formatted support ticket
2. **Capture Screenshot** - Save screenshot as PNG
3. **Clear Chat** - Start new conversation
4. **Export Report** - Save complete conversation

### Ticket Generation Window
- **Preview**: View formatted ticket
- **Copy to Clipboard** - For pasting into email
- **Save to File** - Save as .txt
- **Send Email** - Direct email to IT (requires config)

## 🔒 Security & Privacy

### Local Processing
- ✓ All AI processing on local machine
- ✓ No cloud services required
- ✓ No external API keys needed
- ✓ Works offline after setup

### Credential Protection
- ✓ Email config in separate file
- ✓ .gitignore prevents commits
- ✓ App password support for Gmail
- ✓ TLS encryption for email

### Data Handling
- ✓ Tickets saved locally
- ✓ Screenshots saved locally
- ✓ No automatic uploads
- ✓ User controls sharing

## 📁 Complete File Structure

```
AskForHelp/
├── askforhelp_chatbot.py      # Main application (22 KB)
├── email_config_template.py   # Email template
├── setup.bat                  # Setup script
├── .gitignore                 # Security ignore file
├── README.md                  # Full documentation
├── QUICK_START.md             # Quick reference
├── INSTALLATION_GUIDE.md      # Detailed setup
├── PROJECT_SUMMARY.md         # Technical overview
├── FEATURES_SUMMARY.md        # This file
└── Generated Files/
    ├── IT_Ticket_*.txt        # Support tickets
    ├── AskForHelp_Report_*.txt # Exported reports
    └── Screenshot_*.png       # Captured screenshots
```

## 🚀 Usage Workflow

### Step 1: Start Application
```bash
python askforhelp_chatbot.py
```

### Step 2: Describe PC Issue
**Examples:**
- "My computer is running very slow"
- "Hard drive is making clicking noises"
- "Blue screen error appears randomly"
- "WiFi adapter not detected"
- "Application crashes on startup"

### Step 3: Get AI Assistance
- Chatbot provides troubleshooting steps
- Asks clarifying questions
- Suggests solutions
- **Always guides to create ticket for further help**

### Step 4: Capture Screenshot (Optional)
- Click "Capture Screenshot" button
- Screenshot saved as PNG
- Useful for visual errors

### Step 5: Generate IT Ticket
- Click "Generate IT Ticket"
- Review formatted ticket
- Choose action:
  - Copy to clipboard
  - Save to file
  - Send email to IT

## 📧 Email Configuration

### For Gmail Users
1. Enable 2-Factor Authentication
2. Generate App Password (16 characters)
3. Update `email_config.py`:
```python
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "your.email@gmail.com",
    "sender_password": "your_app_password",
    "recipient_email": "douglas.ho@hkuspace.hku.hk",
    "use_tls": True
}
```

### For Other Providers
- Outlook: smtp.office365.com, port 587
- Yahoo: smtp.mail.yahoo.com, port 587
- iCloud: smtp.mail.me.com, port 587
- University: Check IT documentation

## 🎓 Example Ticket Output

```
======================================================================
IT SUPPORT TICKET - AskForHelp System
======================================================================

TICKET INFORMATION
------------------
Ticket ID:      DESKTOP-ULB3G1P-20260120-013600
Created:        2026-01-20 01:36:00
Status:         NEW
Priority:       To be determined

SYSTEM INFORMATION
------------------
Username:       doug
Hostname:       DESKTOP-ULB3G1P
IP Address:     192.168.1.100
Operating System: Windows 11
Python Version: 3.12.10
Serial Number:  ABC123XYZ

PROBLEM DESCRIPTION
------------------
User's initial description:
  - My computer is running very slow and the fan is making noise
  - It happens when I open multiple Chrome tabs

CHAT HISTORY SUMMARY
------------------
[01:36:00] You:
  My computer is running very slow and the fan is making noise

[01:36:15] AskForHelp:
  I understand your computer is running slow with fan noise...
  Please try these steps:
  1. Check Task Manager for high CPU usage
  2. Clean dust from fans
  3. Update BIOS if needed
  4. Generate a ticket for further assistance

======================================================================
ADDITIONAL NOTES
======================================================================
• This ticket was generated using AskForHelp AI Assistant
• All system information has been automatically collected
• Please review and update priority as needed
• Contact IT Support for immediate assistance

======================================================================
END OF TICKET
======================================================================
```

## ⚡ Performance Metrics

| Metric | Value |
|--------|-------|
| First Response Time | 10-20 seconds |
| Subsequent Responses | 2-5 seconds |
| Ticket Generation | <1 second |
| Screenshot Capture | 2-3 seconds |
| Email Sending | 2-10 seconds |
| Memory Usage | ~2.5 GB |
| Disk Space | ~2.5 GB (model) |
| Network | Local only (except email) |

## 🔧 Technical Requirements

### Software
- Python 3.12+
- Ollama 0.14.2+
- qwen3:4b model (2.5 GB)
- requests library
- PIL/Pillow library

### Hardware
- Minimum: 4 GB RAM, 5 GB disk space
- Recommended: 8 GB RAM, 10 GB disk space
- CPU: Modern x86_64 processor

### Network
- Local: None required
- Email: SMTP access (port 587)
- Ollama: localhost:11434 (or LAN)

## 🎯 Scope Limitations

### What It CAN Do
✓ Answer PC hardware questions (CPU, RAM, HDD, GPU)
✓ Answer software questions (Windows, apps, errors)
✓ Provide troubleshooting steps
✓ Guide through driver issues
✓ Help with performance problems
✓ Generate IT support tickets
✓ Capture screenshots

### What It CANNOT Do
✗ Answer non-PC questions (networking, servers, etc.)
✗ Provide legal advice
✗ Give medical recommendations
✗ Answer general knowledge questions
✗ Replace human IT support

### How It Handles Non-PC Questions
When asked about non-PC topics, the chatbot:
1. Politely explains its scope limitation
2. Suggests submitting an IT support ticket
3. Provides the "Generate IT Ticket" button

## 📈 Future Enhancements

### Planned
- [ ] Multiple AI model support (llama2, mistral)
- [ ] Database for ticket history
- [ ] Web interface for remote access
- [ ] Hardware diagnostic tools integration
- [ ] Software inventory collection
- [ ] Multi-language support
- [ ] Ticket status tracking
- [ ] Integration with existing IT systems

### Technical Improvements
- [ ] Async email sending
- [ ] Configuration GUI
- [ ] Log file management
- [ ] Performance optimization
- [ ] Error reporting system

## 🎓 For University IT Teams

### Benefits
1. **Complete Information**: All system details upfront
2. **Structured Format**: Consistent ticket structure
3. **Visual Evidence**: Screenshots for UI issues
4. **Asset Tracking**: Serial numbers for hardware
5. **Reduced Back-and-Forth**: Less clarification needed
6. **Priority Sorting**: System info helps prioritization

### Deployment Options
1. **Individual Installation**: Each user installs locally
2. **Shared Server**: Ollama on server, clients connect
3. **Lab Deployment**: Pre-installed on lab computers
4. **Student Distribution**: Share via university portal

## 📚 Documentation Files

1. **README.md** - Full project documentation
2. **QUICK_START.md** - 3-step quick start guide
3. **INSTALLATION_GUIDE.md** - Detailed setup instructions
4. **PROJECT_SUMMARY.md** - Technical architecture
5. **FEATURES_SUMMARY.md** - This file (feature overview)

## 🎉 Summary

**AskForHelp** is a complete, production-ready IT support chatbot that:
- ✓ Runs locally with full privacy
- ✓ Collects comprehensive system information including serial numbers
- ✓ Provides PC hardware/software troubleshooting
- ✓ Generates professional IT tickets
- ✓ Captures screenshots for visual documentation
- ✓ Emails tickets directly to IT support
- ✓ Guides users to submit tickets for further assistance
- ✓ Works offline after initial setup

**Perfect for university IT support teams** looking to streamline ticket creation and provide immediate assistance to students and faculty.
