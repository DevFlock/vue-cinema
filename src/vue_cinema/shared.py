from urllib import parse


class VueURL:
    def __init__(self, url) -> None:
        if url.startswith("/-/"):
            self.url = "https://www.myvue.com" + url
        elif url.startswith("//"):
            self.url = "https://" + url[2::]
        elif url.startswith("https://") or url.startswith("http://"):
            self.url = url
        elif url.startswith("/film"):
            self.url = "https://www.myvue.com" + url
        else:
            self.url = None

        if self.url:
            self.url = parse.quote(self.url, safe="%/:=&?~#+!$,;'@()*[]")

    def __str__(self) -> str:
        return self.url
