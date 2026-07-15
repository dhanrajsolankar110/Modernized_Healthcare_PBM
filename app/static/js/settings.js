/*
=========================================================
                SETTINGS MODULE
        Modernized Healthcare PBM Portal
=========================================================
*/

document.addEventListener(

    "DOMContentLoaded",

    function(){

        initializeSettings();

    }

);

// =========================================
// INITIALIZE
// =========================================

function initializeSettings(){

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

        "settingSearch"

    );

    if(!searchBox){

        return;

    }

    searchBox.addEventListener(

        "keyup",

        function(){

            const value = this.value.toLowerCase();

            const rows = document.querySelectorAll(

                ".settings-table tbody tr"

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

        "categoryFilter"

    );

    if(!filter){

        return;

    }

    filter.addEventListener(

        "change",

        function(){

            const value = this.value.toLowerCase();

            const rows = document.querySelectorAll(

                ".settings-table tbody tr"

            );

            rows.forEach(function(row){

                if(value==="all"){

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

                            "Are you sure you want to delete this setting?"

                        )

                    ){

                        event.preventDefault();

                    }

                }

            );

        }

    });

    document.querySelectorAll(

        ".btn-info"

    ).forEach(function(button){

        if(

            button.innerText.includes("Reset")

        ){

            button.addEventListener(

                "click",

                function(event){

                    if(

                        !confirm(

                            "Reset this setting to its default value?"

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
// SETTINGS COUNTER
// =========================================

function updateSettingsCount(){

    const total = document.querySelectorAll(

        ".settings-table tbody tr"

    ).length;

    const badge = document.getElementById(

        "settingsCount"

    );

    if(badge){

        badge.innerText = total;

    }

}

// =========================================
// AUTO REFRESH (Placeholder)
// =========================================

setInterval(function(){

    console.log(

        "Checking for updated system settings..."

    );

},60000);

// =========================================
// PAGE LOAD
// =========================================

window.addEventListener(

    "load",

    function(){

        updateSettingsCount();

    }

);

// =========================================
// UTILITIES
// =========================================

function showToast(message){

    console.log(message);

}