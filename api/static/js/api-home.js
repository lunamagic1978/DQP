function showCreateNameSpace() {
    $('#createNameSpace').css({display:'flex'});
    console.log("createnamespace")
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


function showCreateProject() {
    $('#createProject').css({display:'flex'});

}

function hiddenCreateProject() {
    $('#createProject').css({display: 'none'});
}

function namespaceSelectSwitchClikck() {
    if ($('#namespace-select-switch')[0].className === "dao-select-switch"){
        $('#namespace-select-switch')[0].className = "dao-select-switch open";
        $('#namespace-select').css({display: "flex"})
    }
    else
    {
        $('#namespace-select-switch')[0].className = "dao-select-switch";
        $('#namespace-select').css({display: "none"})
    }
}

function namespaceSelected(namespace){
    console.log(namespace)
    $('#namespace-select').css({display: "none"})
    $('#namespace-select-switch')[0].className = "dao-select-switch";
}