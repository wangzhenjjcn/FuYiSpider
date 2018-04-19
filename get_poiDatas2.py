#coding=utf-8
import urllib2,sys,time,datetime,os,pymysql.cursors
read_file=open("szreadedpoi2.txt","a")
errpoidatas={}
allpoidatas={}
readpoilinks={}
poidatas = {}
poiids_file = open("poiid2.txt","r")
connection = pymysql.connect(host='127.0.0.1', port=3306, user='test', password='test', db='poi', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


for lines in poiids_file:
        data = lines.strip("\n")
        if ":" in data or "--" in data:
                pass
        else:
                allpoidatas[data]=""
                pass
readed_file = open("szreadedpoi2.txt","r")
for lines in readed_file:
        data = lines.strip("\n")
        poidatas[data]="readed"
pagenum=0
hdr = {
        'Host':"www.poi86.com",
       'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
       'Connection': 'keep-alive'
       }
alldatanum=len (allpoidatas)-1

for key in allpoidatas:
          
        poiPageUrl="http://www.poi86.com/poi/"+key+".html"
        if poiPageUrl in poidatas :
                print "Exist Page:"
                print poiPageUrl
                print "readed Next--->"
                pass
                continue
        try:
                print "POI page:", poiPageUrl
                poiPageInfo=urllib2.urlopen(poiPageUrl)        
        except Exception,e:
                print 'openERR:'
                print poiPageUrl
                print str(e)
                if  "Forbidden" in str(e):
                        for n in range(0,10):
                                print "banned!!!!!!!!"   
                                                                                                                    
                         
                        sys.exit(9)
                
                pass
                continue
        try:   
                if poiPageInfo:
                        poiPageDetial=poiPageInfo.read()                                                                                                       
                        if "警告!由于你恶意访问,您的IP已被记录!" in poiPageDetial:
                                for n in range(0,10):
                                        print "banned!!!!!!!!"
                                 
                                 
                                        
                                sys.exit(9)
                        
                        else:
                                id= int(key)
                                name= poiPageDetial[poiPageDetial.index("<h1>")+4:poiPageDetial.index("</h1>")].strip("\n").strip("\"").strip("\\").replace("\'","\\\'").strip(";")

                                poiPageDetial=poiPageDetial[poiPageDetial.index("所属省份"):]
                                poiPageDetial=poiPageDetial[poiPageDetial.index("<a")+1:]
                                province=poiPageDetial[poiPageDetial.index(">")+1:poiPageDetial.index("</a>")].strip("\n").strip("\"").strip(";")
                                if ">" in province:
                                        province=province[province.index(">")+1:]


                                poiPageDetial=poiPageDetial[poiPageDetial.index("所属城市"):]
                                poiPageDetial=poiPageDetial[poiPageDetial.index("<a")+1:]
                                city=poiPageDetial[poiPageDetial.index(">")+1:poiPageDetial.index("</a>")].strip("\n").strip("\"").strip(";")
                                if ">" in city:
                                        city=city[city.index(">")+1:]

                                poiPageDetial=poiPageDetial[poiPageDetial.index("所属区县"):]
                                poiPageDetial=poiPageDetial[poiPageDetial.index("<a")+1:]
                                district=poiPageDetial[poiPageDetial.index(">")+1:poiPageDetial.index("</a>")].strip("\n").strip("\"").strip(";")
                                if ">" in district:
                                        district=district[district.index(">")+1:]

                                poiPageDetial=poiPageDetial[poiPageDetial.index("详细地址"):]
                                address=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")].strip("\n").strip("\"").strip("\\").replace("\'","\\\'").strip(";")
                                
                                poiPageDetial=poiPageDetial[poiPageDetial.index("电话号码"):]
                                phone=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")].strip("\n").strip("\"").strip(";")

                                poiPageDetial=poiPageDetial[poiPageDetial.index("所属分类"):]
                                poiPageDetial=poiPageDetial[poiPageDetial.index("a"):]
                                sort=poiPageDetial[poiPageDetial.index(">")+1:poiPageDetial.index("</a>")].strip("\n").strip("\"").strip(";")
                                if ">" in sort:
                                        sort=sort[sort.index(">")+1:]
                                        if ">" in sort:
                                                predata=sort[:sort.index("<")]
                                                offdata=sort[sort.index(">")+1:]
                                                sort=predata+offdata
                                                if ">" in sort:
                                                        predata=sort[:sort.index("<")]
                                                        offdata=sort[sort.index(">")+1:]
                                                        sort=predata+offdata

                                poiPageDetial=poiPageDetial[poiPageDetial.index("所属标签"):]
                                poiPageDetial=poiPageDetial[poiPageDetial.index("a"):]
                                tag=poiPageDetial[poiPageDetial.index(">")+1:poiPageDetial.index("</a>")].strip("\n").strip("\"")
                                if ">" in tag:
                                        tag=tag[tag.index(">")+1:]
                                        if ">" in tag:
                                                predata=tag[:tag.index("<")]
                                                offdata=tag[tag.index(">")+1:]
                                                tag=predata+offdata
                                                if ">" in tag:
                                                        predata=tag[:tag.index("<")]
                                                        offdata=tag[tag.index(">")+1:]
                                                        tag=predata+offdata


                                poiPageDetial=poiPageDetial[poiPageDetial.index("大地坐标"):]
                                earthGPS=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")].strip("\n").strip("\"")

                                poiPageDetial=poiPageDetial[poiPageDetial.index("火星坐标"):]
                                marsGPS=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")].strip("\n").strip("\"")
                                
                                poiPageDetial=poiPageDetial[poiPageDetial.index("百度坐标"):]
                                baiduGPS=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")].strip("\n").strip("\"")
                                
                                 
                                sqlValues="\'"+key+"\',\'"+name+"\',\'"+province+"\',\'"+ city+"\',\'"+district+"\',\'"+ address+"\',\'"+phone +"\',\'"+ sort +"\',\'"+ tag +"\',\'"+ earthGPS+"\',\'"+ marsGPS+"\',\'"+ baiduGPS+"\'"
                                sql ="INSERT INTO `data2` (`id`, `name`, `province`, `city`, `district`, `address`, `phone`, `sort`, `tag`, `earthGPS`, `marsGPS`, `baiduGPS`) VALUES (" + sqlValues+ ")"
                                try:
                                        cursor.execute(sql)
                                        connection.commit()
                                except Exception,e:
                                       
                                        print "sql err"
                                        print str(e)
                                        pass
                                        continue
                                try:
                                        poidatas[poiPageUrl]=sqlValues
                                        read_file.write(poiPageUrl+"\n")
                                        read_file.flush()    
                                except Exception,e:
                                        
                                        print "save err"
                                        print str(e)
                                        pass
                                        continue                                                                                                 
        except Exception,e:
                print 'saveERR:'
                print str(e)
               
                if  "Forbidden" in str(e):
                        for n in range(0,10):
                                print "banned!!!!!!!!"
                         
                         
                         
                        sys.exit(9)
                pass	
                continue
db.close()     
read_file.close()


for n in range(0,20):
        print "finished!!!!!!!!"
 