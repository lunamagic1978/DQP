function showsuccess(msg) {
    let n = new Noty({  text: msg,
                        type: 'success',
                        theme: 'semanticui',
                        layout: 'topCenter',
        callbacks: {
        onClose:  function () {
            window.history.go(0)
            }
        }
    });



    n.show();
    n.setTimeout(1000);

}

function showerror(msg) {
    let n = new Noty({  text: msg,
                        type: 'error',
                        theme: 'semanticui',
                        layout: 'topCenter',
    });
    n.show();
    n.setTimeout(1000);

}