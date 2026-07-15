/*==========================================================
        Healthcare PBM Portal
        Enterprise Dashboard JS
        Part 1
==========================================================*/

"use strict";

/*==========================================================
                DASHBOARD APPLICATION
==========================================================*/

const Dashboard = {

    charts:{},

    notifications:[],

    refreshInterval:null,

    init(){

        console.log(

            "Healthcare PBM Dashboard Started"

        );

        this.initializeClock();

        this.initializeCounters();

        this.initializeCharts();

        this.initializeButtons();

        this.initializeSearch();

        this.initializeNotifications();

        this.autoRefresh();

    },

/*==========================================================
                LIVE CLOCK
==========================================================*/

    initializeClock(){

        const dateElement=

            document.getElementById(

                "currentDate"

            );

        const timeElement=

            document.getElementById(

                "currentTime"

            );

        const update=()=>{

            const now=new Date();

            if(dateElement){

                dateElement.textContent=

                    now.toLocaleDateString(

                        "en-IN",

                        {

                            weekday:"long",

                            year:"numeric",

                            month:"long",

                            day:"numeric"

                        }

                    );

            }

            if(timeElement){

                timeElement.textContent=

                    now.toLocaleTimeString(

                        "en-IN"

                    );

            }

        };

        update();

        setInterval(

            update,

            1000

        );

    },

/*==========================================================
                COUNTER ANIMATION
==========================================================*/

    initializeCounters(){

        const counters=

            document.querySelectorAll(

                ".counter"

            );

        counters.forEach(counter=>{

            const target=

                parseInt(

                    counter.dataset.target

                )||0;

            let current=0;

            const increment=

                Math.ceil(

                    target/120

                );

            const timer=

                setInterval(()=>{

                    current+=increment;

                    if(current>=target){

                        current=target;

                        clearInterval(

                            timer

                        );

                    }

                    counter.textContent=

                        current.toLocaleString();

                },20);

        });

    },

/*==========================================================
                CHARTS
==========================================================*/

    initializeCharts(){

        if(

            typeof Chart==="undefined"

        ){

            console.warn(

                "Chart.js Missing"

            );

            return;

        }

        this.createClaimsChart();

        this.createRevenueChart();

        this.createStatusChart();

    },

    /*==========================================================
                CLAIMS CHART
==========================================================*/

    createClaimsChart(){

        const canvas = document.getElementById("claimsChart");

        if(!canvas) return;

        this.charts.claims = new Chart(canvas,{

            type:"line",

            data:{

                labels:[
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec"
                ],

                datasets:[{

                    label:"Healthcare Claims",

                    data:[
                        420,
                        510,
                        630,
                        580,
                        690,
                        720,
                        780,
                        830,
                        810,
                        920,
                        980,
                        1050
                    ],

                    borderColor:"#2563eb",

                    backgroundColor:"rgba(37,99,235,.15)",

                    borderWidth:4,

                    tension:.4,

                    fill:true,

                    pointRadius:5,

                    pointHoverRadius:8

                }]

            },

            options:{

                responsive:true,

                maintainAspectRatio:false,

                plugins:{

                    legend:{

                        display:true

                    }

                }

            }

        });

    },

/*==========================================================
                REVENUE CHART
==========================================================*/

    createRevenueChart(){

        const canvas=document.getElementById(

            "revenueChart"

        );

        if(!canvas) return;

        this.charts.revenue=

        new Chart(

            canvas,

            {

                type:"bar",

                data:{

                    labels:[

                        "2023",

                        "2024",

                        "2025",

                        "2026(Now)"

                    ],

                    datasets:[{

                        label:"Revenue in Lakhs ₹",

                        data:[

                            18.5,

                            24.0,

                            31.5,

                            42.0

                        ],

                        backgroundColor:[

                            "#2563eb",

                            "#16a34a",

                            "#7c3aed",

                            "#ea580c"

                        ],

                        borderRadius:10

                    }]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    plugins:{

                        legend:{

                            display:false

                        }

                    }

                }

            }

        );

    },

/*==========================================================
                STATUS PIE CHART
==========================================================*/

    createStatusChart(){

        const canvas=document.getElementById(

            "statusChart"

        );

        if(!canvas) return;

        this.charts.status=

        new Chart(

            canvas,

            {

                type:"doughnut",

                data:{

                    labels:[

                        "Approved",

                        "Pending",

                        "Rejected",

                        "High Risk"

                    ],

                    datasets:[{

                        data:[

                            72,

                            15,

                            8,

                            5

                        ],

                        backgroundColor:[

                            "#16a34a",

                            "#f59e0b",

                            "#dc2626",

                            "#7c3aed"

                        ],

                        borderWidth:0

                    }]

                },

                options:{

                    responsive:true,

                    maintainAspectRatio:false,

                    cutout:"70%",

                    plugins:{

                        legend:{

                            position:"bottom"

                        }

                    }

                }

            }

        );

    },

/*==========================================================
                BUTTONS
==========================================================*/

    initializeButtons(){

        document

        .querySelectorAll(

            ".btn"

        )

        .forEach(button=>{

            button.addEventListener(

                "click",

                ()=>{

                    console.log(

                        button.innerText,

                        "Clicked"

                    );

                }

            );

        });

    },

/*==========================================================
        PART 3 STARTS WITH

        SEARCH
        NOTIFICATIONS
        AUTO REFRESH
        AI FRAUD SIMULATION
==========================================================*/

/*==========================================================
                SEARCH FUNCTION
==========================================================*/

    initializeSearch(){

        const searchBox = document.querySelector(".table-search");

        if(!searchBox) return;

        searchBox.addEventListener("keyup",(event)=>{

            const keyword = event.target.value.toLowerCase();

            const rows = document.querySelectorAll(
                ".claims-table tbody tr"
            );

            rows.forEach(row=>{

                const text = row.innerText.toLowerCase();

                if(text.includes(keyword)){

                    row.style.display = "";

                }else{

                    row.style.display = "none";

                }

            });

        });

    },

/*==========================================================
                LIVE NOTIFICATIONS
==========================================================*/

    initializeNotifications(){

        this.notifications = [

            {

                type:"success",

                title:"Claim Approved",

                message:"Claim C1001 has been approved."

            },

            {

                type:"warning",

                title:"Duplicate Claim",

                message:"Duplicate claim detected."

            },

            {

                type:"danger",

                title:"Fraud Alert",

                message:"AI detected a high-risk claim."

            }

        ];

        console.log(

            "Notifications Loaded:",

            this.notifications.length

        );

    },

/*==========================================================
                SHOW NOTIFICATION
==========================================================*/

    showNotification(title,message,type="info"){

        console.log(

            `[${type.toUpperCase()}] ${title} : ${message}`

        );

        if(window.PBM && PBM.showToast){

            PBM.showToast(message,type);

        }

    },

/*==========================================================
                AI FRAUD SIMULATION
==========================================================*/

    simulateAI(){

        const risks=[

            "Low Risk",

            "Medium Risk",

            "High Risk"

        ];

        const hospitals=[

            "City Hospital",

            "Apollo",

            "Ruby Hall",

            "Sunrise Hospital"

        ];

        const risk=

            risks[Math.floor(

                Math.random()*risks.length

            )];

        const hospital=

            hospitals[Math.floor(

                Math.random()*hospitals.length

            )];

        console.log(

            "AI Analysis",

            risk,

            hospital

        );

    },

/*==========================================================
                AUTO REFRESH
==========================================================*/

    autoRefresh(){

        this.refreshInterval=

        setInterval(()=>{

            console.log(

                "Refreshing Dashboard..."

            );

            this.simulateAI();

        },60000);

    },

/*==========================================================
                REFRESH KPI VALUES
==========================================================*/

    refreshStatistics(){

        document

        .querySelectorAll(".counter")

        .forEach(counter=>{

            const target=

                parseInt(

                    counter.dataset.target

                );

            const random=

                Math.floor(

                    Math.random()*5

                );

            counter.textContent=

                (target+random)

                .toLocaleString();

        });

    },

/*==========================================================
                EXPORT REPORT
==========================================================*/

    exportReport(){

        console.log(

            "Exporting Dashboard Report..."

        );

        alert(

            "Dashboard Report Generated Successfully!"

        );

    },

/*==========================================================
        PART 4 STARTS WITH

        QUICK ACTIONS
        LIVE UPDATES
        WINDOW EVENTS
        INITIALIZATION
==========================================================*/

/*==========================================================
                QUICK ACTIONS
==========================================================*/

    initializeQuickActions(){

        document.querySelectorAll(".action-card").forEach(card=>{

            card.addEventListener("click",()=>{

                const action=

                    card.innerText.trim().toLowerCase();

                switch(action){

                    case "add patient":

                        this.showNotification(

                            "Patients",

                            "Opening Patient Registration...",

                            "success"

                        );

                        break;

                    case "create claim":

                        this.showNotification(

                            "Claims",

                            "Opening Claim Form...",

                            "info"

                        );

                        break;

                    case "pharmacy":

                        this.showNotification(

                            "Pharmacy",

                            "Opening Pharmacy Module...",

                            "success"

                        );

                        break;

                    case "reports":

                        this.exportReport();

                        break;

                    case "ai analysis":

                        this.simulateAI();

                        this.showNotification(

                            "AI",

                            "AI Analysis Completed.",

                            "success"

                        );

                        break;

                    case "export data":

                        this.exportReport();

                        break;

                    default:

                        console.log(action);

                }

            });

        });

    },

/*==========================================================
                LIVE DASHBOARD UPDATE
==========================================================*/

    liveUpdate(){

        setInterval(()=>{

            this.refreshStatistics();

            console.log(

                "Dashboard statistics updated."

            );

        },30000);

    },

/*==========================================================
                WINDOW EVENTS
==========================================================*/

    registerEvents(){

        window.addEventListener(

            "resize",

            ()=>{

                Object.values(this.charts).forEach(chart=>{

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

                    "Dashboard Active"

                );

            }

        );

    },

/*==========================================================
                START APPLICATION
==========================================================*/

    start(){

        this.initializeQuickActions();

        this.registerEvents();

        this.liveUpdate();

        console.log(

            "Healthcare PBM Dashboard Ready"

        );

    }

};

/*==========================================================
                APPLICATION STARTUP
==========================================================*/

document.addEventListener(

    "DOMContentLoaded",

    ()=>{

        Dashboard.init();

        Dashboard.start();

    }

);

/*==========================================================
                END OF FILE
==========================================================*/