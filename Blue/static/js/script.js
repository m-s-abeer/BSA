jQuery(document).ready(function ($) {


    jQuery('.message a').click(function () {
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });


    JoinBtn = jQuery("#join_sheet_btn");
    JoinBtnTitle = JoinBtn.data("sheet-name");

    JoinBtn.confirm({
        title: 'Are you sure?',
        icon: 'fas fa-clipboard-check',
        escapeKey: true,
        columnClass: 'col-md-6',
        type: 'blue',

        content: '<h3> Do you really want to join? <b><br>"'+JoinBtnTitle+'"</b></h3>\n' +
        '    <h3> You cannot leave the sheet after joining until you are removed automatically.</h3>',
        buttons: {
            YES: {
                btnClass: 'btn-primary',
                text: 'Confirm',
                action: function () {

                JoinBtn.fadeOut();

                var currentPath = JoinBtn.data("current");
                jQuery.ajax({
                    url: currentPath + 'confirm',
                    type: 'GET',
                    contentType: "application/json",
                    success: function (res) {
                        jsonResponse = JSON.parse(res);

                        if (jsonResponse.status == 1) {
                            $.alert({
                                icon: 'fas fa-check-square',
                                title: '<h4>Success!<h4>',
                                columnClass: 'col-md-12',
                                escapeKey: true,
                                type: 'green',
                                content: jsonResponse.message,
                            });

                        } else {
                             $.alert({
                                title: 'Oh no!',
                                content: jsonResponse.message,
                            });
                        }
                    }
                });
            }},
            NO: function () {

            }
        }
    });


    var ProblemSolvedBtn = $("#problem_solved_btn");
    ProblemTitle = ProblemSolvedBtn.data("name");

    ProblemSolvedBtn.confirm({
        icon: 'fas fa-clipboard-check',
        escapeKey: true,
        columnClass: 'col-md-10',
        title: 'Confirm!',
        type: 'blue',
        content: '<h1> Do you confirm that you\'ve solved <b><br>"'+ProblemTitle+'"</b>?</h1><h3> You cannot remove this problem' +
        ' from' +
        ' your solve activities after confirmation.</h3>',
        buttons: {
            YES: {
                btnClass: 'btn-primary',
                text: 'Confirm',
                action: function () {

                ProblemSolvedBtn.fadeOut();

                var currentPath = ProblemSolvedBtn.data("current");
                jQuery.ajax({
                    url: currentPath + 'confirmed',
                    type: 'GET',
                    contentType: "application/json",
                    success: function (res) {
                        $.alert({
                            icon: 'fas fa-clipboard-check',
                            title: '<h4>Success!<h4>',
                            columnClass: 'col-md-12',
                            escapeKey: true,
                            type: 'green',
                            content: res,
                        });

                        $(".status.pending").removeClass("pending").addClass("solved").text("Solved").hide().fadeIn();
                    }
                });

            }},

            NO: function () {

            },
        }
    });


});

// requires jquery library
jQuery(document).ready(function() {
   jQuery(".main-table").clone(true).appendTo('#table-scroll').addClass('clone');   
 });


//Dragabble homepage box
$(function() {
    $( ".box" ).draggable();
});