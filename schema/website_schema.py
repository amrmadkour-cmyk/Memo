tool = {
    "type": "function",
    "function": {
        "name": "open_website",
        "description": "Open predefined websites like google, youtube, facebook, github",
        "parameters": {
            "type": "object",
            "properties": {
                "site_name": {
                    "type": "string",
                    "description": "Allowed values: google, youtube, facebook, github"
                }
            },
            "required": ["site_name"]
        }
    }
}
