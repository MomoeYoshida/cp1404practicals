"""
Write a small script that prompts the user for a page title or search phrase,
then prints the summary of that page. Use a simple loop that continues doing
this until the user enters blank input.
"""
import wikipedia

# Write a small script that prompts the user for a page title or search phrase,
# then prints the summary of that page. Use a simple loop that continues doing
# this until the user enters blank input.
def wiki_summary():
    """Print the summary of the page which the user chooses."""
    page_title = input("Enter a page title: ")
    while not page_title == "":
        try:
            print(wikipedia.summary(page_title))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        page_title = input("Enter a page title: ")
    print("Finish!")

# Modify your program so when it gets the page, it prints the title, summary and the URL.
def wiki():
    """Print the title, summary and the URL of the page which the user chooses."""
    page = input("Enter page: ")
    while not page == "":
        try:
            print("Title:", wikipedia.page(page).title)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        print("Summary: \n", wikipedia.summary(page))
        print("URL:", wikipedia.page(page).url)
        page = input("Enter page: ")
    print("Finish!")


# wiki_summary()
wiki()
