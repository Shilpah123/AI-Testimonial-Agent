def validate_testimonial(text):

    result = {
        "professional": True,
        "spam": False,
        "contains_sensitive_info": False
    }

    if len(text.strip()) < 20:
        result["professional"] = False

    return result