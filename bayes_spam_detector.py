def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Enter a valid non-negative integer.")

total_emails = get_valid_input("Enter total number of emails: ")
emails_with_free = get_valid_input("Enter number of emails containing 'free': ")
spam_emails = get_valid_input("Enter number of spam emails: ")
spam_and_free = get_valid_input("Enter number of emails that are both spam and contain 'free': ")

if total_emails == 0 or spam_emails == 0 or emails_with_free == 0:
    print("Cannot compute probability with zero values.")
else:
    p_spam = spam_emails / total_emails
    p_free = emails_with_free / total_emails
    p_free_given_spam = spam_and_free / spam_emails
    p_spam_given_free = (p_free_given_spam * p_spam) / p_free
    print(f"P(Spam | Free): {p_spam_given_free:.4f}")
