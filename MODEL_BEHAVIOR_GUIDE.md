# Model Behavior Configuration Guide

## Overview

The `model_behavior_config.py` file provides a comprehensive configuration system for adjusting the LLM model's behavior to provide better information to users. This file allows you to fine-tune how the AI assistant responds to user queries without modifying the main chatbot code.

## File Structure

The configuration file is organized into several sections:

1. **Response Generation Parameters** - Core LLM parameters
2. **Response Style Parameters** - How the AI communicates
3. **System Prompt Templates** - Different prompt templates for various scenarios
4. **Behavior Guidelines** - Rules and triggers for AI behavior
5. **Safety Settings** - Security and safety configurations
6. **Response Templates** - Pre-defined response formats
7. **Model Behavior Fine-Tuning** - Advanced behavior settings
8. **Debugging and Logging** - Debug configurations
9. **Advanced Settings** - Context and performance settings
10. **Helper Functions** - Utility functions
11. **Configuration Validation** - Settings validation
12. **Configuration Presets** - Pre-configured behavior profiles

## How to Use

### 1. Adjusting Response Generation Parameters

These parameters control how the LLM generates responses:

```python
# Temperature: Controls randomness (0.0-2.0)
# - Lower = more focused, predictable
# - Higher = more creative, diverse
TEMPERATURE = 0.7

# Top-p: Controls response diversity (0.0-1.0)
# - Lower = more focused on high-probability tokens
# - Higher = more diverse responses
TOP_P = 0.9

# Max tokens: Limit response length
# - 512 = brief responses
# - 1024 = standard responses (recommended)
# - 2048 = detailed explanations
MAX_TOKENS = 1024

# Frequency penalty: Reduce repetition (-2.0 to 2.0)
FREQUENCY_PENALTY = 0.5

# Presence penalty: Encourage new topics (-2.0 to 2.0)
PRESENCE_PENALTY = 0.3
```

**When to adjust:**
- **For more precise answers**: Lower temperature (0.3-0.5), lower top-p (0.7-0.8)
- **For more creative/helpful answers**: Higher temperature (0.7-0.9), higher top-p (0.9-0.95)
- **For longer explanations**: Increase MAX_TOKENS to 1536 or 2048
- **For shorter responses**: Decrease MAX_TOKENS to 512

### 2. Customizing Response Style

Control how the AI communicates with users:

```python
RESPONSE_LENGTH = "standard"  # Options: "concise", "standard", "detailed"

TONE_SETTINGS = {
    "professional": True,      # Use professional language
    "friendly": True,          # Be approachable and helpful
    "empathetic": True,        # Show understanding of user issues
    "authoritative": True,     # Demonstrate expertise
    "cautious": True,          # Be careful with recommendations
}

FORMATTING_PREFERENCES = {
    "use_bullets": True,       # Use bullet points for lists
    "use_numbering": True,     # Use numbered lists for steps
    "use_emojis": True,        # Use emojis for visual appeal
    "use_bold": True,          # Use bold text for emphasis
    "use_headers": True,       # Use section headers
}
```

**When to adjust:**
- **For technical users**: Set `jargon_level` to "medium" in LANGUAGE_SETTINGS
- **For non-technical users**: Keep `jargon_level` as "low"
- **For urgent issues**: Use RESPONSE_LENGTH = "concise"
- **For educational purposes**: Use RESPONSE_LENGTH = "detailed"

### 3. Using Different Prompt Templates

The configuration provides alternative prompt templates for different scenarios:

```python
# The main template is used by default
SYSTEM_PROMPT_TEMPLATE = """You are AskForHelp..."""

# Alternative templates for specific scenarios
ALTERNATIVE_PROMPTS = {
    "concise": "...",      # For quick, brief responses
    "educational": "...",  # For teaching/explaining
    "urgent": "...",       # For urgent issues
}
```

**How to use alternative templates:**

You can modify the main chatbot to use different templates based on the situation:

```python
# In askforhelp_chatbot.py, modify query_ai() method:
def query_ai(self, user_message):
    # Check if issue is urgent
    if self.model_behavior.should_escalate(user_message):
        prompt_template = self.model_behavior.ALTERNATIVE_PROMPTS["urgent"]
    # Check if user wants detailed explanation
    elif "explain" in user_message.lower() or "how" in user_message.lower():
        prompt_template = self.model_behavior.ALTERNATIVE_PROMPTS["educational"]
    else:
        prompt_template = self.model_behavior.SYSTEM_PROMPT_TEMPLATE
    
    prompt = prompt_template.format(...)
```

### 4. Configuring Behavior Guidelines

Control when the AI should escalate to IT tickets:

```python
# Escalation triggers - keywords that require IT ticket
ESCALATION_TRIGGERS = [
    "admin", "administrator", "admin rights",
    "system files", "registry", "permissions",
    "install software", "update driver",
    # ... more triggers
]

# Safe troubleshooting - can provide guidance
SAFE_TROUBLESHOOTING = [
    "restart", "reboot", "close program",
    "clear cache", "check connection",
    # ... more safe topics
]

# Always escalate for critical issues
ALWAYS_ESCALATE = [
    "data loss", "security breach", "system crash",
    "hardware failure", "network outage",
    # ... more critical issues
]
```

**When to adjust:**
- **Add organization-specific triggers**: Add keywords related to your company's software or policies
- **Expand safe topics**: Add more non-admin troubleshooting steps
- **Customize escalation**: Adjust based on your IT team's capabilities

### 5. Safety Settings

Configure safety-first behavior:

```python
SAFETY_FIRST = True

FORBIDDEN_INSTRUCTIONS = [
    "registry edit",
    "system file modification",
    "permission changes",
    # ... more forbidden topics
]

ALWAYS_ESCALATE = [
    "data loss",
    "security breach",
    "system crash",
    # ... more critical issues
]
```

**Important**: Never remove safety-critical settings. Only add organization-specific forbidden instructions if needed.

### 6. Using Response Templates

The configuration provides pre-defined response templates:

```python
# Get a template with variables filled in
template = model_behavior_config.get_template(
    "admin_required", 
    issue="modifying system settings"
)
# Returns: "I understand you're experiencing modifying system settings. This requires..."
```

**Available templates:**
- `"admin_required"` - For admin rights requests
- `"outside_scope"` - For non-PC questions
- `"safe_troubleshooting"` - For safe troubleshooting steps
- `"clarification"` - When more information is needed
- `"urgent"` - For urgent issues

### 7. Helper Functions

Use built-in helper functions for decision-making:

```python
# Check if a message should be escalated
if model_behavior_config.should_escalate(user_message):
    # Guide to IT ticket
    pass

# Check if a message is safe for troubleshooting
if model_behavior_config.is_safe_troubleshooting(user_message):
    # Provide troubleshooting steps
    pass
```

### 8. Configuration Presets

Use pre-configured behavior profiles:

```python
# Apply a preset configuration
model_behavior_config.apply_preset("balanced")   # Default settings
model_behavior_config.apply_preset("precise")    # More focused, deterministic
model_behavior_config.apply_preset("educational") # More detailed, explanatory
model_behavior_config.apply_preset("urgent")     # Quick, authoritative responses
```

**Available presets:**
- `"balanced"` - Default settings, good for general use
- `"precise"` - Lower temperature, more focused responses
- `"educational"` - More detailed, explanatory responses
- `"urgent"` - Quick, authoritative responses for urgent issues

### 9. Validation

Validate your configuration before using it:

```python
# Run validation
if model_behavior_config.validate_configuration():
    print("Configuration is valid")
else:
    print("Configuration has errors - check settings")
```

## Integration with Main Chatbot

The main chatbot (`askforhelp_chatbot.py`) has been updated to use the model behavior configuration:

```python
# Import the configuration
import model_behavior_config

# In the __init__ method:
self.model_behavior = model_behavior_config

# In the query_ai method:
prompt = self.model_behavior.SYSTEM_PROMPT_TEMPLATE.format(
    username=self.system_info['username'],
    hostname=self.system_info['hostname'],
    os_info=self.system_info['os_info'],
    ip_address=self.system_info['ip_address'],
    timestamp=self.system_info['timestamp'],
    user_message=user_message
)

payload = {
    "model": self.model,
    "prompt": prompt,
    "stream": False,
    "options": self.model_behavior.get_model_parameters()
}
```

## Common Use Cases

### Use Case 1: More Precise Technical Answers

**Goal**: Get more accurate, less creative responses for technical issues.

**Changes**:
```python
TEMPERATURE = 0.4
TOP_P = 0.8
MAX_TOKENS = 512
RESPONSE_LENGTH = "concise"
TONE_SETTINGS["professional"] = True
TONE_SETTINGS["friendly"] = False
```

### Use Case 2: Better for Non-Technical Users

**Goal**: Make responses more approachable and educational.

**Changes**:
```python
TEMPERATURE = 0.7
TOP_P = 0.9
MAX_TOKENS = 1024
RESPONSE_LENGTH = "standard"
LANGUAGE_SETTINGS["jargon_level"] = "low"
LANGUAGE_SETTINGS["technical_depth"] = "low"
TONE_SETTINGS["friendly"] = True
TONE_SETTINGS["empathetic"] = True
```

### Use Case 3: Urgent Issue Handling

**Goal**: Quick, authoritative responses for urgent issues.

**Changes**:
```python
TEMPERATURE = 0.4
TOP_P = 0.85
MAX_TOKENS = 256
RESPONSE_LENGTH = "concise"
TONE_SETTINGS["authoritative"] = True
TONE_SETTINGS["cautious"] = False
```

### Use Case 4: Educational Mode

**Goal**: Explain issues in detail for learning purposes.

**Changes**:
```python
TEMPERATURE = 0.6
TOP_P = 0.9
MAX_TOKENS = 1536
RESPONSE_LENGTH = "detailed"
LANGUAGE_SETTINGS["technical_depth"] = "high"
TONE_SETTINGS["friendly"] = True
RESPONSE_OPTIMIZATION["explain_reasoning"] = True
```

## Best Practices

### 1. Test Changes Incrementally
- Make one change at a time
- Test with sample queries
- Monitor user feedback

### 2. Keep Safety Settings
- Never disable SAFETY_FIRST
- Keep forbidden instructions comprehensive
- Maintain escalation triggers

### 3. Document Your Changes
- Keep a changelog of configuration modifications
- Note which settings work best for your users
- Share successful configurations with your team

### 4. Validate Before Deploying
- Always run `validate_configuration()` after changes
- Check for typos in parameter names
- Ensure values are within valid ranges

### 5. Use Presets as Starting Points
- Start with "balanced" preset
- Adjust based on user feedback
- Create custom presets for different use cases

## Troubleshooting

### Problem: Responses are too verbose
**Solution**: 
- Decrease MAX_TOKENS to 512
- Set RESPONSE_LENGTH to "concise"
- Lower TEMPERATURE to 0.4

### Problem: Responses are too brief
**Solution**:
- Increase MAX_TOKENS to 1536
- Set RESPONSE_LENGTH to "detailed"
- Raise TEMPERATURE to 0.8

### Problem: AI is too creative/unpredictable
**Solution**:
- Lower TEMPERATURE to 0.3-0.5
- Lower TOP_P to 0.7-0.8
- Set RESPONSE_LENGTH to "concise"

### Problem: AI is not escalating when it should
**Solution**:
- Add more keywords to ESCALATION_TRIGGERS
- Add organization-specific terms to ALWAYS_ESCALATE
- Check that should_escalate() function is being called

### Problem: Configuration validation fails
**Solution**:
- Check that all required tone settings are present
- Ensure temperature is between 0.0 and 2.0
- Verify top_p is between 0.0 and 1.0
- Check that RESPONSE_LENGTH is one of: "concise", "standard", "detailed"

## Advanced Configuration

### Custom Presets

You can create your own presets by adding to the PRESETS dictionary:

```python
PRESETS = {
    # ... existing presets
    "my_custom_preset": {
        "temperature": 0.5,
        "top_p": 0.85,
        "max_tokens": 768,
        "response_length": "standard",
        "tone": "professional",
    },
}
```

### Dynamic Configuration

You can make the configuration dynamic based on time, user, or other factors:

```python
import datetime

# Adjust behavior based on time of day
current_hour = datetime.datetime.now().hour
if current_hour < 9 or current_hour > 17:
    # After hours - more concise, urgent tone
    TEMPERATURE = 0.4
    RESPONSE_LENGTH = "concise"
else:
    # Business hours - standard behavior
    TEMPERATURE = 0.7
    RESPONSE_LENGTH = "standard"
```

### Integration with User Preferences

You could extend the system to load user-specific preferences:

```python
def load_user_preferences(username):
    """Load user-specific behavior preferences"""
    preferences = {
        "technical_level": "medium",  # low, medium, high
        "response_style": "standard",  # concise, standard, detailed
        "tone": "balanced",  # formal, balanced, casual
    }
    return preferences

# Apply user preferences
user_prefs = load_user_preferences(username)
if user_prefs["response_style"] == "concise":
    MAX_TOKENS = 512
    RESPONSE_LENGTH = "concise"
```

## Security Considerations

### 1. Never Expose Configuration in Production
- Keep `model_behavior_config.py` in your codebase
- Don't expose configuration endpoints to users
- Validate all configuration changes

### 2. Maintain Safety Settings
- Always keep SAFETY_FIRST = True
- Never remove critical escalation triggers
- Keep forbidden instructions comprehensive

### 3. Audit Configuration Changes
- Track who modifies the configuration
- Review changes before deployment
- Test thoroughly in development environment

## Summary

The `model_behavior_config.py` file provides a powerful, flexible way to control how the AI assistant behaves. By adjusting parameters, you can:

- **Improve response quality** - Fine-tune creativity vs. precision
- **Customize communication style** - Adjust tone and formatting
- **Enhance safety** - Control when to escalate to IT tickets
- **Optimize for different use cases** - Use presets or create custom configurations
- **Maintain consistency** - Centralized configuration for all AI behavior

Start with the default "balanced" preset and adjust based on user feedback and specific needs. Always test changes thoroughly and maintain safety as the top priority.
