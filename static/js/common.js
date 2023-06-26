$(function(){

    var $close = $('body').find('[layer="close"]');
    $close.on('click',function(){
        $('.layerPopWrap').hide();  
        $('html').removeClass('backLock');
    });



  

})




