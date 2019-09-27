# -*- coding: utf-8 -*-
import re
import requests
import json
p1=r'\d{11}'
p2=r'^((河北|山西|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾)省?)|((内蒙古|广西(壮族)?|西藏|宁夏(回族)?|新疆(维吾尔)?)(自治区)?)|((北京|天津|上海|重庆))'
p3=r'((石家庄|张家口|承德|唐山|秦皇岛|廊坊|保定|沧州|衡水|邢台|邯郸|太原|大同|朔州|忻州|阳泉|晋中|吕梁|长治|临汾|晋城|运城|呼和浩特|呼伦贝尔|通辽|赤峰|巴彦淖尔|乌兰察布|包头|鄂尔多斯|乌海|哈尔滨|黑河|伊春|齐齐哈尔|鹤岗|佳木斯|双鸭山|绥化|大庆|七台河|鸡西|牡丹江|长春|白城|松原|吉林|四平|辽源|白山|通化|沈阳|铁岭|阜新|抚顺|朝阳|本溪|辽阳|鞍山|盘锦|锦州|葫芦岛|营口|丹东|大连|南京|连云港|徐州|宿迁|淮安|盐城|泰州|扬州|镇江|南通|常州|无锡|苏州|杭州|湖州|嘉兴|绍兴|舟山|宁波|金华|衢州|台州|丽水|温州|合肥|淮北|亳州|宿州|蚌埠|阜阳|淮南|滁州|六安|马鞍山|芜湖|宣城|铜陵|池州|安庆|黄山|福州|宁德|南平|三明|莆田|龙岩|泉州|漳州|厦门|南昌|九江|景德镇|上饶|鹰潭|抚州|新余|宜春|萍乡|吉安|赣州|济南|德州|滨州|东营|烟台|威海|淄博|潍坊|聊城|泰安|莱芜|青岛|日照|济宁|菏泽|临沂|枣庄|郑州|安阳|鹤壁|濮阳|新乡|焦作|三门峡|开封|洛阳|商丘|许昌|平顶山|周口|漯河|南阳|驻马店|信阳|武汉|十堰|襄樊|随州|荆门|孝感|宜昌|黄冈|鄂州|荆州|黄石|咸宁|长沙|岳阳|张家界|常德|益阳|湘潭|株洲|娄底|怀化|邵阳|衡阳|永州|郴州|广州|韶关|梅州|河源|清远|潮州|揭阳|汕头|肇庆|惠州|佛山|东莞|云浮|汕尾|江门|中山|深圳|珠海|阳江|茂名|湛江|南宁|桂林|河池|贺州|柳州|百色|来宾|梧州|贵港|玉林|崇左|钦州|防城港|北海|海口|三亚|三沙|儋州|成都|广元|巴中|绵阳|德阳|达州|南充|遂宁|广安|资阳|眉山|雅安|内江|乐山|自贡|泸州|宜宾|攀枝花|贵阳|遵义|六盘水|安顺|铜仁|毕节|昆明|昭通|丽江|曲靖|保山|玉溪|临沧|普洱|拉萨|日喀则|昌都|林芝|山南|那曲|西安|榆林|延安|铜川|渭南|宝鸡|咸阳|商洛|汉中|安康|兰州|嘉峪关|酒泉|张掖|金昌|武威|白银|庆阳|平凉|定西|天水|陇南|西宁|海东|银川|石嘴山|吴忠|中卫|固原|乌鲁木齐|克拉玛依|吐鲁番|哈密)市?|上海市|重庆市|北京市|天津市|自治州)'
p4=r'(市|县|区)'
p5=r'(镇|街道|乡)'
p6=r'(路|街|巷|委会|道)'
p7=r'((\d+)?-?(\d+)号)'
p8=r'(,)'
p9=r'(省)'
p10=r'(市)'
p11=r'(镇|街道|乡|\d+)'
p12=r'\d+'
p13=r'\d+.?\d+,\d+.?\d+'
s=input()
match=re.search(p1,s,re.A)
tel=match.group()
s=s[:match.start()]+s[match.end():]
s0=s[0:1]
s=s[2:]
s=s.strip()
s=s.strip('.')
match=re.search(p8,s,re.A)
name=s[:match.start()]
s=s[match.end():]
s9=s
match=re.search(p2,s[:9],re.A)
if (match==None)or(s[match.end()]=='市'):
    s1=''
elif (match.group()=='内蒙古')or(match.group()=='西藏'):
    s1=match.group()+'自治区'
elif match.group()=='宁夏':
    s1=match.group()+'回族自治区'
elif match.group()=='广西':
    s1=match.group()+'回族自治区'
elif match.group()=='新疆':
    s1=match.group()+'维吾尔自治区'
elif (match.group()=='北京')or(match.group()=='上海')or(match.group()=='天津')or(match.group()=='重庆')or(match.group()=='广西壮族自治区')or(match.group()=='宁夏回族自治区')or(match.group()=='新疆维吾尔自治区')or(match.group()=='内蒙古自治区')or(match.group()=='西藏自治区'):
    s1=match.group()
elif re.search(p9,match.group(),re.A)==None:
    s1=match.group()+'省'
else:
    s1=match.group()
if (match!=None) and(s[match.end()]!='市'):
    s=s[match.end():]
match=re.search(p3,s,re.A)
if match==None:
    s2=''
elif match.group()=='自治州':
    s2=s[:match.end()]
elif re.search(p10,match.group(),re.A)==None:
    s2=match.group()+'市'
else:
    s2=match.group()
if match!=None:
    s=s[match.end():]
if (s1=='上海')or(s1=='北京')or(s1=='天津')or(s1=='重庆'):
    s2=s1+'市'
if(s2=='上海市')or(s2=='北京市')or(s2=='天津市')or(s2=='重庆市'):
    s1=s2[0:2]
match=re.search(p4,s,re.A)
if (match==None )or (re.search(p11,s[:match.end()],re.A)!=None):
    s3=''
else:
    s3=s[:match.end()]
if match!=None and (re.search(p11,s[:match.end()],re.A)==None):
    s=s[match.end():]
match=re.search(p5,s,re.A)
if match==None or (re.search(p12,s[:match.end()],re.A)!=None):
    s4=''
else:
    s4=s[:match.end()]
if match!=None and (re.search(p12,s[:match.end()],re.A)==None):
    s=s[match.end():]
if s0=='1':
    s5=s
    list1=[s1,s2,s3,s4,s5]
    data={}
    data={'名字':name, '手机':tel,'地址':list1}
    string=json.dumps(data,ensure_ascii=False)
    
else:
    match=re.search(p7,s,re.I)
    if (match !=None):
        s5=s[:match.start()]
        s6=match.group()
        s=s[match.end():]
    else:
        s6=''
        match=re.search(p6,s,re.A)
        if match==None:
            s5=''
        else:
            s5=s[:match.end()]
            s=s[match.end():]
    s7=s
    if s0=='3':
        url='https://restapi.amap.com/v3/geocode/geo?address='+s9+'&output=XML&key=55102a2c4b79bf8c87cab849177e086a'
        #print(s9)
        al=requests.get(url).text
        match=re.search(p13,str(al),re.I)
        url='https://restapi.amap.com/v3/geocode/regeo?output=xml&location='+match.group()+'&key=55102a2c4b79bf8c87cab849177e086a&radius=1000&extensions=base'
        al=requests.get(url).text
        al=str(al)
        p=re.compile('<province>(.+?)</')
        s1=p.findall(al)[0]
        p=re.compile('<city>(.+?)</')
        s2=p.findall(al)[0]
        if (s1=='上海市')or( s1=='北京市')or( s1=='重庆市')or( s1=='天津市'):
            s2=s1
            s1=s1[0:2]
        p=re.compile('<district>(.+?)</')
        s3=p.findall(al)[0]
        p=re.compile('<township>(.+?)</')
        s4=p.findall(al)[0]
    list1=[s1,s2,s3,s4,s5,s6,s7]
    data={'名字':name, '手机':tel,'地址':list1}
    string=json.dumps(data,ensure_ascii=False)
    #string=r'{"姓名":"'+name+r'","手机":"'+str(tel)+r'","地址":["'+s1+r'","'+s2+r'","'+s3+r'","'+s4+r'","'+s5+r'","'+s6+r'","'+s7+r'"]},'
print(string)

        

