# -*- coding: utf-8 -*-
import re
import requests
import json

sf1 = '^(河北|山西|辽宁|吉林|黑龙江|江苏|浙江|安徽|福建|江西|山东|河南|湖北|湖南|广东|海南|四川|贵州|云南|陕西|甘肃|青海|台湾)'
sf2 = '^(北京|天津|上海|重庆)'
sf3 = '^(内蒙古自治区|广西壮族自治区|西藏自治区|宁夏回族自治区|新疆维吾尔自治区|香港特别行政区|澳门特别行政区)'
zxs = ('北京市', '上海市', '天津市', '重庆市')
sj = '^(石家庄|张家口|承德|唐山|秦皇岛|廊坊|保定|沧州|衡水|邢台|邯郸|太原|大同|朔州|忻州|阳泉|晋中|吕梁|长治|临汾|晋城|运城|呼和浩特|呼伦贝尔|通辽|赤峰|巴彦淖尔|乌兰察布|包头|鄂尔多斯|乌海|哈尔滨|黑河|伊春|齐齐哈尔|鹤岗|佳木斯|双鸭山|绥化|大庆|七台河|鸡西|牡丹江|长春|白城|松原|吉林|四平|辽源|白山|通化|沈阳|铁岭|阜新|抚顺|朝阳|本溪|辽阳|鞍山|盘锦|锦州|葫芦岛|营口|丹东|大连|南京|连云港|徐州|宿迁|淮安|盐城|泰州|扬州|镇江|南通|常州|无锡|苏州|杭州|湖州|嘉兴|绍兴|舟山|宁波|金华|衢州|台州|丽水|温州|合肥|淮北|亳州|宿州|蚌埠|阜阳|淮南|滁州|六安|马鞍山|芜湖|宣城|铜陵|池州|安庆|黄山|福州|宁德|南平|三明|莆田|龙岩|泉州|漳州|厦门|南昌|九江|景德镇|上饶|鹰潭|抚州|新余|宜春|萍乡|吉安|赣州|济南|德州|滨州|东营|烟台|威海|淄博|潍坊|聊城|泰安|莱芜|青岛|日照|济宁|菏泽|临沂|枣庄|郑州|安阳|鹤壁|濮阳|新乡|焦作|三门峡|开封|洛阳|商丘|许昌|平顶山|周口|漯河|南阳|驻马店|信阳|武汉|十堰|襄樊|随州|荆门|孝感|宜昌|黄冈|鄂州|荆州|黄石|咸宁|长沙|岳阳|张家界|常德|益阳|湘潭|株洲|娄底|怀化|邵阳|衡阳|永州|郴州|广州|韶关|梅州|河源|清远|潮州|揭阳|汕头|肇庆|惠州|佛山|东莞|云浮|汕尾|江门|中山|深圳|珠海|阳江|茂名|湛江|南宁|桂林|河池|贺州|柳州|百色|来宾|梧州|贵港|玉林|崇左|钦州|防城港|北海|海口|三亚|三沙|儋州|成都|广元|巴中|绵阳|德阳|达州|南充|遂宁|广安|资阳|眉山|雅安|内江|乐山|自贡|泸州|宜宾|攀枝花|贵阳|遵义|六盘水|安顺|铜仁|毕节|昆明|昭通|丽江|曲靖|保山|玉溪|临沧|普洱|拉萨|日喀则|昌都|林芝|山南|那曲|西安|榆林|延安|铜川|渭南|宝鸡|咸阳|商洛|汉中|安康|兰州|嘉峪关|酒泉|张掖|金昌|武威|白银|庆阳|平凉|定西|天水|陇南|西宁|海东|银川|石嘴山|吴忠|中卫|固原|乌鲁木齐|克拉玛依|吐鲁番|哈密|北京|上海|天津|重庆|.*?自治州)'
pp = ('(.*?县|.*?(?<!社|小|校)区|.*?市)', '(.*?街道|.*?镇|.*?乡)', '(.*?街|.*?路|.*?巷|.*?道|.*?村|.*？委会|.*?区)', '(.*?号(?!楼))|.*?弄|.*?栋')
jj = ('')
line = input()
num = line[:1]
line = line[2:].strip('.|\n')
tel = re.search(r'(\d){11}', line).group()
line = line.replace(tel, '')
line = re.split(',', line)
loc = line[1]
loc_list = []  # 地址列表
p = 0  # p控制开始匹配地址
flag = re.match(sf1, loc[p:])  # 匹配普通省份
if flag:
    p = p+flag.end()
    loc_list.append(flag.group(1) + '省')
    if loc[p] == '省':
        p = p + 1
else:
    flag = re.match(sf2, loc[p:])  # 匹配直辖市
    if flag:
        loc_list.append(flag.group(1))
    else:
        flag = re.match(sf3, loc[p:])
        if flag:
            p = p + flag.end()
            loc_list.append(flag.group(1))  # 匹配自治区
        else:
            loc_list.append('')
flag = re.search(sj, loc[p:])  # 匹配地级市
if flag:
    p = p + flag.end()
    loc_list.append(flag.group(0) + '市')
    if loc[p] == '市':
        p = p + 1
else:
    loc_list.append('')
n = 4
if num == '1':
    n = 2
for i in range(n):    # 后续匹配
    flag = re.match(pp[i], loc[p:])
    if flag:
        p = p + flag.end()
        loc_list.append(flag.group(0))
    else:
        loc_list.append('')
loc_list.append(loc[p:])
if num=='3':
    url = 'https://restapi.amap.com/v3/geocode/geo?address=' + loc + '&output=XML&key=55102a2c4b79bf8c87cab849177e086a'
    al = requests.get(url).text
    al = re.search('\d+.?\d+,\d+.?\d+', al).group()
    url = 'https://restapi.amap.com/v3/geocode/regeo?output=xml&location=' + al + '&key=55102a2c4b79bf8c87cab849177e086a&radius=1000&extensions=base'
    al = requests.get(url).text
    al = re.search('<province>(.*?)</province>.*?<city>(.*?)</city>.*?<district>(.*?)</district>.*?<township>(.*?)</township>', al)
    if loc_list[0] == '':
        if al.group(1) in zxs:
            loc_list[0] = al.group(1)[:2]
            loc_list[1] = al.group(1)
        else:
            loc_list[0] = al.group(1)
    if loc_list[1] == '':
        loc_list[1] = al.group(2)
    if loc_list[2] == '':
        loc_list[2] = al.group(3)
    if loc_list[3] == '':
        loc_list[3] = al.group(4)
information = {'姓名': line[0], '手机': tel, '地址': loc_list}
print(json.dumps(information, ensure_ascii=False))
