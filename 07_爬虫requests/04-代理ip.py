import requests
url = 'https://www.baidu.com/s?'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "BIDUPSID=B155AF69668749693E8050320212854A; PSTM=1731591834; BAIDUID=B155AF6966874969D3D666FC212D4F35:FG=1; BD_UPN=12314753; H_WISE_SIDS_BFESS=61217_60853_61350_61361_61391_61430_61466_61503_61525_61539_61608_61632; BDUSS=UJFMnl0UHZKTVZxVjRGWklxTnpQeWpxblpidWhEd215ZGR3RXNJRURRUFlwcTVuSVFBQUFBJCQAAAAAAQAAAAEAAADsU~EZS0lLSWZyYW50AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANgZh2fYGYdnU; BDUSS_BFESS=UJFMnl0UHZKTVZxVjRGWklxTnpQeWpxblpidWhEd215ZGR3RXNJRURRUFlwcTVuSVFBQUFBJCQAAAAAAQAAAAEAAADsU~EZS0lLSWZyYW50AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANgZh2fYGYdnU; BAIDUID_BFESS=B155AF6966874969D3D666FC212D4F35:FG=1; ZFY=HRDD4ZnLj7vXFRi:BAh:B3:ACJz4reraqUQPNbrDVoPJh4:C; ispeed_lsm=0; H_WISE_SIDS=61678_61987_62055_62063_62076_62091_62111_62147_62168; __bid_n=19425aed5df9824f77657f; RT=\"z=1&dm=baidu.com&si=123e073d-1d7d-421e-896a-d5f2016e9ac9&ss=m74dcoif&sl=6&tt=6fc&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=n5g&ul=s6o&hd=s6u\"; H_PS_PSSID=61678_61987_62044_62055_62063_62076_62091_62100_62103_62111_62147_62168_62187_62180_62195; delPer=0; BD_CK_SAM=1; PSINO=6; sugstore=1; H_PS_645EC=9693WOdLIgJuUB66oJFOdg8ms321TkC3IuZvtg17r48Alg1rmDEiVBnjczc; BA_HECTOR=00a00l04al2la5ag04ah8g801gvge91jr5neq1u; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; B64_BOT=1; baikeVisitId=97319dba-fd42-494e-8763-f85889660c5e; COOKIE_SESSION=260353_1_5_7_6_6_1_0_5_5_3_0_75682_0_0_0_1739514001_1739329490_1739775449%7C9%233803816_6_1739329486%7C3",
    "Host": "www.baidu.com",
    "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
data = {
    'wd': 'ip'
}
response = requests.get(url=url, params=data, headers=headers)
content = response.text
with open('04-代理ip.html', 'w', encoding='utf-8') as fp:
    fp.write(content)