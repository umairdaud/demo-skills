#!/usr/bin/env python3
"""
Email Tone Analyzer
Provides feedback on email tone and suggests improvements
"""

import sys
import re

def analyze_email_tone(email_text):
    """Analyze the tone of an email and provide feedback"""
    feedback = []

    # Check for overly aggressive language
    aggressive_words = ['unacceptable', 'inexcusable', 'ridiculous', 'outrageous', 'terrible']
    found_aggressive = [word for word in aggressive_words if word.lower() in email_text.lower()]
    if found_aggressive:
        feedback.append(f"Warning: Found potentially aggressive language: {', '.join(found_aggressive)}")

    # Check for positive language
    positive_words = ['thank you', 'appreciate', 'excellent', 'great', 'wonderful', 'helpful']
    found_positive = [word for word in positive_words if word.lower() in email_text.lower()]
    if not found_positive:
        feedback.append("Consider adding positive language to improve tone")

    # Check for clarity
    if len(email_text.split()) < 20:
        feedback.append("Email may be too brief - consider adding more context")

    # Check for personalization
    if not re.search(r'\b(you|your|we|our)\b', email_text, re.IGNORECASE):
        feedback.append("Consider personalizing the email with 'you' or 'your'")

    return feedback

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_email_tone.py \"<email_text>\"")
        sys.exit(1)

    email_text = sys.argv[1]
    feedback = analyze_email_tone(email_text)

    if feedback:
        print("Tone Analysis Feedback:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Email tone appears appropriate")

if __name__ == "__main__":
    main()