# import json

class DemoTestPipeline:
 
    #程序执行前第一个开始此方法，该方法是框架内置方法，方法名一定不能修改，否则会报错
    def open_spider(self,spider):
        #打开文件
        self.fp = open("book.json",'w',encoding='utf-8')
        # self.fp.write("[\n")
 
    def process_item(self, item, spider):
        #item 中就是 dytt.py 文件中 yield book 中返回的数据
        #注意 item 要转化成字符串类型，否则会报错
        curItem = str(item)
        curItem = curItem.replace("'", '"')
        curItem += '\n\n'
        self.fp.write(curItem)
        return item
 
    def closer_spider(self):
        #关闭文件
        self.fp.close()