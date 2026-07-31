function randomColor() {
    var hue = Math.floor(Math.random() * 360);
    return 'hsl(' + hue + ', 80%, 60%)';
}

if (typeof jQuery !== 'undefined') {
    (function($) {
        var a_idx = 0;
        var a = new Array("富强", "民主", "文明", "和谐", "自由", "平等", "公正", "法治", "爱国", "敬业", "诚信", "友善");

        $("body").click(function(e) {
            var $i = $("<span/>").text(a[a_idx]);
            a_idx = (a_idx + 1) % a.length;

            var x = e.pageX,
                y = e.pageY;
            $i.css({
                "z-index": 99999,
                "top": y - 20,
                "left": x,
                "position": "absolute",
                "font-weight": "bold",
                "color": randomColor(),
                "font-size": "15px",
                "pointer-events": "none"
            });
            $("body").append($i);
            $i.animate({
                "top": y - 180,
                "opacity": 0
            }, 1500, function() {
                $i.remove();
            });
        });
    })(jQuery);
}
