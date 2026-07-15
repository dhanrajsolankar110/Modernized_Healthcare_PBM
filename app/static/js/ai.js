/*==========================================================
        Healthcare PBM Portal
        AI Module JavaScript
        Part 1
==========================================================*/

"use strict";

/*==========================================================
                AI APPLICATION
==========================================================*/

const AI = {

    charts:{},

    currentPage:1,

    recordsPerPage:10,

    init(){

        console.log("AI Module Started");

        this.initializeCounters();

        this.initializeCharts();

        this.initializeSearch();

        this.initializeFilters();

        this.initializeModal();

        this.initializeButtons();

    },

/*==========================================================
                COUNTERS
==========================================================*/

    initializeCounters(){

        const counters=document.querySelectorAll(".counter");

        counters.forEach(counter=>{

            const target=parseInt(counter.dataset.target)||0;

            let current=0;

            const increment=Math.ceil(target/100);

            const timer=setInterval(()=>{

                current+=increment;

                if(current>=target){

                    current=target;

                    clearInterval(timer);

                }

                counter.textContent=current.toLocaleString();

            },20);

        });

    },

/*==========================================================
                INITIALIZE CHARTS
==========================================================*/

    initializeCharts(){

        if(typeof Chart==="undefined"){

            console.warn("Chart.js Missing");

            return;

        }

        this.createFraudTrendChart();

        this.createRiskDistributionChart();

        this.createModelAccuracyChart();

        this.createPredictionChart();

    },

/*==========================================================
                FRAUD TREND
==========================================================*/

    createFraudTrendChart(){

        const canvas=document.getElementById(

            "fraudTrendChart"

        );

        if(!canvas) return;

        this.charts.trend=new Chart(canvas,{

            type:"line",

            data:{

                labels:[

                    "Jan","Feb","Mar","Apr",

                    "May","Jun","Jul","Aug",

                    "Sep","Oct","Nov","Dec"

                ],

                datasets:[{

                    label:"Fraud Cases",

                    data:[

                        42,

                        50,

                        61,

                        73,

                        66,

                        82,

                        91,

                        85,

                        76,

                        68,

                        59,

                        48

                    ],

                    borderColor:"#dc2626",

                    backgroundColor:

                        "rgba(220,38,38,.15)",

                    borderWidth:4,

                    fill:true,

                    tension:.4,

                    pointRadius:5,

                    pointHoverRadius:8

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false

            }

        });

    },

/*==========================================================
                RISK DISTRIBUTION
==========================================================*/

    createRiskDistributionChart(){

        const canvas=document.getElementById(

            "riskDistributionChart"

        );

        if(!canvas) return;

        this.charts.risk=new Chart(canvas,{

            type:"doughnut",

            data:{

                labels:[

                    "Low Risk",

                    "Medium Risk",

                    "High Risk"

                ],

                datasets:[{

                    data:[

                        74,

                        18,

                        8

                    ],

                    backgroundColor:[

                        "#16a34a",

                        "#f59e0b",

                        "#dc2626"

                    ]

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false

            }

        });

    },

/*==========================================================
        PART 2 STARTS WITH

        MODEL ACCURACY CHART
        PREDICTION CHART
        SEARCH
        FILTERS

==========================================================*/

/*==========================================================
                MODEL ACCURACY CHART
==========================================================*/

    createModelAccuracyChart(){

        const canvas=document.getElementById(

            "modelAccuracyChart"

        );

        if(!canvas) return;

        this.charts.accuracy=new Chart(canvas,{

            type:"bar",

            data:{

                labels:[

                    "Fraud Detection",

                    "Risk Prediction",

                    "Duplicate Detection",

                    "Pattern Analysis"

                ],

                datasets:[{

                    label:"Accuracy (%)",

                    data:[

                        98.7,

                        96.4,

                        99.1,

                        97.8

                    ],

                    backgroundColor:[

                        "#2563eb",

                        "#16a34a",

                        "#f59e0b",

                        "#7c3aed"

                    ],

                    borderRadius:10

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                scales:{

                    y:{

                        beginAtZero:true,

                        max:100

                    }

                },

                plugins:{

                    legend:{

                        display:false

                    }

                }

            }

        });

    },

/*==========================================================
                PREDICTION PERFORMANCE
==========================================================*/

    createPredictionChart(){

        const canvas=document.getElementById(

            "predictionChart"

        );

        if(!canvas) return;

        this.charts.prediction=new Chart(canvas,{

            type:"line",

            data:{

                labels:[

                    "Mon",

                    "Tue",

                    "Wed",

                    "Thu",

                    "Fri",

                    "Sat",

                    "Sun"

                ],

                datasets:[{

                    label:"Predictions",

                    data:[

                        145,

                        162,

                        178,

                        191,

                        205,

                        198,

                        214

                    ],

                    borderColor:"#7c3aed",

                    backgroundColor:

                        "rgba(124,58,237,.15)",

                    fill:true,

                    tension:.4,

                    borderWidth:4,

                    pointRadius:5

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false

            }

        });

    },

/*==========================================================
                SMART SEARCH
==========================================================*/

    initializeSearch(){

        const search=document.getElementById(

            "aiSearch"

        );

        if(!search) return;

        search.addEventListener("keyup",(event)=>{

            const keyword=

                event.target.value.toLowerCase();

            const rows=document.querySelectorAll(

                ".ai-table tbody tr"

            );

            rows.forEach(row=>{

                if(

                    row.innerText

                    .toLowerCase()

                    .includes(keyword)

                ){

                    row.style.display="";

                }

                else{

                    row.style.display="none";

                }

            });

        });

    },

/*==========================================================
                FILTERS
==========================================================*/

    initializeFilters(){

        const riskFilter=document.getElementById(

            "riskFilter"

        );

        const modelFilter=document.getElementById(

            "modelFilter"

        );

        const applyFilters=()=>{

            const risk=

                riskFilter.value.toLowerCase();

            const model=

                modelFilter.value.toLowerCase();

            const rows=document.querySelectorAll(

                ".ai-table tbody tr"

            );

            rows.forEach(row=>{

                const cells=row.querySelectorAll("td");

                const aiModel=

                    cells[3].innerText.toLowerCase();

                const status=

                    cells[6].innerText.toLowerCase();

                let visible=true;

                if(

                    risk!=="all risk levels"

                ){

                    if(

                        !status.includes(

                            risk.replace(" risk","")

                        )

                    ){

                        visible=false;

                    }

                }

                if(

                    model!=="all ai models"

                ){

                    if(

                        !aiModel.includes(

                            model

                        )

                    ){

                        visible=false;

                    }

                }

                row.style.display=

                    visible ? "" : "none";

            });

        };

        riskFilter.addEventListener(

            "change",

            applyFilters

        );

        modelFilter.addEventListener(

            "change",

            applyFilters

        );

    },

/*==========================================================
        PART 3 STARTS WITH

        AI MODAL
        ACTION BUTTONS
        GENERATE REPORT
        AI ANALYSIS
        NOTIFICATIONS

==========================================================*/

/*==========================================================
                AI MODAL
==========================================================*/

    initializeModal(){

        const modal=document.getElementById("aiModal");

        const openButton=document.querySelector(".btn-primary");

        const closeButton=document.querySelector(".close-modal");

        if(openButton && modal){

            openButton.addEventListener("click",()=>{

                modal.classList.add("active");

            });

        }

        if(closeButton && modal){

            closeButton.addEventListener("click",()=>{

                modal.classList.remove("active");

            });

        }

        window.addEventListener("click",(event)=>{

            if(event.target===modal){

                modal.classList.remove("active");

            }

        });

        const form=document.getElementById("aiForm");

        if(form){

            form.addEventListener("submit",(event)=>{

                event.preventDefault();

                this.runAIAnalysis();

                modal.classList.remove("active");

                form.reset();

            });

        }

    },

/*==========================================================
                ACTION BUTTONS
==========================================================*/

    initializeButtons(){

        document.querySelectorAll(".btn-view").forEach(button=>{

            button.addEventListener("click",()=>{

                this.showNotification(

                    "Opening AI analysis details...",

                    "info"

                );

            });

        });

        document.querySelectorAll(".btn-report").forEach(button=>{

            button.addEventListener("click",()=>{

                this.generateReport();

            });

        });

        document.querySelectorAll(".btn-delete").forEach(button=>{

            button.addEventListener("click",()=>{

                const confirmDelete=confirm(

                    "Delete this AI analysis record?"

                );

                if(confirmDelete){

                    const row=button.closest("tr");

                    if(row){

                        row.remove();

                    }

                    this.showNotification(

                        "AI record deleted successfully.",

                        "success"

                    );

                }

            });

        });

    },

/*==========================================================
                GENERATE REPORT
==========================================================*/

    generateReport(){

        this.showNotification(

            "Generating AI report...",

            "info"

        );

        setTimeout(()=>{

            this.showNotification(

                "AI report generated successfully.",

                "success"

            );

        },2000);

    },

/*==========================================================
                RUN AI ANALYSIS
==========================================================*/

    runAIAnalysis(){

        this.showNotification(

            "Running AI analysis...",

            "info"

        );

        setTimeout(()=>{

            this.showNotification(

                "Collecting healthcare claim data...",

                "info"

            );

        },1000);

        setTimeout(()=>{

            this.showNotification(

                "Fraud Detection Model completed.",

                "success"

            );

        },2500);

        setTimeout(()=>{

            this.showNotification(

                "Risk Prediction completed.",

                "success"

            );

        },3500);

        setTimeout(()=>{

            this.showNotification(

                "Duplicate Detection completed.",

                "success"

            );

        },4500);

        setTimeout(()=>{

            this.showNotification(

                "Pattern Analysis completed.",

                "success"

            );

        },5500);

        setTimeout(()=>{

            this.showNotification(

                "AI analysis finished successfully.",

                "success"

            );

        },6500);

    },

/*==========================================================
                NOTIFICATION SYSTEM
==========================================================*/

    showNotification(message,type="info"){

        console.log(

            "["+type.toUpperCase()+"]",

            message

        );

        if(window.PBM && PBM.showToast){

            PBM.showToast(message,type);

        }else{

            alert(message);

        }

    },

/*==========================================================
        PART 4 STARTS WITH

        PAGINATION
        LIVE UPDATE
        REAL-TIME MONITORING
        WINDOW EVENTS
        APPLICATION STARTUP

==========================================================*/

/*==========================================================
                PAGINATION
==========================================================*/

    initializePagination(){

        const rows=Array.from(

            document.querySelectorAll(

                ".ai-table tbody tr"

            )

        );

        const pageButtons=document.querySelectorAll(

            ".page-btn"

        );

        if(rows.length===0 || pageButtons.length===0){

            return;

        }

        const showPage=(page)=>{

            this.currentPage=page;

            const start=

                (page-1)*this.recordsPerPage;

            const end=

                start+this.recordsPerPage;

            rows.forEach((row,index)=>{

                row.style.display=

                    (index>=start && index<end)

                    ? ""

                    : "none";

            });

            pageButtons.forEach(btn=>{

                btn.classList.remove("active");

            });

            pageButtons.forEach(btn=>{

                if(btn.textContent.trim()==page){

                    btn.classList.add("active");

                }

            });

        };

        pageButtons.forEach(button=>{

            const page=parseInt(button.textContent);

            if(!isNaN(page)){

                button.addEventListener(

                    "click",

                    ()=>showPage(page)

                );

            }

        });

        showPage(1);

    },

/*==========================================================
                LIVE COUNTER UPDATE
==========================================================*/

    liveUpdate(){

        setInterval(()=>{

            document.querySelectorAll(

                ".counter"

            ).forEach(counter=>{

                const target=

                    parseInt(

                        counter.dataset.target

                    ) || 0;

                const random=

                    Math.floor(

                        Math.random()*5

                    );

                counter.textContent=

                    (target+random)

                    .toLocaleString();

            });

            console.log(

                "AI Dashboard Updated"

            );

        },60000);

    },

/*==========================================================
                REAL-TIME AI MONITOR
==========================================================*/

    realTimeMonitoring(){

        setInterval(()=>{

            const alerts=[

                "New suspicious claim detected.",

                "Duplicate claim identified.",

                "AI model completed prediction.",

                "High-risk claim requires review.",

                "Pattern analysis finished."

            ];

            const types=[

                "warning",

                "danger",

                "success",

                "info"

            ];

            const message=

                alerts[

                    Math.floor(

                        Math.random()*alerts.length

                    )

                ];

            const type=

                types[

                    Math.floor(

                        Math.random()*types.length

                    )

                ];

            this.showNotification(

                message,

                type

            );

        },180000);

    },

/*==========================================================
                AUTO FRAUD ALERTS
==========================================================*/

    fraudAlertMonitor(){

        setInterval(()=>{

            const highRisk=

                Math.floor(

                    Math.random()*100

                );

            if(highRisk>85){

                this.showNotification(

                    "Critical fraud risk detected!",

                    "danger"

                );

            }

        },120000);

    },

/*==========================================================
                WINDOW EVENTS
==========================================================*/

    registerEvents(){

        window.addEventListener(

            "resize",

            ()=>{

                Object.values(

                    this.charts

                ).forEach(chart=>{

                    if(chart){

                        chart.resize();

                    }

                });

            }

        );

        window.addEventListener(

            "focus",

            ()=>{

                console.log(

                    "AI Module Active"

                );

            }

        );

    },

/*==========================================================
                START APPLICATION
==========================================================*/

    start(){

        this.initializePagination();

        this.registerEvents();

        this.liveUpdate();

        this.realTimeMonitoring();

        this.fraudAlertMonitor();

        console.log(

            "AI Module Ready"

        );

    }

};

/*==========================================================
                APPLICATION STARTUP
==========================================================*/

document.addEventListener(

    "DOMContentLoaded",

    ()=>{

        AI.init();

        AI.start();

    }

);

/*==========================================================
                END OF AI.JS
==========================================================*/