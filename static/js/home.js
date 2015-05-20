var ball_opened = false;

function ball_open() {
    if(!ball_opened){
        $('#ball-redhalf').animate({top: '-43%'}, 800);
        $('#ball-whitehalf').animate({bottom: '-43%'}, 800);
        $('#main-content-bg').animate({opacity: '1'}, 800, function () {
            ball_opened = true;
        });
    }
    else {
        $('#ball-redhalf').animate({top: '0'}, 800);
        $('#ball-whitehalf').animate({bottom: '0'}, 800);
        $('#main-content-bg').animate({opacity: '0'}, 800, function () {
            ball_opened = false;
        });
    }
}
$(document).ready(function (){
        $('.ball-half').click(ball_open);
    }
);

