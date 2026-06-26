from lxml import etree

tree = etree.parse('xpath.html')

# li_list = tree.xpath('//ul/li[@id]/text()')
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')

# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')

# li_list = tree.xpath('//ul/li[@id ="l1"/text() | //ul/li[@id="l2"]/text()')
print(li_list)
print(len(li_list))


