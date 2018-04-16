#coding=utf-8
import urllib2,sys
poi_file=open("sz3.txt","a")
err_file=open("errs3.txt","a")
read_file=open("szreaded3.txt","a")
errpoidatas={}
allpoidatas={}
readpoilinks={}
poidatas = {"http://www.poi86.com/poi/city/224.html":1}
readed_file = open("szreaded3.txt","r")
for lines in readed_file:
        data = lines.strip("\n")
        poidatas[data]="readed"
pagenum=0
hdr = {
       'user-agent': "Mozilla/5.0 (Wi ndows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'deflate',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
       }
 

try:
        urlsz="http://www.poi86.com/poi/city/224.html"
        pagesz=urllib2.urlopen(urlsz)
except Exception,e:
        if  "Forbidden" in str(e):
                for n in range(0,10):
                        print "banned!!!!!!!!"
                err_file.write(urlsz+'\n'+str(e)+"\n")
                err_file.flush()
                sys.exit(9)
        print str(e)
        err_file.write(districtUrl+'\n'+str(e)+"\n")
        err_file.flush()
        pass
                                        
else:
        if pagesz:
                cityPageDetial=pagesz.read()
                if "警告!由于你恶意访问,您的IP已被记录!" in cityPageDetial:
                        for n in range(0,10):
                                print "banned!!!!!!!!"               
                        sys.exit(9)
                for n in range(0,49):
                        if " <li class=\"list-group-item\"><a href=" in cityPageDetial and "</a><span" in cityPageDetial:
                                cityPageDetial=cityPageDetial[cityPageDetial.index("/poi/district/")+14:]
                                districtIdString=cityPageDetial[0:cityPageDetial.index("1.html")-1]
                                print "District ID:"
                                print districtIdString
                                intdis=int(districtIdString)
                                if intdis <2700:
                                        continue
                                districtUrl="http://www.poi86.com/poi/district/"+districtIdString+"/1.html"
                                print "District WebLink:"
                                print districtUrl
                                try:
                                        districtPage=urllib2.urlopen(districtUrl)
                                        if districtPage:
                                                cityPageInfo=districtPage.read()
                                                if "警告!由于你恶意访问,您的IP已被记录!" in cityPageInfo:
                                                        for n in range(0,10):
                                                                print "banned!!!!!!!!"
                                                        sys.exit(9)
                                                if "<a href=\"javascript:;\">1" in cityPageInfo:
                                                        districtPageNumInfo=cityPageInfo[cityPageInfo.index("<a href=\"javascript:;\">1"):]
                                                        districtPageNumString=districtPageNumInfo[districtPageNumInfo.index(">1/")+3:districtPageNumInfo.index("</a></li></ul>")]
                                                        print "District Pages:"
                                                        print districtPageNumString
                                                        #  http://www.poi86.com/poi/district/1332/1.html
                                                        for i in range(1,int(districtPageNumString)):
                                                                districtPagesUrl="http://www.poi86.com/poi/district/"+districtIdString+"/"+str(i)+".html"
                                                                if districtPagesUrl in poidatas :
                                                                        print "Exist Page:"
                                                                        print districtPagesUrl
                                                                        print "readed Next--->"
                                                                        continue
                                                                print "District PageWebLink:"                                                        
                                                                print districtPagesUrl
                                                                try:
                                                                        districtPagesUrlPage=urllib2.urlopen(districtPagesUrl)
                                                                except Exception,e:
                                                                        print 'openERR:'
                                                                        print districtPagesUrl                                                               
                                                                        if  "Forbidden" in str(e):
                                                                                print "banned!!!!!!!!"
                                                                                sys.exit(9)
                                                                        print Exception,":",e
                                                                        err_file.write(districtPagesUrl+'\n'+str(e)+"\n")
                                                                        err_file.flush()
                                                                pass
                                                                if districtPagesUrlPage:
                                                                        districtPagesUrlPageText=districtPagesUrlPage.read()
                                                                        if "警告!由于你恶意访问,您的IP已被记录!" in districtPagesUrlPageText:
                                                                                for n in range(0,10):
                                                                                        print "banned!!!!!!!!"
                                                                                sys.exit(9)
                                                                        for j in range(0,49): 
                                                                                if "<td><a href=" in districtPagesUrlPageText and "</a></td>" in districtPagesUrlPageText:  
                                                                                        districtPagesUrlPageText=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+1:]
                                                                                        poiPageId=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+13:]
                                                                                        poiPageUrl="http://www.poi86.com"+poiPageId[:poiPageId.index("html")+4]
                                                                                        if poiPageUrl in poidatas :
                                                                                                print "Exist Page:"
                                                                                                print poiPageUrl
                                                                                                print "readed Next--->"
                                                                                                continue
                                                                                        if "category" in poiPageUrl:
                                                                                                continue     
                                                                                        print "No: " , len (poidatas)                                                                        
                                                                                        print "POI page:", poiPageUrl
                                                                                        pagenum+=1
                                                                                        try:
                                                                                                poiPageInfo=urllib2.urlopen(poiPageUrl)
                                                                                        except Exception,e:
                                                                                                print 'openERR:'
                                                                                                print poiPageUrl
                                                                                                print Exception,":",e
                                                                                                if  "Forbidden" in str(e):
                                                                                                        for n in range(0,10):
                                                                                                                print "banned!!!!!!!!"                                                                                       
                                                                                                        sys.exit(9)
                                                                                                err_file.write(poiPageUrl+'\n'+str(e)+"\n")
                                                                                                err_file.flush()
                                                                                                pass
                                                                                                continue
                                                                                        try:
                                                                                                if poiPageInfo:
                                                                                                        poiPageDetial=poiPageInfo.read()
                                                                                                        if "警告!由于你恶意访问,您的IP已被记录!" in poiPageDetial:
                                                                                                                for n in range(0,10):
                                                                                                                        print "banned!!!!!!!!"
                                                                                                                sys.exit(9)
                                                                                                        if "火星坐标" in poiPageDetial and "百度坐标" in poiPageDetial:
                                                                                                                poiPageDetial=poiPageDetial[poiPageDetial.index("火星坐标"):poiPageDetial.index("百度坐标")]
                                                                                                        if "</span>" in poiPageDetial and "</li>" in poiPageDetial:
                                                                                                                poi=poiPageDetial[poiPageDetial.index("</span>")+8:poiPageDetial.index("</li>")]+"\n"
                                                                                                                poi_file.write(poi)
                                                                                                                poi_file.flush()
                                                                                                                print "POI:   ", poi
                                                                                                                poidatas[poiPageUrl]=poi
                                                                                                                read_file.write(poiPageUrl+"\n")
                                                                                                                read_file.flush()
                                                                                        except Exception,e:
                                                                                                print 'saveERR:'
                                                                                                print e.message
                                                                                                err_file.write(poiPageUrl+'\n'+str(e)+"\n")
                                                                                                err_file.flush()
                                                                                                if  "Forbidden" in str(e):
                                                                                                        for n in range(0,10):
                                                                                                                print "banned!!!!!!!!"
                                                                                                        sys.exit(9)
                                                                                                pass	
                                                                                                continue
                                                                poidatas[districtPagesUrl]="readed"
                                                                read_file.write(districtPagesUrl+"\n")
                                                                read_file.flush()
                                except Exception,e:
                                        if  "Forbidden" in str(e):
                                                for n in range(0,10):
                                                        print "banned!!!!!!!!"
                                                err_file.write(districtUrl+'\n'+str(e)+"\n")
                                                err_file.flush()
                                                sys.exit(9)
                                        print str(e)
                                        err_file.write(districtUrl+'\n'+str(e)+"\n")
                                        err_file.flush()
                                        
                                        pass			
poi_file.close()
err_file.close()
read_file.close()