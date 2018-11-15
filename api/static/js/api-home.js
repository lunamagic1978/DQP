function showCreateNameSpace() {
    $('#createNameSpace').css({display:'flex'});

}

function hiddenCreateNameSpace() {
    $('#createNameSpace').css({display:'none'});
    $('#input-namespace').val("")
}

function createCreateNameSpace() {
    var namespace = $('#input-namespace').val();
    console.log(namespace);
    $.ajax({
        "url": "/api/createnamespace/",
        "async": true,
        "crossDomain": true,
        "method": "POST",
        "headers": {
                "content-type": "application/x-www-form-urlencoded",
                "cache-control": "no-cache",
              },
        "data": {
            "namespace": namespace
        },
        success: function (res) {

            let msg = res.msg;
            if(res.code ===  200) {
                showsuccess(msg);
            }
            else{
                showerror(msg);
            }

        }
    })
    ;

    hiddenCreateNameSpace();

}