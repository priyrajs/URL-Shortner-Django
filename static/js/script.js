// $(document).ready( function (){
//     $('#myTable').DataTable();
// } );

$('document').ready(function() {
    //alert(target_url);
    $('#op_url').hide();
    $('#msg-box').hide();
    $('.submit').on('click',function(){
        var inp_url = $('#inp_url').val();
        var target_url = "/shortit"
        var csrf = $('input[name=csrfmiddlewaretoken]').val();
        var data = {inp_url:inp_url, csrfmiddlewaretoken: csrf}
        $.ajax( {
            url: target_url,
            type: "post",
            data: data,
            // datatype: "text",
            success:function(response) {
                console.log(response)
                if (response.status == "shorted"){
                    final_op = window.location.origin+"/"+response.op_url
                    $('#op_url').show();
                    $('#op_url').val(final_op);
                }
                else if(response.status == "SHORTURL")
                {
                    $('#msg-box').show();
                    $('#err-msg').html(response.er_msg);
                }
                else if(response.status == "INVALIDURL")
                {
                    $('#msg-box').show();
                    $('#err-msg').html(response.er_msg);
                }
            }
            });
    });
    // $.ajax( {
    //     url: "/handlerRedirect",
    //     type: "post",
    //     // data: data,
    //     // datatype: "text",
    //     success:function(response) {
    //         console.log(response)
    //         if (response.status == "shorted"){
    //             final_op = window.location.origin+"/"+response.op_url
    //             $('#op_url').show();
    //             $('#op_url').val(final_op);
    //         }
    //     }
    //     });
});
