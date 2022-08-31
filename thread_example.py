# import time
# import threading
#
#
# # First Method
# def greet_them(people):
#     for person in people:
#         print("Hello Dear " + person + ". How are you?")
#         time.sleep(0.5)
#
#
# # Second Method
# def assign_id(people):
#     i = 1
#     for person in people:
#         print("Hey! {}, your id is {}.".format(person, i))
#         i += 1
#         time.sleep(0.5)
#
#
# people = ['Richard', 'Dinesh', 'Elrich', 'Gilfoyle', 'Gevin', 'Micheal']
#
# t = time.time()
# t1 = threading.Thread(target=greet_them, args=(people,))
# t2 = threading.Thread(target=assign_id, args=(people,))
# # Started the threads
# t1.start()
# t2.start()
#
# # Joined the threads
# t1.join()
# t2.join()
# # greet_them(people)
# # assign_id(people)
#
# print("Woaahh!! My work is finished..")
# print("I took " + str(time.time() - t))

# import logging
# import threading
# import time
#
#
# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)
#
#
# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#
#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()
#
#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)


## asyncio
# import asyncio
# import time
# import aiohttp
#
#
# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))
#
#
# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)
#
#
# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 100
#     start_time = time.time()
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")

## Multipleprocess
import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "http://olympus.realpython.org/dice",
            ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
