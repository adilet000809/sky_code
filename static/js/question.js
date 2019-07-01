$(document).ready(function () {
    $('.question-form').on('submit', function (e) {
        var name = $('#contactName').val();
        var email = $('#contactEmail').val();
        var question = $('#contactQuestion').val();
        e.preventDefault();
        $.ajax({
            url: '/ask/',
            data: {
                name: name,
                email: email,
                question: question,
            },
            dataType: 'json',
            success: function (response) {
                console.log('shit1');
                $('.alert').alert();

                console.log('shit1');
            }
        });
    });
});