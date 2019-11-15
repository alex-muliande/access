$(document).ready(()=>{
    let imgDefer = document.getElementsByTagName('img');
    for (img of imgDefer) {
        if (img.getAttribute('data-src')) {
            img.setAttribute('src', img.getAttribute('data-src'));
        }
    }
});