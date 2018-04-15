#coding=utf-8
import urllib2
poi_file=open("sz.txt","a")
err_file=open("errs.txt","a")
read_file=open("szreaded.txt","a")
errpoidatas={}
allpoidatas={}
readpoilinks={}
poidatas = {"http://www.poi86.com/poi/city/224.html":1}
readed_file = open("szreaded.txt","r")
for lines in readed_file:
        data = lines.strip("\n")
        poidatas[data]="readed"
pagenum=0
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


urlsz="http://www.poi86.com/poi/city/224.html"
try:
        pagesz=urllib2.urlopen(urlsz)
except:
        pass
if pagesz:
        textsz=pagesz.read()
        if "警告!由于你恶意访问,您的IP已被记录!" in textsz:
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"
                print "banned!!!!!!!!"                
                sys.exit(9)
        for n in range(0,49):
                if " <li class=\"list-group-item\"><a href=" in textsz and "</a><span" in textsz:
                        textsz=textsz[textsz.index("/poi/district/")+14:]
                        textsz_1=textsz[0:textsz.index("1.html")-1]
                        print "District ID:"
                        print textsz_1
                        urlszqu="http://www.poi86.com/poi/district/"+textsz_1+"/1.html"
                        print "District WebLink:"
                        print urlszqu
                        try:
                                pageszqysy=urllib2.urlopen(urlszqu)
                                if pageszqysy:
                                        textszqysy=pageszqysy.read()
                                        if "警告!由于你恶意访问,您的IP已被记录!" in textszqysy:
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                print "banned!!!!!!!!"
                                                
                                                sys.exit(9)
                                        if "<a href=\"javascript:;\">1" in textszqysy:
                                                textszqunum=textszqysy[textszqysy.index("<a href=\"javascript:;\">1"):]
                                                textszqunum_1=textszqunum[textszqunum.index(">1/")+3:textszqunum.index("</a></li></ul>")]
                                                print "District Pages:"
                                                print textszqunum_1
                                                #  http://www.poi86.com/poi/district/1332/1.html
                                                for i in range(1,int(textszqunum_1)):
                                                        url1="http://www.poi86.com/poi/district/"+textsz_1+"/"+str(i)+".html"
                                                        if url1 in poidatas :
                                                                print "Exist Page:"
                                                                print url1
                                                                print "readed Next--->"
                                                                continue
                                                        print "District FirstPageWebLink:"                                                        
                                                        print url1
                                                        try:
                                                                page1=urllib2.urlopen(url1)
                                                        except Exception,e:
                                                                print 'openERR:'
                                                                print url1                                                               
                                                                if  "Forbidden" in str(e):
                                                                        print "banned!!!!!!!!"
                                                                        sys.exit(9)
                                                                print Exception,":",e
                                                                err_file.write(url1+'\n'+str(e)+"\n")
                                                                err_file.flush()
                                                        pass
                                                        if page1:
                                                                text1=page1.read()
                                                                if "警告!由于你恶意访问,您的IP已被记录!" in text1:
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        print "banned!!!!!!!!"
                                                                        
                                                                        sys.exit(9)
                                                                for j in range(0,49): 
                                                                        if "<td><a href=" in text1 and "</a></td>" in text1:  
                                                                                text1=text1[text1.index("<td><a href=")+1:]
                                                                                text1_1=text1[text1.index("<td><a href=")+13:]
                                                                                url2="http://www.poi86.com"+text1_1[:text1_1.index("html")+4]
                                                                                if url2 in poidatas :
                                                                                        print "Exist Page:"
                                                                                        print url2
                                                                                        print "readed Next--->"
                                                                                        continue
                                                                                if "category" in url2:
                                                                                        continue     
                                                                                print pagenum                                                                           
                                                                                print "POI page:"
                                                                                print url2
                                                                                k=j+i*50 -50
                                                                                pagenum+=1
				                                                print k
                                                                                
				                                                try:
                                                                                        page2=urllib2.urlopen(url2)
                                                                                except Exception,e:
                                                                                        print 'openERR:'
                                                                                        print url2
                                                                                        print Exception,":",e
                                                                                        if  "Forbidden" in str(e):
                                                                                                print "banned!!!!!!!!"
                                                                                                sys.exit(9)
                                                                                        err_file.write(url2+'\n'+str(e)+"\n")
                                                                                        err_file.flush()
                                                                                        pass
                                                                                        continue
                                                                                try:
                                                                                        if page2:
                                                                                                text2=page2.read()
                                                                                                if "警告!由于你恶意访问,您的IP已被记录!" in text2:
                                                                                                        print "banned!!!!!!!!"
                                                                                                if "火星坐标" in text2 and "百度坐标" in text2:
                                                                                                        text2=text2[text2.index("火星坐标"):text2.index("百度坐标")]
                                                                                                if "</span>" in text2 and "</li>" in text2:
                                                                                                        poi=text2[text2.index("</span>")+8:text2.index("</li>")]+"\n"
                                                                                                        poi_file.write(poi)
                                                                                                        print poi
                                                                                                        poi_file.flush()
                                                                                                        poidatas[url2]="readed"
                                                                                                        read_file.write(url2+"\n")
                                                                                                        read_file.flush()
                                                                                except Exception,e:
                                                                                        print 'saveERR:'
                                                                                        print e.message
                                                                                        err_file.write(url2+'\n'+str(e)+"\n")
                                                                                        err_file.flush()
                                                                                        if  "Forbidden" in str(e):
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                print "banned!!!!!!!!"
                                                                                                
                                                                                                sys.exit(9)
                                                                                        pass	
                                                                                        continue
                                                        poidatas[url1]="readed"
                                                        read_file.write(url1+"\n")
                                                        read_file.flush()
			except:
                                if  "Forbidden" in str(e):
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        print "banned!!!!!!!!"
                                        err_file.write(urlszqu+'\n'+str(e)+"\n")
                                        err_file.flush()
                                print str(e)
                                err_file.write(urlszqu+'\n'+str(e)+"\n")
                                err_file.flush()
                                pass			
poi_file.close()
err_file.close()
read_file.close()