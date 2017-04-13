def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link != -1:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    else:
        return None,0   

def print_all_links(page):
    while page:
        url, endops = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            page = None
            
