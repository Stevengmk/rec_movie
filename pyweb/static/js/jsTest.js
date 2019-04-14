var myChart1 = echarts.init(document.getElementById('charts_1'))
var options1 = {
    title:{
        // text:"科幻电影排行榜"
    },
    legend: {
        data:['评分']
    },
    tooltip:{

    },
    xAxis: {
        data:[],
        axisLabel: {
            interval:0,
            rotate:40
        }
    },
    yAxis: {},
    series: [
        {
        name:'评分',
        type:'bar',
        data:[]
        }
    ]
}
myChart1.setOption(options1)


var myChart2 = echarts.init(document.getElementById('charts_2'))
var options2 = {
    title:{
        // text:"科幻电影排行榜"
    },
    legend: {
        data:['评分']
    },
    tooltip:{

    },
    xAxis: {
        data:[],
        axisLabel: {
            interval:0,
            rotate:40
        }
    },
    yAxis: {},
    series: [
        {
        name:'评分',
        type:'bar',
        data:[]
        }
    ]
}
myChart2.setOption(options2)


var myChart3 = echarts.init(document.getElementById('charts_3'))
var options3 = {
    title:{
        // text:"科幻电影排行榜"
    },
    legend: {
        data:['评分']
    },
    tooltip:{

    },
    xAxis: {
        data:[],
        axisLabel: {
            interval:0,
            rotate:40
        }
    },
    yAxis: {},
    series: [
        {
        name:'评分',
        type:'bar',
        data:[]
        }
    ]
}
myChart3.setOption(options3)



var myChart4 = echarts.init(document.getElementById('charts_4'))
var options4 = {
    title:{
        // text:"科幻电影排行榜"
    },
    legend: {
        data:['评分']
    },
    tooltip:{

    },
    xAxis: {
        data:[],
        axisLabel: {
            interval:0,
            rotate:40
        }
    },
    yAxis: {},
    series: [
        {
        name:'评分',
        type:'bar',
        data:[]
        }
    ]

}
myChart4.setOption(options4)



// var name=[]
// var val=[]
//清理了一下Chrome的缓存之后ajax就好了
$("#rank_test").click(function () {
    $.ajax({
        url:"/top/",
        type: "Get",
        dataType:"json",
        async: true,
        success:function (result) {
            //作用域的问题，var name和val如果声明在ajax外部的话push函数会报错。如果想查看错误原因，需要在ajax内部调用typeof name
            var name1=[]
            var val1=[]
            var url1=[]
            var name2=[]
            var val2=[]
            var url2=[]
            var name3=[]
            var val3=[]
            var url3=[]
            var name4=[]
            var val4=[]
            var url4=[]
            for(var i=0;i<10;i++){
                name1.push(result[i].name)
                val1.push(result[i].val)
                url1.push(result[i].url)
            }
            for(var j=10;j<20;j++){
                name2.push(result[j].name)
                val2.push(result[j].val)
                url2.push(result[j].url)
            }
            for(var k=20;k<30;k++){
                name3.push(result[k].name)
                val3.push(result[k].val)
                url3.push(result[k].url)
            }
            for(var m=30;m<40;m++){
                name4.push(result[m].name)
                val4.push(result[m].val)
                url4.push(result[m].url)
            }
            myChart1.setOption({
                xAxis: {
                    data: name1
                },
                series: [{
                    name:"评分",
                    data:val1,url1
                }]
            })
            myChart2.setOption({
                xAxis: {
                    data: name2
                },
                series: [{
                    name:"评分",
                    data:val2,url2
                }]
            })
            myChart3.setOption({
                xAxis: {
                    data: name3
                },
                series: [{
                    name:"评分",
                    data:val3,url3
                }]
            })
            myChart4.setOption({
                xAxis: {
                    data: name4
                },
                series: [{
                    name:"评分",
                    data:val4,url4
                }]
            })


            myChart1.on('click',function (param) {
                console.log(param.seriesIndex)
                // let url = param.data.url
                // console.log(url)
                // alert(param.data.url1)
                for(let i=0;i<10;i++){
                        if(param.seriesIndex==i+1){
                            console.log(url1[i])
                        }
                }
                // window.location.href = url
            });


            myChart2.on('click',function (param) {
                console.log(param.seriesIndex)
                // let url = param.data.url
                // console.log(url)
                // alert(param.data.url2)
                for(let i=0;i<10;i++){
                        if(param.seriesIndex==i+1){
                            console.log(url2[i])
                        }
                }
                // window.location.href = url
            });


            myChart3.on('click',function (param) {
                console.log(param.seriesIndex)
                // let url = param.data.url
                // console.log(url)
                // alert(param.data.url3)
                for(let i=0;i<10;i++){
                        if(param.seriesIndex==i+1){
                            console.log(url3[i])
                        }
                }
                // window.location.href = url
            })
            myChart4.on('click',function (param) {
                console.log(param.seriesIndex)
                // let url = param.data.url
                // console.log(param)
                // alert(param.data.url4)
                    for(let i=0;i<10;i++){
                        if(param.seriesIndex==i+1){
                            console.log(url4[i])
                        }
                    }

                // window.location.href = url

            })
        },
        error:function (errorMsg) {
            alert("bar charts failed")
            myChart1.hideLoading()
        }
    })
})


$("#target_test").click(function(){
    $.ajax({
            url:"/test/",
            type:"GET",
            dataType:"json",
            async:true,
            // data:$("#my_form").serialize(),
            data:{user:$("#rec_text").serialize()},
            // headers:{"X-CSRFToken":$.cookie("csrftoken")},
            success:function (result) {
                // console.log(result)
                var html = result["movieURL"]
                var img = result["img_url"]
                var title = result["Name"]
                var type = result["type"]
                var o1 = html[0]
                var i1 = img[0]
                var t1 = title[0]
                var p1 = type[0]
                var o2 = html[1]
                var i2 = img[1]
                var t2 = title[1]
                var p2 = type[1]
                var o3 = html[2]
                var i3 = img[2]
                var t3 = title[2]
                var p3 = type[2]
                var o4 = html[3]
                var i4 = img[3]
                var t4 = title[3]
                var p4 = type[3]
                document.getElementById("rec_1").setAttribute("href",o1)
                document.getElementById("img_1").setAttribute("src",i1)
                document.getElementById("text_1").setAttribute("href",o1)
                $("#text_1").html(t1+"<br>" +"类型 :  "+p1)
                document.getElementById("rec_2").setAttribute("href",o2)
                document.getElementById("img_2").setAttribute("src",i2)
                document.getElementById("text_2").setAttribute("href",o2)
                $("#text_2").html(t2+"<br>" +"类型 :  "+p2)
                document.getElementById("rec_3").setAttribute("href",o3)
                document.getElementById("img_3").setAttribute("src",i3)
                document.getElementById("text_3").setAttribute("href",o3)
                $("#text_3").html(t3+"<br>" +"类型 :  "+p3)
                document.getElementById("rec_4").setAttribute("href",o4)
                document.getElementById("img_4").setAttribute("src",i4)
                document.getElementById("text_4").setAttribute("href",o4)
                $("#text_4").html(t4+"<br>" +"类型 :  "+p4)
            },
             error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status)
                alert(XMLHttpRequest.readyState)
                alert(textStatus)

            },

         });
})

// $('#my_form').submit(function () {
//     $.ajax({
//         url:'',
//     })
// })





// var jsondata = $.parseJSON(result)
                // var obj = result.parseJSON()
                // var namekey="Name"
                // console.log(result[namekey])
                // console.log(result["movieURL"])
                // console.log(result)
                // console.log(Object.keys(result))
// html+="<a href=''+o+''>"+o+"</a>"
                // $("#rec_1").html(o)
                // console.log(typeof result)
                // for(var i=0;i<result.length;i++){
                //     console.log(result[i])
                // }