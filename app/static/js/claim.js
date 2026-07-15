/*
==========================================================
            CLAIM MANAGEMENT
            claim.js
            PART 1
==========================================================
*/

document.addEventListener("DOMContentLoaded", function () {

    initializeSearch();

    initializeFlashMessages();

    initializeButtons();

});


/*==========================================================
                SEARCH
==========================================================*/

function initializeSearch() {

    const searchInput = document.querySelector(
        'input[name="search"]'
    );

    if (!searchInput) return;

    searchInput.addEventListener("keyup", function (event) {

        if (event.key === "Enter") {

            event.target.form.submit();

        }

    });

}


/*==========================================================
                FLASH MESSAGES
==========================================================*/

function initializeFlashMessages() {

    const messages = document.querySelectorAll(".flash-message");

    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.opacity = "0";

            message.style.transition = "0.5s";

            setTimeout(function () {

                message.remove();

            }, 500);

        }, 3000);

    });

}


/*==========================================================
                BUTTON LOADING
==========================================================*/

function initializeButtons() {

    const forms = document.querySelectorAll("form");

    forms.forEach(function (form) {

        form.addEventListener("submit", function () {

            const submitButton = form.querySelector(
                'button[type="submit"]'
            );

            if (!submitButton) return;

            submitButton.disabled = true;

            submitButton.innerHTML =

                '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';

        });

    });

}

/*
==========================================================
            CLAIM MANAGEMENT
            claim.js
            PART 2

            FORM VALIDATION
==========================================================
*/

document.addEventListener("DOMContentLoaded", function () {

    initializeValidation();

});


/*==========================================================
                FORM VALIDATION
==========================================================*/

function initializeValidation() {

    const form = document.querySelector(".claim-form");

    if (!form) return;

    form.addEventListener("submit", function (e) {

        const claimID = document.querySelector(
            'input[name="claim_id"]'
        );

        const hospital = document.querySelector(
            'input[name="hospital_name"]'
        );

        const doctor = document.querySelector(
            'input[name="doctor_name"]'
        );

        const disease = document.querySelector(
            'input[name="disease"]'
        );

        const amount = document.querySelector(
            'input[name="claim_amount"]'
        );

        const treatmentDate = document.querySelector(
            'input[name="treatment_date"]'
        );

        if (
            !claimID.value.trim() ||
            !hospital.value.trim() ||
            !doctor.value.trim() ||
            !disease.value.trim()
        ) {

            alert("Please fill in all required fields.");

            e.preventDefault();

            return;

        }

        if (

            parseFloat(amount.value) <= 0 ||

            isNaN(parseFloat(amount.value))

        ) {

            alert("Claim amount must be greater than 0.");

            amount.focus();

            e.preventDefault();

            return;

        }

        const selectedDate = new Date(treatmentDate.value);

        const today = new Date();

        today.setHours(0,0,0,0);

        if (selectedDate > today) {

            alert("Treatment date cannot be in the future.");

            treatmentDate.focus();

            e.preventDefault();

            return;

        }

    });

}


/*==========================================================
                CLAIM AMOUNT
==========================================================*/

const amountInput = document.querySelector(
    'input[name="claim_amount"]'
);

if (amountInput) {

    amountInput.addEventListener("input", function () {

        if (this.value < 0) {

            this.value = "";

        }

    });

}


/*==========================================================
                CLAIM ID
==========================================================*/

const claimIDInput = document.querySelector(
    'input[name="claim_id"]'
);

if (claimIDInput) {

    claimIDInput.addEventListener("input", function () {

        this.value = this.value.toUpperCase();

    });

}


/*==========================================================
                HOSPITAL & DOCTOR
==========================================================*/

const textFields = [

    'input[name="hospital_name"]',

    'input[name="doctor_name"]',

    'input[name="disease"]'

];

textFields.forEach(function(selector){

    const field = document.querySelector(selector);

    if(!field) return;

    field.addEventListener("input", function(){

        this.value = this.value.replace(/\s{2,}/g," ");

    });

});

/*
==========================================================
            CLAIM MANAGEMENT
            claim.js
            PART 3

            DELETE
            RESET
            UTILITIES
==========================================================
*/


/*==========================================================
                DELETE CONFIRMATION
==========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const deleteForm = document.querySelector(".delete-card form") ||
                       document.querySelector('form[action*="delete"]');

    if (deleteForm) {

        deleteForm.addEventListener("submit", function (e) {

            const confirmDelete = confirm(
                "Are you sure you want to permanently delete this claim?"
            );

            if (!confirmDelete) {

                e.preventDefault();

            }

        });

    }

});


/*==========================================================
                RESET CONFIRMATION
==========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const resetButton = document.querySelector(
        'button[type="reset"]'
    );

    if (!resetButton) return;

    resetButton.addEventListener("click", function (e) {

        const confirmReset = confirm(
            "Do you want to clear all entered data?"
        );

        if (!confirmReset) {

            e.preventDefault();

        }

    });

});


/*==========================================================
                COPY CLAIM ID
==========================================================*/

function copyClaimID(id){

    navigator.clipboard.writeText(id);

    alert("Claim ID copied successfully.");

}


/*==========================================================
                KEYBOARD SHORTCUTS
==========================================================*/

document.addEventListener("keydown", function (e) {

    // Ctrl + S

    if (e.ctrlKey && e.key.toLowerCase() === "s") {

        const form = document.querySelector(".claim-form");

        if (form) {

            e.preventDefault();

            form.requestSubmit();

        }

    }

    // ESC

    if (e.key === "Escape") {

        const backButton = document.querySelector(".btn-outline");

        if (backButton) {

            backButton.click();

        }

    }

});


/*==========================================================
                AUTO FOCUS
==========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const firstInput = document.querySelector(

        'input[name="claim_id"]'

    );

    if(firstInput){

        firstInput.focus();

    }

});


/*==========================================================
                CONSOLE MESSAGE
==========================================================*/

console.log(
    "Claims Management Module Loaded Successfully."
);

/*==========================================================
                    END OF FILE
==========================================================*/