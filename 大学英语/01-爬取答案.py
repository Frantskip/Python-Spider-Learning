import requests
from bs4 import BeautifulSoup
import os
import urllib.request
try:
    os.makedirs('./答案/')
except:
    print('文件夹已存在')
    url = 'https://mp.weixin.qq.com/s?search_click_id=6747174975146274972-1740623527765-1977460029&__biz=MzI0MzY5MjAwMQ==&mid=2247525208&idx=5&sn=4b0e98b54c6959fb60b937ab6c5943eb&chksm=e83247061f6d034f0125f70ee073a22bd617281e601fcdf08dce8592cfd703d6b6a458b77dee&scene=7&subscene=10000&sessionid=1740623434&clicktime=1740623527&enterid=1740623527&ascene=65&fasttmpl_type=0&fasttmpl_fullversion=7621112-zh_CN-zip&fasttmpl_flag=0&realreporttime=1740623527784&devicetype=android-35&version=28003895&nettype=3gnet&lang=zh_CN&countrycode=CN&exportkey=n_ChQIAhIQpb5P8HznkE9s4GymNV1yOxLiAQIE97dBBAEAAAAAAKpJEeQV%2BjEAAAAOpnltbLcz9gKNyK89dVj0Dr45PIC%2FJWKV9Xf5gKWxNZ1xTAngHQijEjpmyfVFlSiddB1wJxIUzHPZ97a2Lz%2BVhQP%2BDoQSNpc4JLGZmrfBiXhu%2BvVMaHUjHk2cE%2BKqj5G989sCCB8UxDEBM%2FJl7YKIuxvd54uYpp%2BZ0XioARdLkyGej%2BNnBbakyNCojL%2BNvsQlKe976sHWomcmSTyXmuRLGd2Wmfp3M0F8fzgk3JwQ1u3dVK9f4PawF%2BAuIcFiQsXA9ikNM9JUhSI7Dro%3D&pass_ticket=sUDY5M69daD6rpzrulOt6DzGogD%2BLlj1finFg3bd9RPnU93bmpy0h6c3UTXdrgKf&wx_header=3'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }
    resp=requests.get(url,headers=headers)
    resp.encoding='utf-8'
    content=resp.text
    # print(content)
    # with open('./答案/答案.html','w',encoding='utf-8') as fp:
    #     fp.write(content)
    soup=BeautifulSoup(content,'html.parser')
    img_src=soup.find_all('img',{'data-type':'jpeg'})
    print(img_src)
    i=0
    for img in img_src:
        urllib.request.urlretrieve(url=img['data-src'],filename='./答案/'+str(i)+'.jpg')
        i+=1
        print(f"\r完成比例{i/len(img_src):.2%}",end='')

    print("完成")
