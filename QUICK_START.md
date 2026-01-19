# AskForHelp - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Run Setup
Double-click or run:
```bash
setup.bat
```

This will check if everything is installed.

### Step 2: Configure Email (Optional but Recommended)
1. Copy `email_config_template.py` to `email_config.py`
2. Open `email_config.py` in a text editor
3. Fill in your email credentials:
   - `sender_email`: your.email@university.edu
   - `sender_password`: your_app_password
   - `recipient_email`: douglas.ho@hkuspace.hku.hk (already set)

**For Gmail Users:**
- Enable 2-Factor Authentication
- Generate App Password at: https://myaccount.google.com/apppasswords
- Use the 16-character app password (not your regular password)

### Step 3: Start Chatting
```bash
python askforhelp_chatbot.py
```

## 💡 Quick Tips

### What to Ask
- "My computer is running slow"
- "Excel keeps crashing"
- "WiFi won't connect"
- "Blue screen error"
- "Printer not working"

### After Chatting
1. Click **"Generate IT Ticket"**
2. Choose an action:
   - **Copy to Clipboard** - Paste into email
   - **Save to File** - Save as text file
   - **Send Email** - Directly email to IT (requires email config)

## 🔧 Troubleshooting

### "Cannot connect to Ollama"
```bash
ollama serve
```

### "Model not found"
```bash
ollama pull qwen3:4b
```

### "Email authentication failed"
- Use App Password (not regular password)
- Check email credentials
- Verify SMTP settings

## 📁 Files Created

- `askforhelp_chatbot.py` - Main application
- `email_config_template.py` - Email template
- `email_config.py` - Your email settings (create this)
- `setup.bat` - Setup script
- `README.md` - Full documentation
- `INSTALLATION_GUIDE.md` - Detailed setup
- `PROJECT_SUMMARY.md` - Project overview
- `QUICK_START.md` - This file

## 🎯 Key Features

✓ **Local AI** - Privacy-focused, no cloud  
✓ **Auto System Info** - Username, hostname, OS, IP  
✓ **IT Tickets** - Professional formatted reports  
✓ **Email Support** - Send directly to IT  
✓ **Export** - Save or copy tickets  

## 📞 Support

Need help? Check:
- `README.md` - Full documentation
- `INSTALLATION_GUIDE.md` - Detailed instructions
- `PROJECT_SUMMARY.md` - Project details

## ⚡ Performance

- First response: 10-20 seconds (model loads)
- Subsequent: 2-5 seconds
- Memory: ~2.5 GB
- Works offline after setup

## 🎓 For University IT

This tool helps students:
1. Get AI troubleshooting help
2. Generate complete tickets automatically
3. Include all system information
4. Email directly to IT support

**IT receives:** Complete ticket with username, hostname, IP, OS, and problem description.

---

**Ready to go!** Run `python askforhelp_chatbot.py` and start chatting!
