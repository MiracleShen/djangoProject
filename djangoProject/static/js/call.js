function makecall(callnum) {
    $.ajax({
        crossDomain: true,
        // contentType:"application/json;charset=utf-8",#这一段不能加，加上了就会导致csrf_token丢失
        headers: {
            "Access-Control-Allow-Origin": "http://127.0.0.1:8000",
            "Access-Control-Allow-Headers": "Authentication",
            "Access-Control-Allow-Headers": "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        },
        method: 'POST',
        type: 'post',
        url: '/makecall/',
        dataType: "json",
        data: {
            destNumber: callnum,
            csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success: function (data) {
            //这里返回请求成功的数据，数据包含在data中
            console.log(data)
            if (data['returnInfo'] = 'Succeeded!') {
                // alert("拨打电话成功！")
            } else {
                alert("拨打电话失败！失败原因是：" + data['returnCode'])
            }
        },
        error: function (res,textStatus, errorThrown) {
            //这里返回请求失败得到的数据，数据包含在res中
            console.log(res)
            alert(res.responseText);
            alert(callnum);
        }
    })

}
