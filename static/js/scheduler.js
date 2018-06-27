// Submit scheduler on submit
$('#scheduler_form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    create_scheduler();
});

$('#scheds_form').on('submit', function (event) {
    event.preventDefault();
    console.log("form submitted!");  // sanity check
    get_schedulers();
});

//Buttons

$('[data-toggle="wizard-radio"]').click(function () {
        wizard = $(this).closest('.wizard-card');
        find('[data-toggle="wizard-radio"]').removeClass('active');
        $(this).addClass('active');
        find('[type="radio"]').removeAttr('checked');
        $(this).find('[type="radio"]').attr('checked', 'true');
    });


// AJAX for busy scheduler get
function get_schedulers() {
    console.log("Get sched is working!"); // sanity check
    $.ajax({
        url: "scheduler/get_scheds/", // the endpoint
        type: "POST", // http method
        data: {
            post_username: $('#username_input').val(),
        }, // data sent with the post request

        // handle a successful response
        success: function (data) {
            console.log("success"); // another sanity check

            // Получение свободных заявок
            var calendar_box = $("#calendar-box");
            calendar_box.empty();
            var sched_data = data.busy_times;

            for (dates in sched_data) {
                if (sched_data.hasOwnProperty(dates)) {

                    // Дата в номральном виде
                    var dateParsed = dates.match(/(\d{1,2})-(\d{1,2})-(\d{2,4})/);
                    var hum_date = new Date(dateParsed[3], dateParsed[2] - 1, dateParsed[1]).toLocaleString('ru', {
                        weekday: 'long',
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                    });

                    console.log("Ключ = " + dates)
                    $("#calendar-box").append("<li class='calendar-day'>" + "<p class='calendar-day-header'>" + hum_date + "</p>" + "<div id='calendar-times-" + dates +"' class='btn-group btn-group-toggle' data-toggle='buttons'></div>" + "</li>");
                    var sched_times = sched_data[dates];
                    for (times in sched_times) {
                        if (sched_times.hasOwnProperty(times)) {
                            console.log("Значение = " + sched_times[times]);
                            $("#calendar-times-" + dates).append("<div class='btn btn-secondary' data-toggle='wizard-radio' rel='tooltip' data-original-title='Select this room if you're traveling with your family.'>" + "<input id='' name='' value='" + times + "' data-date='" + dates + "' class='' type='radio' autocomplete='off'>" + sched_times[times] + "</div>");

                        }
                    }
                }
            }

        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

// AJAX for scheduler add
function create_scheduler() {
    console.log("create post is working!"); // sanity check
    $.ajax({
        url: "add/", // the endpoint
        type: "POST", // http method
        data: {
            post_username: $('#username_input').val(),
            post_address: $('#address_input').val(),
            post_telephone: $('#telephone_input').val(),
            post_comment: $('#comment_input').val(),
            post_repair_date: $('#date_input').val(),
            post_repair_time: $('#time_input:checked').val(),
        }, // data sent with the post request

        // handle a successful response
        success: function (json) {
            $('#time_input').val('T7'); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}


$(function () {

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url === origin || url.slice(0, origin.length + 1) === origin + '/') ||
            (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

jQuery.extend(jQuery.validator.messages, {
        required: "Это поле необходимо заполнить",
        remote: "Исправьте это поле чтобы продолжить",
        email: "Введите правильный email адрес.",
        url: "Введите верный URL.",
        date: "Введите правильную дату.",
        dateISO: "Введите правильную дату (ISO).",
        number: "Введите число.",
        digits: "Введите только цифры.",
        creditcard: "Введите правильный номер вашей кредитной карты.",
        equalTo: "Повторите ввод значения еще раз.",
        accept: "Пожалуйста, введите значение с правильным расширением.",
        maxlength: jQuery.validator.format("Нельзя вводить более {0} символов."),
        minlength: jQuery.validator.format("Должно быть не менее {0} символов."),
        rangelength: jQuery.validator.format("Введите от {0} до {1} символов."),
        range: jQuery.validator.format("Введите число от {0} до {1}."),
        max: jQuery.validator.format("Введите число меньше или равное {0}."),
        min: jQuery.validator.format("Введите число больше или равное {0}.")
});