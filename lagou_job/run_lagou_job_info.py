from scrapy import cmdline

cmd = 'scrapy crawl lagou_job_info -s JOBDIR=crawls/somespider-1'
cmdline.execute(cmd.split(' '))