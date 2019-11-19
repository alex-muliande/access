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

// second email
$(document).ready(function(){
    console.log('I am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $('.congrats1').click(function(){

    $.ajax({
        url:'/congrats/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('I have gone');
        
        }
    })
    .done(function(data){
        $('.loader').css({'display':'none'})
        console.log('I am done');
        console.log(data.sent);
        
        
    })
    })
    
})

// send email3
$(document).ready(function(){
    console.log('I am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $('.congrats2').click(function(){

    $.ajax({
        url:'/congrats3/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('I have gone');
        
        }
    })
    .done(function(data){
        $('.loader').css({'display':'none'})
        console.log('I am done');
        console.log(data.sent);
        
        
    })
    })
    
})