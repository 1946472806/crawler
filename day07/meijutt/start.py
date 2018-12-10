import scrapy.cmdline

#执行scrapy命令
def main():
    scrapy.cmdline.execute(['scrapy','crawl','mymeijutt'])

if __name__ == '__main__':
    main()