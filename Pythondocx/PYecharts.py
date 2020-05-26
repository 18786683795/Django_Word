# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:18:48 2020

@author: Lenovo
"""

"""pyecharts是一个用于生成echart（百度开源的数据可视化javascript库）图表的类库。
pyecharts 分为 v0.5.x 和 v1.x 两个大版本，版本不兼容，本篇所有的案例基于v1.6.2。
"""

# 柱状图
import random
import pyecharts.options as opts
from pyecharts.charts import Bar

#柱状图
x_vals = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
bar = (
    Bar()
    .add_xaxis(x_vals)
    .add_yaxis('商家A', [random.randint(10, 100) for _ in range(6)])
    .add_yaxis('商家B', [random.randint(10, 100) for _ in range(6)])
    .add_yaxis('商家C', [random.randint(10, 100) for _ in range(6)])
    .add_yaxis('商家D', [random.randint(10, 100) for _ in range(6)])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14),
                          markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(y=40, name="达标线=40")]))
    .set_global_opts(title_opts=opts.TitleOpts(title='柱状图示例-销量', subtitle='四个商家'),
                     xaxis_opts=opts.AxisOpts(name='商品'),
                     yaxis_opts=opts.AxisOpts(name='单位:件'))
)
bar.render('柱状图.html')

# html转图片
from pyecharts.charts import Bar,Grid,Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

init_opts = opts.InitOpts(width="600px", height="360px")
path_html = '柱状图.html'
path_png = "E:/GZ/Django/Django_API-1/Django_baogao/DjangoWord/Python_docx/柱状图.png"

grid = Grid(init_opts=init_opts)
grid.add(bar, grid_opts=opts.GridOpts(pos_top='5'))  # 仅使用pos_top修改相对顶部的位置
grid.render(path_html)

make_snapshot(snapshot, grid.render(path_html), path_png,delay=2,pixel_ratio=2)


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

make_snapshot(snapshot, bar_chart().render(), "bar0.png")



# 柱状堆叠图
import pyecharts.options as opts
from pyecharts.charts import Bar

goods = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
bar = (
    Bar()
    .add_xaxis(goods)
    .add_yaxis('商家A', [random.randint(10, 100) for _ in range(6)], stack='stack1')
    .add_yaxis('商家B', [random.randint(10, 100) for _ in range(6)], stack='stack1')
    .add_yaxis('商家C', [random.randint(10, 100) for _ in range(6)], stack='stack1')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title='柱状堆叠图示例-商品销量'),
                     xaxis_opts=opts.AxisOpts(name='品类'),       
                     yaxis_opts=opts.AxisOpts(name='销量（单位:件）'))
)

bar.render('柱状堆叠图.html')


# 条形图
x_vals1 = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
x_vals2 = ['POLO', '篮球鞋', '羽绒服', '皮鞋', '领带', '睡衣']
x_vals3 = ['羽毛球服', '羽毛球鞋', '护腕', '护膝', '护踝', '毛巾']
y_vals = [random.randint(10, 100) for _ in range(18)]
bar = Bar().add_xaxis(x_vals1 + x_vals2 + x_vals3)      
bar.add_yaxis('商家A', y_vals, 
              markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='average'),
                                                opts.MarkPointItem(type_='max'),
                                                opts.MarkPointItem(type_='min')], 
                                                symbol_size=80)
              ) 
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='right'))
bar.set_global_opts(title_opts=opts.TitleOpts(title='条形图示例-商品销量', subtitle='条目较多条形图比较好看点'))
bar.reversal_axis() #翻转XY轴，将柱状图转换为条形图
bar.render('条形图.html')


# 直方图
import random
import pyecharts.options as opts
from pyecharts.charts import Bar
x_vals = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
xlen = len(x_vals)

# 设置成两种颜色
y_vals = []
for idx, item in enumerate(x_vals):
    if idx % 2 == 0:
        y_vals.append(
            opts.BarItem(
                name = item,
                value = random.randint(10, 100),
                itemstyle_opts = opts.ItemStyleOpts(color="#749f83"),
            )
        )
    else:
        y_vals.append(
            opts.BarItem(
                name = item,
                value = random.randint(10, 100),
                itemstyle_opts = opts.ItemStyleOpts(color="#d48265"),
            )
        )

bar_histogram = (
    Bar()
    .add_xaxis(x_vals)
    .add_yaxis('商家A', y_vals, category_gap=0)
     # .add_yaxis('商家A', [random.randint(10, 100) for _ in range(6)], category_gap=0)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14))
    .set_global_opts(title_opts=opts.TitleOpts(title='直方图示例-选择赠品', subtitle=''),
                     xaxis_opts=opts.AxisOpts(name='赠品类型'),
                     yaxis_opts=opts.AxisOpts(name='选择相应赠品的人数'))
)
bar_histogram.render('直方图.html')


# 帕累托图--# 左边纵坐标表示频数,右边纵坐标表示频率.分析线表示累积频率
import random
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
import pandas as pd

# 随机颜色, from faker
def rand_color() -> str:
    return random.choice(
        [
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
            "#ca8622",
            "#bda29a",
            "#6e7074",
            "#546570",
            "#c4ccd3",
            "#f05b72",
            "#444693",
            "#726930",
            "#b2d235",
            "#6d8346",
            "#ac6767",
            "#1d953f",
            "#6950a1",
        ]
    )

df_origin = pd.DataFrame({'categories':['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'],'sales': [random.randint(10, 100) for _ in range(6)]})
print(df_origin)
# 按销量降序排列
df_sorted = df_origin.sort_values(by='sales' , ascending=False)
print(df_sorted)

# 折线图x轴
x_line_categories = [*range(7)] 
# 折线图y轴--向下累积频率
cum_percent = df_sorted['sales'].cumsum() / df_sorted['sales'].sum() * 100
cum_percent = cum_percent.append(pd.Series([0])) # 添加起始频率0
cum_percent = cum_percent.sort_values(ascending=True)

print(df_sorted.categories.values.tolist()) 
print(cum_percent.values.tolist())
def pareto_bar() -> Bar: 
    line = (
        Line()
        .add_xaxis(x_line_categories)        
        .add_yaxis("累计百分比",
                   cum_percent.values.tolist(),    
                   xaxis_index=1,
                   yaxis_index=1,             # 使用次y坐标轴，即bar中的extend_axis
                   label_opts=opts.LabelOpts(is_show=False),
                   is_smooth=True,
                  )
    )
    
    bar = (
        Bar()
        .add_xaxis(df_sorted.categories.values.tolist())
        .add_yaxis('销售额', df_sorted.sales.values.tolist(), category_gap=0)
        # .add_yaxis('总额百分比', cum_percent.values.tolist())   
        .extend_axis(xaxis=opts.AxisOpts(is_show=False, position='top')) 
        .extend_axis(yaxis=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_inside=True),  # 刻度尺朝内
            axislabel_opts=opts.LabelOpts(formatter='{value}%'), position='right') )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14))
        .set_global_opts(title_opts=opts.TitleOpts(title='帕累托图示例-销售额', subtitle=''),
                             xaxis_opts=opts.AxisOpts(name='商品类型', type_='category'),
                             yaxis_opts=opts.AxisOpts(
                                axislabel_opts=opts.LabelOpts(formatter="{value} 件")
                             )
                         )
    )
    bar.overlap(line)
    return bar


pareto_bar().render('帕累托图.html')


# 帕累托图--# 左边纵坐标表示频数,右边纵坐标表示频率.分析线表示累积频率
import random
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
import pandas as pd

# 随机颜色, from faker
def rand_color() -> str:
    return random.choice(
        [
            "#c23531",
            "#2f4554",
            "#61a0a8",
            "#d48265",
            "#749f83",
            "#ca8622",
            "#bda29a",
            "#6e7074",
            "#546570",
            "#c4ccd3",
            "#f05b72",
            "#444693",
            "#726930",
            "#b2d235",
            "#6d8346",
            "#ac6767",
            "#1d953f",
            "#6950a1",
        ]
    )

df_origin = pd.DataFrame({'categories':['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'],'sales': [random.randint(10, 100) for _ in range(6)]})
print(df_origin)
# 按销量降序排列
df_sorted = df_origin.sort_values(by='sales' , ascending=False)
print(df_sorted)

# 折线图x轴
x_line_categories = [*range(7)] 
# 折线图y轴--向下累积频率
cum_percent = df_sorted['sales'].cumsum() / df_sorted['sales'].sum() * 100
cum_percent = cum_percent.append(pd.Series([0])) # 添加起始频率0
cum_percent = cum_percent.sort_values(ascending=True)

print(df_sorted.categories.values.tolist()) 
print(cum_percent.values.tolist())
def pareto_bar() -> Bar: 
    line = (
        Line()
        .add_xaxis(x_line_categories)        
        .add_yaxis("累计百分比",
                   cum_percent.values.tolist(),    
                   xaxis_index=1,
                   yaxis_index=1,             # 使用次y坐标轴，即bar中的extend_axis
                   label_opts=opts.LabelOpts(is_show=False),
                   is_smooth=True,
                  )
    )
    
    bar = (
        Bar()
        .add_xaxis(df_sorted.categories.values.tolist())
        .add_yaxis('销售额', df_sorted.sales.values.tolist(), category_gap=0)
        # .add_yaxis('总额百分比', cum_percent.values.tolist())   
        .extend_axis(xaxis=opts.AxisOpts(is_show=False, position='top')) 
        .extend_axis(yaxis=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_inside=True),  # 刻度尺朝内
            axislabel_opts=opts.LabelOpts(formatter='{value}%'), position='right') )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, font_size=14))
        .set_global_opts(title_opts=opts.TitleOpts(title='帕累托图示例-销售额', subtitle=''),
                             xaxis_opts=opts.AxisOpts(name='商品类型', type_='category'),
                             yaxis_opts=opts.AxisOpts(
                                axislabel_opts=opts.LabelOpts(formatter="{value} 件")
                             )
                         )
    )
    bar.overlap(line)
    return bar


pareto_bar().render('帕累托图.html')


# 饼图
from pyecharts import options as opts
from pyecharts.charts import Page, Pie

pie = (
    Pie()
    .add('鼠标选中分区后的tip',
         [list(z) for z in zip(['20{}年第{}季'.format(year,season)   
                                        for year in [19, 20]  # count 2                                        
                                                for season in range(1,5)] # count 2
                ,[random.randint(2, 10) for _ in range(8)])]) # count 8
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}: {c}万套'))
    .set_global_opts(title_opts=opts.TitleOpts(title='饼图实例-近两年季度销售'),
                         legend_opts=opts.LegendOpts(is_show=False))
)
pie.render('饼图.html')


#圆环图
from pyecharts.charts import Pie
pie = (
    Pie()
    .add(
        '鼠标选中分区后的tip',
        [list(z) for z in zip(['20{}年第{}季'.format(year,season)   
                                    for year in [19, 20]  # count 2                                        
                                            for season in range(1,5)] # count 2
            ,[random.randint(2, 10) for _ in range(8)])],
        radius=['50%', '75%'],          #设置内径外径           
        label_opts=opts.LabelOpts(is_show=True)        
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='圆环图示例-近两年季度销售'),
                     legend_opts=opts.LegendOpts(is_show=False))
)
pie.render('圆环图.html')


# 玫瑰图
from pyecharts.charts import Pie
pie = (
    Pie()
    .add(
        '鼠标选中分区后的tip',
        [list(z) for z in zip(['20{}年第{}季'.format(year,season)   
                                    for year in [19, 20]  # count 2                                        
                                            for season in range(1,5)] # count 2
            ,[random.randint(0, 10) for _ in range(8)])],
        radius=['10%', '75%'],          #设置内径外径
        # rosetype='radius' 圆心角展现数据百分比，半径展现数据大小
        # rosetype='area' 圆心角相同，为通过半径展现数据大小
        rosetype='radius',             
        label_opts=opts.LabelOpts(is_show=True)        
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='玫瑰图示例-近两年季度销售'),
                     legend_opts=opts.LegendOpts(is_show=False))
)
pie.render('玫瑰图.html')


# 折线图
import random
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
 
line = (
    Line()
    .add_xaxis(['{}月第{}周周赛'.format(y,z) 
                     for y in range(1, 3)  # 1、2月  
                         for z in range(1, 5)])  # 1-4周
    .add_yaxis('A题', [random.randint(10, 20) for _ in range(8)], 
               is_smooth=True, # 平滑
               markpoint_opts=opts.MarkPointOpts(
                           # 使用coord这个属性设置自定义标记点数值，我这儿随便写
                           data=[opts.MarkPointItem(name='自定义标记点',coord=[2,18],value='标注值')]
                       )
               )
    .add_yaxis('B题', [random.randint(5, 20) for _ in range(8)])
    .add_yaxis('C题', [random.randint(5, 20) for _ in range(8)])
    .set_series_opts(label_opts=opts.LabelOpts(
                    formatter=JsCode( # 通过定义JavaScript回调函数自定义标签
                         "function(params){"
                                "return params.value[1].toString() + '%';}"  # 外层单引号内存双引号亲测不行！
                    )
                ))
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), # 设置x轴标签旋转角度
                     yaxis_opts=opts.AxisOpts(name='AC率', min_=3), 
                     title_opts=opts.TitleOpts(title='折线示例_ACM题目分析'))        
    )

line.render('折线图.html')


# 折线面积图
import random
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.commons.utils import JsCode
 
line = (
    Line()
    .add_xaxis(['{}月第{}周周赛'.format(y,z) 
                     for y in range(1, 3)  # 1、2月  
                         for z in range(1, 5)])  # 1-4周
    .add_yaxis('蔡队', 
               [random.randint(10, 20) for _ in range(8)], 
               is_symbol_show=False,         
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='average', name='均值'),
                                                   opts.MarkPointItem(type_='max', name='最大值'),
                                                   opts.MarkPointItem(type_='min', name='最小值')], 
                                                   symbol_size=50)           
               )
    .add_yaxis('旺神', 
               [random.randint(6, 20) for _ in range(8)], 
               is_smooth=True, 
               is_symbol_show=False,
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5)
               )
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)), # 设置x轴标签旋转角度
                     yaxis_opts=opts.AxisOpts(name='完成积分', min_=5), 
                     title_opts=opts.TitleOpts(title='折线面积图示例_周赛分析'))        
    )

line.render('折线面积图.html')


# 散点图
from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import pandas as pd

def scatter_simple() -> Scatter:
    # 数据源
    df = pd.DataFrame({'AC':[21,22,23,24,28,30,34,35,40,44,45],  # 刷题数
                       'ACB':[140,120,380,120,200,190,160,300,300,400,500],
                       '姓名':['小军','NIL','假冒NOI','小白','弱刚','晓雷','窜天','云云','依图','蔡队','旺神',]})
    # inplace=True：不创建新的对象，直接对原始对象进行修改
    # 升序
    df.sort_values('AC', inplace=True, ascending=True)  
    
    c = (
        Scatter()
        .add_xaxis(df.AC.values.tolist())
        .add_yaxis(
            '刷题_能力_姓名',
            df[['ACB','姓名']].values.tolist(),
            label_opts=opts.LabelOpts(
                formatter=JsCode(
                    'function(params){return params.value[2];}' #通过定义JavaScript回调函数自定义标签
                )
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='散点图示例--ACM集训队队员能力'),
            xaxis_opts=opts.AxisOpts(name='AC(刷题数)', type_='value', min_=20),  #x轴从20开始，原点不为0
            yaxis_opts=opts.AxisOpts(name='ACB(能力值)', min_=100),  # y轴起始点的值
            legend_opts=opts.LegendOpts(is_show=True)
        )
    )
    return c
scatter_simple().render('散点图.html')


# 雷达图
import random
from pyecharts import options as opts
from pyecharts.charts import Page, Radar
def radar_simple() -> Radar:
    c = (
        Radar()
        .add_schema(
            # 各项的max_值可以不同
            schema=[
                opts.RadarIndicatorItem(name='计算几何学', max_=100),
                opts.RadarIndicatorItem(name='动态规划', max_=100),
                opts.RadarIndicatorItem(name='图论', max_=100),
                opts.RadarIndicatorItem(name='搜索', max_=100),
                opts.RadarIndicatorItem(name='模拟', max_=100),
                opts.RadarIndicatorItem(name='数论', max_=100),
            ]
        )
        .add('旺神', [[random.randint(10, 101) for _ in range(6)]],           
             color='red',           
             areastyle_opts = opts.AreaStyleOpts(  #设置填充的属性
                 opacity = 0.5,                  
                 color='red'                     
         ),)
        .add('蔡队', [[random.randint(10, 101) for _ in range(6)]],
             color='blue',
             areastyle_opts = opts.AreaStyleOpts(
                 opacity = 0.5,#透明度
                 color='blue'
         ),)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title='雷达图示例-ACM集训队队员能力'))
    )
    return c
radar_simple().render('雷达图.html')


# 箱线图--描述离散程度
from pyecharts import options as opts
from pyecharts.charts import Boxplot
def boxpolt_base() -> Boxplot:
    v_sophomore = [
        [1.1, 2.2, 2.6, 3.2, 3.7, 4.2, 4.7, 4.7, 5.5, 6.3, 8.0],
        [2.5, 2.5, 2.8, 3.2, 3.7, 4.2, 4.7, 4.7, 5.5, 6.3, 7.0]
    ]
    v_junior = [
        [3.6, 3.7, 4.7, 4.9, 5.1, 5.2, 5.3, 5.4, 5.7, 5.8, 5.8],
        [3.6, 3.7, 4.7, 4.9, 5.1, 5.2, 5.3, 5.4, 5.7, 5.8, 5.8]
    ]
    # 最小值，下四分位数，中位数、上四分位数、最大值
    # [min, Q1, median (or Q2), Q3, max]
    c = (
        Boxplot()
        .add_xaxis(['寒假作业','暑假作业'])
        .add_yaxis('大二队员', Boxplot.prepare_data(v_sophomore))
        .add_yaxis('大三队员', Boxplot.prepare_data(v_junior))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        .set_global_opts(title_opts=opts.TitleOpts(title='ACM集训队祖传练习完成时长离散度'),
                         xaxis_opts=opts.AxisOpts(name='单位：小时'), 
                         legend_opts=opts.LegendOpts(is_show=True))
        .reversal_axis() #翻转XY轴
    )
    return c

boxpolt_base().render('箱线图.html')


# 词云图
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

words = [
    ('背包问题', 10000),
    ('大整数', 6181),
    ('Karatsuba乘法算法', 4386),
    ('穷举搜索', 4055),
    ('傅里叶变换', 2467),
    ('状态树遍历', 2244),
    ('剪枝', 1868),
    ('Gale-shapley', 1484),
    ('最大匹配与匈牙利算法', 1112),
    ('线索模型', 865),
    ('关键路径算法', 847),
    ('最小二乘法曲线拟合', 582),
    ('二分逼近法', 555),
    ('牛顿迭代法', 550),
    ('Bresenham算法', 462),
    ('粒子群优化', 366),
    ('Dijkstra', 360),
    ('A*算法', 282),
    ('负极大极搜索算法', 273),
    ('估值函数', 265)
]
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.ROUND_RECT)
        .set_global_opts(title_opts=opts.TitleOpts(title='WordCloud示例-OJ搜索关键字'))
    )
    return c
wordcloud_base().render('词云图.html')









