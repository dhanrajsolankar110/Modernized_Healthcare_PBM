/*
=========================================================
            NOTIFICATIONS MODULE
    Modernized Healthcare PBM Portal
=========================================================
*/

document.addEventListener(

    "DOMContentLoaded",

    function () {

        initializeNotifications();

    }

);

// =========================================
// INITIALIZE
// =========================================

function initializeNotifications(){

    initializeSearch();

    initializeFilters();

    initializeButtons();

    animateCards();

}

// =========================================
// SEARCH
// =========================================

function initializeSearch(){

    const searchBox = document.getElementById(

        "notificationSearch"

    );

    if(!searchBox){

        return;

    }

    searchBox.addEventListener(

        "keyup",

        function(){

            const value = this.value.toLowerCase();

            const rows = document.querySelectorAll(

                ".notifications-table tbody tr"

            );

            rows.forEach(function(row){

                row.style.display = row.innerText
                    .toLowerCase()
                    .includes(value)

                    ? ""

                    : "none";

            });

        }

    );

}

// =========================================
// FILTER
// =========================================

function initializeFilters(){

    const filter = document.getElementById(

        "notificationFilter"

    );

    if(!filter){

        return;

    }

    filter.addEventListener(

        "change",

        function(){

            const value = this.value.toLowerCase();

            const rows = document.querySelectorAll(

                ".notifications-table tbody tr"

            );

            rows.forEach(function(row){

                if(

                    value==="all"

                ){

                    row.style.display="";

                    return;

                }

                row.style.display=row.innerText
                    .toLowerCase()
                    .includes(value)

                    ? ""

                    : "none";

            });

        }

    );

}

// =========================================
// BUTTONS
// =========================================

function initializeButtons(){

    document.querySelectorAll(

        ".btn-danger"

    ).forEach(function(button){

        if(

            button.innerText.includes("Delete")

        ){

            button.addEventListener(

                "click",

                function(event){

                    if(

                        !confirm(

                            "Are you sure you want to delete this notification?"

                        )

                    ){

                        event.preventDefault();

                    }

                }

            );

        }

    });

    document.querySelectorAll(

        ".btn-success"

    ).forEach(function(button){

        if(

            button.innerText.includes("Mark All")

        ){

            button.addEventListener(

                "click",

                function(event){

                    if(

                        !confirm(

                            "Mark all notifications as read?"

                        )

                    ){

                        event.preventDefault();

                    }

                }

            );

        }

    });

}

// =========================================
// CARD ANIMATION
// =========================================

function animateCards(){

    const cards = document.querySelectorAll(

        ".stat-card"

    );

    cards.forEach(function(card,index){

        card.style.opacity="0";

        card.style.transform="translateY(20px)";

        setTimeout(function(){

            card.style.transition="0.4s ease";

            card.style.opacity="1";

            card.style.transform="translateY(0)";

        },index*100);

    });

}

// =========================================
// NOTIFICATION COUNT
// =========================================

function updateNotificationCount(){

    const total=document.querySelectorAll(

        ".notifications-table tbody tr"

    ).length;

    const badge=document.getElementById(

        "notificationCount"

    );

    if(badge){

        badge.innerText=total;

    }

}

// =========================================
// AUTO REFRESH
// =========================================

setInterval(function(){

    console.log(

        "Notification auto-refresh check..."

    );

},60000);

// =========================================
// PAGE LOAD
// =========================================

window.addEventListener(

    "load",

    function(){

        updateNotificationCount();

    }

);

// =========================================
// UTILITIES
// =========================================

function showToast(message){

    console.log(message);

}