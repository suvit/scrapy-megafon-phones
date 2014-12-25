# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class PhonePipeline(object):
    def __init__(self):
        self.file = None

    def create_exporter(self, spider):
        file = open('%s_data.txt' % spider.name, 'w+b')
        self.file = file

    def process_item(self, item, spider):
        if self.file is None:
            self.create_exporter(spider)

        datafile = self.file
        datafile.write(item['phone'])
        datafile.write('\n')
        return item

    def close_spider(self, spider):
        self.file.close()

