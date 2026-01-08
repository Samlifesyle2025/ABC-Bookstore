from chatbot import greet

def test_greeting():
    expected_message = "Welcome to ABC Bookstore! How can I help you find your next great read today?"
    assert greet() == expected_message
