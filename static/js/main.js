// Get utm tags and set cookie
let search = location.search;
let params = new URLSearchParams(search);
for (let [key, value] of params.entries()){
    if (key.startsWith('utm_')){
        document.cookie = `${encodeURIComponent(key)}=${encodeURIComponent(value)};path=/;max-age=604800`
    }
}
// Set referer cookie if it hasn't been set
if (document.cookie.indexOf("; referer=") === -1 && !document.cookie.startsWith("referer=")) {
    let referer = null;
    if (document.referrer === "") {
        referer = new URL(document.URL).host;
    } else {
        referer = new URL(document.referrer).host;
    }
    if (referer.startsWith("www.")){
        referer = referer.slice(4)
    }
    document.cookie = `referer=${encodeURIComponent(referer)};path=/;max-age=604800`
}
window.onscroll = function () {
    scrollFunction();
};
window.preload = function () {
    setAttrib();
};


function scrollFunction() {
    const element = document.getElementById("navbar");
    if (element)
        if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
            element.style.backgroundColor = "#637C33";
        } else {
            element.style.backgroundColor = "transparent";
        }
}

function setAttrib() {
    document.getElementsByClassName('collapsed').setAttribute('aria-expanded', 'true');
}

$(document).ready(function () {
    $('ul.nav li.dropdown').hover(function () {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(400);
    }, function () {
        $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeOut(400);
    });
});

$(document).ready(function () {
    $('.carousel .carousel-item:first').addClass('active');
});

$(document).ready(function () {
    $('#myTabs a').click(function (e) {
        e.preventDefault();

        let url = $(this).attr("data-url");
        let href = this.hash;
        let pane = $(this);

        // ajax load from data-url
        $(href).load(url, function (result) {
            pane.tab('show');
        });
    });
});



