 $(document).ready(function() {
     var wrapper = $( ".file_upload" ),
        inp = wrapper.find( "input" ),
        btn = wrapper.find( "button" ),
        lbl = wrapper.find( "div" );
    btn.focus(function(){
        inp.focus()
    });
    // Crutches for the :focus style:
    inp.focus(function(){
        wrapper.addClass( "focus" );
    }).blur(function(){
        wrapper.removeClass( "focus" );
    });
    // Yep, it works!
    btn.add( lbl ).click(function(){
        inp.click();
    });
     var file_api = ( window.File && window.FileReader && window.FileList && window.Blob ) ? true : false;

    inp.change(function(){
        var file_name;
        if( file_api && inp[ 0 ].files[ 0 ] )
            file_name = inp[ 0 ].files[ 0 ].name;
        else
            file_name = inp.val().replace( "C:\\fakepath\\", '' );

        if( ! file_name.length )
            return;

        if( lbl.is( ":visible" ) ){
            lbl.text( file_name );
            btn.text( "Выбрать" );
        }else
            btn.text( file_name );
    }).change();
    $( window ).resize(function(){
    $( ".file_upload input" ).triggerHandler( "change" );
});
    //$('input[type="submit"]').prop('disabled', true);
    $("input").prop('required',true);
    $("select").prop('required',true);
    $( ".likeButtonText" ).click(function() {
     //alert( "The Function start" );
     var catid = 0;
     var url=window.location.pathname;
     url = url + "vote";
     var url2=window.location.pathname + " .galleryText_pic";
     //alert(url);
     $.get(url, {art_id: catid}, function(data){
                //alert("It's Gone");
               $('.galleryText_pic').load(url2,function(){
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
    /*$( "#more" ).click(function() {
       alert('Avada Kedavra');
       var url=$("#moreButton").attr("href");
       alert(url);
       $.get(url, {}, function(data){
                alert("It's Gone");
               $(".galleryWrap").append("<ul id='loadersub'></ul>");

                $("#loadersub").load(url+" #loader", function(){
                    var buffer = $("#loadersub").html();
                    $(".loade").append(buffer);
                    alert("Rocn'Roll");

               });


           });
       return false;

    });*/

});