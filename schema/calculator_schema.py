tool = {
    "type": "function",
    "function": {
        "name": "safe_calculator",
        "description": "Safely evaluate mathematical expressions",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Math expression like 5 + 3 * 2"
                }
            },
            "required": ["expression"]
        }
    }
}
