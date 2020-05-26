"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

#新添加的用于报表的文件
import os
from django.http import StreamingHttpResponse
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework.decorators import api_view
from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Mm, Inches, Pt


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


# 流方式读取文件
def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break


#def delete_docx_file(filepath):
#    if os.path.exists(filepath):
#        files = os.listdir(filepath)
#        for file in files:
#            if file != "template.docx":
#                os.remove(os.path.join(filepath, file))
                
            
#直接生成图片
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot

from snapshot_selenium import snapshot

def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

make_snapshot(snapshot, bar_chart().render(), "E:/GZ/Django/Django_API-1/Django_baogao/Django_Word/wordDjangoTest/app/bar.png")




@api_view(['GET'])
def downloadreport(request):
    
    filename = 'test.docx'        # 所生成的word文档需要以.docx结尾，文档格式需要
    filepath = 'E:/GZ/Django/Django_API-1/Django_baogao/Django_Word/wordDjangoTest/app/'
    template_path = os.getcwd() + '/test.docx'
    template = DocxTemplate(template_path)
    context = {'text': '哈哈哈，来啦',
           't1':'燕子',
            't2':'杨柳',
            't3':'桃花',
            't4':'针尖',
            't5':'头涔涔',
            't6':'泪潸潸',
            't7':'茫茫然',
            't8':'伶伶俐俐',
            'picture1': InlineImage(template, 'E:/GZ/Django/Django_API-1/Django_baogao/Django_Word/wordDjangoTest/app/bar.png', width=Mm(80), height=Mm(60)),}

    user_labels = ['姓名', '年龄', '性别', '入学日期']
    context['user_labels'] = user_labels
    user_dict1 = {'number': 1, 'cols': ['林小熊', '27', '男', '2019-03-28']}
    user_dict2 = {'number': 2, 'cols': ['林小花', '27', '女', '2019-03-28']}
    user_list = []
    user_list.append(user_dict1)
    user_list.append(user_dict2)

    context['user_list'] = user_list
    template.render(context)
    

    template.save(os.path.join(filepath,filename))
    response = StreamingHttpResponse(read_file(os.path.join(filepath, filename), 512))
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    # time.sleep(10)
    return response
    