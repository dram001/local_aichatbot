#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AskForHelp - PC Hardware and Software Help Support Chatbot
A local AI-powered chatbot to assist with IT support ticket creation
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import json
import platform
import os
import socket
import datetime
import threading
import subprocess
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import subprocess
import base64
from PIL import ImageGrab
import io
import model_config
import model_behavior_config


class AskForHelpChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("AskForHelp - IT Support Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # System Information
        self.system_info = self.get_system_info()
        
        # Ollama API Configuration (from model_config.py)
        self.ollama_url = model_config.OLLAMA_URL
        self.model = model_config.MODEL_NAME
        self.available_models = []
        self.get_available_models()
        
        # Model behavior configuration
        self.model_behavior = model_behavior_config
        
        # Email Configuration
        self.email_config = {
            "smtp_server": "smtp.gmail.com",  # Change to your SMTP server
            "smtp_port": 587,
            "sender_email": "",  # Your email address
            "sender_password": "",  # Your email password or app password
            "recipient_email": "douglas.ho@hkuspace.hku.hk",  # IT support email
            "use_tls": True
        }
        
        # Chat history
        self.chat_history = []
        
        # Create UI
        self.create_ui()
        
        # Start with welcome message
        self.show_welcome_message()
    
    def get_available_models(self):
        """Get list of available Ollama models (for admin use)"""
        try:
            response = requests.get(
                "http://localhost:11434/api/tags",
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                models = result.get('models', [])
                self.available_models = [model['name'] for model in models]
                
                # Ensure current model is in the list
                if self.model not in self.available_models and self.available_models:
                    self.model = self.available_models[0]
            else:
                # Fallback to default model if API fails
                self.available_models = [self.model]
                
        except Exception as e:
            print(f"Error fetching models: {e}")
            # Fallback to default model
            self.available_models = [self.model]
    
    def get_serial_number(self):
        """Get PC serial number (Windows only)"""
        try:
            if platform.system() == "Windows":
                # Get serial number using WMIC
                result = subprocess.run(
                    ["wmic", "bios", "get", "serialnumber"],
                    capture_output=True,
                    text=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                serial = result.stdout.strip().split('\n')[-1].strip()
                return serial if serial and serial != "" else "Unknown"
            else:
                # For Linux/Mac, try different methods
                try:
                    # Linux
                    result = subprocess.run(
                        ["cat", "/sys/class/dmi/id/product_uuid"],
                        capture_output=True,
                        text=True
                    )
                    if result.returncode == 0:
                        return result.stdout.strip()
                except:
                    pass
                return "Unknown"
        except:
            return "Unknown"
    
    def capture_screenshot(self):
        """Capture screenshot and return as base64 encoded image"""
        try:
            # Capture screenshot
            screenshot = ImageGrab.grab()
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            screenshot.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            # Encode to base64
            img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')
            
            return img_base64
        except Exception as e:
            print(f"Screenshot capture failed: {e}")
            return None
    
    def get_system_info(self):
        """Collect system information for IT reports"""
        try:
            username = os.getlogin()
        except:
            username = "Unknown"
        
        try:
            hostname = platform.node()
        except:
            hostname = "Unknown"
        
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except:
            ip_address = "Unknown"
        
        try:
            os_info = platform.system() + " " + platform.release()
        except:
            os_info = "Unknown"
        
        try:
            python_version = platform.python_version()
        except:
            python_version = "Unknown"
        
        try:
            serial_number = self.get_serial_number()
        except:
            serial_number = "Unknown"
        
        return {
            "username": username,
            "hostname": hostname,
            "ip_address": ip_address,
            "os_info": os_info,
            "python_version": python_version,
            "serial_number": serial_number,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def create_ui(self):
        """Create the main UI components"""
        # Header Frame
        header_frame = tk.Frame(self.root, bg='#2c3e50', padx=10, pady=10)
        header_frame.pack(fill='x')
        
        title_label = tk.Label(
            header_frame, 
            text="AskForHelp - IT Support Assistant", 
            font=('Arial', 18, 'bold'),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame,
            text="Local AI Chatbot for PC Hardware & Software Support",
            font=('Arial', 10),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        subtitle_label.pack()
        
        # System Info Display
        info_frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=5)
        info_frame.pack(fill='x')
        
        info_text = f"User: {self.system_info['username']} | Host: {self.system_info['hostname']} | OS: {self.system_info['os_info']}"
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#555555'
        )
        info_label.pack()
        
        # Chat Display Area
        chat_frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=10)
        chat_frame.pack(fill='both', expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            bg='white',
            fg='#333333',
            state='disabled',
            padx=10,
            pady=10
        )
        self.chat_display.pack(fill='both', expand=True)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=10)
        input_frame.pack(fill='x')
        
        # User input box with red border
        input_box = tk.Frame(input_frame, bg='white', relief='solid', bd=1)
        input_box.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        self.user_input = tk.Entry(
            input_box,
            font=('Arial', 11),
            width=70,
            bg='white',
            fg='green',  # Green text for user input
            relief='flat'
        )
        self.user_input.insert(0, "Type your issues here...")
        self.user_input.pack(fill='x', expand=True, padx=5, pady=5)
        self.user_input.bind('<Return>', self.send_message)
        
        submit_button = tk.Button(
            input_frame,
            text="Submit",
            command=self.send_message,
            font=('Arial', 10, 'bold'),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            width=10
        )
        submit_button.pack(side='right')
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=5)
        button_frame.pack(fill='x')
        
        ticket_button = tk.Button(
            button_frame,
            text="Generate IT Ticket",
            command=self.generate_ticket,
            font=('Arial', 10),
            bg='#27ae60',
            fg='white',
            activebackground='#229954',
            width=20
        )
        ticket_button.pack(side='left', padx=(0, 10))
        
        screenshot_button = tk.Button(
            button_frame,
            text="Capture Screenshot",
            command=self.capture_and_save_screenshot,
            font=('Arial', 10),
            bg='#f39c12',
            fg='white',
            activebackground='#e67e22',
            width=18
        )
        screenshot_button.pack(side='left', padx=(0, 10))
        
        clear_button = tk.Button(
            button_frame,
            text="Clear Chat",
            command=self.clear_chat,
            font=('Arial', 10),
            bg='#e74c3c',
            fg='white',
            activebackground='#c0392b',
            width=15
        )
        clear_button.pack(side='left', padx=(0, 10))
        
        export_button = tk.Button(
            button_frame,
            text="Export Report",
            command=self.export_report,
            font=('Arial', 10),
            bg='#9b59b6',
            fg='white',
            activebackground='#8e44ad',
            width=15
        )
        export_button.pack(side='left')
        
        # Status Bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=('Arial', 9),
            bg='#e0e0e0',
            fg='#333333',
            anchor='w',
            padx=10
        )
        status_bar.pack(fill='x')
    
    def show_welcome_message(self):
        """Display welcome message with instructions"""
        welcome_msg = """
🤖 Welcome to AskForHelp!

I'm your local AI assistant for PC hardware and software support.

📋 What I can help you with:
• PC hardware issues (hard drive, RAM, CPU, etc.)
• Software problems (Windows, applications, errors)
• Driver issues and updates
• System performance troubleshooting
• Generate IT support tickets

⚠️ IMPORTANT RULES:
1. I can only answer questions about PC hardware and software
2. For ANY task requiring admin rights or system modification, I will guide you to create an IT support ticket
3. See AI_GUIDANCE.md for complete guidance on how I answer questions

💡 System Information Collected:
• Username: {username}
• Hostname: {hostname}
• OS: {os_info}
• IP: {ip_address}

Type your PC-related question below or click "Generate IT Ticket" to create a support report.
        """.format(**self.system_info)
        
        self.add_message("System", welcome_msg, is_system=True)
    
    def add_message(self, sender, message, is_system=False):
        """Add a message to the chat display"""
        self.chat_display.config(state='normal')
        
        if is_system:
            tag = "system"
            self.chat_display.tag_configure(tag, foreground='#2c3e50', font=('Arial', 10, 'bold'))
        elif sender == "You":
            tag = "user"
            self.chat_display.tag_configure(tag, foreground='red', font=('Arial', 11, 'bold'))
        else:
            tag = "bot"
            self.chat_display.tag_configure(tag, foreground='#27ae60', font=('Arial', 11, 'bold'))
        
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"\n[{timestamp}] {sender}:\n", tag)
        self.chat_display.insert(tk.END, f"{message}\n", ('normal',))
        self.chat_display.tag_configure('normal', foreground='#333333', font=('Arial', 11))
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
        
        # Store in history
        self.chat_history.append({
            "timestamp": timestamp,
            "sender": sender,
            "message": message,
            "is_system": is_system
        })
    
    def send_message(self, event=None):
        """Send user message to the AI"""
        user_text = self.user_input.get().strip()
        if not user_text:
            return
        
        self.user_input.delete(0, tk.END)
        self.add_message("You", user_text)
        
        # Disable input during processing
        self.user_input.config(state='disabled')
        self.status_var.set("Thinking...")
        
        # Run AI query in background thread
        thread = threading.Thread(target=self.query_ai, args=(user_text,))
        thread.daemon = True
        thread.start()
    
    def query_ai(self, user_message):
        """Query the Ollama API"""
        try:
            # Prepare the prompt with context using model behavior configuration
            prompt = self.model_behavior.SYSTEM_PROMPT_TEMPLATE.format(
                username=self.system_info['username'],
                hostname=self.system_info['hostname'],
                os_info=self.system_info['os_info'],
                ip_address=self.system_info['ip_address'],
                timestamp=self.system_info['timestamp'],
                user_message=user_message
            )
            
            # Prepare the request using model behavior configuration
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": self.model_behavior.get_model_parameters()
            }
            
            # Send request to Ollama
            response = requests.post(
                self.ollama_url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result.get('response', 'No response received.')
                
                # Update UI in main thread
                self.root.after(0, lambda: self.add_message("AskForHelp", ai_response))
                self.root.after(0, lambda: self.status_var.set("Ready"))
            else:
                error_msg = f"API Error: {response.status_code} - {response.text}"
                self.root.after(0, lambda: self.add_message("System", error_msg, is_system=True))
                self.root.after(0, lambda: self.status_var.set("Error"))
                
        except requests.exceptions.ConnectionError:
            error_msg = "❌ Error: Cannot connect to Ollama. Please ensure Ollama is running on localhost:11434."
            self.root.after(0, lambda: self.add_message("System", error_msg, is_system=True))
            self.root.after(0, lambda: self.status_var.set("Connection Error"))
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            self.root.after(0, lambda: self.add_message("System", error_msg, is_system=True))
            self.root.after(0, lambda: self.status_var.set("Error"))
        finally:
            # Re-enable input
            self.root.after(0, lambda: self.user_input.config(state='normal'))
            self.root.after(0, lambda: self.user_input.focus())
    
    def send_ticket_email(self, ticket_content):
        """Send ticket via email to IT support with automatic screenshot attachment"""
        if not self.email_config["sender_email"] or not self.email_config["sender_password"]:
            messagebox.showerror("Email Error", 
                "Email not configured!\n\n"
                "Please configure your email settings:\n"
                "1. Edit the askforhelp_chatbot.py file\n"
                "2. Update 'sender_email' and 'sender_password' in email_config\n"
                "3. For Gmail, use an App Password (not your regular password)")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email_config["sender_email"]
            msg['To'] = self.email_config["recipient_email"]
            
            ticket_id = f"{self.system_info['hostname']}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
            msg['Subject'] = f"IT Support Ticket - {ticket_id}"
            
            # Email body
            body = f"""
IT Support Ticket Request

A new ticket has been generated using AskForHelp AI Assistant.

Ticket ID: {ticket_id}
User: {self.system_info['username']}
Hostname: {self.system_info['hostname']}
IP Address: {self.system_info['ip_address']}
OS: {self.system_info['os_info']}
Timestamp: {self.system_info['timestamp']}

Please see the attached ticket content below:

{'='*70}
{ticket_content}
{'='*70}

This email was sent automatically by AskForHelp Chatbot.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Check for and attach the most recent screenshot
            screenshot_attached = False
            screenshot_pattern = f"Screenshot_{self.system_info['hostname']}*.png"
            import glob
            screenshot_files = glob.glob(screenshot_pattern)
            
            if screenshot_files:
                # Get the most recent screenshot
                latest_screenshot = max(screenshot_files, key=os.path.getctime)
                
                with open(latest_screenshot, 'rb') as f:
                    screenshot_data = f.read()
                
                # Attach screenshot
                screenshot_attachment = MIMEBase('application', 'octet-stream')
                screenshot_attachment.set_payload(screenshot_data)
                encoders.encode_base64(screenshot_attachment)
                
                filename = os.path.basename(latest_screenshot)
                screenshot_attachment.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{filename}"'
                )
                msg.attach(screenshot_attachment)
                screenshot_attached = True
            
            # Connect to SMTP server
            server = smtplib.SMTP(
                self.email_config["smtp_server"], 
                self.email_config["smtp_port"]
            )
            
            if self.email_config["use_tls"]:
                server.starttls()
            
            # Login
            server.login(
                self.email_config["sender_email"], 
                self.email_config["sender_password"]
            )
            
            # Send email
            server.send_message(msg)
            server.quit()
            
            return True
            
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Email Error", 
                "Authentication failed!\n\n"
                "Please check:\n"
                "• Your email address and password are correct\n"
                "• For Gmail, you need to use an App Password\n"
                "• Enable 'Less secure app access' if using other providers")
            return False
        except Exception as e:
            messagebox.showerror("Email Error", 
                f"Failed to send email:\n{str(e)}\n\n"
                "Please check your email configuration and network connection.")
            return False
    
    def generate_ticket(self):
        """Generate an IT support ticket from the chat history"""
        if not self.chat_history:
            messagebox.showinfo("Info", "No chat history to generate a ticket from. Please chat first.")
            return
        
        # Create ticket dialog
        ticket_window = tk.Toplevel(self.root)
        ticket_window.title("Generate IT Support Ticket")
        ticket_window.geometry("700x650")
        
        # Ticket content
        ticket_content = self.create_ticket_content()
        
        # Text area for ticket
        text_frame = tk.Frame(ticket_window, padx=10, pady=10)
        text_frame.pack(fill='both', expand=True)
        
        ticket_text = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=('Courier New', 10),
            padx=10,
            pady=10
        )
        ticket_text.pack(fill='both', expand=True)
        ticket_text.insert('1.0', ticket_content)
        ticket_text.config(state='disabled')
        
        # Button frame
        button_frame = tk.Frame(ticket_window, padx=10, pady=10)
        button_frame.pack(fill='x')
        
        def copy_ticket():
            ticket_window.clipboard_clear()
            ticket_window.clipboard_append(ticket_content)
            messagebox.showinfo("Copied", "Ticket copied to clipboard!")
        
        def save_ticket():
            filename = f"IT_Ticket_{self.system_info['hostname']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(ticket_content)
            messagebox.showinfo("Saved", f"Ticket saved as {filename}")
        
        def send_email():
            if messagebox.askyesno("Send Email", 
                f"Send ticket to:\n{self.email_config['recipient_email']}?\n\n"
                "Make sure email is configured in the script first!"):
                self.status_var.set("Sending email...")
                ticket_window.update()
                
                # Send email in background thread
                def send_in_thread():
                    success = self.send_ticket_email(ticket_content)
                    self.root.after(0, lambda: self.status_var.set("Ready" if success else "Email Failed"))
                
                thread = threading.Thread(target=send_in_thread)
                thread.daemon = True
                thread.start()
        
        copy_btn = tk.Button(
            button_frame,
            text="Copy to Clipboard",
            command=copy_ticket,
            bg='#3498db',
            fg='white',
            font=('Arial', 10)
        )
        copy_btn.pack(side='left', padx=5)
        
        save_btn = tk.Button(
            button_frame,
            text="Save to File",
            command=save_ticket,
            bg='#27ae60',
            fg='white',
            font=('Arial', 10)
        )
        save_btn.pack(side='left', padx=5)
        
        email_btn = tk.Button(
            button_frame,
            text="Send Email",
            command=send_email,
            bg='#e67e22',
            fg='white',
            font=('Arial', 10)
        )
        email_btn.pack(side='left', padx=5)
        
        close_btn = tk.Button(
            button_frame,
            text="Close",
            command=ticket_window.destroy,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10)
        )
        close_btn.pack(side='right', padx=5)
    
    def create_ticket_content(self):
        """Create formatted IT support ticket content"""
        ticket = f"""
{'='*70}
IT SUPPORT TICKET - AskForHelp System
{'='*70}

TICKET INFORMATION
------------------
Ticket ID:      {self.system_info['hostname']}-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}
Created:        {self.system_info['timestamp']}
Status:         NEW
Priority:       To be determined

SYSTEM INFORMATION
------------------
Username:       {self.system_info['username']}
Hostname:       {self.system_info['hostname']}
IP Address:     {self.system_info['ip_address']}
Operating System: {self.system_info['os_info']}
Python Version: {self.system_info['python_version']}
Serial Number:  {self.system_info['serial_number']}

PROBLEM DESCRIPTION
------------------
"""
        
        # Extract problem description from chat
        user_messages = [msg for msg in self.chat_history if msg['sender'] == 'You']
        if user_messages:
            ticket += "User's initial description:\n"
            for msg in user_messages[:3]:  # First 3 user messages
                ticket += f"  - {msg['message']}\n"
        else:
            ticket += "  [No specific problem description provided]\n"
        
        ticket += f"""
CHAT HISTORY SUMMARY
------------------
"""
        
        # Add relevant chat exchanges
        for msg in self.chat_history:
            if not msg['is_system']:
                ticket += f"[{msg['timestamp']}] {msg['sender']}:\n"
                ticket += f"  {msg['message']}\n\n"
        
        ticket += f"""
{'='*70}
ADDITIONAL NOTES
{'='*70}
• This ticket was generated using AskForHelp AI Assistant
• All system information has been automatically collected
• Please review and update priority as needed
• Contact IT Support for immediate assistance

{'='*70}
END OF TICKET
{'='*70}
"""
        
        return ticket
    
    def clear_chat(self):
        """Clear the chat history"""
        if messagebox.askyesno("Confirm", "Clear all chat history?"):
            self.chat_display.config(state='normal')
            self.chat_display.delete('1.0', tk.END)
            self.chat_display.config(state='disabled')
            self.chat_history = []
            self.show_welcome_message()
    
    def capture_and_save_screenshot(self):
        """Capture screenshot and save to file"""
        self.status_var.set("Capturing screenshot...")
        self.root.update()
        
        # Capture in background thread
        def capture_in_thread():
            try:
                screenshot_base64 = self.capture_screenshot()
                
                if screenshot_base64:
                    # Decode and save
                    img_bytes = base64.b64decode(screenshot_base64)
                    filename = f"Screenshot_{self.system_info['hostname']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    
                    with open(filename, 'wb') as f:
                        f.write(img_bytes)
                    
                    self.root.after(0, lambda: messagebox.showinfo("Screenshot Captured", 
                        f"Screenshot saved as:\n{filename}"))
                    self.root.after(0, lambda: self.status_var.set("Ready"))
                else:
                    self.root.after(0, lambda: messagebox.showerror("Screenshot Error", 
                        "Failed to capture screenshot. Please check permissions."))
                    self.root.after(0, lambda: self.status_var.set("Error"))
                    
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Screenshot Error", 
                    f"Failed to capture screenshot:\n{str(e)}"))
                self.root.after(0, lambda: self.status_var.set("Error"))
        
        thread = threading.Thread(target=capture_in_thread)
        thread.daemon = True
        thread.start()
    
    def export_report(self):
        """Export the entire chat history and system info as a report"""
        if not self.chat_history:
            messagebox.showinfo("Info", "No chat history to export.")
            return
        
        report_content = self.create_ticket_content()
        
        filename = f"AskForHelp_Report_{self.system_info['hostname']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            messagebox.showinfo("Export Successful", f"Report saved as:\n{filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export report:\n{str(e)}")


def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = AskForHelpChatbot(root)
    root.mainloop()


if __name__ == "__main__":
    main()
