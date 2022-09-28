#pip install pyecharts
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
def geo_effectscatter() -> Geo:

    # 初始化地图参数 page_title: 页面标题， theme: 画布主题（主题列表可见Echarts官网）
    InitOpts = opts.InitOpts(page_title="中国地图", theme="light")
    c = (
        # 声明对象时将初始化参数
        Geo(InitOpts)
        # 添加底部地图
        .add_schema(
            maptype="china")

        # 增加区域点（阿克赛钦和藏南地区）
        .add_coordinate(
            name='阿克赛钦',
            longitude=78.928266,
            latitude=35.115117
        )
        .add_coordinate(
            name='藏南地区',
            longitude=93.128902,
            latitude=27.616436
        )

        # 将剧中地图缺少的地方标记出来
        .add(
            "《亲爱的 热爱的》剧中地图缺少的部分",
            [['海南',100], ['台湾', 100], ['阿克赛钦', 100], ['藏南地区', 100]],
            type_=ChartType.EFFECT_SCATTER,
        )
        # 显示出这个点的标签（formatter={b} 表示显示地区名称，详细可见：
        #  https://pyecharts.org/#/zh-cn/series_options ）
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter="{b}", font_size=14))

        # 设置地图名称，即左上角
        .set_global_opts(title_opts=opts.TitleOpts(title="中国地图"))
    )
    return c

# 生成对象
c = geo_effectscatter()

# 渲染地图
c.render()

# 生成图片
make_snapshot(snapshot, c.render(), "map_marked.png")