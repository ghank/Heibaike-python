#!/usr/bin/env python
# encoding: utf-8
"""
@author: Hank zhang
@contract:zhanghao_87@aliyun.com
@file: homework5_2.py
@time: 2016/10/27 14:47
"""

#5-2 修改wx_01_shape，画三角形，椭圆，五角星
#5-3 扩展area计算各个形状的面积

import numpy as np
import wx

class MyFrame(wx.Frame):
    def __init__(self, title, shapes):
        super(MyFrame, self).__init__(None, title=title, size=(600, 400))
        self.shapes = shapes
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.points)

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    @property
    def xy(self):
        return (self.x, self.y)

    def __str__(self):
        return "x={0}, y={1}".format(self.x, self.y)
    #返回一个可以用来表示对象的可打印字符串
    def __repr__(self):
        return str(self.xy)


class Shape(object):
    __slots__ = ('points', 'color')
    def __init__(self, points_list, **kwargs):
        for point in points_list:
            assert isinstance(point, Point), "input must be Point type"
        self.points = []
        for point in points_list:
            self.points.append(point.xy)
        self.points.append(points_list[0].xy)
        self.color = kwargs.get('color', '#000000')

    @property
    def area(self):
        return 0

    def __str__(self):
        return str(self.points)

class Triangle(Shape):
    def __init__(self, points_list, **kwargs):
        assert len(points_list)==3, "triangle need three points"
        super(Triangle, self).__init__(points_list, **kwargs)
        self._x = points_list[0]
        self._y = points_list[1]
        self._z = points_list[2]

    def length(self, x, y):
        # assert isinstance(x, Point) and isinstance(y, Point), "input must be Point type"
        z = Point(0,0)
        z = x - y
        return np.sqrt(z.x**2 + z.y**2)

    @property
    def area(self):
        a = self.length(self._x, self._y)
        b = self.length(self._y, self._z)
        c = self.length(self._x, self._z)
        return (1.0/4.0) * np.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a))


class RectAngle(Shape):
    def __init__(self, startPoint, w, h, **kwargs):
        self._w = w
        self._h = h
        super(RectAngle, self).__init__([startPoint, startPoint+Point(w, 0), startPoint+Point(w, h), startPoint+Point(0, h), startPoint], **kwargs)

    @property
    def area(self):
        return self._w * self._h

import math
class Circle(Shape):
    def __init__(self, center_p, radius, **kwargs):
        points_list = []
        self._radius = radius
        self._center_p = center_p
        N_circle = 24
        for i in xrange(N_circle):
            points_list.append(center_p + Point(radius*math.cos(2.0*math.pi*i/N_circle),radius*math.sin(2.0*math.pi*i/N_circle)))
        super(Circle, self).__init__(points_list, **kwargs)

    @property
    def area(self):
        return math.pi*self._radius**2

class FiveStars(Shape):
    def __init__(self, center_p, radius, **kwargs):
        points_list = []
        self._radius = radius
        self._center_p = center_p
        N_circle = 5
        for i in xrange(N_circle):
            print i
            points_list.append(center_p + Point(radius*math.cos(2.0*math.pi*i/N_circle),radius*math.sin(2.0*math.pi*i/N_circle)))
            points_list.append(center_p + Point((radius*math.sin(math.pi/10.0)/math.sin(math.pi/5.0))*math.cos(2.0*math.pi*i/ N_circle+2.0*math.pi/10.0),
                                                (radius * math.sin(math.pi / 10.0) / math.sin(math.pi / 5.0))*math.sin(2.0*math.pi*i/N_circle+2.0*math.pi/10.0)))

        super(FiveStars, self).__init__(points_list, **kwargs)

    @property
    def area(self):
        S = 1.0/2.0 * self._radius**2 / (math.atan(36) + math.atan(18))
        return S * 10.0


if __name__ == '__main__':
    prepare_draws = []
    start_p = Point(50, 60)
    a = RectAngle(start_p, 100, 80, color="#ff0000")
    prepare_draws.append(a)

    t = Triangle([Point(100, 100), Point(150, 100), Point(120,150)], color="#00ff00")
    prepare_draws.append(t)

    c = Circle(Point(200,200), 100, color="#0000ff")
    prepare_draws.append(c)

    f = FiveStars(Point(250,250), 80, color="#0ff000")
    prepare_draws.append(f)

    for s in prepare_draws:
        print s.area

    app = wx.App()
    MyFrame('Shapes', prepare_draws)
    app.MainLoop()


