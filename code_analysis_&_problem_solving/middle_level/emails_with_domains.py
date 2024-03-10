# Given a list of emails and URLs, return a dictionary, where each key is a URL and the value is how many emails
# have the same domain.
# Note that the domain begin with www. whereas the emails do not, and that emails with domains not in the list of urls
# should be ignored.

'''count_email_domains(
      emails=['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com'],
      urls=['www.a.com', 'www.b.com', 'www.c.com']
'''

# Solution
# To solve this problem, we need to follow these steps:

# 1.	Extract the domain from each email.
# 2.	Match the extracted domain with the given URLs.
# 3.	Count the occurrences of each domain associated with the given URLs.
# 4.	Create a dictionary where the keys are the URLs and the values are the counts of emails having domains associated with those URLs.

from collections import defaultdict


def count_email_domains(emails, urls):
    # Initialize a default dict to store the counts of email domains
    domain_counts = defaultdict(int)

    # Initialize counts for all URLs to 0
    for url in urls:
        domain_counts[url] = 0

    # Iterate through each email
    for email in emails:
        # Extract the domain part of the email
        domain = email.split('@')[-1]  # Split by '@' and take the last part

        # Check if the domain is in the list of URLs
        for url in urls:
            if domain == url[4:]:
                # Increment the count for the corresponding URL
                domain_counts[url] += 1
                break  # Move to the next email once a match is found

    return dict(domain_counts)


# Test the function
emails = ['foo@a.com', 'bar@a.com', 'baz@b.com', 'qux@d.com']
urls = ['www.a.com', 'www.b.com', 'www.c.com']
result = count_email_domains(emails, urls)
print(result)
