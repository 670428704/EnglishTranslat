
'''
    Demo：pdf2htmlex解析pdf
    Datetime：2018-02-22 15:30:00
    Author：lizm
'''

import importlib
import sys
import random
from urllib.request import urlopen
from urllib.request import Request
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument
import csv
import re

'''
 解析pdf 文本，保存到txt文件中
'''
importlib.reload(sys)

def parseLocal(pdfPath):
    outPath = pdfPath.replace(".pdf",".csv")
    fil = open(outPath,"wb")
    fil.close()

    fp = open(pdfPath, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    praser_pdf = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser_pdf.set_document(doc)
    doc.set_parser(praser_pdf)
    # 提供初始化密码doc.initialize("123456")
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()
    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF参数分析器
        laparams = LAParams()
        # 创建聚合器
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF页面解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pageCount = 0
        # 循环遍历列表，每次处理一页的内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            # 使用页面解释器来读取
            interpreter.process_page(page)
            pageCount = pageCount +1
            # 使用聚合器获取内容
            layout = device.get_result()
            count = 0
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure,
            # LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            for out in layout:
                count = count + 1
                # 判断是否含有get_text()方法，图片之类的就没有
                # if hasattr(out,"get_text"):
                if isinstance(out, LTTextBoxHorizontal):
                    results = out.get_text()
                    results = results.strip().replace(',', '').replace('\n', '|')
                    results = re.sub(r'[^A-Za-z]', ' ', results)
                    print("results:(%s/%s):%s " % (count, pageCount,results) )

                    with open(outPath, 'a+',newline ="") as f:
                        csv_write = csv.writer(f)
                        data_row = [count,pageCount,str(results) ]
                        csv_write.writerow(data_row)




if __name__ == '__main__':


    pdfPathArray = [
        "./CFApdf/2019 CFA Curriculum Level I Volume 1.pdf",
        "./CFApdf/2019 CFA Curriculum Level I Volume 2.pdf",
        "./CFApdf/2019 CFA Curriculum Level I Volume 3.pdf",
        "./CFApdf/CFA Program Curriculum Level I Vol 4.pdf",
        "./CFApdf/CFA Program Curriculum Level I Vol 5.pdf",
        "./CFApdf/CFA Program Curriculum Level I Vol 6.pdf"
    ]
    for pdfPath in pdfPathArray:
        parseLocal(pdfPath)

