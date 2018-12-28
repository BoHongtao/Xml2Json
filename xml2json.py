# encoding: utf-8
# @author: John
# @contact: BoHongtao@yeah.net
# @software: PyCharm
# @time: 2018/12/28 13:29
from xml.etree import cElementTree as Tree
from cElementTree import XmlDictConfig

tree = Tree.parse('Xml.xml')
root = tree.getroot()
xmldict = XmlDictConfig(root)
print(xmldict)