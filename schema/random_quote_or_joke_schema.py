tool = {
            "type": "function",
            "function": {
                "name": "random_quote_or_joke",
                "description": "Returns a random joke, an inspirational quote, or the user's specific favorite quote. Call this tool when the user asks for a joke, motivation, or their favorite quote.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "enum": ["joke", "quote", "favorite"],  # <--- إضافة favorite هنا
                            "description": "Choose 'joke' for funny content, 'quote' for inspiration, or 'favorite' if the user explicitly asks for their favorite quote."
                        }
                    },
                    "required": ["category"]
                }
            }
        }