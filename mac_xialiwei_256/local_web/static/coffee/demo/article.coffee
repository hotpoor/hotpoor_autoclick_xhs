root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs

$ ->
    console.log "article coffee"

    $("body").on "click",".get_info",(evt)->
        dom  = $(this)
        dom.text("解析中")
        short_link_val = $("input[data-name=short_link]").val()
        short_link = "http://"+short_link_val.split("，")[1].split("http://")[1]
        $.ajax
            url:"/api/tool/article/get_info"
            type: "GET"
            dataType: "json"
            data:
                short_link:short_link
            success:(data)->
                dom.text("查询")
                if data.info == "ok"
                    result = data.result
                    title = result["title"].toLocaleUpperCase().replaceAll("puco","口红博主").replaceAll("唇泥","唇釉")
                    content = result["content"].toLocaleUpperCase().replaceAll("puco","口红博主").replaceAll("唇泥","唇釉")
                    $("input[data-name=json_file]").val(result["t"])
                    $("input[data-name=article_title]").val(title)
                    $("textarea[data-name=article_content]").val(content)
                    $(".line_images").empty()
                    time_now = (new Date()).getTime()
                    for i in result["image_links"]
                        $(".line_images").append """
                            <div><img class="line_images_div_img" src="#{i}"></div>
                        """
                    $(".line_author_info_img").attr "src",result["user_headimgurl"]
                    $(".line_author_info_name").text result["user_name"]
            error:(data)->
                dom.text("解析失败")
    $("body").on "click",".get_json",(evt)->
        dom  = $(this)
        dom.text("解析中")

        $.ajax
            url:"/api/tool/article/get_json"
            type: "GET"
            dataType: "json"
            data:
                t:$("input[data-name=json_file]").val()
            success:(data)->
                dom.text("查询")
                if data.info == "ok"
                    result = data.result
                    title = result["title"].toLocaleUpperCase().replaceAll("puco","口红博主").replaceAll("唇泥","唇釉")
                    content = result["content"].toLocaleUpperCase().replaceAll("puco","口红博主").replaceAll("唇泥","唇釉")
                    $("input[data-name=article_title]").val(title)
                    $("textarea[data-name=article_content]").val(content)
                    $(".line_images").empty()
                    time_now = (new Date()).getTime()
                    for i in result["image_links"]
                        $(".line_images").append """
                            <div><img class="line_images_div_img" src="#{i}"></div>
                        """
                    $(".line_author_info_img").attr "src",result["user_headimgurl"]
                    $(".line_author_info_name").text result["user_name"]
            error:(data)->
                dom.text("解析失败")