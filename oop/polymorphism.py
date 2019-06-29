class News(object):

    def news_all(self):
        print("Online news")
        print("Offline news")


class MyNews(object):

    def news(self, n):
        n.news_all()


_news = News()
_my_news = MyNews()

_my_news.news(_news)
