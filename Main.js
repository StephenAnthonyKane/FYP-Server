/**
Sources:
https://www.w3schools.com/js/default.asp
https://stackoverflow.com/questions/tagged/javascript
 * Created by steve on 17/04/2017.
 */

$(document).ready(function () {
    $(".accordion").click(function () {
        var a = "#" + $(this).attr("id") + "-panel"
        $(a).slideToggle("slow");
    });
});


$(document).ready(function () {

    $('#submitCreate').click(function () {
        console.log("Running POST")

        var data = {"Beacons":[
            { "UID":"4", "RSS":"1" },
            { "UID":"4", "RSS":"2" },
            { "UID":"4", "RSS":"4" },
            { "UID":"4", "RSS":"5"}
          ]}

        // process the form
        $.ajax({
            type: "POST",
            dataType: "json",
            url: "RequestHandler.py",
            data: JSON.stringify(data),
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
    });


    $('#submitGet').click(function () {
        console.log("Running GET")

        var UID = $('#Uid').val();
        console.log(UID)
        
        $.ajax({
            type: "GET",
            dataType: "json",
            url: "RequestHandler.py?DeviceID="+UID,
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            },

        });
    });

});
