window.onload = function () {

    Vue.config.delimiters = ['<<', '>>'];
    Vue.config.unsafeDelimiters = ['{!!', '!!}']

    var static_path = '/static/pmo2016/';
    var data = {
        map: [
            [-1, -1, -1, -1, -1, -1, -1, -1],
            ['computer', 'table', 'table', 0, 0, 0, 0, 'stair'],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 'tv', 0, 0, 0, 0],
            [0, 0, 0, 'wiiu', 0, 0, 0, 0],
            ['bed', 0, 0, 0, 0, 0, 'tree', 0],
            ['bed', 0, 0, 0, 0, 0, 'tree', 0]
        ],
        totalImages: [4, 2, 4, 2],
        computer: {
            type: 2,
            message: ['你打开了电脑', '', '', '要做什么？'],
            options: ['PMO官博', '对战报名', '摊位申请', '关闭'],
            hrefs: ['http://weibo.com/SHPMO', 'register/battle/', 'register/stall/'],
            callback: function (notcancelled) {
                if (notcancelled && vm.select.status != 3) {
                    window.open(this.hrefs[vm.select.status], '_blank');
                }
                waiting = null;
                clearDialog();
            }
        },
        stair: {
            type: 1,
            message: ['出发去PMO吧！'],
            yes: '是',
            no: '否',
            callback: function (notcancelled) {
                if (notcancelled && vm.yesno.status == 1) {
                    window.open('baseinfo/place/', '_blank');
                }
                waiting = null;
                clearDialog();
            }
        },
        table: {
            type: 1,
            message: ['桌上什么都没有...', '', '',
                '...', '', '',
                '桌底好像有东西？'],
            yes: '捡起',
            no: '无视',
            items: ['不变石', '金珠', '精灵球', '大师球', '伤药', '奇异甜食'],
            getItem: {
                type: 0,
                message: [
                    ''
                ],
                callback: function (notcancelled) {
                    waiting = null;
                    clearDialog();
                }
            },
            callback: function (notcancelled) {
                if (notcancelled && vm.yesno.status == 1) {
                    this.getItem.message[0] = '——你得到了一个...' +
                        this.items[Math.floor(this.items.length * Math.random())] + '！';
                    trigger(this.getItem);
                } else {
                    clearDialog();
                }
                waiting = null;
            }
        },
        tree: {
            type: 0,
            message: ['只是一盆普通的景观植物'],
            callback: function (notcancelled) {
                waiting = null;
                clearDialog();
            }
        },
        tv: {
            type: 0,
            message: [
                '「嘻嘻嘻嘻嘻——」', '', '',
                '？... ...', '', '',
                '好像听到了奇怪的笑声'
            ],
            callback: function (notcancelled) {
                waiting = null;
                clearDialog();
            }
        },
        wiiu: {
            type: 0,
            message: [
                '你在玩宝可梦拳', '... ...',
                '怪力的肌肉实在太美了！', '',
                '你心满意足准备出发去PMO'
            ],
            callback: function (notcancelled) {
                waiting = null;
                clearDialog();
            }
        },
        bed: {
            type: 1,
            message: ['要睡觉吗？'],
            yes: '是',
            no: '否',
            callback: function (notcancelled) {
                if (notcancelled && vm.yesno.status == 1) {
                    trigger({
                        type: 0,
                        message: [
                            '检测连接到PGL', '... ...', '',
                            'error-code：006-0112', '... ...', '',
                            'SAD'
                        ],
                        callback: function (notcancelled) {
                            waiting = null;
                            clearDialog();
                        }
                    })
                } else {
                    clearDialog();
                }
                waiting = null;
            }
        },
        menu: {
            type: 3,
            options: [
                {
                    name: '基本信息',
                    href: 'baseinfo/',
                    options: [
                        {name: '活动时间与当日行程', href: 'schedule/'},
                        {name: '场地信息', href: 'place/'},
                        {name: '票务信息', href: 'ticket/'},
                        {name: '奖品一览', href: 'prize/'}
                    ]
                }, {
                    name: '现场摊位',
                    href: 'stall/',
                    options: [
                        {name: '现场摊位', href: 'diagram/'},
                        {name: '参展社团', href: 'circle/'},
                        {name: '参展贩售物', href: 'item/'}
                    ]
                }, {
                    name: '现场活动',
                    href: 'event/',
                    options: [
                        {name: '联机对战', href: 'battle/'},
                        {name: '场地活动', href: 'venue/'},
                        {name: '幸运抽奖', href: 'raffle/'}
                    ]
                }, {
                    name: '报名申请',
                    href: 'register/',
                    options: [
                        {name: '对战报名', href: 'battle/'},
                        {name: '摊位申请', href: 'stall/'}
                    ]
                }, {
                    name: 'QA留言板',
                    href: 'qabook/',
                    options: [
                        {name: '常见Q&A', href: 'faq/'},
                        {name: '参展礼仪与建议', href: 'manner/'},
                        {name: '留言板', href: 'guestbook/'}
                    ]
                }, {name: '关闭'}
            ],
            callback: function (notcancelled) {
                if (notcancelled && vm.menu.status != 5) {
                    var option = this.options[vm.menu.status];
                    var list = '';
                    for (var i = 0; i < option.options.length; ++i) {
                        var link = option.href + option.options[i].href;
                        list += '<a href="' + link + '" target="_blank">' + option.options[i].name + '</a><br>';
                    }
                    vm.menu.submenu.message = list;
                    vm.menu.submenu.status = 0;
                    waiting = this.submenu;
                } else {
                    clearDialog();
                    waiting = null;
                }
            },
            submenu: {
                type: 4,
                callback: function (notcancelled) {
                    if (notcancelled) {
                        var link = data.menu.options[vm.menu.status].href +
                            data.menu.options[vm.menu.status].options[vm.menu.submenu.status].href;
                        window.open(link, '_blank');
                        menuLast = vm.menu.status;
                        waiting = null;
                        clearDialog();
                    } else {
                        waiting = data.menu;
                        vm.menu.submenu.status = -1;
                    }
                }
            }

        }
    };

    var gb = document.getElementById('gb');
    var screen = document.getElementById('gb-screen');
    window.onresize = function () {
        vm.unit -= 1;
        if (gb.clientWidth / 287 * 450 <= gb.clientHeight) {
            vm.unit = gb.clientWidth / 287;
        } else {
            vm.unit = gb.clientHeight / 450;
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
            select: {
                status: -1,
                options: []
            },
            yesno: {
                status: -1,
                yes: null,
                no: null
            },
            dialog: {
                status: -1,
                message: "",
                cursor: false
            },
            menu: {
                status: -1,
                message: "",
                submenu: {
                    status: -1,
                    message: ""
                }
            },
            welcome: {
                bgLeftRight: false,
                bgYears: false,
                gb: false,
                pikachu: false,
                gbScreen: false,
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
                    display: this.power ? 'block' : 'none',
                    left: gb.clientWidth / 2 - 76.5 * this.unit + 'px',
                    top: gb.clientHeight - 381 * this.unit + 'px',
                    width: 160 * this.unit + 'px',
                    height: 144 * this.unit + 'px',
                    backgroundSize: 128 * this.unit + 'px, ' + 128 * this.unit + 'px',
                    backgroundPositionX: this.cell * (4 - this.hero.x) + 'px',
                    backgroundPositionY: this.cell * (4 - this.hero.y) + 'px',
                    fontSize: 11 * this.unit + 'px'
                }
            },
            buttonsStyle: function () {
                return {
                    top: gb.clientHeight - 331 * this.unit + 'px',
                    height: 150 * this.unit + 'px',
                    width: 287 * this.unit + 'px'
                }
            },
            selectStyle: function () {
                return {
                    display: this.select.status == -1 ? 'none' : 'block',
                    height: 80 * this.unit + 'px',
                    width: 96 * this.unit + 'px',
                    paddingTop: 9 * this.unit + 'px',
                    paddingLeft: 15 * this.unit + 'px',
                    paddingBottom: 12 * this.unit + 'px',
                    lineHeight: 16 * this.unit + 'px'
                }
            },
            selectCursorStyle: function () {
                return {
                    display: this.select.status == -1 ? 'none' : 'block',
                    height: 7 * this.unit + 'px',
                    width: 5 * this.unit + 'px',
                    left: 8 * this.unit + 'px',
                    top: (14 + 15.1 * this.select.status ) * this.unit + 'px'
                }
            },
            yesnoStyle: function () {
                return {
                    display: this.yesno.status == -1 ? 'none' : 'block',
                    bottom: 48 * this.unit + 'px',
                    height: 40 * this.unit + 'px',
                    width: 48 * this.unit + 'px',
                    paddingTop: 9 * this.unit + 'px',
                    paddingLeft: 15 * this.unit + 'px',
                    paddingBottom: 12 * this.unit + 'px',
                }
            },
            yesnoCursorStyle: function () {
                return {
                    display: this.yesno.status == -1 ? 'none' : 'block',
                    height: 7 * this.unit + 'px',
                    width: 5 * this.unit + 'px',
                    right: 34 * this.unit + 'px',
                    bottom: (59 + 11.5 * this.yesno.status ) * this.unit + 'px'
                }
            },
            dialogStyle: function () {
                return {
                    display: this.dialog.status == -1 ? 'none' : 'block',
                    height: 48 * this.unit + 'px',
                    width: 160 * this.unit + 'px',
                    padding: 12 * this.unit + 'px'
                }
            },
            dialogCursorStyle: function () {
                return {
                    display: this.dialog.cursor ? 'block' : 'none',
                    height: 5 * this.unit + 'px',
                    width: 7 * this.unit + 'px',
                    bottom: 12 * this.unit + 'px',
                    right: 12 * this.unit + 'px'
                }
            },
            menuStyle: function () {
                return {
                    display: this.menu.status == -1 ? 'none' : 'block',
                    height: 112 * this.unit + 'px',
                    width: 64 * this.unit + 'px',
                    paddingTop: 10 * this.unit + 'px',
                    paddingLeft: 12 * this.unit + 'px',
                    paddingBottom: 12 * this.unit + 'px',
                    lineHeight: 16 * this.unit + 'px'
                }
            },
            menuCursorStyle: function () {
                return {
                    display: this.menu.status == -1 ? 'none' : 'block',
                    height: 7 * this.unit + 'px',
                    width: 5 * this.unit + 'px',
                    right: 52 * this.unit + 'px',
                    top: (14 + 15.55 * this.menu.status ) * this.unit + 'px'
                }
            },
            submenuStyle: function () {
                return {
                    display: this.menu.submenu.status == -1 ? 'none' : 'block',
                    height: 88 * this.unit + 'px',
                    width: 128 * this.unit + 'px',
                    paddingTop: 10 * this.unit + 'px',
                    paddingLeft: 12 * this.unit + 'px',
                    paddingBottom: 12 * this.unit + 'px',
                    lineHeight: 16 * this.unit + 'px',
                    top: 16 * this.unit + 'px'
                }
            },
            submenuCursorStyle: function () {
                return {
                    display: this.menu.submenu.status == -1 ? 'none' : 'block',
                    height: 7 * this.unit + 'px',
                    width: 5 * this.unit + 'px',
                    left: 39 * this.unit + 'px',
                    top: (30 + 15.55 * this.menu.submenu.status ) * this.unit + 'px'
                }
            }
        },
        methods: {
            buttonPressed: function (event) {
                var x = event.offsetX / this.unit, y = event.offsetY / this.unit;
                console.log(x, y);
                if (x >= 56.333 && x <= 83.333 && y >= 0 && y <= 22) {
                    pressUp();
                } else if (x >= 56.333 && x <= 83.333 && y >= 49 && y <= 71) {
                    pressDown();
                } else if (y >= 22 && y <= 49 && x >= 34.333 && x <= 56.333) {
                    pressLeft();
                } else if (y >= 22 && y <= 49 && x >= 83.333 && x <= 105.333) {
                    pressRight();
                } else if (Math.pow(x - 250.119, 2) + Math.pow(y - 25.071, 2) <= Math.pow(14.572, 2)) {
                    pressA();
                } else if (Math.pow(x - 214.904, 2) + Math.pow(y - 46.929, 2) <= Math.pow(14.571, 2)) {
                    pressB();
                } else if (x >= 100 && x <= 132.47 && y >= 91 && y <= 106.62) {
                    pressSelect();
                } else if (x >= 141 && x <= 173.47 && y >= 91 && y <= 106.62) {
                    pressStart();
                }
            }
        },
        ready: function () {
            this.$el.style.display = "flex";
            this.welcome.bgLeftRight = true;
        },
        watch: {
            'welcome.bgLeftRight': function () {
                setTimeout(function () {
                    vm.welcome.bgYears = true;
                }, 800);
            },
            'welcome.bgYears': function () {
                setTimeout(function () {
                    vm.welcome.gb = true;
                }, 800);
            },
            'welcome.gb': function () {
                setTimeout(function () {
                    vm.welcome.pikachu = true;
                }, 800);
            },
            'welcome.pikachu': function () {
                setTimeout(function () {
                    window.onresize();
                    vm.welcome.gbScreen = true;
                }, 800);
            }
        }
    });
    window.vm = vm;

    var moving = null;
    var talking = null;
    var waiting = null;

    function move(direction) {
        if (moving || talking || waiting)
            return;
        if (direction != vm.hero.direction) {
            vm.hero.status = 0;
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
        if (y < 0 || x < 0 || y > 7 || x > 7 || (data.map[y][x] != 0 && data.map[y][x] != 'stair')) {
            return;
        }
        (function go(status) {
            if (status % 5 == 0) {
                var p = vm.hero.status + 1;
                vm.hero.status = p % data.totalImages[vm.hero.direction];
            }
            if (status == 10) {
                vm.hero.x = Math.round(vm.hero.x);
                vm.hero.y = Math.round(vm.hero.y);
                if (vm.hero.status % 2 != 0)
                    vm.hero.status--;
                moving = null;
                if (data.map[vm.hero.y][vm.hero.x] == 'stair') {
                    trigger(data.stair);
                }
                return;
            }
            vm.hero.x += dx / 10;
            vm.hero.y += dy / 10;
            moving = setTimeout(go, 40, status + 1);
        })(0);
    }

    function pressUp() {
        if (waiting) {
            if (waiting.type == 1 && vm.yesno.status == 0) {
                vm.yesno.status = 1;
            } else if (waiting.type == 2) {
                if (vm.select.status > 0) {
                    vm.select.status--;
                } else {
                    vm.select.status = 3;
                }
            } else if (waiting.type == 3) {
                if (vm.menu.status > 0) {
                    vm.menu.status--;
                } else {
                    vm.menu.status = 5;
                }
            } else if (waiting.type == 4) {
                if (vm.menu.submenu.status > 0) {
                    vm.menu.submenu.status--;
                } else {
                    vm.menu.submenu.status = data.menu.options[vm.menu.status].options.length - 1;
                }
            }
        } else {
            move(2);
        }
    }

    function pressDown() {
        if (waiting) {
            if (waiting.type == 1 && vm.yesno.status == 1) {
                vm.yesno.status = 0;
            } else if (waiting.type == 2) {
                if (vm.select.status < 3) {
                    vm.select.status++;
                } else {
                    vm.select.status = 0
                }
            } else if (waiting.type == 3) {
                if (vm.menu.status < 5) {
                    vm.menu.status++;
                } else {
                    vm.menu.status = 0;
                }
            } else if (waiting.type == 4) {
                if (vm.menu.submenu.status < data.menu.options[vm.menu.status].options.length - 1) {
                    vm.menu.submenu.status++;
                } else {
                    vm.menu.submenu.status = 0;
                }
            }
        } else {
            move(0);
        }
    }

    function pressLeft() {
        move(1);
    }

    function pressRight() {
        move(3);
    }

    function pressA() {
        if (moving) {
            return;
        }
        if (talking) {
            if (waiting) {
                vm.dialog.cursor = false;
                if (sentence == waiting.message.length - 1) {
                    clearDialog();
                    waiting = null;
                    return;
                }

                var tmp = waiting.message[sentence] + '<br>';
                sentence++;
                if (waiting.message[sentence] == '') {
                    tmp = '';
                    oneline = true;
                    sentence++;
                }
                vm.dialog.message = tmp;
                setTimeout(talk, talkDelay, 0, waiting);
                waiting = null;
            } else {

            }
        } else if (waiting) {
            waiting.callback(true);
        } else {
            var x = vm.hero.x + (vm.hero.direction == 1 ? -1 : 0) + (vm.hero.direction == 3 ? 1 : 0);
            var y = vm.hero.y + (vm.hero.direction == 0 ? 1 : 0) + (vm.hero.direction == 2 ? -1 : 0);
            if (y < 0 || x < 0 || y > 7 || x > 7 || data.map[y][x] == 0 && data.map[y][x] == -1) {
                return;
            }
            var event = data.map[y][x];
            if (typeof event === 'string') {
                if (event == 'tv' && vm.hero.direction != 0) {
                    return;
                }
                trigger(data[event]);
            }
        }
    }

    function pressB() {
        if (moving) {
            return;
        }
        if (talking) {
            if (waiting) {
                pressA()
            } else {

            }
        } else if (waiting) {
            waiting.callback(false);
        } else {

        }
    }

    function pressSelect() {

    }

    var menuLast = 0;

    function pressStart() {
        if (moving || talking)
            return;
        if (waiting && waiting.type == 3) {
            clearDialog();
            waiting = null;
            return;
        }
        var list = data.menu.options[0].name;
        for (var i = 1; i < data.menu.options.length; ++i)
            list += '<br>' + data.menu.options[i].name;
        vm.menu.message = list;
        waiting = data.menu;
        vm.menu.status = menuLast;
    }

    function trigger(event) {
        clearDialog();
        vm.dialog.status = 0;
        talking = setTimeout(talk, 0, 0, event);
    }

    var talkDelay = 60;
    var sentence = 0;
    var waitDelay = 800;
    var oneline = true;
    var shining = null;

    function wait() {
        if (shining && waiting) {
            vm.dialog.cursor = !vm.dialog.cursor;
            shining = setTimeout(wait, waitDelay);
        } else {
            vm.dialog.cursor = false;
            shining = null;
        }
    }

    function talk(status, event) {
        if (status >= event.message[sentence].length) {
            if (oneline && sentence != event.message.length - 1) {
                vm.dialog.message += '<br>';
                oneline = false;
                sentence++;
                talking = setTimeout(talk, talkDelay, 0, event);
            } else if (sentence != event.message.length - 1) {
                waiting = event;
                shining = setTimeout(wait, talkDelay);
            } else {
                if (event.type == 1) {
                    vm.yesno.status = 1;
                    vm.yesno.yes = event.yes;
                    vm.yesno.no = event.no;
                    shining = null;
                    waiting = event;
                    talking = null;
                } else if (event.type == 2) {
                    vm.select.status = 0;
                    vm.select.options = event.options;
                    shining = null;
                    waiting = event;
                    talking = null;
                }
                else {
                    waiting = event;
                    talking = null;
                }
            }
        } else {
            vm.dialog.message += event.message[sentence][status];
            talking = setTimeout(talk, talkDelay, status + 1, event);
        }
    }

    function clearDialog() {
        vm.dialog.message = '';
        vm.dialog.status = -1;
        vm.select.status = -1;
        vm.yesno.status = -1;
        vm.menu.status = -1;
        vm.menu.submenu.status = -1;
        shining = null;
        vm.dialog.cursor = false;
        sentence = 0;
        oneline = true;
    }
};
