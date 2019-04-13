// var myChart = echarts.init(document.getElementById('main-gmk'));
//
// // 指定图表的配置项和数据
// var option = {
//     title: {
//         text: ''
//     },
//     tooltip: {},
//     legend: {
//         data:['销量']
//     },
//     xAxis: {
//         data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
//     },
//     yAxis: {},
//     series: [{
//         name: '销量',
//         type: 'bar',
//         data: [5, 20, 36, 10, 10, 20]
//     }]
// };
//
// // 使用刚指定的配置项和数据显示图表。
// myChart.setOption(option);

//清理了一下Chrome的缓存之后ajax就好了
$("#target_test").click(function(){
    $.ajax({
            url:"/test/",
            type:"GET",
            dataType:"json",
            async:true,
            success:function (result) {

                var html = result["movieURL"]
                var img = result["img_url"]
                var title = result["Name"]
                var type = result["type"]
                var o1 = html[0]
                var i1 = img[0]
                var t1 = title[0]
                var p1 = type[0]
                document.getElementById("rec_1").setAttribute("href",o1)
                document.getElementById("img_1").setAttribute("src",i1)
                document.getElementById("text_1").setAttribute("href",o1)
                $("#text_1").append(t1+"<br>" +"类型 :  "+p1)
            },
             error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert(XMLHttpRequest.status)
                alert(XMLHttpRequest.readyState)
                alert(textStatus)

            },

         });
})


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