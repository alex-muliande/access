$(document).ready(function(){
    console.log('ready');

    $('.hide').click(function(){
        $('.all').slideUp('slow')
    })
    $('.all_data').click(function(){
        pk = $(this).find('.getData').val()
        console.log('pk =',pk);
        $.ajax({
            url:'/get_data/',
            method:'GET',
            data:{
                'pk':pk
            },
            statusCode:{
                500:function(){
                    console.error('INTERNAL ERROR')
                }
            }
        })
        .done(function(data){
            console.log(data);
            $('.my-data').empty()
            $('.my-data').append(''+data+'')
            // $('.my-data').prepend(
            //     '<h5>All Names</h5>'+
            //     '<h6>'+data["all_names"]+'</h6>'
            // )
            $('.all').slideDown('slow')
            
        })
        
    })
    
})