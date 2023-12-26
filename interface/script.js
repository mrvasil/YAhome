function reload() {
    fetch("/table")
        .then(response => response.text())
        .then(data => {
            document.getElementById('device_table').innerHTML = data;
        });
}

setInterval(reload, 500);



function openPage(pageName, elmnt) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("selected");
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.classList.add("selected");
    
}

function open_device_info(pageName, elmnt) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("selected");
    }
    document.getElementById(pageName).style.display = "block";
}
// document.getElementById("defaultOpen").click();


function showNotification(text, color) {
    var notification = document.createElement('div');
    notification.innerHTML = text;
    notification.style.backgroundColor = color;
    notification.classList.add("notification");
    var notificationsContainer = document.getElementById('notifications');
    notificationsContainer.prepend(notification); 
    setTimeout(function() {
        notification.classList.add('notification_remove');
    }, 1500);
}

function button_click(button, id) {
    if (button.classList.contains('enable_button')) {
        var state = "false";
    } else {
        var state = "true";
    }


    $.ajax({
        url: '/device',
        type: 'POST',
        data: {id: id, state: state},
        success: function(response) {

            if (response.res == 'successful') {
                button.classList.toggle('enable_button'); 
                button.classList.toggle('disable_button');
                showNotification(response.text, response.color);
            } 

            else {
                showNotification(response.text, response.color);
            }
        },
    });

}



function updateButtons() {
    $.getJSON('/get_info', function(data) {
        for (let i = 0; i < data['devices'].length; i++) {
            let button = document.getElementById(data['devices'][i]+"_button");
            if (data['state'][i]) {
                button.className = "enable_button on_off_button";
            } else {
                button.className = "disable_button on_off_button";
            }
        }
    });
}

setInterval(updateButtons, 501);