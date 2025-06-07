def is_safe(prompt):
    blocked_keywords = ['hate', 'kill', 'violence', 'racism', 'abuse']
    lower_prompt = prompt.lower()
    return not any(word in lower_prompt for word in blocked_keywords)
