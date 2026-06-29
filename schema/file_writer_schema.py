tool = {
    "type": "function",
    "function": {
        "name": "save_text_to_file",
        "description": "Save text into a file, either append or overwrite",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "Text to save"
                },
                "filename": {
                    "type": "string",
                    "description": "File name (default output.txt)"
                },
                "append": {
                    "type": "boolean",
                    "description": "If true append, if false overwrite"
                }
            },
            "required": ["text"]
        }
    }
}
