#coding=utf-8
import weibo
import json

# APP_KEY = ''
APP_KEY =raw_input("input the APP_KEY(check at http://open.weibo.com/apps/   you can change this code yourself): ")
# APP_SECRET = ''
APP_SECRET = raw_input("input the APP_SECRET (check at http://open.weibo.com/apps/): ")
# CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
CALL_BACK =raw_input("input the CALL_BACK address (if dont know,you can use this :https://api.weibo.com/oauth2/default.html) : ")
def run():
        client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)
        auth_url = client.get_authorize_url()
        print "auth_url : " + auth_url
        # code = " "
        code = raw_input("input the retured code : ")
        r = client.request_access_token(code)
        client.set_access_token(r.access_token, r.expires_in)
        poiFile = open("poi.txt","r")
        poiResaultFile = open("checkInNum.txt","a")
        cache = []
        for lines in poiFile:
                try:
                        checkin_num = 0
                        title = None
                        lat_long = lines.strip("\n").split(",")
                        longitude = lat_long[0]
                        latitude = lat_long[1]
                        poi_result = str(client.place.nearby.pois.get(lat=latitude,long=longitude))
                        poi_list = eval(poi_result)
                        poi_string = json.dumps(poi_list)
                        poi_json = json.loads(poi_string)
                        for i in range(0,len(poi_json["pois"])):
                                if poi_json["pois"][i]["poiid"] in cache:
                                        pass
                                else:
                                        poi_id = poi_json["pois"][i]["poiid"]
                                        cache.append(poi_id)
                                        checkin_result=str(client.place.pois.show.get(poiid=poi_id))
                                        checkin_list = eval(checkin_result)
                                        checkin_string = json.dumps(checkin_list)
                                        checkin_json = json.loads(checkin_string)
                                        checkin_num = checkin_json["checkin_num"]#签到数
                                        lon = checkin_json["lon"]#经度
                                        lat = checkin_json["lat"]#纬度
                                        title = checkin_json["title"]#地点名称
                                        if checkin_num !=0 and title != None:
                                                print lon,lat,checkin_num,title
                                                poiResaultFile.write(lon,lat,checkin_num,title+"\n")
                                                poiResaultFile.flush()
                except Exception,e:
                    print str(e)
                    pass

if __name__ == "__main__":
        run()
