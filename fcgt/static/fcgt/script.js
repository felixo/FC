 $(document).ready(function() {

    //$('input[type="submit"]').prop('disabled', true);
    $("input").prop('required',true);
    $("select").prop('required',true);
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
    /*$('input[type="submit"]').click(function(){
        if ($('#div_art_host').var == ''){
            alert ("Avada Kedavra");
            //$('input[type="submit"]').prop('disabled', true);
        }
    });*/


});