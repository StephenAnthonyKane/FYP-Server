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

    var canvas = document.getElementById("myCanvas");
    var ctx = canvas.getContext("2d");

    //Circles
    ctx.fillStyle = "Green";
    ctx.beginPath();
    ctx.arc(245, 25, 10, 0, Math.PI * 2, true);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(620, 25, 10, 0, Math.PI * 2, true);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(245, 470, 10, 0, Math.PI * 2, true);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(620, 470, 10, 0, Math.PI * 2, true);
    ctx.fill();

    //Text Background
    ctx.fillStyle = "White"
    ctx.fillRect(255, 25, 140, 30);

    ctx.fillRect(630, 25, 140, 30);

    ctx.fillRect(255, 470, 140, -30);

    ctx.fillRect(630, 470, 140, -30);

    //Text

    //ctx.fillStyle = "Black"
    //ctx.font = "15px Arial";
    //ctx.fillText("UID: 1", 255, 35);
    //ctx.fillText("RSS: 1", 255, 50);

    ctx.font = "15px Arial";
    ctx.fillText("UID: 2", 630, 35);
    ctx.fillText("RSS: 2", 630, 50);

    ctx.font = "15px Arial";
    ctx.fillText("UID: 3", 255, 455);
    ctx.fillText("RSS: 3", 255, 470);

    ctx.font = "15px Arial";
    ctx.fillText("UID: 4", 630, 455);
    ctx.fillText("RSS: 4", 630, 470);

    setInterval(sendGetRequest, 2000, "allbeacondata", 2);

    function sendGetRequest(DeviceID, OffSet) {
        console.log("Running GET")

        var URL = "RequestHandler.py?DeviceID=" + DeviceID + "&Offset=" + OffSet
        $.ajax({
            type: "GET",
            dataType: "json",
            url: URL,
            contentType: "application/json; charset=utf-8",
            success: function (data) {
                console.log(data);
                displayData(data)
            },
            error: function (data) {
                console.log(data);
            },

        });
        return;
    }

    function displayData(data) {
        var canvas = document.getElementById("myCanvas");
        var ctx = canvas.getContext("2d");

        fillCanvas(canvas, ctx);

        var closest = { "UID": 0, "RSS": Number.MIN_SAFE_INTEGER }
        data.forEach(beacon=> {
            if(beacon['RSS'] > closest['RSS']){
                closest = beacon;
            }
        })

        data.forEach(beacon => {
            ctx.fillStyle = "Black"

            if (beacon['UID'] == "b9407f30-f5f8-466e-aff9-25556b57fe6d") {
                if(closest['UID'] == beacon['UID']){
                    ctx.fillStyle = "Green";
                    ctx.beginPath();
                    ctx.arc(245, 25, 10, 0, Math.PI * 2, true);
                    ctx.fill();
                }
                else{
                    ctx.fillStyle = "Red";
                    ctx.beginPath();
                    ctx.arc(245, 25, 10, 0, Math.PI * 2, true);
                    ctx.fill();
                }
                ctx.fillStyle = "Black"
                ctx.font = "15px Arial";
                ctx.fillText("UID: " + String(beacon['UID']), 255, 35);
                ctx.fillText("RSS: " + String(beacon['RSS']), 255, 50);
            }
            
            if (beacon['UID'] == "acfd065e-c3c0-11e3-9bbe-1a514932ac01") {
                if(closest['UID'] == beacon['UID']){
                    ctx.fillStyle = "Green";
                    ctx.beginPath();
                    ctx.arc(620, 25, 10, 0, Math.PI * 2, true);
                    ctx.fill();
                }
                else{
                    ctx.fillStyle = "Red";
                    ctx.beginPath();
                    ctx.arc(620, 25, 10, 0, Math.PI * 2, true);
                    ctx.fill();
                }
                ctx.fillStyle = "Black"
                ctx.font = "15px Arial";
                ctx.fillText("UID: " + beacon['UID'], 630, 35);
                ctx.fillText("RSS: " + beacon['RSS'], 630, 50);
            }

            if (beacon['UID'] == "") {
                ctx.fillStyle = "Black"
                ctx.font = "15px Arial";
                ctx.fillText("UID: " + beacon['UID'], 255, 455);
                ctx.fillText("RSS: " + beacon['RSS'], 255, 470);
            }

            if (beacon['UID'] == "") {
                ctx.fillStyle = "Black"
                ctx.font = "15px Arial";
                ctx.fillText("UID: " + beacon['UID'], 630, 455);
                ctx.fillText("RSS: " + beacon['RSS'], 630, 470);
            }
        });
    }

    function fillCanvas(canvas, ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        //Circles



        ctx.beginPath();
        ctx.arc(245, 470, 10, 0, Math.PI * 2, true);
        ctx.fill();

        ctx.beginPath();
        ctx.arc(620, 470, 10, 0, Math.PI * 2, true);
        ctx.fill();

        //Text Background
        ctx.fillStyle = "White"
        ctx.fillRect(255, 25, 140, 30);

        ctx.fillRect(630, 25, 140, 30);

        ctx.fillRect(255, 470, 140, -30);

        ctx.fillRect(630, 470, 140, -30);
    }


    $('#submitCreate').click(function () {
        console.log("Running POST")

        var UID = $('#PostUID').val();
        var RSS = $('#PostRSS').val();

        /*
        var data = {"Beacons":[
            { "UID":"4", "RSS":"1" },
            { "UID":"4", "RSS":"2" },
            { "UID":"4", "RSS":"4" },
            { "UID":"4", "RSS":"5"}
          ]}
        */
        var data = {
            "Beacons": [
                { "UID": UID, "RSS": RSS }]
        }
        console.log(data)
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
        var UID = $('#Uid').val();
        console.log(UID)
        sendGetRequest(UID, 120)
    });

});
