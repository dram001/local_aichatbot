#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Model Behavior Configuration
Configuration file for adjusting LLM model behavior to provide better information to users.
This file contains parameters and settings that can be tuned to optimize AI responses.
"""

# ============================================================================
# RESPONSE GENERATION PARAMETERS
# ============================================================================

# Temperature: Controls randomness in responses
# - Lower (0.1-0.3): More focused, deterministic, predictable responses
# - Medium (0.4-0.7): Balanced between creativity and accuracy
# - Higher (0.8-1.0): More creative, diverse, but potentially less predictable
TEMPERATURE = 0.7

# Top-p (Nucleus Sampling): Controls response diversity
# - Lower (0.7-0.8): More focused on high-probability tokens
# - Higher (0.9-0.95): More diverse responses
TOP_P = 0.9

# Maximum tokens: Limit response length
# - Short: 512 tokens (brief responses)
# - Medium: 1024 tokens (standard responses)
# - Long: 2048 tokens (detailed explanations)
MAX_TOKENS = 1024

# Frequency penalty: Reduce repetition
# - Positive values penalize frequent tokens
# - Range: -2.0 to 2.0
FREQUENCY_PENALTY = 0.5

# Presence penalty: Encourage new topics
# - Positive values encourage new tokens
# - Range: -2.0 to 2.0
PRESENCE_PENALTY = 0.3

# ============================================================================
# RESPONSE STYLE PARAMETERS
# ============================================================================

# Response length preference
# - "concise": Brief, to-the-point responses
# - "standard": Balanced detail level
# - "detailed": Comprehensive explanations
RESPONSE_LENGTH = "standard"

# Tone settings
TONE_SETTINGS = {
    "professional": True,      # Use professional language
    "friendly": True,          # Be approachable and helpful
    "empathetic": True,        # Show understanding of user issues
    "authoritative": True,     # Demonstrate expertise
    "cautious": True,          # Be careful with recommendations
}

# Formatting preferences
FORMATTING_PREFERENCES = {
    "use_bullets": True,       # Use bullet points for lists
    "use_numbering": True,     # Use numbered lists for steps
    "use_code_blocks": False,  # Use code formatting (not needed for this use case)
    "use_emojis": True,        # Use emojis for visual appeal
    "use_bold": True,          # Use bold text for emphasis
    "use_headers": True,       # Use section headers
}

# ============================================================================
# SYSTEM PROMPT TEMPLATES
# ============================================================================

# Base system prompt template
SYSTEM_PROMPT_TEMPLATE = """You are AskForHelp, a PC hardware and software support assistant for ITSU IT support.

System Information:
- Username: {username}
- Hostname: {hostname}
- OS: {os_info}
- IP Address: {ip_address}
- Timestamp: {timestamp}

User Question: {user_message}

IMPORTANT RULES:
1. You ONLY answer questions about PC hardware and software issues
2. NEVER ask users to perform actions requiring admin rights
3. NEVER ask users to modify Windows system files or settings
4. NEVER ask users to update software/drivers themselves
5. For ANY task requiring admin rights or system modification, ALWAYS guide them to create an IT support ticket
6. For non-PC questions, explain your scope limitation and guide them to submit an IT ticket
7. Refer to AI_GUIDANCE.md for complete guidance on response protocols and limitations

For PC hardware/software questions:
- Provide helpful troubleshooting steps that don't require admin rights
- Ask clarifying questions
- Suggest safe, non-invasive solutions
- For complex issues or anything requiring admin rights, guide them to create a ticket for further assistance

For issues requiring admin rights or system modification:
- Politely explain that this requires IT administrator assistance
- Guide them to create an IT support ticket immediately
- Do NOT provide step-by-step instructions for admin tasks

For non-PC questions:
- Explain your scope limitation
- Guide them to submit an IT ticket for help

Response:"""

# Alternative prompt templates for different scenarios
ALTERNATIVE_PROMPTS = {
    # For quick, concise responses
    "concise": """You are AskForHelp, a PC hardware and software support assistant.

User: {user_message}

Rules:
- Only PC hardware/software questions
- No admin rights instructions
- Guide to IT ticket for complex issues

Response:""",
    
    # For detailed, educational responses
    "educational": """You are AskForHelp, a PC hardware and software support assistant for ITSU IT support.

Your goal is to educate users about their PC issues while maintaining safety.

System Info:
- User: {username}
- Host: {hostname}
- OS: {os_info}

User Question: {user_message}

Guidelines:
1. Explain the issue in simple terms
2. Provide safe troubleshooting steps
3. Explain WHY certain actions require IT support
4. Guide to IT ticket when needed
5. Be educational but concise

Response:""",
    
    # For urgent issues
    "urgent": """You are AskForHelp, a PC hardware and software support assistant.

URGENT ISSUE DETECTED: {user_message}

Immediate Actions:
1. Acknowledge the urgency
2. Explain why this needs immediate IT attention
3. Guide user to create IT ticket IMMEDIATELY
4. Do NOT provide troubleshooting steps
5. Emphasize the importance of professional assistance

Response:""",
}

# ============================================================================
# BEHAVIOR GUIDELINES
# ============================================================================

# Response quality settings
RESPONSE_QUALITY = {
    "clarity": "high",          # Priority: Clear, understandable responses
    "accuracy": "high",         # Priority: Factually correct information
    "safety": "high",           # Priority: Never suggest unsafe actions
    "helpfulness": "high",      # Priority: Actually help the user
    "completeness": "medium",   # Balance: Provide enough detail without overwhelming
}

# Escalation triggers (when to immediately guide to IT ticket)
ESCALATION_TRIGGERS = [
    "admin", "administrator", "admin rights", "administrator rights",
    "system files", "registry", "permissions", "security settings",
    "install software", "update driver", "driver update", "software update",
    "modify system", "change settings", "access denied", "permission denied",
    "group policy", "windows update", "bios", "firmware", "hardware modification",
    "physical repair", "data recovery", "backup restore", "network configuration",
    "firewall", "antivirus", "security policy", "system policy",
]

# Safe troubleshooting keywords (can provide guidance)
SAFE_TROUBLESHOOTING = [
    "restart", "reboot", "close program", "clear cache", "check connection",
    "verify settings", "basic troubleshooting", "simple steps", "non-admin",
    "user level", "application error", "software crash", "performance issue",
    "slow", "freezing", "not responding", "error message", "warning",
]

# ============================================================================
# SAFETY SETTINGS
# ============================================================================

# Safety first: Always prioritize user safety and system security
SAFETY_FIRST = True

# Never provide these types of instructions
FORBIDDEN_INSTRUCTIONS = [
    "registry edit",
    "system file modification",
    "permission changes",
    "security bypass",
    "admin privilege elevation",
    "driver installation",
    "software installation",
    "system configuration changes",
    "network configuration changes",
    "hardware modifications",
]

# Always escalate for these topics
ALWAYS_ESCALATE = [
    "data loss",
    "security breach",
    "system crash",
    "hardware failure",
    "network outage",
    "virus infection",
    "malware",
    "ransomware",
    "blue screen",
    "boot failure",
]

# ============================================================================
# RESPONSE TEMPLATES
# ============================================================================

# Template for admin rights required
TEMPLATE_ADMIN_REQUIRED = """I understand you're experiencing {issue}. This requires administrative privileges to resolve. Please click the "Generate IT Ticket" button to create a support request, and our IT team will assist you with this issue."""

# Template for outside scope
TEMPLATE_OUTSIDE_SCOPE = """I'm specialized in PC hardware and software support. For questions about {topic}, please click "Generate IT Ticket" to submit your request to our IT support team who can better assist you."""

# Template for safe troubleshooting
TEMPLATE_SAFE_TROUBLESHOOTING = """I can help with that! Here are some safe troubleshooting steps you can try:

{steps}

If these steps don't resolve the issue, please click "Generate IT Ticket" for further assistance."""

# Template for clarification needed
TEMPLATE_CLARIFICATION = """I'd like to help you with {issue}. To provide the best assistance, could you please provide more details about:

• What exactly is happening?
• When did this start?
• What error messages are you seeing?

This will help me guide you to the right solution or create an appropriate IT ticket."""

# Template for urgent issues
TEMPLATE_URGENT = """This appears to be an urgent issue. Please click "Generate IT Ticket" immediately to create a high-priority support request. Our IT team will respond as soon as possible."""

# ============================================================================
# MODEL BEHAVIOR FINE-TUNING
# ============================================================================

# Response optimization
RESPONSE_OPTIMIZATION = {
    "avoid_repetition": True,           # Avoid repeating the same phrases
    "use_variety": True,                # Use varied vocabulary
    "maintain_context": True,           # Remember conversation context
    "ask_clarifying_questions": True,   # Ask questions when needed
    "provide_examples": False,          # Provide examples (not needed for this use case)
    "explain_reasoning": False,         # Explain why (keep responses concise)
}

# Language settings
LANGUAGE_SETTINGS = {
    "primary_language": "English",
    "formality": "semi-formal",         # semi-formal, formal, casual
    "jargon_level": "low",              # low, medium, high
    "technical_depth": "medium",        # low, medium, high
}

# ============================================================================
# DEBUGGING AND LOGGING
# ============================================================================

# Debug settings
DEBUG_MODE = False

# Log level
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR

# Enable response logging
LOG_RESPONSES = True

# ============================================================================
# ADVANCED SETTINGS
# ============================================================================

# Context window management
CONTEXT_SETTINGS = {
    "max_history_messages": 10,         # Number of previous messages to remember
    "summarize_old_messages": True,     # Summarize old messages to save tokens
    "forget_after_hours": 24,           # Forget conversation after hours
}

# Performance settings
PERFORMANCE_SETTINGS = {
    "cache_responses": False,           # Cache common responses (not recommended for dynamic content)
    "preload_models": False,            # Preload models on startup
    "async_processing": True,           # Process requests asynchronously
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_model_parameters():
    """Get all model parameters as a dictionary"""
    return {
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS,
        "frequency_penalty": FREQUENCY_PENALTY,
        "presence_penalty": PRESENCE_PENALTY,
    }

def get_response_style():
    """Get response style configuration"""
    return {
        "length": RESPONSE_LENGTH,
        "tone": TONE_SETTINGS,
        "formatting": FORMATTING_PREFERENCES,
        "quality": RESPONSE_QUALITY,
    }

def get_safety_settings():
    """Get safety configuration"""
    return {
        "safety_first": SAFETY_FIRST,
        "forbidden_instructions": FORBIDDEN_INSTRUCTIONS,
        "always_escalate": ALWAYS_ESCALATE,
        "escalation_triggers": ESCALATION_TRIGGERS,
    }

def get_template(template_name, **kwargs):
    """Get a response template with variables filled in"""
    templates = {
        "admin_required": TEMPLATE_ADMIN_REQUIRED,
        "outside_scope": TEMPLATE_OUTSIDE_SCOPE,
        "safe_troubleshooting": TEMPLATE_SAFE_TROUBLESHOOTING,
        "clarification": TEMPLATE_CLARIFICATION,
        "urgent": TEMPLATE_URGENT,
    }
    
    template = templates.get(template_name, "")
    if template and kwargs:
        return template.format(**kwargs)
    return template

def should_escalate(user_message):
    """Determine if a message should be escalated to IT ticket"""
    message_lower = user_message.lower()
    
    # Check for always escalate topics
    for topic in ALWAYS_ESCALATE:
        if topic in message_lower:
            return True
    
    # Check for escalation triggers
    for trigger in ESCALATION_TRIGGERS:
        if trigger in message_lower:
            return True
    
    return False

def is_safe_troubleshooting(user_message):
    """Determine if a message is safe for troubleshooting"""
    message_lower = user_message.lower()
    
    for safe_keyword in SAFE_TROUBLESHOOTING:
        if safe_keyword in message_lower:
            return True
    
    return False

# ============================================================================
# CONFIGURATION VALIDATION
# ============================================================================

def validate_configuration():
    """Validate the configuration settings"""
    errors = []
    
    # Validate temperature
    if not 0.0 <= TEMPERATURE <= 2.0:
        errors.append("Temperature must be between 0.0 and 2.0")
    
    # Validate top_p
    if not 0.0 <= TOP_P <= 1.0:
        errors.append("Top-p must be between 0.0 and 1.0")
    
    # Validate max_tokens
    if MAX_TOKENS < 1:
        errors.append("Max tokens must be positive")
    
    # Validate response length
    valid_lengths = ["concise", "standard", "detailed"]
    if RESPONSE_LENGTH not in valid_lengths:
        errors.append(f"Response length must be one of: {valid_lengths}")
    
    # Validate tone settings
    required_tones = ["professional", "friendly", "empathetic", "authoritative", "cautious"]
    for tone in required_tones:
        if tone not in TONE_SETTINGS:
            errors.append(f"Tone setting '{tone}' is missing")
    
    if errors:
        print("Configuration validation errors:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    return True

# ============================================================================
# CONFIGURATION PRESETS
# ============================================================================

# Preset configurations for different use cases
PRESETS = {
    "balanced": {
        "temperature": 0.7,
        "top_p": 0.9,
        "max_tokens": 1024,
        "response_length": "standard",
        "tone": "balanced",
    },
    "precise": {
        "temperature": 0.3,
        "top_p": 0.8,
        "max_tokens": 512,
        "response_length": "concise",
        "tone": "formal",
    },
    "educational": {
        "temperature": 0.6,
        "top_p": 0.9,
        "max_tokens": 1536,
        "response_length": "detailed",
        "tone": "friendly",
    },
    "urgent": {
        "temperature": 0.4,
        "top_p": 0.85,
        "max_tokens": 256,
        "response_length": "concise",
        "tone": "authoritative",
    },
}

def apply_preset(preset_name):
    """Apply a preset configuration"""
    if preset_name not in PRESETS:
        print(f"Preset '{preset_name}' not found. Available presets: {list(PRESETS.keys())}")
        return False
    
    preset = PRESETS[preset_name]
    
    # Update global variables (note: this is a simplified approach)
    print(f"Applying preset: {preset_name}")
    for key, value in preset.items():
        print(f"  {key}: {value}")
    
    return True

# ============================================================================
# INITIALIZATION
# ============================================================================

# Validate configuration on import
if __name__ == "__main__":
    print("Validating model behavior configuration...")
    if validate_configuration():
        print("✓ Configuration is valid")
    else:
        print("✗ Configuration has errors")
    
    print("\nAvailable presets:")
    for preset_name in PRESETS.keys():
        print(f"  - {preset_name}")
