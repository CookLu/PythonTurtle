from pyecharts.charts import Geo

# ->Geo 是函数注解，表示该函数返回值为Geo对象
def geo_effectscatter() -> Geo:
    # 以下为链式调用方法声明对象
    c = (
        Geo()

        # 添加底部地图
        .add_schema(maptype="china")
    )
    return c

# 生成对象
c = geo_effectscatter()

# 渲染地图
c.render()