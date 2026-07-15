/*
=========================================================
        PATIENT MODULE JAVASCRIPT
    Modernized Healthcare PBM Web Portal
=========================================================
*/

document.addEventListener("DOMContentLoaded", () => {

    initializeSearch();

    initializeDeleteConfirmation();

    initializeStatusToggle();

    initializeFormValidation();

    initializeTableHover();

    initializeStatisticsAnimation();

});


/* =========================================================
                SEARCH
========================================================= */

function initializeSearch(){

    const searchInput=document.querySelector(
        "input[name='search']"
    );

    if(!searchInput) return;

    searchInput.addEventListener("keyup",function(event){

        if(event.key==="Enter"){

            this.form.submit();

        }

    });

}


/* =========================================================
                DELETE
========================================================= */

function initializeDeleteConfirmation(){

    const deleteButtons=document.querySelectorAll(".delete");

    deleteButtons.forEach(button=>{

        button.addEventListener("click",function(event){

            const result=confirm(

                "Do you really want to delete this patient?"

            );

            if(!result){

                event.preventDefault();

            }

        });

    });

}


/* =========================================================
                STATUS
========================================================= */

function initializeStatusToggle(){

    const statusButtons=document.querySelectorAll(".status");

    statusButtons.forEach(button=>{

        button.addEventListener("click",function(event){

            const result=confirm(

                "Change patient status?"

            );

            if(!result){

                event.preventDefault();

            }

        });

    });

}


/* =========================================================
                FORM VALIDATION
========================================================= */

function initializeFormValidation(){

    const form=document.querySelector(".patient-form");

    if(!form) return;

    form.addEventListener("submit",function(event){

        const firstName=document.querySelector(
            "input[name='first_name']"
        );

        const lastName=document.querySelector(
            "input[name='last_name']"
        );

        const phone=document.querySelector(
            "input[name='phone']"
        );

        const age=document.querySelector(
            "input[name='age']"
        );

        if(firstName && firstName.value.trim().length<2){

            alert("First name must contain at least 2 characters.");

            firstName.focus();

            event.preventDefault();

            return;

        }

        if(lastName && lastName.value.trim().length<2){

            alert("Last name must contain at least 2 characters.");

            lastName.focus();

            event.preventDefault();

            return;

        }

        if(phone){

            const regex=/^[0-9]{10}$/;

            if(!regex.test(phone.value.trim())){

                alert("Enter a valid 10-digit mobile number.");

                phone.focus();

                event.preventDefault();

                return;

            }

        }

        if(age){

            const value=parseInt(age.value);

            if(value<0 || value>120){

                alert("Age must be between 0 and 120.");

                age.focus();

                event.preventDefault();

                return;

            }

        }

    });

}


/* =========================================================
                TABLE EFFECT
========================================================= */

function initializeTableHover(){

    const rows=document.querySelectorAll(

        ".patient-table tbody tr"

    );

    rows.forEach(row=>{

        row.addEventListener("mouseenter",()=>{

            row.style.transition=".25s";

            row.style.transform="scale(1.003)";

        });

        row.addEventListener("mouseleave",()=>{

            row.style.transform="scale(1)";

        });

    });

}


/* =========================================================
                STATISTICS
========================================================= */

function initializeStatisticsAnimation(){

    const cards=document.querySelectorAll(".stat-card");

    cards.forEach((card,index)=>{

        card.style.opacity="0";

        card.style.transform="translateY(20px)";

        setTimeout(()=>{

            card.style.transition=".5s";

            card.style.opacity="1";

            card.style.transform="translateY(0)";

        },index*150);

    });

}


/* =========================================================
                FLASH MESSAGE
========================================================= */

window.addEventListener("load",()=>{

    const flash=document.querySelector(".flash-container");

    if(!flash) return;

    setTimeout(()=>{

        flash.style.transition=".5s";

        flash.style.opacity="0";

        setTimeout(()=>{

            flash.remove();

        },500);

    },4000);

});


/* =========================================================
                PAGE LOADED
========================================================= */

console.log(

    "Patient Module Loaded Successfully."

);