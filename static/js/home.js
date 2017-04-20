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
$(document).ready(function (){
        $('.ball-half').click(ball_open);
    }
);

