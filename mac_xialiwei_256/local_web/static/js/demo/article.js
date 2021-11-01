// Generated by CoffeeScript 2.3.0
(function() {
  var Hs, root;

  root = typeof exports !== "undefined" && exports !== null ? exports : this;

  // !!!! Hotpoor root object
  root.Hs || (root.Hs = {});

  Hs = root.Hs;

  $(function() {
    console.log("article coffee");
    $("body").on("click", ".get_info", function(evt) {
      var dom, short_link, short_link_val;
      dom = $(this);
      dom.text("解析中");
      short_link_val = $("input[data-name=short_link]").val();
      short_link = "http://" + short_link_val.split("，")[1].split("http://")[1];
      return $.ajax({
        url: "/api/tool/article/get_info",
        type: "GET",
        dataType: "json",
        data: {
          short_link: short_link
        },
        success: function(data) {
          var content, i, j, len, ref, result, time_now, title;
          dom.text("查询");
          if (data.info === "ok") {
            result = data.result;
            title = result["title"].toLocaleUpperCase().replaceAll("PUCO", "口红博主").replaceAll("唇泥", "唇釉");
            content = result["content"].toLocaleUpperCase().replaceAll("PUCO", "口红博主").replaceAll("唇泥", "唇釉");
            $("input[data-name=json_file]").val(result["t"]);
            $("input[data-name=article_title]").val(title);
            $("textarea[data-name=article_content]").val(content);
            $(".line_images").empty();
            time_now = (new Date()).getTime();
            ref = result["image_links"];
            for (j = 0, len = ref.length; j < len; j++) {
              i = ref[j];
              $(".line_images").append(`<div><img class="line_images_div_img" src="${i}"></div>`);
            }
            $(".line_author_info_img").attr("src", result["user_headimgurl"]);
            return $(".line_author_info_name").val(result["user_name"]);
          }
        },
        error: function(data) {
          return dom.text("解析失败");
        }
      });
    });
    $("body").on("click", ".get_json", function(evt) {
      var dom;
      dom = $(this);
      dom.text("解析中");
      return $.ajax({
        url: "/api/tool/article/get_json",
        type: "GET",
        dataType: "json",
        data: {
          t: $("input[data-name=json_file]").val()
        },
        success: function(data) {
          var content, i, j, len, ref, result, time_now, title;
          dom.text("查询");
          if (data.info === "ok") {
            result = data.result;
            title = result["title"].toLocaleUpperCase().replaceAll("PUCO", "口红博主").replaceAll("唇泥", "唇釉");
            content = result["content"].toLocaleUpperCase().replaceAll("PUCO", "口红博主").replaceAll("唇泥", "唇釉");
            $("input[data-name=article_title]").val(title);
            $("textarea[data-name=article_content]").val(content);
            $(".line_images").empty();
            time_now = (new Date()).getTime();
            ref = result["image_links"];
            for (j = 0, len = ref.length; j < len; j++) {
              i = ref[j];
              $(".line_images").append(`<div><img class="line_images_div_img" src="${i}"></div>`);
            }
            $(".line_author_info_img").attr("src", result["user_headimgurl"]);
            return $(".line_author_info_name").val(result["user_name"]);
          }
        },
        error: function(data) {
          return dom.text("解析失败");
        }
      });
    });
    return $("body").on("click", ".copy_plus", function(evt) {
      var copy_aim, dom;
      dom = $(this);
      copy_aim = dom.parents(".line").find(".copy_plus_content").select();
      return document.execCommand("Copy");
    });
  });

}).call(this);
