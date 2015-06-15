
function bindHeight() {
    function autoHeight() {
        var h = $(window).height();
        var w = $(window).width();
        var ph = Math.floor(h / 2) + 179.5;
        var body = $('#home-body');
        var zh = Math.floor(h / 2) - 271;
        body.height(h);
        body.width(w);
        $('#home-header').height(zh);
    //    $('#home-main-container').height(ph);
    //    var qh = ph - 506;
    //    if (qh<0) qh = 0;
    //    $('#home-content').css({"top": qh});
        var qw = Math.floor(w / 2) - 640;
        if (qw<0) qw = 0;
        $('#home-content').css({"left": qw});

        $('.home-footer-side').width(Math.round((w - 1280) / 2));
        $('#home-footer').height(ph - 405);
        $('#home-footer-center-bottom').height(ph - 500);
    }
    $(window).resize(autoHeight);
    autoHeight();

}

var p, q = 0;
var hostesses;
var icons;
var mouths;
var section = "";
var pst = {
    "baseinfo": [0, 0, {
        "活动时间与当日行程": "schedule",
        "场地信息": "place",
        "票务信息": "ticket",
        "奖品一览": "prize"
    }],
    "stall": [0, 1, {
        "现场摊位": "diagram",
        "参展社团": "circle",
        "参展贩售物": "goods"
    }],
    "event": [1, 0, {
        "联机对战": "battle",
        "舞台游戏": "stage",
        "场地活动": "venue",
        "幸运抽奖": "raffle"
    }],
    "register": [1, 1, {
        "对战报名": "battle",
        "摊位申请": "stall",
        "寄卖申请": "consign"
    }],
    "news": [2, 0, {
        "新闻列表": ""
    }],
    "qabook": [2, 1, {
        "常见Q&A": "faq",
        "参展礼仪与建议": "manner",
        "留言板": "guestbook"
    }]
};
var lines = [
    [
        '我们水舰队的目标是扩张海洋的面积。海洋，是所有生命的起源，藉由我们的双手，把更加丰饶的栖息地还给精灵们，让世界迈向新的境界！训练家们欢迎啊，跟着水梧桐总长一起前进！',
        [
            '嗯？找我有事吗？',
            '我们家总长真的是有梦想的男人。',
            '水舰队的团员们每天都保持着愉悦的心情，怎么样，羡慕吗？',
            '潮水那个家伙，又不知道到哪里去鬼混了。',
            '喔！我的老天爷，欢迎你的光临啊！',
            '游泳是入团的必备技能呢~我们是最喜欢海洋的组织。',
            '我要一生追随总长，支持着他的梦想。'
        ],
        [
            '谢谢你！选择我们是你的福气，我们水舰队是最强的！',
            '你！选择了熔岩团就是与我们水舰队作对！要让你后悔没选择我们！',
            '注意，重复投票是禁止的哦！敢这麽做的也挺有胆量的嘛！'
        ]
    ],
    [
        '……麻古麻古团……你追来了呢。',
        [
            '基地里……岩浆咕噜噜♪……毛衣……好热……',
            '……闪闪发亮……老大的额头。',
            '九尾……？并没有…………树果……给我……？为什咩……？',
            '……Keystone……交出来……哟。',
            '果滋（汁）……老大……印在上面……（咕嘟咕嘟咕嘟）',
            '这样……世界就，结束了♪'
        ],
        [
            '……你……遵（真）有趣……',
            '……快要……实现了……老大的……梦想~♪',
            '……投票……只能……一次。老大……只有……一个。'
        ]
    ]
];
var tvOn = false;

function startTV() {
    $("#tv-off").addClass("hidden-object");
    $("#home-content-tv").append(tvContent);
    setTimeout(function () {
        $("#tv-off").addClass("nodisplay-object");
        doSpeak(lines[q][0]);
    }, 500);
    $("#tv-ins").click(switchHostess);
    $('.tv-section-text').click(switchSection);
    $('#tv-nise-hostess').click(switchSentence);
    hostesses = [$('.izumi'), $('.kagari')];
    icons = [$('#tv-icon-izumi'), $('#tv-icon-kagari')];
    mouths = [$('#mouth-izumi'), $('#mouth-kagari')];
    q = Math.floor(Math.random() * 2);
    p = 1;
    ts = sa = $('#tv-selection');
    hostesses[1-q].addClass("hidden-object");
    bindVote();
    tvOn = true;
}

function switchHostess() {
    q = 1 - q;
    hostesses[1-q].css({'z-index': 0});
    hostesses[q].css({'z-index': 1});
    hostesses[1-q].addClass("hidden-object");
    hostesses[q].removeClass("hidden-object");
    icons[1-q].css({'z-index': 0});
    icons[q].css({'z-index': 1});
    icons[1-q].addClass("hidden-object");
    doSpeak(lines[q][0]);
}

var nowObject, nowString, nowIndex;
var nowKeys, nowKeyIndex;
var sa, href;
var sot = null;
function doPrint() {
    if (sot != null) clearTimeout(sot);
    if(nowIndex>=nowString.length) {
        nowKeyIndex++;
        sot=setTimeout(doAppend, 100);
        return;
    }
    nowObject.append(nowString[nowIndex]);
    nowIndex++;
    sot = setTimeout(doPrint, 100);
}
function doAppend() {
    if(nowKeyIndex>nowKeys.length) {
        sa.append('<div id="tv-selection-end"></div>');
        return;
    }
    if(nowKeyIndex==nowKeys.length) {
        sa.append('<span id="s'+ nowKeyIndex +'"></span>');
        nowObject = $('#s'+nowKeyIndex);
        nowString = "【请选择】";
        nowIndex = 0;
        doPrint();
        return;
    }
    href = section + "/";
    var pz = pst[section][2][nowKeys[nowKeyIndex]];
    if (pz != "")
        href += pz + "/";
    sa.append('<a id="s'+ nowKeyIndex +'" href="'+href+'"></a>');
    nowObject = $('#s'+nowKeyIndex);
    nowString = nowKeys[nowKeyIndex];
    nowIndex = 0;
    doPrint();
}

function switchSection() {
    section = this.id.substring(11);
    var t = pst[section];
    $('.tv-icon').css({
        'top': 10 + t[0] * 40,
        'left': 3 + t[1] * 120
    });
    icons[q].removeClass("hidden-object");
    sa.empty();
    nowKeys = Object.keys(t[2]);
    nowKeyIndex = 0;
    doAppend();
}

function switchMouth() {
    p = 1 - p;
    if(p==1)
        mouths[q].addClass("nodisplay-object");
    else
        mouths[q].removeClass("nodisplay-object");
}

var nowSentence, nowSIndex;
var ts;
function doSay() {
    if (sot != null) clearTimeout(sot);
    if(nowSIndex>nowSentence.length){
        ts.append('<div id="tv-selection-end"></div>');
        mouths[q].addClass("nodisplay-object");
        return;
    }
    switchMouth();
    ts.text(nowSentence.substring(0, nowSIndex));//.substring(nowSIndex-29, nowSIndex));
    nowSIndex++;
    sot = setTimeout(doSay, 100);
}
function doSpeak(sentence) {
    nowSentence = sentence;
    nowSIndex = 0;
    ts.empty();
    icons[q].addClass("hidden-object");
    doSay()
}
function switchSentence() {
    var newSentence = nowSentence;
    while (newSentence==nowSentence)
        newSentence = lines[q][1][Math.floor(Math.random()*lines[q][1].length)];
    doSpeak(newSentence);
}

var tvContent = '<div id="tv-dialog"><div id="tv-nise-hostess"></div></div><div id="tv-ins"></div><div id="tv-hostess' +
    '"><div id="hostess-izumi" class="izumi hostess"></div><div id="mouth-izumi" class="izumi hostess nodisplay-objec' +
    't"></div><div id="hostess-kagari" class="kagari hostess"></div><div id="mouth-kagari" class="kagari hostess nodi' +
    'splay-object"></div></div><div id="tv-section"><div id="tv-icon-izumi" class="tv-icon hidden-object"></div><div ' +
    'id="tv-icon-kagari" class="tv-icon hidden-object"></div><div id="tv-section-baseinfo" class="tv-section-text"><s' +
    'pan>基本信息</span></div><div id="tv-section-stall" class="tv-section-text"><span>现场摊位</span></div><div id="t' +
    'v-section-event" class="tv-section-text"><span>现场活动</span></div><div id="tv-section-register" class="tv-sect' +
    'ion-text"><span>在线报名</span></div><div id="tv-section-news" class="tv-section-text"><span>PMO新闻</span></div>' +
    '<div id="tv-section-qabook" class="tv-section-text"><span>QA留言板</span></div></div><div id="tv-selection"></di' +
    'v><div id="tv-sentence">大海对陆地，结果我第一</div>';
function bindTV() {
    $('#tv-off').click(startTV);
}

function bindVote() {
    var vbs = $('.vote-bar-content');
    function updateVote() {
        vbs.each(function () {
            this.style.width = (this.dataset.vote / 3).toString() +'%';
        })
    }
    var url = $('#home-vote').data('url');
    $('.vote-href').click(function () {
        var s = this;
        $.post(
            url,
            {
                'team': s.id.substr(5,2),
                'csrfmiddlewaretoken': $.cookie('csrftoken')
            },
            function (data) {
                var msg;
                switch(data.error){
                    case 0:
                        msg = lines[q][2][data.vote];
                        $("#"+s.id.substr(0, 8)+"bar-content")[0].dataset.vote++;
                        updateVote();
                        break;
                    case 1:
                        msg = lines[q][2][2];
                        break;
                    default:
                        msg = '未知错误';
                }
                if (tvOn)
                    doSpeak(msg);
                updateVote();
            }
        );
    });
    updateVote();
}

$(document).ready(function (){
    bindHeight();
    bindTV();
});
