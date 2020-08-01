class Codec:
    longToShort = {}
    shortToLong = {}
    count = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        ans = 'http://tinyurl.com/'+str(self.count)
        self.longToShort['longUrl'] = ans
        self.shortToLong[str(self.count)] = longUrl
        self.count += 1
        return ans

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        
        return self.shortToLong[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))