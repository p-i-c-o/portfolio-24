$(document).ready(function() {
    // Function to get the visitor's IP address
    function getIPAddress() {
        $.getJSON("https://api.ipify.org?format=json", function(data) {
            $("#ipAddress").text(data.ip);
        });
    }

    // Call the function to get the IP address
    getIPAddress();
});