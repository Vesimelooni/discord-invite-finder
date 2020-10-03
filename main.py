import requests
import random
import string
import multiprocessing
from random import choice
def link_create(random_length):
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(random_length))
    main_discord_server = 'https://discord.com/invite/'
    discord_server_link = str(main_discord_server + random_string)
    return discord_server_link
def check_link(link, server_name):
    print("Checking link " + link)
    source = requests.get(link).text
    if server_name in str(source):
        return True
    else:
        return False
def runtime(server_name):
    while True:
        link = link_create(random.randint(5, 7))
        if check_link(link, server_name=server_name):
            print("Server link found for server {0}: {1}".format(link, server_name))
            break
if "__main__" == __name__:
    server_name = input("Enter Discord server name: ")
    print("""DISCLAIMER, THIS PROGRAM WILL REQUIRE ALOT OF TIME AND RESOURCES.
BY USING THIS PROGRAM YOU ALLOW THE PROGRAM TO DO ITS NEEDS.
IF SOMETHING HAPPES, IT IS THE USER OF THIS SOFTWARE'S FAULT.
I WONT BE INVOLVED WHAT YOU MAY USE THIS PROGRAM FOR.""")
    processes = []
    for x in range(1, multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=runtime, args=(server_name,))
        processes.append(p)
        p.start()
    for process in processes:
        process.join()
