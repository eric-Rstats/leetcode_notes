#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
K1, K2 = 1117, 10**9 + 7


class Codec:
    def __init__(self):
        self.dataBase = {}
        self.urlToKey = {}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.urlToKey:
            return "http://tinyurl.com/" + str(self.urlToKey[longUrl])
        key, base = 0, 1
        for c in longUrl:
            key = (key + ord(c) * base) % K2
            base = (base * K1) % K2
        while key in self.dataBase:
            key = (key + 1) % K2
        self.dataBase[key] = longUrl
        self.urlToKey[longUrl] = key
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        i = shortUrl.rfind("/")
        key = int(shortUrl[i + 1 :])
        return self.dataBase[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
