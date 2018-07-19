var ball_opened = false;
var moving = false;

function ball_open() {
    if(moving) return;
    moving = true;
    if(!ball_opened){
        $('#ball-redhalf').animate({top: '-43%'}, 800);
        $('#ball-whitehalf').animate({bottom: '-43%'}, 800, function () {
            moving = false;
            ball_opened = true;
        });
        $('#main-content-bg').animate({opacity: '1'}, 400);
    }
    else {
        $('#ball-redhalf').animate({top: '0'}, 800);
        $('#ball-whitehalf').animate({bottom: '0'}, 800, function () {
            moving = false;
            ball_opened = false;
        });
        $('#main-content-bg').animate({opacity: '0'}, 400);
    }
}

function show_pmos(toshow) {
    return function () {
        var main = $('#main-hrefs');
        var sub = $('#sub-hrefs');
        if (toshow){
            main.addClass('nodisplay-object');
            sub.removeClass('nodisplay-object');
        } else {
            main.removeClass('nodisplay-object');
            sub.addClass('nodisplay-object');
        }
    }
}

$(document).ready(function (){
        $('.ball-half').click(ball_open);
        $('#href-pmos').click(show_pmos(true));
        $('#href-back').click(show_pmos(false));
    }
);

