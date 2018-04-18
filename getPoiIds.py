#coding=utf-8
import urllib2,sys,time,datetime,os
poiid_file=open("poiid.txt","a")
err_file=open("iderrs.txt","a")
read_file=open("szidreaded.txt","a")
errpoidatas={}
allpoidatas={}
readpoilinks={}
poidatas = {}
readed_file = open("szidreaded.txt","r")
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
 

try:
        urlsz="http://www.poi86.com/poi/city/224.html"
        pagesz=urllib2.urlopen(urlsz)
except Exception,e:
        if  "Forbidden" in str(e):
                for n in range(0,10):
                        print "banned!!!!!!!!"
                err_file.write(urlsz+'\n'+str(e)+"\n")
                err_file.flush()
                os.system("run_szidReader.bat")
        sys.exit(9)
        print str(e)
        err_file.write(urlsz+'\n'+str(e)+"\n")
        err_file.flush()
        pass
                                        
else:
        if pagesz:
                cityPageDetial=pagesz.read()
                if "警告!由于你恶意访问,您的IP已被记录!" in cityPageDetial:
                        for n in range(0,10):
                                print "banned!!!!!!!!"  
                        os.system("run_szidReader.bat")             
                        sys.exit(9)
                for n in range(0,49):
                        if " <li class=\"list-group-item\"><a href=" in cityPageDetial and "</a><span" in cityPageDetial:
                                cityPageDetial=cityPageDetial[cityPageDetial.index("/poi/district/")+14:]
                                districtIdString=cityPageDetial[0:cityPageDetial.index(".html")-2]
                                print "District ID:"
                                print districtIdString
                                intdis=int(districtIdString)
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
                                                        os.system("run_szidReader.bat")
                                                        sys.exit(9)
                                                if "<a href=\"javascript:;\">1" in cityPageInfo:
                                                        districtPageNumInfo=cityPageInfo[cityPageInfo.index("<a href=\"javascript:;\">1"):]
                                                        districtPageNumString=districtPageNumInfo[districtPageNumInfo.index(">1/")+3:districtPageNumInfo.index("</a></li></ul>")]
                                                        #  http://www.poi86.com/poi/district/1332/1.html
                                                        poiid_file.write("----district:"+districtIdString+"\n")
                                                        poiid_file.flush()
                                                        read_file.write("----district:"+districtIdString+"\n")
                                                        read_file.flush()
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
                                                                                for n in range(0,10):
                                                                                        print "banned!!!!!!!!"
                                                                        os.system("run_szidReader.bat")
                                                                        sys.exit(9)
                                                                        print str(e)
                                                                        err_file.write(districtPagesUrl+'\n'+str(e)+"\n")
                                                                        err_file.flush()
                                                                        pass
                                                                        continue
                                                                
                                                                if districtPagesUrlPage:
                                                                        districtPagesUrlPageText=districtPagesUrlPage.read()
                                                                        if "警告!由于你恶意访问,您的IP已被记录!" in districtPagesUrlPageText:
                                                                                for n in range(0,10):
                                                                                        print "banned!!!!!!!!"
                                                                                os.system("run_szidReader.bat")
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
                                                                                                print "-----errklink:" +  poiPageUrl
                                                                                                districtPagesUrlPageText=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+1:]
                                                                                                poiPageId=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+13:]
                                                                                                poiPageUrl="http://www.poi86.com"+poiPageId[:poiPageId.index("html")+4]                                                                                                
                                                                                                if "category" in poiPageUrl:
                                                                                                        print "----------errklink:" +  poiPageUrl
                                                                                                        districtPagesUrlPageText=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+1:]
                                                                                                        poiPageId=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+13:]
                                                                                                        poiPageUrl="http://www.poi86.com"+poiPageId[:poiPageId.index("html")+4]
                                                                                                        if "category" in poiPageUrl:
                                                                                                                print "---------------errklink:" +  poiPageUrl
                                                                                                                districtPagesUrlPageText=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+1:]
                                                                                                                poiPageId=districtPagesUrlPageText[districtPagesUrlPageText.index("<td><a href=")+13:]
                                                                                                                poiPageUrl="http://www.poi86.com"+poiPageId[:poiPageId.index("html")+4]
                                                                                                print "-----right:" + poiPageUrl         
                                                                                        print "No: " , len (poidatas)
                                                                                        pagenum+=1
                                                                                        if poiPageUrl  in poidatas:
                                                                                                continue;
                                                                                        try:   
                                                                                                poiid_file.write(poiPageId[poiPageId.index("/poi/")+5:poiPageId.index("html")-1]+"\n")
                                                                                                poiid_file.flush()                                                                                                
                                                                                                poidatas[poiPageUrl]=poiPageId[poiPageId.index("/poi/")+5:poiPageId.index("html")-1]
                                                                                                read_file.write(poiPageUrl+"\n")
                                                                                                read_file.flush()
                                                                                        except Exception,e:
                                                                                                print 'openERR:'
                                                                                                print poiPageUrl
                                                                                                print str(e)
                                                                                                if  "Forbidden" in str(e):
                                                                                                        for n in range(0,10):
                                                                                                                print "banned!!!!!!!!"                                                                                       
                                                                                                        os.system("run_szidReader.bat")
                                                                                                        sys.exit(9)
                                                                                                err_file.write(poiPageUrl+'\n'+str(e)+"\n")
                                                                                                err_file.flush()
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
                                                os.system("run_szidReader.bat")
                                                sys.exit(9)
                                        print str(e)
                                        err_file.write(districtUrl+'\n'+str(e)+"\n")
                                        err_file.flush()
                                        pass			
poiid_file.close()
err_file.close()
read_file.close()

for n in range(0,100):
        print "finished!!!!!!!!"

os.system("run_szidReader.bat")