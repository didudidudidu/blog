#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from django import template


register = template.Library()


@register.filter()
def handel_time(time):
    """
      time距离现在的时间间隔
      1. 如果时间间隔小于5分钟以内，那么就显示“刚刚”
      2. 如果是大于5分钟小于1小时，那么就显示“xx分钟前”
      3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
      4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
      5. 否则就是显示具体的时间
      """
    if isinstance(time, datetime.datetime):#两个if else，外层的先判断数据格式是否是datetime
        now = datetime.datetime.now()
        timestampe = (now - time).total_seconds()  # 取得两个时间差，并且转为秒
        if timestampe < 60 * 5:
            return "刚刚"
        elif 60 * 5 <= timestampe < 60 * 60:
            minutes = timestampe / 60
            return f"{int(minutes)}分钟前"
        elif 60 * 60 <= timestampe < 60 * 60 * 24:
            minutes = timestampe / 60
            hours = minutes / 60
            return f"{int(hours)}小时前"
        elif 60 * 60 * 24 <= timestampe <60 * 60 * 24 * 30:
            minutes = timestampe / 60
            hours = minutes / 60
            day = hours / 24
            return f"{int(day)}天前"
        else:
            return time.strftime('%Y/%m/%d')

    else:
        return time.strftime('%Y/%m/%d')
