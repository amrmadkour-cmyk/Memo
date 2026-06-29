# plugins/random_quote_or_joke.py
import random

def random_quote_or_joke(category):
    try:
        category = category.lower().strip()
        
        # 15 English Jokes (Tech, Programming, and General)
        jokes = [
            "Why do programmers wear glasses? Because they can't C#!",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
            "Why do frogs love working in tech? Because they are excellent at debugging and catching flies!",
            "What is a programmer's favorite hangout place? The Foo Bar.",
            "Why did the computer go to the hospital? It had a virus!",
            "Why do Java developers wear glasses? Because they don't C.",
            "To understand what recursion is, you must first understand what recursion is.",
            "Optimist: The glass is half full. Pessimist: The glass is half empty. Programmer: The glass is twice as large as it needs to be.",
            "Where is the best place to hide a dead body? Page two of Google search results.",
            "Why did the functions stop arguing? They just couldn't find a common return value.",
            "What do you call a programmer from Finland? Nerdic.",
            "Why did the developer go broke? Because he used up all his cache!"
        ]
        
        # 16 English Quotes (Including your special additions)
        quotes = [
            "Martin Scorsese once said The most personal is the most creative keep it in mind",
            "A moment of pain is worth a lifetime of glory",
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Code is like humor. When you have to explain it, it’s bad. - Cory House",
            "Fix the cause, not the symptom. - Steve Maguire",
            "Talk is cheap. Show me the code. - Linus Torvalds",
            "The best way to predict the future is to invent it. - Alan Kay",
            "Artificial intelligence is growing fast, but human determination is unstoppable.",
            "It's not a bug; it's an undocumented feature!",
            "Your success begins when you decide to keep going when everyone else decides to stop.",
            "Intelligence is not about never making mistakes, it's about debugging them and learning for the next time.",
            "In the journey of learning, every hour spent focusing saves you years of wandering.",
            "Mathematics and logic are the language of the universe; mastering them unlocks technology.",
            "Building smart systems is like building castles; it requires patience with foundations.",
            "Never worry about moving slowly, only worry about standing still.",
            "A real engineer doesn't just memorize code, they master the mindset of problem-solving."
        ]
        
        # Handling specific Favorite Quote request
        if category == "favorite":
            return "Martin Scorsese once said The most personal is the most creative keep it in mind"
            
        elif category == "joke":
            return random.choice(jokes)
            
        elif category == "quote":
            return random.choice(quotes)
            
        else:
            return "I can give you a 'joke', a 'quote', or your 'favorite' quote."
            
    except Exception as e:
        return f"Error getting content: {str(e)}"