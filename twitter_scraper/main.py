import unittest
from twitter_scraper import get_tweets, get_trends
import csv

def write_posts_to_csv(query=None, filename=None, pages=None, **kwargs):
    """
    :param account:     Facebook account name e.g. "nike", string
    :param group:       Facebook group id
    :param filename:    File name, defaults to <<account_posts.csv>>
    :param pages:       Number of pages to scan, integer
    :param timeout:     Session response timeout in seconds, integer
    :param sleep:       Sleep time in s before every call, integer
    :param credentials: Credentials for login - username and password, tuple
    :return:            CSV written in the same location with <<account_name>>_posts.csv
    """
    list_of_posts = list(get_tweets(query=query, pages=pages, **kwargs))

    if not list_of_posts:
        print("Couldn't get any posts.", file=sys.stderr)
        return

    keys = list_of_posts[0].keys()

    if filename is None:
        filename = str(account or group) + "_posts.csv"

    with open(filename, 'w', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(list_of_posts)

def _main():
    """facebook-scraper entry point when used as a script"""
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tweet', type=str, help="Twitter tweet and Hashtags")
    #parser.add_argument('-r', '--trend', type=str, help="Twitter trend")
    parser.add_argument('-f', '--filename', type=str, help="Output filename")
    parser.add_argument('-p', '--pages', type=int, help="Number of pages to download", default=5)
    
    args = parser.parse_args()

    write_posts_to_csv(query=args.tweet, filename=args.filename, pages=args.pages)

if __name__ == "__main__":
    _main()
