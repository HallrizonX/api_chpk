django.jQuery( document ).ready(function() {
    // Set list of student in create new journal
    var $ = django.jQuery;
    var ALL_STUDENTS = '/api/v1/subjects/';
    $('#id_subject').on('change', function (e) {
        var val = $(this).val();
        $.get(ALL_STUDENTS + val + '/students/journals/').done(function (res) {
            var str = "";
            res.data.result.map(function (student) {
                str += `<option value='${student.id}'>${student.profile.name} ${student.profile.surname} ${student.profile.last_name}</option>`
            });
            $("#id_student").html(str)
        })
    })
});