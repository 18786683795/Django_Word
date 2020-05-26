# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:09:05 2020

@author: Lenovo
"""
#https://blog.csdn.net/yycoolsam/article/details/103255271/

# ************************************画图*****************************************
from pyecharts.charts import Bar,Grid,Pie
from pyecharts import options as opts

# 方形图
subtitle = ''
title = '图1.1：***********投资前10省分布'
path_html = './picture/1.小册子-总体情况.html'
path_png = "./picture/1.小册子-总体情况.png"
draw_data = table_1[:10].sort_values(['toimie'], ascending=True)
x_lable = draw_data['city'].to_list()
y_data_1 = [format('%.2f'%i) for i in draw_data['toimie'].to_list()]
y_data_2 = [format('%.2f'%i) for i in draw_data['toiqie'].to_list()]
init_opts = opts.InitOpts(width="480px", height="360px")
plt = (
    Bar(init_opts=init_opts)
        .set_global_opts(title_opts=opts.TitleOpts(title=title, # 标题
                                                   # subtitle = subtitle, # 副标题
                                                   pos_left='center',pos_top='bottom', # 标题位置
                                                   title_textstyle_opts = {
                                                       'fontSize':10.5
                                                   }
                                                   ),
                         yaxis_opts=opts.AxisOpts( # Y轴设置

                         ),
                         xaxis_opts=opts.AxisOpts(   # X轴设置
                            # type_="category"     # 行坐标类型
                         ),
                         legend_opts=opts.LegendOpts(type_='scroll',    # 图例
                                                     orient='vertical',  # 图例列表的布局朝向
                                                     pos_left="center", pos_top='center'   # 图例位置
                                                     ),
                         tooltip_opts=opts.TooltipOpts(trigger='axis'),
                         toolbox_opts=opts.ToolboxOpts(),  # 工具栏
                         # datazoom_opts=opts.DataZoomOpts(),  # 缩放功能

                         )
        .set_series_opts(label_opts=opts.LabelOpts(# is_show=False,       # 是否显示数值
                                                   position="right" ,     # 设置字体对齐
                                                   ))
    #     .extend_axis(           # 双轴
    #     yaxis=opts.AxisOpts()
    # )
        .add_xaxis(x_lable
                   )
        .add_yaxis('****投资总额(亿元)', y_data_1,label_opts=opts.LabelOpts(position='right', # 标签文字位置
                                                                    font_weight='bolder',    # 标签字体
                                                                    # color='#FFC8B4'
                                                                    ),
                                                # color='#FFC8B4'

                   )
        .add_yaxis('对****投资总额(亿元)', y_data_2,label_opts=opts.LabelOpts(position='right',font_weight='bolder'))
        .reversal_axis()  # 转轴
)
grid = Grid(init_opts=init_opts)
grid.add(plt, grid_opts=opts.GridOpts(pos_top='5'))  # 仅使用pos_top修改相对顶部的位置
grid.render(path_html)


# 玫瑰图
subtitle = '图1.2：**********互投行业明细'
title = '外圈:***投资总额  内圈:对****投资总额'
path_html_1 = './picture/1.小册子-总体情况_1.html'
path_png_1 = "./picture/1.小册子-总体情况_1.png"
code_num = len(table_2['code'].to_list())
# code_num = 10
draw_data = \
    [[table_2['code'].to_list()[i],format('%.2f'%table_2['toimie'].to_list()[i])]
     for i in range(code_num) ]
draw_data_1 = \
    [[table_2['code'].to_list()[i],format('%.2f'%table_2['toiqie'].to_list()[i])]
     for i in range(code_num)]
init_opts_pie = opts.InitOpts(width="640px", height="480px")
plt = (
    Pie(init_opts=init_opts_pie)
        .set_global_opts(title_opts=opts.TitleOpts(title=title,  # 标题
                                                   subtitle = subtitle, # 副标题
                                                   pos_left='center', pos_bottom='0',  # 标题位置
                                                   title_textstyle_opts={              # 主标题
                                                       'fontSize': 16.5,               # 字体大小
                                                       "fontWeight": "bolder",         # 字体:加粗
                                                       "color": "#444444"              # 字体颜色
                                                   },
                                                   subtitle_textstyle_opts={           # 负标题
                                                       'fontSize': 16.5,
                                                        "fontWeight": "bolder",
                                                        "color": "#000000"
                                                   }
                                                   ),
                         yaxis_opts=opts.AxisOpts(  # Y轴设置

                         ),
                         xaxis_opts=opts.AxisOpts(  # X轴设置
                             # type_="category"     # 行坐标类型
                         ),
                         legend_opts=opts.LegendOpts(type_='scroll',  # 图例
                                                     orient='vertical',  # 图例列表的布局朝向
                                                     pos_left="left", pos_top='center'  # 图例位置
                                                     ),
                         tooltip_opts=opts.TooltipOpts(trigger='axis'),
                         toolbox_opts=opts.ToolboxOpts(),  # 工具栏
                         # datazoom_opts=opts.DataZoomOpts(),  # 缩放功能

                         )
        .set_series_opts(label_opts=opts.LabelOpts(# is_show=False,       # 是否显示数值
        position="right",  # 设置字体对齐
    ))
        .add(
        "对****投资总额",
        draw_data_1,
        radius=["15%", "30%"],
        # center=["25%", "50%"],    # 中心点位置
        # rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True,formatter="{b}: {c}",font_weight='bolder',),
    )
        .add(
        "****投资总额",
        draw_data,
        radius=["65%", "80%"],
        # center=["75%", "50%"],
        # rosetype="area",
        label_opts=opts.LabelOpts(is_show=True,formatter="{b}: {c}",font_weight='bolder',),
    )
)
grid_1 = Grid(init_opts=init_opts_pie)
grid_1.add(plt, grid_opts=opts.GridOpts(pos_top='5'))  # 仅使用pos_top修改相对顶部的位置
grid_1.render(path_html_1)


# html转图片
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
make_snapshot(snapshot, grid.render(path_html), path_png,delay=2,pixel_ratio=2)
make_snapshot(snapshot, grid_1.render(path_html_1), path_png_1,delay=2,pixel_ratio=2)

