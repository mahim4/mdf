from argparse import ArgumentParser
from requests import get, HTTPError, ConnectionError
from platform import system as getos
from os import system
from sys import exit
from re import findall
from urllib.parse import unquote
from tqdm import tqdm


def banner():
    if getos().lower()[0] != "w":
        system("clear")
    else:
        system("cls")
    print("""
                                                              
          \033[1;31;40m+-+-+-+-+-+ 
          \033[1;32;40m|M|a|h|i|m| 
          \033[1;33;40m+-+-+-+-+-+ 
          \033[1;34;40mBy : Mazidul 
    \033[1;35;40mhttps://github.com/mahim4  
    """)
    pass


def main(url, path):
    banner()
    print("\033[1;34;40mURL :\033[1;32;40m", url,"\n")
    print("\033[1;34;40mSave As :\033[1;32;40m", path,"\n","\n\033[1;31;40mYou can setup a name by (default=url.mp4)","\n\033[1;34;40m      mdf [url] -s [file.mp4]")
    link = getdownlink(url)
    download(link, path)
    pass


def download(url, path):
    chunk = 1024  # 1kB
    r = get(url, stream=True)
    total = int(r.headers.get("content-length"))
    print("\n\033[1;34;40mVideo Size :\033[1;33;40m ", round(total / chunk, 2), "KB", end="\n\n")
    with open(path, "wb") as file:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk), total=total / chunk, unit="KB"):
            file.write(data)
        file.close()

    print("\n\033[1;32;40mDownload Complete !!!")

    pass


def getdownlink(url):
    url = url.replace("www", "mbasic")
    try:
        r = get(url, timeout=5, allow_redirects=True)
        if r.status_code != 200:
            raise HTTPError
        a = findall("/video_redirect/", r.text)
        if len(a) == 0:
            print("\033[1;31;40m[!] Video Not Found...")
            exit(0)
        else:
            return unquote(r.text.split("?src=")[1].split('"')[0])
    except (HTTPError, ConnectionError):
        print("\033[1;31;40m[x] Invalid URL")
        exit(1)
    pass


def defaultOP(url):
    data = url.split("/")
    if data[-1] == "":
        return data[-2] + ".mp4"
    else:
        return data[-1] + ".mp4"


def parse():
    global url
    global path
    parser = ArgumentParser(description="\033[2;33;40mMDN is a open source program to download facebook videos easily")
    parser.add_argument("url", help="Facebook Video URL To Download")
    parser.add_argument("-s", metavar="Optional", nargs="?", type=str, default='$random_value.mp4',
                        help="Facebook Video Name to Save As. This is an optional argument")
    args = parser.parse_args()
    url = args.url
    path = defaultOP(url)
    if args.s !='$random_value.mp4':
        path = args.s
    return url, path


def TheMain():
    args = parse()
    main(args[0], args[1])
    pass


if __name__ == '__main__':
    TheMain()
