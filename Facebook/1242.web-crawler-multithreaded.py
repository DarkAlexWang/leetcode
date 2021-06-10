#
# @lc app=leetcode id=1242 lang=python3
#
# [1242] Web Crawler Multithreaded
#

# @lc code=start
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
import threading
from queue import Queue
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def hostname(url):
            start = len("http://")
            i = start
            while i < len(url) and url[i] != "/":
                i += 1
            return url[start:i]

        queue = Queue()
        seen = {startUrl}
        start_hostname = hostname(startUrl)
        seen_lock = threading.Lock()

        def worker():
            while True:
                url = queue.get()
                if url is None:
                    return

                for next_url in htmlParser.getUrls(url):
                    if next_url not in seen and hostname(next_url) == start_hostname:
                        seen_lock.acquire()
                        # Acquire lock to ensure urls are no enqueed multiple
                        # times
                        if next_url not in seen:
                            seen.add(next_url)
                            queue.put(next_url)
                        seen_lock.release()

                queue.task_done()

        num_workers = 8
        workers = []
        queue.put(startUrl)

        for i in range(num_workers):
            t = threading.Thread(target=worker)
            t.start()
            workers.append(t)

        # wait until empty

        queue.join()

        for i in range(num_workers):
            queue.put(None)

        for t in workers:
            t.join()

        return list(seen)

# @lc code=end
