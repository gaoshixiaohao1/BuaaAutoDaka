# coding=utf-8
import socket


config = {
    "users": [
        {
            "username": "统一认证账号",
            "password": "统一认证密码",
            "realname": "名字",
            "number": "学号"
        },
        {
            "username": "如果有多个，这样添加",
            "password": "",
            "realname": "",
            "number": ""
        }
    ],
    "submit_data": {
        "sfzs": "1",        # 是否住宿，1住0不住
        "bzxyy": "",          # 不在校原因，不住宿时要填写，1开始为：临时出校，寒假返乡，境外科研，境内出差实习，请假，其他
        "bzxyy_other": "",             # 不在校原因
        "brsfzc": "1",                 # 本人是否正常
        "tw": "",
        "sfcxzz": "",
        "zdjg": "",
        "zdjg_other": "",
        "sfgl": "",
        "gldd": "",
        "gldd_other": "",
        "glyy": "",
        "glyy_other": "",
        "gl_start": "",
        "gl_end": "",
        "sfmqjc": "",
        "sfzc_14": "1",                # 14日内正常
        "sfqw_14": "",
        "sfqw_14_remark": "",
        "sfzgfx": "",
        "sfzgfx_remark": "",
        "sfjc_14": "",
        "sfjc_14_remark": "",
        "sfjcqz_14": "",
        "sfjcqz_14_remark": "",
        "sfgtjz_14": "",
        "sfgtjz_14_remark": "",
        "szsqqz": "",
        "sfyqk": "",
        "szdd": "1",                   # 所在地点
        "area": "北京市 海淀区",
        "city": "北京市",
        "province": "北京市",
        "address": "北京市海淀区花园路街道北京航空航天大学学生公寓13号楼北京航空航天大学学院路校区",
        "geo_api_info": "{\"type\":\"complete\",\"info\":\"SUCCESS\",\"status\":1,\"XDa\":\"jsonp_229421_\",\"position\":{\"Q\":39.98488,\"R\":116.34623999999997,\"lng\":116.34624,\"lat\":39.98488},\"message\":\"Get ipLocation success.Get address success.\",\"location_type\":\"ip\",\"accuracy\":null,\"isConverted\":true,\"addressComponent\":{\"citycode\":\"010\",\"adcode\":\"110108\",\"businessAreas\":[{\"name\":\"五道口\",\"id\":\"110108\",\"location\":{\"Q\":39.99118,\"R\":116.34157800000003,\"lng\":116.341578,\"lat\":39.99118}}],\"neighborhoodType\":\"生活服务;生活服务场所;生活服务场所\",\"neighborhood\":\"北京航空航天大学\",\"building\":\"北京航空航天大学学生公寓13号楼\",\"buildingType\":\"商务住宅;住宅区;宿舍\",\"street\":\"北四环中路\",\"streetNumber\":\"248楼\",\"country\":\"中国\",\"province\":\"北京市\",\"city\":\"\",\"district\":\"海淀区\",\"township\":\"花园路街道\"},\"formattedAddress\":\"北京市海淀区花园路街道北京航空航天大学学生公寓13号楼北京航空航天大学学院路校区\",\"roads\":[],\"crosses\":[],\"pois\":[]}",
        "gwdz": "",
        "is_move": "0",
        "move_reason": "",
        "move_remark": "",
    },
    "user-agent": {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'app.buaa.edu.cn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    },
    "login_url": 'https://app.buaa.edu.cn/uc/wap/login/check',  # 登录的链接
    "submit_url": 'https://app.buaa.edu.cn/buaaxsncov/wap/default/save',  # 打卡的链接
    "loki_config": {
        "url": "http://116.62.247.0:3100/loki/api/v1/push",
        "tags": {
            "application": "auto-daka-app",
            "pc": socket.gethostname()
        },
        "version": "1"
    }  # 日志相关
}
