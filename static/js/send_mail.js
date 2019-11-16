$(document).ready(function(){
    console.log('i am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'none'})
    })
    $('.congrats').click(function(){

    $.ajax({
        url:'/bulk/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('i have gone');
        }
    })
    .done(function(data){
        $('.loader').css({'display':'none'})
        console.log('i am done');
        console.log(data.sent);
        
    })
})
})
