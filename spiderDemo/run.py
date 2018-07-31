from scrapy import cmdline


name = 'download_movie'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())