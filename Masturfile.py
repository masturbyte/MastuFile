#CODED BY : AHMED KORI
#GITHUB : @masturbyte
#just say : alhamdullah
#_______________________
import argparse
from googlesearch import search
from bs4 import BeautifulSoup
import requests
import threading

def banner():
    font = """
\033[95m███╗   ███╗ █████╗ ███████╗████████╗██╗   ██╗███████╗██╗██╗     ███████╗
\033[95m████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██║   ██║██╔════╝██║██║     ██╔════╝
\033[95m██╔████╔██║███████║███████╗   ██║   ██║   ██║█████╗  ██║██║     █████╗  
\033[95m██║╚██╔╝██║██╔══██║╚════██║   ██║   ██║   ██║██╔══╝  ██║██║     ██╔══╝  
\033[95m██║ ╚═╝ ██║██║  ██║███████║   ██║   ╚██████╔╝██║     ██║███████╗███████╗
\033[95m╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝
\033[0m\033[92m                                                                                     
  \033[38;2;180;181;223mcode by : Ahmed Kori | @masturbyte
"""
    print(font)

def get_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        return title
    except:
        return "Title not found"

def search_with_number_and_name(number, name):
    number_query = f'"{number}"'
    name_query = f'"{name}"'
    number_results = search(number_query, num=10, stop=10, pause=2)
    name_results = search(name_query, num=10, stop=10, pause=2)
    facebook_links = []
    linkedin_links = []
    other_links = []

    for link in number_results:
        if "facebook.com" in link:
            facebook_links.append(link)
        elif "linkedin.com" in link:
            linkedin_links.append(link)
        else:
            other_links.append(link)

    for link in name_results:
        if "facebook.com" in link and link not in facebook_links:
            facebook_links.append(link)
        elif "linkedin.com" in link and link not in linkedin_links:
            linkedin_links.append(link)
        elif link not in other_links:
            other_links.append(link)

    return facebook_links, linkedin_links, other_links

def perform_search(number_to_search, name_to_search, output_file, results):
    if number_to_search and name_to_search:
        print(f"\nSearching for : {name_to_search}\r")
        facebook_links, linkedin_links, other_links = search_with_number_and_name(number_to_search, name_to_search)
        results[name_to_search] = (facebook_links, linkedin_links, other_links)

    if output_file:
        save_results(output_file, results)
    else:
        display_results(results)

def display_results(results):
    print("\033[92m\nSearch results for the number and name combined:\033[0m")
    for name, (facebook_links, linkedin_links, other_links) in results.items():
        if facebook_links:
            print("\033[94m\nFacebook:")
            for i, link in enumerate(facebook_links[:7], start=1):
                title = get_page_title(link)
                print(f"{i}. \033[33m{title}\033[0m: {link}")
        if linkedin_links:
            print("\033[34m\nLinkedIn:")
            for i, link in enumerate(linkedin_links[:7], start=1):
                title = get_page_title(link)
                print(f"{i}. \033[33m{title}\033[0m: {link}")
        if other_links:
            print("\033[92m\nOther websites:")
            for i, link in enumerate(other_links[:7], start=1):
                title = get_page_title(link)
                print(f"{i}. \033[33m{title}\033[0m: {link}")

def save_results(file_path, results):
    with open(file_path, 'w') as f:
        for name, (facebook_links, linkedin_links, other_links) in results.items():
            f.write(f"{name}:\n")
            if facebook_links:
                f.write("Facebook:\n")
                for i, link in enumerate(facebook_links, start=1):
                    title = get_page_title(link)
                    f.write(f"{i}. {title}: {link}\n")
            if linkedin_links:
                f.write("LinkedIn:\n")
                for i, link in enumerate(linkedin_links, start=1):
                    title = get_page_title(link)
                    f.write(f"{i}. {title}: {link}\n")
            if other_links:
                f.write("Other websites:\n")
                for i, link in enumerate(other_links, start=1):
                    title = get_page_title(link)
                    f.write(f"{i}. {title}: {link}\n")

def main():
    try:
        parser = argparse.ArgumentParser(description="\033[96mMastuFile for a phone number and name .\033[0m")
        parser.add_argument("-n", "--number", type=str, help="\033[95mThe phone number to search for\033[0m")
        parser.add_argument("-m", "--name", type=str, help="\033[95mThe name associated with the phone number\033[0m")
        parser.add_argument("-L", "--list", type=str, help="\033[95mPath to a file containing a list of phone numbers and names\033[0m")
        parser.add_argument("-d", "--output", type=str, help="\033[95mOutput file to save the search results\033[0m")
        args = parser.parse_args()

        number_to_search = args.number
        name_to_search = args.name
        list_file = args.list
        output_file = args.output
        results = {}

        if list_file:
            with open(list_file, 'r') as f:
                for line in f:
                    number, name = line.strip().split(',')
                    perform_search(number.strip(), name.strip(), output_file, results)
        else:
            perform_search(number_to_search, name_to_search, output_file, results)				
    except KeyboardInterrupt:
       print("\n\033[92mhey dont shut me like this If you're a script, would you be satisfied if someone just closed you like this?\033[0m")



if __name__ == "__main__":
    banner()
    main()
