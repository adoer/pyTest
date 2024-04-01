import scrapy
 
 
class DemoTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #定义好数据结构
    name = scrapy.Field()   #书名
    author = scrapy.Field() #作者
    imgSrc = scrapy.Field() #图片
    price = scrapy.Field()  #价格
    index = scrapy.Field()  #索引
    length = scrapy.Field()  #长度
    pass