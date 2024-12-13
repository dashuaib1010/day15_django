from django.http import JsonResponse
from django.shortcuts import render


def chart_list(request):
    return render(request, 'chart_list.html', )


def chart_bar(request):
    legend = ['销量', '营收']
    xAxis = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    series = [
        {
            "name": '销量',
            "type": 'bar',
            "data": [5, 20, 36, 10, 10, 20]
        },
        {
            "name": '营收',
            "type": 'bar',
            "data": [15, 50, 76, 30, 20, 60]
        }]
    return JsonResponse({
        "status": True,
        'data': {
            "legend": legend,
            "series": series,
            "xAxis": xAxis,
        }

    })


def chart_pie(request):
    data = [
        {'value': 1048, 'name': 'IT部门'},
        {'value': 735, 'name': '人事部门'},
        {'value': 580, 'name': '财务部门'},
        {'value': 484, 'name': '业务部门'},
        {'value': 300, 'name': '公关部门'},
    ]
    return JsonResponse({
        "status": True,
        'data': data

    })


def chart_line(request):
    legend = ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
    xAxis = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    series = [
        {
            'name': 'Email',
            'type': 'line',
            'stack': 'Total',
            'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
            'name': 'Union Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [220, 182, 191, 234, 290, 330, 310]
        },
        {
            'name': 'Video Ads',
            'type': 'line',
            'stack': 'Total',
            'data': [150, 232, 201, 154, 190, 330, 410]
        }, ]
    return JsonResponse({
        "status": True,
        'data': {
            "legend": legend,
            "series": series,
            "xAxis": xAxis,
        }

    })
