# Scrapy settings for megafon_phones project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'megafon_phones'

SPIDER_MODULES = ['megafon_phones.spiders']
NEWSPIDER_MODULE = 'megafon_phones.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'catalog (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)'

ITEM_PIPELINES = {
    'megafon_phones.pipelines.PhonePipeline': 500,
}
