/*
=========================================================
        REPORTS & ANALYTICS JAVASCRIPT
=========================================================
*/

document.addEventListener("DOMContentLoaded", function () {

    /* =====================================================
                    PATIENT CHART
    ====================================================== */

    const patientCanvas = document.getElementById("patientChart");

    if (patientCanvas && typeof reportData !== "undefined") {

        new Chart(patientCanvas, {

            type: "pie",

            data: {

                labels: [

                    "Male",

                    "Female"

                ],

                datasets: [{

                    data: [

                        reportData.male,

                        reportData.female

                    ],

                    backgroundColor: [

                        "#2563eb",

                        "#ec4899"

                    ]

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        position: "bottom"

                    }

                }

            }

        });

    }

    /* =====================================================
                    CLAIM CHART
    ====================================================== */

    const claimCanvas = document.getElementById("claimChart");

    if (claimCanvas && typeof reportData !== "undefined") {

        new Chart(claimCanvas, {

            type: "bar",

            data: {

                labels: [

                    "Approved",

                    "Pending",

                    "Rejected"

                ],

                datasets: [{

                    label: "Claims",

                    data: [

                        reportData.approved,

                        reportData.pending,

                        reportData.rejected

                    ],

                    backgroundColor: [

                        "#16a34a",

                        "#d97706",

                        "#dc2626"

                    ]

                }]

            },

            options: {

                responsive: true,

                scales: {

                    y: {

                        beginAtZero: true

                    }

                }

            }

        });

    }

    /* =====================================================
                    REFRESH BUTTON
    ====================================================== */

    const refreshBtn = document.querySelector(".toolbar-right .btn");

    if (refreshBtn) {

        refreshBtn.addEventListener(

            "click",

            function () {

                window.location.reload();

            }

        );

    }

    /* =====================================================
                    PDF EXPORT
    ====================================================== */

    const pdfButton = document.querySelector(

        ".header-buttons .btn-primary"

    );

    if (pdfButton) {

        pdfButton.addEventListener(

            "click",

            function () {

                window.location.href = "/reports/export/pdf";

            }

        );

    }

    /* =====================================================
                    EXCEL EXPORT
    ====================================================== */

    const excelButton = document.querySelector(

        ".header-buttons .btn-success"

    );

    if (excelButton) {

        excelButton.addEventListener(

            "click",

            function () {

                window.location.href = "/reports/export/excel";

            }

        );

    }

    /* =====================================================
                    CSV EXPORT
    ====================================================== */

    const csvButton = document.querySelector(

        ".header-buttons .btn-info"

    );

    if (csvButton) {

        csvButton.addEventListener(

            "click",

            function () {

                window.location.href = "/reports/export/csv";

            }

        );

    }

});

window.addEventListener("load", function () {

    document.getElementById("loadingOverlay").style.display = "none";

});