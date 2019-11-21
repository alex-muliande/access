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
// send congratulatulation4
$(document).ready(function(){
    console.log('I am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $('.congrats4').click(function(){

   
    
    $.ajax({
        url:'/congrats4/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('I have gone');

        
        }
    })
    .done(function(data){
        $('.loader').css ({'display':'none'})
        console.log('I am done');
        console.log(data.sent);
        
        
    })
})
})

// send congratulation6

$(document).ready(function(){
    console.log('I am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $('.congrats6').click(function(){

   
    
    $.ajax({
        url:'/congrats6/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('I have gone');

        
        }
    })
    .done(function(data){
        $('.loader').css ({'display':'none'})
        console.log('I am done');
        console.log(data.sent);
        
        
    })
})
})


// Send email to all rejected people

$(document).ready(function(){
    console.log('I am ready');
    $(document).ajaxStart(function(){
        $('.loader').css({'display':'block'})
    })
    $('.rejected').click(function(){

   
    
    $.ajax({
        url:'/rejected/',
        method:'GET',
        beforeSend:function(){
        $('.loader').css({'display':'block'})
        console.log('I have gone');

        
        }
    })
    .done(function(data){
        $('.loader').css ({'display':'none'})
        console.log('I am done');
        console.log(data.sent);
        
        
    })
})
})