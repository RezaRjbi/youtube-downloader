import requests
from bs4 import BeautifulSoup
import youtube_dl


def aparat_link_finder(pagelink):
    res = requests.get(pagelink)
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.select(".menu-item-link.link")
    a_tags = list(map(lambda x: x.select("a"), links))
    download_links = list(map(lambda x: x[0]["href"], a_tags))
    return download_links


def aparat_dl(link):
    file = requests.get(aparat_link_finder(link)[0])
    f_ext = aparat_link_finder(link)[0].split(".")[-1]
    with open(f"aparat-video.{f_ext}", "wb") as output:
        output.write(file.content)


def yt_link_finder(pagelink):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

    with ydl:
        try:
            result = ydl.extract_info(pagelink, download=False, )
            return result["formats"]
        except:
            return "check your link again!"


def yt_q_checker(pagelink, quality="144p"):
    all_formats = yt_link_finder(pagelink)
    if isinstance(all_formats, list):
        for fn in all_formats:
            if fn["format_note"] == quality:
                return (fn['url'], fn["ext"])
                break
        return (None, f"this video doesnt have a {quality} version. chose something else")

    return all_formats


def yt_download(pagelink, quality):
    url, ext = yt_q_checker(pagelink, quality)
    try:
        res = requests.get(url)
    except:
        return None
    else:
        with open(f"yt-video.{ext}", "wb") as output:
            output.write(res.content)
