var ball_opened = false;

function autoheight() {
    $('body').height($(window).height());
}
function ball_open() {
    if(!ball_opened){
        $('#ball-redhalf').animate({bottom: '40%'}, 800);
        $('#ball-whitehalf').animate({top: '40%'}, 800);
        $('#main-container').animate({opacity: '1'}, 800, function () {
            ball_opened = true;
        });
    }
    else {
        $('#ball-redhalf').animate({bottom: '0'}, 800);
        $('#ball-whitehalf').animate({top: '0'}, 800);
        $('#main-container').animate({opacity: '0'}, 800, function () {
            ball_opened = false;
        });
    }
}
$(document).ready(function (){
        $(window).resize(autoheight);
        $('.ball-half').click(ball_open);
        autoheight();
    }
);

