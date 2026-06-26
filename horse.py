from lxml import etree
import requests
import os

# 创建img文件夹（如果不存在）
if not os.path.exists('./img'):
    os.makedirs('./img')
word = input("请输入要查询的内容：")
word_encode = requests.utils.quote(word)
print(word_encode)
# url = "https://aspx.sc.chinaz.com/query.aspx?keyword=%E9%A9%AC&issale=&classID=11&navindex=0&page=2"
url = f"https://aspx.sc.chinaz.com/query.aspx?classid=11&keyWord={word_encode}"
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36',
        'cookie':'Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1749740044; qHistory=aHR0cDovL3Nlby5jaGluYXouY29tX1NFT+e7vOWQiOafpeivog==; cz_statistics_visitor=500be9e9-b399-b6c7-4157-b1867f4f2c44; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1758188372; Hm_lvt_aecc9715b0f5d5f7f34fba48a3c511d6=1759557563; _clck=1u52gs6%5E2%5Efzv%5E0%5E1989; ASP.NET_SessionId=qqhkchu0knmm5wkn1vrc1q4t; HMACCOUNT=EBCE68312C388D20; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1763462470'
}

response = requests.get(url=url, headers=headers)

content = response.text

tree = etree.HTML(content)

src_list = tree.xpath("//div[@class='im']//img/@data-src")
print(src_list)
print(f"共发现 {len(src_list)} 张图片需要下载")

count = 0
for ele in src_list:
    ele = ele.replace("\\", "/")
    img_content = requests.get(url="https:"+ele, headers=headers).content
    with open('./img/'+str(count)+'.jpg', 'wb') as f:
        f.write(img_content)
    count += 1
    print(f"已下载 {count} 张图片")

# for ele in src_list:
#     ele = ele.replace("\\", "/")
#     print("https:"+ele)
