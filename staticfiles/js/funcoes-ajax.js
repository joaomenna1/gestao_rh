function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken ")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken : token,
            outro_param: 123
        },
        success: function(result){
            console.log('sucesso!!!');
            $("#mensagem").text('Hora Extra marcada como utilizada');
        }
    })
}