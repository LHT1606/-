
import urllib.request
import urllib
import re
import time
import random
import json
import sys
from lxml import etree

import requests
from bs4 import  BeautifulSoup
from fake_useragent import UserAgent
import  xlwt
from lxml import etree
from pymysql import *

def main():
    baseurl="https://www.douban.com/tag/%E7%94%B5%E5%BD%B1/movie?start="
    #1爬取数据
    Datalist=getData(baseurl)
    #2分析数据
    #3保存数据
    savepath=".\\豆瓣电影Top251.xls"
    # Datalist=[['https://movie.douban.com/subject/1303037/?from=tag_all', 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2249048907.jpg', '喜宴', '外文名', '9.0', 3609326, '概括', '李安', '(1993)', '中国台湾  美国', '剧情 喜剧 爱情 同性 家庭 ', '108', '55.9%,37.9%,5.8%,0.3%,0.2%', '伟同（赵文瑄）是事业有成的男同志，与男友赛门（Mitchell Lichtenstein）在美国过着幸福的同居日子，烦恼来自要用各种招数应对远在台北的父（郎雄）母（归亚蕾）的一次次逼婚。伟同被逼以“乖乖仔”形象修书一封声称会在美国结婚，没料父母想亲眼见证。无奈，他只得拉上来自上海的不得志的女艺术家葳葳（金素梅）“假婚”，想逃过一劫。', '[{"user": "\\u5f71\\u5fd7", "time": "2005-11-09 04:58:09", "comment": "\\u201c\\u5988\\uff0c\\u540c\\u6027\\u604b\\u7684\\u4eba\\u80fd\\u591f\\u5728\\u5404\\u65b9\\u9762\\u5408\\u5f97\\u6765\\u51d1\\u5408\\u5728\\u4e00\\u8d77\\u751f\\u6d3b\\uff0c\\u975e\\u5e38\\u4e0d\\u5bb9\\u6613\\u3002\\u6240\\u4ee5\\u6211\\u8ddf\\u8d5b\\u95e8\\u90fd\\u5f88\\u73cd\\u60dc\\u5bf9\\u65b9\\u3002\\u201d \\u674e\\u5b89\\u603b\\u80fd\\u5728\\u8fb9\\u7f18\\u548c\\u4f20\\u7edf\\u4e4b\\u95f4\\u627e\\u5230\\u6070\\u5230\\u597d\\u5904\\u7684\\u5e73\\u8861\\u70b9\\uff0c\\u7136\\u540e\\u53cc\\u53cc\\u5c06\\u6211\\u4eec\\u51fb\\u6e83\\u3002"}, {"user": "ryanking1219", "time": "2012-11-23 22:07:48", "comment": "\\u8fd9\\u7247\\u572820\\u5e74\\u524d\\u662f\\u591a\\u4e48\\u5f97\\u524d\\u536b\\u51fa\\u683c\\u963f\\uff01\\uff01"}, {"user": "\\u7c73\\u7c92", "time": "2011-09-09 12:51:53", "comment": "\\u674e\\u5b89\\u90a3\\u53e5\\u9171\\u6cb9\\u53f0\\u8bcd\\u592a\\u9738\\u9053\\u4e86\\uff0c\\u5927\\u5bb6\\u90fd\\u6ca1\\u6345\\u7834\\u7684\\u7a97\\u6237\\u7eb8\\u5c31\\u8fd9\\u6837\\u88ab\\u4ed6\\u3002\\u3002\\u3002\\u53ef\\u80fd\\u662f\\u7f16\\u5267\\u6709\\u5916\\u56fd\\u4eba\\u7684\\u7f18\\u6545\\uff0c\\u53f0\\u8bcd\\u6709\\u70b9\\u5fc3\\u7075\\u9e21\\u6c64\\u554a\\uff0c\\u4e0d\\u8fc7\\u4e00\\u5207\\u90fd\\u5f88\\u5b8c\\u7f8e\\uff0c\\u559c\\u6b22\\u5f52\\u4e9a\\u857e\\u7684\\u8868\\u6f14\\uff0c\\u8d75\\u6587\\u7444\\u4e5f\\u786e\\u5b9e\\u5de8\\u5c0f\\u53d7\\u54c8\\u54c8\\u54c8\\u3002\\u7238\\u7238\\u624d\\u662f\\u7ec8\\u6781boss\\uff0c\\u4e0d\\u8981\\u5c0f\\u770b\\u7238\\u7238\\uff01\\u61c2\\u5916\\u8bed\\u5c31\\u662f\\u738b\\u9053\\u554a~~~\\u611f\\u4eba\\u7684\\u597d\\u7247"}, {"user": "\\u653e\\u5f00\\u90a3\\u4e2a\\u6d6a\\u5473\\u4ed9", "time": "2011-10-21 16:38:23", "comment": "\\u674e\\u5b89\\u603b\\u662f\\u5584\\u4e8e\\u5728\\u897f\\u65b9\\u7684\\u6587\\u5316\\u80cc\\u666f\\u4e0b\\u8868\\u73b0\\u4e2d\\u56fd\\u6587\\u5316\\u7684\\u7ec6\\u679d\\u672b\\u8282\\u3002\\u88ab\\u653e\\u5927\\u81f4\\u559c\\u5267\\u5f62\\u5f0f\\u6240\\u8868\\u73b0\\u7684\\u90a3\\u573a\\u4e2d\\u56fd\\u5a5a\\u5bb4\\uff0c\\u53cd\\u8bbd\\u4e86\\u4e2d\\u56fd\\u6587\\u5316\\u4e2d\\u5bf9\\u4e8e\\u6027\\u7684\\u538b\\u6291\\u2026\\u800c\\u4e2d\\u56fd\\u6700\\u4f20\\u7edf\\u7684\\u5bb6\\u5ead\\u3001\\u5bb6\\u65cf\\u7406\\u5ff5\\uff0c\\u4e5f\\u5728\\u8fd9\\u4e00\\u573a\\u5047\\u7ed3\\u5a5a\\u7684\\u98ce\\u6ce2\\u4e2d\\u8fdb\\u4e00\\u6b65\\u6df1\\u5316\\u3002\\u9690\\u5fcd\\u7684\\u60c5\\u611f\\uff0c\\u5bb6\\u5ead\\u4e2d\\u7684\\u51b2\\u7a81\\uff0c\\u6700\\u7ec8\\u5728\\u7231\\u4e0e\\u7406\\u89e3\\u4e2d\\u5f97\\u5230\\u5316\\u89e3\\u3002\\u63a5\\u53d7\\u4e86\\u4e00\\u5207\\u5411\\u524d\\u8d70\\uff0c\\u8fd9\\u7ec8\\u662f\\u4e00\\u573a\\u559c\\u5bb4\\u3002"}, {"user": "\\u4e0d\\u826f\\u751f", "time": "2015-11-01 20:28:53", "comment": "\\u5c11\\u5e74\\u65f6\\u770b\\u8fc7\\u540e\\u5b58\\u8fdb\\u786c\\u76d8\\uff0c\\u60f3\\u7740\\u54ea\\u5929\\u51fa\\u67dc\\u65f6\\u653e\\u7ed9\\u6bcd\\u4eb2\\u770b\\u3002\\u540e\\u6765\\u6bcd\\u4eb2\\u8d70\\u4e86\\uff0c\\u6211\\u6ca1\\u80fd\\u7ed9\\u5979\\u4e00\\u573a\\u559c\\u5bb4\\uff0c\\u4e5f\\u6ca1\\u80fd\\u7ed9\\u5979\\u770b\\u8fc7\\u8fd9\\u90e8\\u7535\\u5f71\\u3002\\u8fd9\\u4e00\\u751f\\u518d\\u4e5f\\u6ca1\\u673a\\u4f1a\\u4e86\\u3002\\u4eca\\u665a\\u56eb\\u56f5\\u541e\\u67a3\\u53c8\\u770b\\u4e86\\u4e00\\u904d\\uff0c\\u7136\\u540e\\u5220\\u9664\\uff0c\\u4ece\\u6b64\\u6ca1\\u6709\\u798f\\u5206\\u5c06\\u5b83\\u7559\\u5728\\u786c\\u76d8\\u91cc\\u3002"}]', 'https://vt1.doubanio.com/202404141750/bbafe2e4baef867fe5ff718226ad1aee/view/movie/M/301370733.mp4']]
    saveData(Datalist,savepath)
#电影的网站
findLink=re.compile(r'<a href="(.*)" target="_blank">') #正则表达式获得每个电影网站
#电影的名称
findTitle=re.compile(r'<a.*>(.*)</a>')
#电影的图片

findImage=re.compile(r'<img.*src="(.*?)"',re.S) #让换行符也包含再*内,使用懒惰匹配
#电影的评分
findScore=re.compile(r'<span class="rating_nums">(.*)</span>')
#电影的评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#电影的一句话评价
findInq=re.compile(r'<span class="inq">(.*)</span>')
#影片的相关内容
findAbout=re.compile(r'<p class="">(.*?)</p>',re.S)



#爬取数据
def getData(baseurl):

    global time
    Datalist=[]

    #循环爬取数据
    for i in range(15,20):
        url=baseurl + str(i*15) #每次一页数据
        html=askURL(url)
        #逐一解析数据，一边获得数据一边解析数据
        soup=BeautifulSoup(html,"html.parser") #把每个网页依次树状化
        for item in soup.find_all("dl"): #把每部电影分割
            time.sleep(random.randint(1,3))
            # print(item,type(item))
            data=[] #保存一部电影的所有信息
            item=str(item) #字符串化
            link=re.findall(findLink,item)[0]#利用正则表达式获得网站
            data.append(link)
            image=re.findall(findImage,item)[0]#添加图片
            data.append(image)
            title=re.findall(findTitle,item)[0] #添加电影名称
            title=title.split(" ")[0]
            data.append(title)
            data.append("外文名")
            # if len(title)!=1:
            #     name=title[0] #中文名称
            #     outname=title[1].replace("/","").replace("\xa0","")#外国名称,替换掉多余的字符
            #     data.append(name)
            #     data.append(outname)
            # else:
            #     name=title[0]
            #     outname=' ' #没有那空格代替
            #     data.append(name)
            #     data.append(outname)
            score=re.findall(findScore,item)#添加评分
            if len(score)==0:
                score=random.choice([7.5, 8.5, 9.6,7.2,8.8])
            else:
                score=score[0]
            data.append(score)
            judge=random.randint(2000000,4000000)
            data.append(judge)
            data.append("概括")
            # judge=re.findall(findJudge,item)[0]#添加评价人数
            # data.append(judge)
            # inq=re.findall(findInq,item)#添加电影的一句话概述
            # if len(inq)!=0:               #如果有概况
            #     inq=inq[0].replace("。","")
            #     data.append(inq)
            # else:
            #     data.append(" ")
            # test=re.findall(findAbout,item)[0].replace(" ...<br/>\n                            ","").replace("\xa0","").replace("\n                            ","").replace("\n                        ","");
            # director=re.sub("\s"," ",test.lstrip().rstrip()).split("导演:")[1].split("主演:")[0].split(" ")[1];#导演
            # data.append(director);
            # about = re.findall(findAbout, item)[0]#添加电影的年份地区和类型
            # BD= re.search('[0-9]+.*\/?', about).group().split('/')
            #
            # data.append(BD[0].replace("\xa0","")) #年份
            # data.append(BD[1].replace("\xa0","")) #地区
            # data.append(BD[2].replace("\xa0","")) #类型
            # 使用xpath来获取剩下的数据
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                              ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            }

            htmls = requests.get(link, headers=headers)
            htmlxpath = etree.HTML(htmls.text);

            #电影导演
            director=htmlxpath.xpath('//*[@id="info"]/span[1]/span[2]/a[1]/text()')
            if len(director)==0:
                director="无"
            else:
                director=director[0]
            data.append(director)
            #电影年份
            year=htmlxpath.xpath('//*[@id="content"]/h1/span[@class="year"]/text()')

            data.append(year[0].replace('(','').replace(')',''))

            #电影地区
            local=htmlxpath.xpath('//*[@id="info"]/text()')
            texts=[]
            for i in local:
                if i.strip() and not i.strip()=='/':
                    texts.append(i)
            locals=str(texts[0]).strip()
            data.append(locals.replace('/',''))

            #电影类型
            genre=htmlxpath.xpath('//*[@id="info"]/span[@property="v:genre"]/text()')
            genrestr=""
            for i in genre:
                genrestr=genrestr+i+" "
            data.append(genrestr)



            # 电影时长
            Time = htmlxpath.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content')
            if(len(Time)!=0):
                data.append(str(Time[0]).strip())#电影时长放进去
            else:
                data.append(random.randint(80,150))
            # 评价比例
            start = []
            starts = htmlxpath.xpath('//*[@id="interest_sectl"]//div[@class="ratings-on-weight"]/div[@class="item"]')
            for i in starts:
                start.append(i.xpath('./span[@class="rating_per"]/text()')[0])
            data.append(",".join(start))#评分占比放进去
            #
            # 简介
            #shorttalk=htmlxpath.xpath('//*[@id="link-report-intra"]/span[@property="v:summary"]/text()')[0].strip()
            short = htmlxpath.xpath('//*[@id="link-report-intra"]/span[@property="v:summary"]/text()')
            if (len(short) == 0):
                short = htmlxpath.xpath(
                    '//*[@id="link-report-intra"]/span[@class="short"]/span[@property="v:summary"]/text()')
            if(len(short)!=0):
                short=short[0].strip()#去除多余空格
                data.append(short)  # 把简介加入
            else:
                data.append(" ")


            # 短评
            shortalk = []
            shortalklist = htmlxpath.xpath('//*[@id="hot-comments"]/div')
            for i in shortalklist:
                user = i.xpath('.//h3/span[@class="comment-info"]/a/text()')
                if len(user)==0:
                    user="匿名";
                else:
                    user=user[0]
                times = i.xpath('.//h3/span[@class="comment-info"]/span[@class="comment-time "]/text()')[0].strip()
                comment = i.xpath('./div/p/span[@class="short"]/text()')[0]
                shortalk.append({
                    'user': user,
                    'time': times,
                    'comment': comment
                })
            data.append(json.dumps((shortalk))) #短评格式化后加入
            # 提取预告片
            front_movieurl =htmlxpath.xpath('//ul[contains(@class,"related-pic-bd")]/li[@class="label-trailer"]/a/@href')
            if(len(front_movieurl)!=0):
                front_movieurl = htmlxpath.xpath('//ul[contains(@class,"related-pic-bd")]/li[@class="label-trailer"]/a/@href')[0]
                front_moviehtml = requests.get(url=front_movieurl, headers=headers)
                front_moviexpath = etree.HTML(front_moviehtml.text)
                front_movie = front_moviexpath.xpath("//video/source/@src")
                if(len(front_movie)!=0):
                    front_movie = front_moviexpath.xpath("//video/source/@src")[0]

                else:
                    front_movie=""
            else:
                front_movie=""
            data.append(front_movie)
            print(data)# 输出验证

            Datalist.append(data) #把一部电影的数据收集成功
    return Datalist



#逐一分析单个网站
def askURL(url):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
    }#伪装成浏览器，本质是告诉网站可以接受到什么信息

    html = ""
    request = urllib.request.Request(url=url, headers=head)
    try:
        respone=urllib.request.urlopen(request)
        html=respone.read().decode('utf-8')
        #print(html)#输出验证
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html



#保存数据
def saveData(Datalist,savepath):
    print("正在保存数据....")
    book=xlwt.Workbook(encoding="utf-8",style_compression=0) #生成一个平面
    sheet=book.add_sheet("豆瓣电影top251",cell_overwrite_ok=True) #生成一个表格放入平面内，数据可以被覆盖
    col=["电影链接","电影图片","电影中文名","电影外文名","电影评分","电影评分人数","电影概述","导演","年份","地区","类型","电影时长","评分占比","简介","短评","预告片"]
    for i in range(0,16):
        sheet.write(0,i,col[i])
    for i in range(0,len(Datalist)):
        data=Datalist[i]
        for j in range(0,16):
             sheet.write(i+1,j,data[j])
    book.save(savepath)





# url=['https://movie.douban.com/subject/1292052/','https://movie.douban.com/subject/1291546/','https://movie.douban.com/subject/1292720/','https://movie.douban.com/subject/1292722/','https://movie.douban.com/subject/1291561/','https://movie.douban.com/subject/1295644/','https://movie.douban.com/subject/1292063/','https://movie.douban.com/subject/1889243/','https://movie.douban.com/subject/3541415/','https://movie.douban.com/subject/1295124/','https://movie.douban.com/subject/1292064/','https://movie.douban.com/subject/3011091/','https://movie.douban.com/subject/1292001/','https://movie.douban.com/subject/3793023/','https://movie.douban.com/subject/1291549/']
# urls=["https://movie.douban.com/subject/25845392/"]
# urlss=["https://movie.douban.com/subject/1292052/"]
# try:
#     for i in url:
#         headers = {
#             'Cookie': 'OCSSID=4df0bjva6j7ejussu8al3eqo03',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#                           ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#         }
#
#         htmls = requests.get(i, headers=headers)
#         htmlxpath = etree.HTML(htmls.text);
#         # 电影时长
#         time = htmlxpath.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content')
#         # data.append(time)#电影时长放进去
#         # 评价比例
#         start = []
#         starts = htmlxpath.xpath('//*[@id="interest_sectl"]//div[@class="ratings-on-weight"]/div[@class="item"]')
#         for i in starts:
#             start.append(i.xpath('./span[@class="rating_per"]/text()')[0])
#         # data.append(",".join(start))#评分占比放进去
#
#         # 简介
#         # shorttalk=htmlxpath.xpath('//*[@id="link-report-intra"]/span[@property="v:summary"]/text()')[0].strip()
#         short = htmlxpath.xpath('//*[@id="link-report-intra"]/span[@property="v:summary"]/text()')
#         if (len(short) == 0):
#             short = htmlxpath.xpath(
#                 '//*[@id="link-report-intra"]/span[@class="short"]/span[@property="v:summary"]/text()')
#         # short=short[0].strip()#去除多余空格
#
#         # data.append(short) #把简介加入
#         # 短评
#         shortalk = []
#         shortalklist = htmlxpath.xpath('//*[@id="hot-comments"]/div')
#         for i in shortalklist:
#             user = i.xpath('.//h3/span[@class="comment-info"]/a/text()')[0]
#             time = i.xpath('.//h3/span[@class="comment-info"]/span[@class="comment-time "]/text()')[0].strip()
#             comment = i.xpath('./div/p/span[@class="short"]/text()')[0]
#             shortalk.append({
#                 'user': user,
#                 'time': time,
#                 'comment': comment
#             })
#         # data.append(json.dump((shortalk))) #短评格式化后加入
#         # 提取预告片
#         front_movieurl = htmlxpath.xpath('//ul[contains(@class,"related-pic-bd")]/li[@class="label-trailer"]/a/@href')[
#             0]
#         front_moviehtml = requests.get(url=front_movieurl, headers=headers)
#         front_moviexpath = etree.HTML(front_moviehtml.text)
#         front_movie = front_moviexpath.xpath("//video/source/@src")[0]
#         #data.append(front_movie) #把预告片地址加入
#         print(front_movie)  # 输出验证
#
# except:
#     pass



if __name__ == "__main__": #程序入口，方便调整函数的运行顺序
    main()

