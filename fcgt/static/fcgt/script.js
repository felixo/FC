 $(document).ready(function() {


    $( ".likeButtonText" ).click(function() {
     //alert( "The Function start" );
     var catid = 0;
     var url=window.location.pathname;
     url = url + "vote";
     var url2=window.location.pathname + " .galleryText";
     //alert(url);
     $.get(url, {art_id: catid}, function(data){
                //alert("It's Gone");
               $('.galleryText').load(url2,function(){
                    //alert("Rocn'Roll");
                    $('.likeButtonText').text('Спасибо за ваш голос!');
               });

           });
    });

});