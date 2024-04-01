import scrapy
import json
 
 
class DyttSpider(scrapy.Spider):
    name = 'dytt'
    #链接范围，不在该范围内的url请求，都会报错，一般只写域名
    allowed_domains = ['e.dangdang.com']
    #执行文件请求的url，也就是我们创建文件的是给的url，
    #但是又不懂是不是，这是因为框架内部的原因弄的，大家不用在意，把刚才的url重新复制在里面就可以了。
    #改一下strat 和 end 这两个是前面提过的 strat=0  和 end=20
    #   意思也就是从索引0开始，一直到索引20，也就是21本书
    start_urls = ['http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20220424124301850188613824148624365&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=0&end=20&category=QCWX&dimension=dd_sale&order=0']
 
    def parse(self, response):
 
 
        json_list = json.loads(response.text)
        #  json_list['data']['saleList']  获取每一本书的信息
        json_list = json_list['data']['saleList']
        json_list_length= len(json_list)
        for index, element in enumerate(json_list): #遍历每一本书 获取其中需要的数据
            author = element['mediaList'][0]["authorPenname"]
            imgSrc = element['mediaList'][0]["coverPic"]
            name = element['mediaList'][0]["title"]
            price =element['mediaList'][0]["lowestPrice"]
            #导入items.py 中的类 也就是我们刚刚定义好的数据结构 会定义成一个字典格式的数据结构
            from ..items import DemoTestItem
            book = DemoTestItem(author=author,imgSrc=imgSrc,name=name,price=price,index=index,length=json_list_length)

            #把数据交给管道  piplines.py  进行数据的下载
            yield book