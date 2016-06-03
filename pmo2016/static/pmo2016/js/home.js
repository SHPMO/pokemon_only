window.onload = function () {
    var static_path = '/static/pmo2016/';
    var data = {
        map: [
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, -1, -1, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, -1, 0],
            [-1, 0, 0, 0, 0, 0, -1, 0]
        ],
        totalImages: [3, 2, 3, 2]
    };

    var gb = document.getElementById('gb');
    var screen = document.getElementById('gb-screen');
    window.onresize = function () {
        if (gb.clientWidth / 287 * 413 <= gb.clientHeight) {
            vm.unit = gb.clientWidth / 287;
        } else {
            vm.unit = gb.clientHeight / 413;
        }
    };

    var vm = new Vue({
        el: '#main-container',
        data: {
            unit: 0,
            hero: {
                direction: 0,
                status: 0,
                x: 3,
                y: 3
            },
            dialog: {
                status: 0
            }
        },
        computed: {
            cell: function () {
                return 16 * this.unit;
            },
            heroImage: function () {
                return static_path + 'images/hero-' + this.hero.direction + '-' + this.hero.status + '.svg';
            },
            heroStyle: function () {
                return {
                    width: this.cell + 'px',
                    height: this.cell + 'px',
                    left: 4 * this.cell + 'px',
                    top: 3.75 * this.cell + 'px'
                }
            },
            screenStyle: function () {
                return {
                    left: gb.clientWidth / 2 - 76.5 * this.unit + 'px',
                    top: gb.clientHeight - 344 * this.unit + 'px',
                    width: 160 * this.unit + 'px',
                    height: 144 * this.unit + 'px',
                    backgroundSize: 128 * this.unit + 'px, ' + 128 * this.unit + 'px',
                    backgroundPositionX: this.cell * (4 - this.hero.x) + 'px',
                    backgroundPositionY: this.cell * (4 - this.hero.y) + 'px'
                }
            },
            buttonsStyle: function () {
                return {
                    top: gb.clientHeight - 294 * this.unit + 'px',
                    height: 150 * this.unit + 'px'
                }
            }
        },
        methods: {
            buttonPressed: function (event) {
                var x = event.offsetX / this.unit, y = event.offsetY / this.unit;
                if (x >= 56.333 && x <= 83.333) {
                    if (y >= 0 && y <= 22)
                        pressUp();
                    else if (y >= 49 && y <= 71)
                        pressDown();
                } else if (y >= 22 && y <= 49) {
                    if (x >= 34.333 && x <= 56.333)
                        pressLeft();
                    else if (x >= 83.333 && x <= 105.333)
                        pressRight();
                } else if (Math.pow(x - 250.119, 2) + Math.pow(y - 25.071, 2) <= Math.pow(14.572, 2)) {
                    pressA();
                } else if (Math.pow(x - 214.904, 2) + Math.pow(y - 46.929, 2) <= Math.pow(14.571, 2)) {
                    pressB();
                } else if (y >= 99 && y <= 114.62) {
                    if (x >= 100 && x <= 132.47)
                        pressSelect();
                    else if (x >= 141 && x <= 173.47) {
                        pressStart();
                    }
                }
            }
        }
    });
    window.vm = vm;

    var moving = null;

    function move(direction) {
        if (moving)
            return;
        if (direction != vm.hero.direction) {
            vm.hero.direction = direction;
            return;
        }
        var dx = 0, dy = 0;
        switch (vm.hero.direction) {
            case 0:
                dy = 1;
                break;
            case 1:
                dx = -1;
                break;
            case 2:
                dy = -1;
                break;
            case 3:
                dx = 1;
                break;
        }
        var y = vm.hero.y + dy;
        var x = vm.hero.x + dx;
        if (y < 0 || x < 0 || y > 7 || x > 7 || data.map[y][x] != 0) {
            return;
        }
        (function go(status) {
            if (status == 3) {
                moving = null;
                vm.hero.x = Math.round(vm.hero.x);
                vm.hero.y = Math.round(vm.hero.y);
                vm.hero.status = 0;
                return;
            }
            vm.hero.x += dx / 3;
            vm.hero.y += dy / 3;
            vm.hero.status += 1;
            vm.hero.status %= data.totalImages[vm.hero.direction];
            moving = setTimeout(go, 300, status + 1);
        })(0);
    }

    function pressUp() {
        move(2);
    }

    function pressDown() {
        move(0);
    }

    function pressLeft() {
        move(1);
    }

    function pressRight() {
        move(3);
    }

    function pressA() {

    }

    function pressB() {

    }

    function pressSelect() {

    }

    function pressStart() {

    }

    window.onresize();
};
