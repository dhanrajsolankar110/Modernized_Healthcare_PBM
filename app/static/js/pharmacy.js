/* ==========================================================
                PHARMACY MANAGEMENT
        Modernized Healthcare PBM Web Portal
========================================================== */

document.addEventListener("DOMContentLoaded", function () {

    console.log("Pharmacy Module Loaded Successfully");

    /* ==========================================
            Auto Close Flash Messages
    ========================================== */

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        setTimeout(function(){

            alert.style.opacity = "0";

            alert.style.transform = "translateY(-10px)";

            setTimeout(function(){

                alert.remove();

            },300);

        },4000);

    });

    /* ==========================================
            Search Input
    ========================================== */

    const searchInput = document.querySelector(".search-box input");

    if(searchInput){

        searchInput.addEventListener("focus",function(){

            this.parentElement.style.boxShadow =
                "0 0 0 3px rgba(37,99,235,.20)";

        });

        searchInput.addEventListener("blur",function(){

            this.parentElement.style.boxShadow =
                "0 4px 15px rgba(0,0,0,.05)";

        });

    }

    /* ==========================================
            Delete Confirmation
    ========================================== */

    const deleteForm = document.querySelector(".pharmacy-delete-page form");

    if(deleteForm){

        deleteForm.addEventListener("submit",function(e){

            const confirmed = confirm(
                "Are you sure you want to permanently delete this medicine?"
            );

            if(!confirmed){

                e.preventDefault();

            }

        });

    }

    /* ==========================================
            Table Hover Effect
    ========================================== */

    document.querySelectorAll(".medicine-table tbody tr")
        .forEach(function(row){

        row.addEventListener("mouseenter",function(){

            this.style.transition=".25s";

        });

    });

    /* ==========================================
            Form Validation
    ========================================== */

    const medicineForm = document.querySelector(".pharmacy-form");

    if(medicineForm){

        medicineForm.addEventListener("submit",function(e){

            const medicineName =
                document.querySelector(
                    'input[name="medicine_name"]'
                );

            if(medicineName){

                if(medicineName.value.trim()===""){

                    alert("Medicine Name is required.");

                    medicineName.focus();

                    e.preventDefault();

                    return;

                }

            }

            const stock =
                document.querySelector(
                    'input[name="stock_quantity"]'
                );

            if(stock){

                if(parseInt(stock.value)<0){

                    alert("Stock Quantity cannot be negative.");

                    stock.focus();

                    e.preventDefault();

                    return;

                }

            }

            const price =
                document.querySelector(
                    'input[name="unit_price"]'
                );

            if(price){

                if(parseFloat(price.value)<=0){

                    alert("Unit Price must be greater than zero.");

                    price.focus();

                    e.preventDefault();

                    return;

                }

            }

        });

    }

});