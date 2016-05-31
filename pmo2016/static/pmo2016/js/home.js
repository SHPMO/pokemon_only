window.onload = function () {
    var static_path = "/static/pmo2016/";
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
        ]
    };
    var vm = new Vue({
        el: '#main-container',
        data: {
            cell: 0,
            hero: {
                x: 3,
                y: 6,
                direction: 0,
                status: 0
            }
        },
        computed: {
            heroImage: function () {
                return static_path + "images/hero-" + this.hero.direction + "-" + this.hero.status + ".svg";
            },

            heroObject: function () {
                return {
                    width: this.cell + "px",
                    height: this.cell + "px",
                    left: this.hero.x * this.cell + "px",
                    top: this.hero.y * this.cell + "px"
                }
            }
        },
        methods: {}
    });
    window.vm = vm;


    var gb = document.getElementById('gb');
    var screen = document.getElementById('gb-screen');
    window.onresize = function () {
        if (gb.clientWidth / 287 * 413 <= gb.clientHeight) {
            var unit = gb.clientWidth / 287;
        } else {
            var unit = gb.clientHeight / 413;
        }
        screen.style.left = (gb.clientWidth / 2 - 60.5 * unit) + "px";
        screen.style.top = (gb.clientHeight - 328 * unit) + "px";
        screen.style.width = 128 * unit + "px";
        screen.style.height = 128 * unit + "px";
        vm.cell = 16 * unit;
    };
    window.onresize();
};
