# -*- coding: utf-8 -*-
"""
@author: cite from https://blog.csdn.net/qq_38778838/article/details/89040722?utm_medium=distribute.wap_feed_404.none-task-blog-OPENSEARCH-2.nonecase&dist_request_id=&depth_1-utm_source=distribute.wap_feed_404.none-task-blog-OPENSEARCH-2.nonecase
@Created on
@instruction：用于matplotlib绘图后的鼠标交互显示，本例为实现随鼠标滑动自动标注（在pycharm自带的toolwindow、Jupyter notebook中均不能实现交互，原生基于pyqt5的fig窗口应该能够实现）
@Version update log:
"""

import matplotlib.pyplot as plt
import numpy as np


def Show(y):
    """
    绘制交互图
    :param y:
    :return:
    """

    len_y = len(y)
    x = range(len_y)
    _y = [y[-1]] * len_y

    fig = plt.figure(figsize=(960 / 72, 360 / 72))
    ax1 = fig.add_subplot(1, 1, 1)

    ax1.plot(x, y, color='blue')
    line_x = ax1.plot(x, _y, color='green')[0]  # 数据标记横线
    line_y = ax1.axvline(x=len_y - 1, color='skyblue')  # 数据标记纵线

    ax1.set_title('figMouseInteraction')
    text0 = plt.text(len_y - 1, y[-1], str(y[-1]), fontsize=10)  # 主函数里的静态标签

    # def scroll(event):
    #     """
    #     这个函数好像没啥作用，注释掉之后的实现结果和存在的时候一样
    #     :param event:
    #     :return:
    #     """
    #     axtemp = event.inaxes
    #     x_min, x_max = axtemp.get_xlim()
    #     fanwei_x = (x_max - x_min) / 10
    #     if event.button == 'up':
    #         axtemp.set(xlim=(x_min + fanwei_x, x_max - fanwei_x))
    #     elif event.button == 'down':
    #         axtemp.set(xlim=(x_min - fanwei_x, x_max + fanwei_x))
    #     fig.canvas.draw_idle()


    def motion(event):
        """
        这个函数实时更新图片的显示内容
        :param event:
        :return:
        """
        try:
            temp = y[int(np.round(event.xdata))]
            for i in range(len_y):
                _y[i] = temp
            line_x.set_ydata(_y)
            line_y.set_xdata(event.xdata)
            ######
            text0.set_position((event.xdata, temp))
            text0.set_text(str(temp))

            fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
        except:
            pass

    # fig.canvas.mpl_connect('scroll_event', scroll)
    fig.canvas.mpl_connect('motion_notify_event', motion)

    plt.show()


if __name__ == '__main__':
    Show(np.random.random(100) * 100)
