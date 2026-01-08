def get_response(user_input):
    """
    Simple function to return a greeting.
    """
    if "hello" in user_input.lower():
        return "Hello! Welcome to ABC Bookstore. How can I help you today?"
    else:
        return "I am just a simple bot. Please say hello!"

if __name__ == "__main__":
    # Test the greeting manually
    print(get_response("Hello"))
