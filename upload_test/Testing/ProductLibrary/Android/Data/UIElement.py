#coding=utf-8

ui_element = {}

element_system = {
    "btn_clear_notification": {"id_": "com.android.systemui:id/clear_all_button",

    },
}

upload_page = {
    #resourceId可以用find_element_by_id来进行定位
    'http': {
        'name': 'http'},
    'https': {
        'name': 'https'},

}

file_select_page = {
    "file_manager":{
        "name":"Downloads"
    },
     "file0":{
        "name":"QQ_156.apk"
    },
    "file1":{
        "name":"PPTVjuli_98.apk"
    },

    "file2":{
        "name":"appsearch_AndroidPhone_1000364c.apk"
    },

    "file3":{
        "name":"1-140522163547-1.jpg"
    },

     "file4":{
        "name":"1-140522163547.jpg"
    },
      "file5":{
        "name":"BaiduMusic-webappheader.apk"
    },
        "Button_confirm":{
            "name":"确定"

        },

}


ui_element.update(element_system)
ui_element.update(upload_page)
ui_element.update(file_select_page)



def get_selectors(element_key):
    selector = ""
    if ui_element.has_key(element_key):
        for prop, value in ui_element[element_key].items():
            if prop == "child": continue
            if type(value) == str or type(value) == unicode:
                selector += '%s="%s",' % (prop, value)
            else:
                selector += '%s=%s,' % (prop, value)
        selector = selector[:-1] # remove the last comma
    else:
        pass
    return selector


if __name__ == '__main__':
    print get_selectors('txt_username')