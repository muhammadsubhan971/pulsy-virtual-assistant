$(document).ready(function () {
    eel.expose(DisplayMessage)
    function DisplayMessage(m) {

        $('.siri-message').text(m);
        $('.siri-message').texllate('start');

    }
});