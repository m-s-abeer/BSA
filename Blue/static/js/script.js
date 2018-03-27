jQuery(document).ready(function ($) {


    jQuery('.message a').click(function () {
        $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
    });


    JoinBtn = jQuery("#join_sheet_btn");
    JoinBtnTitle = JoinBtn.data("sheet-name");

    JoinBtn.confirm({
        title: 'Confirm!',
        content: '<h3> Do you really want to join <b>"'+JoinBtnTitle+'"</b>?</h3>\n' +
        '    <h3> You cannot leave the sheet after joining until you are removed automatically.</h3>',
        buttons: {
            YES: function () {

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
                                title: 'Success!',
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
            },
            NO: function () {

            }
        }
    });


    var ProblemSolvedBtn = $("#problem_solved_btn");
    ProblemTitle = ProblemSolvedBtn.data("name");

    ProblemSolvedBtn.confirm({
        title: 'Confirm!',
        content: '<h1> Are you sure you\'ve solved <b>"'+ProblemTitle+'"</b>?</h1><h3> You cannot remove this problem' +
        ' from' +
        ' your solve activities after confirmation.</h3>',
        buttons: {
            YES: function () {

                ProblemSolvedBtn.fadeOut();

                var currentPath = ProblemSolvedBtn.data("current");
                jQuery.ajax({
                    url: currentPath + 'confirmed',
                    type: 'GET',
                    contentType: "application/json",
                    success: function (res) {
                        $.alert({
                            title: 'Solved!',
                            content: res,
                        });

                        $(".status.pending").removeClass("pending").addClass("solved").text("Solved").hide().fadeIn();
                    }
                });
            },
            NO: function () {

            }
        }
    });


});
