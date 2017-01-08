import scrapy


class QuotesSpider(scrapy.Spider):
    """Creates a spider that will crawl and scrape your named urls.
    name is the name of your spider. It must be unique."""

    name = "quotes"

    def start_requests(self):
        """Makes the initial request to the page you want to scrape.
        Returns an iterable of Requests, which the Spider can crawl.
        More requests will be generated successively from initial requests."""
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        for url in urls:
            """For each url you're sending the spider to, make a request.
            Run parse() on the response object you get back."""
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """Parses the response object and extracts data as dicts.
        Saves the response body in a txt file.
        Name of txt file is generated by the page number in the url."""
        page = response.url.split("/")[-2]
        filename = 'quotes-{}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log("Saved file {}".format(filename))
