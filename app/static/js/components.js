/*==========================================================
        PBM HEALTHCARE PORTAL
        COMPONENTS.JS
        PART 1
==========================================================*/

"use strict";

/*==========================================================
                PBM CORE
==========================================================*/

const PBM = {

    modules:{},

    register(name,module){

        this.modules[name]=module;

        this[name]=module;

    }

};

/*==========================================================
                COMPONENTS
==========================================================*/

PBM.register("Components",{

    sidebar:null,

    sidebarCollapseBtn:null,

    mobileMenuBtn:null,

    scrollTopBtn:null,

    themeToggle:null,

    init(){

        this.cacheDOM();

        this.bindEvents();

        this.updateDate();

        this.updateTime();

        setInterval(

            ()=>this.updateTime(),

            1000

        );

    },

    cacheDOM(){

        this.sidebar=document.getElementById(

            "sidebar"

        );

        this.sidebarCollapseBtn=document.getElementById(

            "sidebarCollapseBtn"

        );

        this.mobileMenuBtn=document.getElementById(

            "mobileMenuBtn"

        );

        this.scrollTopBtn=document.getElementById(

            "scrollTopBtn"

        );

        this.themeToggle=document.getElementById(

            "themeToggle"

        );

    },

    bindEvents(){

        /* Sidebar */

        if(this.sidebarCollapseBtn){

            this.sidebarCollapseBtn.addEventListener(

                "click",

                ()=>this.toggleSidebar()

            );

        }

        /* Mobile */

        if(this.mobileMenuBtn){

            this.mobileMenuBtn.addEventListener(

                "click",

                ()=>this.toggleMobileSidebar()

            );

        }

        /* Scroll */

        if(this.scrollTopBtn){

            window.addEventListener(

                "scroll",

                ()=>this.handleScroll()

            );

            this.scrollTopBtn.addEventListener(

                "click",

                ()=>{

                    window.scrollTo({

                        top:0,

                        behavior:"smooth"

                    });

                }

            );

        }

        /* Theme */

        if(this.themeToggle){

            this.themeToggle.addEventListener(

                "click",

                ()=>this.toggleTheme()

            );

        }

    },

    toggleSidebar(){

        if(this.sidebar){

            this.sidebar.classList.toggle(

                "collapsed"

            );

        }

    },

    toggleMobileSidebar(){

        if(this.sidebar){

            this.sidebar.classList.toggle(

                "active"

            );

        }

    },

    handleScroll(){

        if(!this.scrollTopBtn){

            return;

        }

        if(window.scrollY>250){

            this.scrollTopBtn.classList.add(

                "show"

            );

        }

        else{

            this.scrollTopBtn.classList.remove(

                "show"

            );

        }

    },

    updateDate(){

        const element=document.getElementById(

            "currentDate"

        );

        if(!element){

            return;

        }

        element.textContent=

            new Date().toLocaleDateString(

                "en-IN",

                {

                    weekday:"long",

                    day:"numeric",

                    month:"long",

                    year:"numeric"

                }

            );

    },

    updateTime(){

        const element=document.getElementById(

            "currentTime"

        );

        if(!element){

            return;

        }

        element.textContent=

            new Date().toLocaleTimeString(

                "en-IN"

            );

    },

    toggleTheme(){

        document.body.classList.toggle(

            "dark-theme"

        );

    }

});

/*==========================================================
        PBM HEALTHCARE PORTAL
        COMPONENTS.JS
        PART 2

        DROPDOWNS
        NOTIFICATIONS
        PROFILE
        KEYBOARD SHORTCUTS
==========================================================*/

PBM.register("Header",{

    notificationBtn:null,

    messageBtn:null,

    profileBtn:null,

    notificationDropdown:null,

    messageDropdown:null,

    profileDropdown:null,

    init(){

        this.cacheDOM();

        this.bindEvents();

    },

    cacheDOM(){

        this.notificationBtn=document.getElementById(

            "notificationBtn"

        );

        this.messageBtn=document.getElementById(

            "messageBtn"

        );

        this.profileBtn=document.getElementById(

            "profileBtn"

        );

        this.notificationDropdown=document.getElementById(

            "notificationDropdown"

        );

        this.messageDropdown=document.getElementById(

            "messageDropdown"

        );

        this.profileDropdown=document.querySelector(

            ".profile-dropdown"

        );

    },

    bindEvents(){

        if(this.notificationBtn){

            this.notificationBtn.addEventListener(

                "click",

                (event)=>{

                    event.stopPropagation();

                    this.closeAll();

                    this.toggle(

                        this.notificationDropdown

                    );

                }

            );

        }

        if(this.messageBtn){

            this.messageBtn.addEventListener(

                "click",

                (event)=>{

                    event.stopPropagation();

                    this.closeAll();

                    this.toggle(

                        this.messageDropdown

                    );

                }

            );

        }

        if(this.profileBtn){

            this.profileBtn.addEventListener(

                "click",

                (event)=>{

                    event.stopPropagation();

                    this.closeAll();

                    this.toggle(

                        this.profileDropdown

                    );

                }

            );

        }

        document.addEventListener(

            "click",

            ()=>{

                this.closeAll();

            }

        );

        document.addEventListener(

            "keydown",

            (event)=>{

                if(event.key==="Escape"){

                    this.closeAll();

                }

            }

        );

    },

    toggle(dropdown){

        if(!dropdown){

            return;

        }

        dropdown.style.display=

            dropdown.style.display==="block"

            ?"none"

            :"block";

    },

    closeAll(){

        [

            this.notificationDropdown,

            this.messageDropdown,

            this.profileDropdown

        ].forEach(dropdown=>{

            if(dropdown){

                dropdown.style.display="none";

            }

        });

    }

});

/*==========================================================
                SEARCH
==========================================================*/

PBM.register("Search",{

    input:null,

    button:null,

    init(){

        this.input=document.getElementById(

            "globalSearch"

        );

        this.button=document.querySelector(

            ".search-btn"

        );

        if(this.button){

            this.button.addEventListener(

                "click",

                ()=>this.search()

            );

        }

        if(this.input){

            this.input.addEventListener(

                "keypress",

                (event)=>{

                    if(event.key==="Enter"){

                        this.search();

                    }

                }

            );

        }

    },

    search(){

        if(!this.input){

            return;

        }

        const keyword=this.input.value.trim();

        if(keyword===""){

            alert(

                "Please enter something to search."

            );

            return;

        }

        console.log(

            "Searching:",

            keyword

        );

    }

});

/*==========================================================
                KEYBOARD SHORTCUTS
==========================================================*/

PBM.register("Keyboard",{

    init(){

        document.addEventListener(

            "keydown",

            (event)=>{

                /* Ctrl + / */

                if(event.ctrlKey && event.key==="/"){

                    event.preventDefault();

                    const input=document.getElementById(

                        "globalSearch"

                    );

                    if(input){

                        input.focus();

                    }

                }

                /* Ctrl + H */

                if(event.ctrlKey &&

                    event.key.toLowerCase()==="h"){

                    event.preventDefault();

                    location.href="/dashboard";

                }

            }

        );

    }

});

/*==========================================================
        PBM HEALTHCARE PORTAL
        COMPONENTS.JS
        PART 3

        LOADER
        TOAST
        FLASH MESSAGE
        SIDEBAR DROPDOWN
        THEME
==========================================================*/

PBM.register("UI",{

    loader:null,

    toastContainer:null,

    init(){

        this.loader=document.getElementById(

            "globalLoader"

        );

        this.toastContainer=document.getElementById(

            "toastContainer"

        );

        this.initFlashMessages();

        this.initSidebarDropdown();

        this.loadTheme();

    },

    /*======================================================
                    LOADER
    ======================================================*/

    showLoader(){

        if(this.loader){

            this.loader.classList.add(

                "active"

            );

        }

    },

    hideLoader(){

        if(this.loader){

            this.loader.classList.remove(

                "active"

            );

        }

    },

    /*======================================================
                    TOAST
    ======================================================*/

    toast(

        title,

        message,

        type="info"

    ){

        if(!this.toastContainer){

            return;

        }

        const toast=document.createElement(

            "div"

        );

        toast.className=

            `toast ${type}`;

        toast.innerHTML=`

            <div class="toast-icon">

                <i class="fa-solid fa-circle-info"></i>

            </div>

            <div class="toast-content">

                <h4>${title}</h4>

                <p>${message}</p>

            </div>

            <button class="toast-close">

                <i class="fa-solid fa-xmark"></i>

            </button>

        `;

        this.toastContainer.appendChild(

            toast

        );

        toast.querySelector(

            ".toast-close"

        ).onclick=()=>{

            toast.remove();

        };

        setTimeout(()=>{

            toast.remove();

        },5000);

    },

    /*======================================================
                    FLASH
    ======================================================*/

    initFlashMessages(){

        document.querySelectorAll(

            ".flash-message"

        ).forEach(message=>{

            setTimeout(()=>{

                message.style.opacity="0";

                message.style.transform=

                    "translateY(-20px)";

                setTimeout(()=>{

                    message.remove();

                },300);

            },5000);

        });

    },

    /*======================================================
                SIDEBAR DROPDOWN
    ======================================================*/

    initSidebarDropdown(){

        document.querySelectorAll(

            ".dropdown-btn"

        ).forEach(button=>{

            button.addEventListener(

                "click",

                ()=>{

                    const parent=

                        button.parentElement;

                    parent.classList.toggle(

                        "open"

                    );

                }

            );

        });

    },

    /*======================================================
                    THEME
    ======================================================*/

    loadTheme(){

        const theme=

            localStorage.getItem(

                "pbm-theme"

            );

        if(theme==="dark"){

            document.body.classList.add(

                "dark-theme"

            );

        }

    },

    saveTheme(){

        if(

            document.body.classList.contains(

                "dark-theme"

            )

        ){

            localStorage.setItem(

                "pbm-theme",

                "dark"

            );

        }

        else{

            localStorage.setItem(

                "pbm-theme",

                "light"

            );

        }

    }

});

/*==========================================================
                UPDATE THEME BUTTON
==========================================================*/

if(

    PBM.Components

){

    const oldToggle=

        PBM.Components.toggleTheme;

    PBM.Components.toggleTheme=function(){

        oldToggle.call(this);

        if(PBM.UI){

            PBM.UI.saveTheme();

        }

    };

}

/*==========================================================
                COMMON UTILITIES
==========================================================*/

PBM.register("Utils",{

    formatDate(date){

        return new Date(date)

            .toLocaleDateString(

                "en-IN"

            );

    },

    formatTime(date){

        return new Date(date)

            .toLocaleTimeString(

                "en-IN"

            );

    },

    randomID(){

        return Math.random()

            .toString(36)

            .substring(2,10)

            .toUpperCase();

    },

    debounce(callback,delay){

        let timer;

        return(...args)=>{

            clearTimeout(timer);

            timer=setTimeout(

                ()=>callback(...args),

                delay

            );

        };

    }

});

/*==========================================================
        PBM HEALTHCARE PORTAL
        COMPONENTS.JS
        PART 4

        APPLICATION
        RESPONSIVE
        SIDEBAR
        BOOTSTRAP
==========================================================*/

/*==========================================================
                RESPONSIVE
==========================================================*/

PBM.register("Responsive",{

    init(){

        this.bindEvents();

        this.checkWindow();

    },

    bindEvents(){

        window.addEventListener(

            "resize",

            ()=>this.checkWindow()

        );

        document.addEventListener(

            "click",

            (event)=>this.handleOutsideClick(event)

        );

    },

    checkWindow(){

        const sidebar=document.getElementById(

            "sidebar"

        );

        if(!sidebar){

            return;

        }

        if(window.innerWidth>992){

            sidebar.classList.remove(

                "active"

            );

        }

    },

    handleOutsideClick(event){

        const sidebar=document.getElementById(

            "sidebar"

        );

        const menu=document.getElementById(

            "mobileMenuBtn"

        );

        if(

            !sidebar ||

            window.innerWidth>992

        ){

            return;

        }

        if(

            !sidebar.contains(event.target) &&

            menu &&

            !menu.contains(event.target)

        ){

            sidebar.classList.remove(

                "active"

            );

        }

    }

});

/*==========================================================
                PAGE LOADER
==========================================================*/

window.addEventListener(

    "load",

    ()=>{

        if(

            PBM.UI

        ){

            PBM.UI.hideLoader();

        }

    }

);

/*==========================================================
                ERROR HANDLER
==========================================================*/

window.addEventListener(

    "error",

    function(event){

        console.error(

            "PBM Error:",

            event.message

        );

    }

);

/*==========================================================
                APPLICATION START
==========================================================*/

document.addEventListener(

    "DOMContentLoaded",

    ()=>{

        Object.keys(PBM.modules).forEach(

            function(module){

                if(

                    typeof PBM[module].init==="function"

                ){

                    try{

                        PBM[module].init();

                    }

                    catch(error){

                        console.error(

                            module,

                            error

                        );

                    }

                }

            }

        );

        console.log(

            "%cPBM Healthcare Portal Loaded",

            "color:#2563eb;font-size:16px;font-weight:bold;"

        );

    }

);

/*==========================================================
                GLOBAL FUNCTIONS
==========================================================*/

window.showLoader=function(){

    if(PBM.UI){

        PBM.UI.showLoader();

    }

};

window.hideLoader=function(){

    if(PBM.UI){

        PBM.UI.hideLoader();

    }

};

window.showToast=function(

    title,

    message,

    type="info"

){

    if(PBM.UI){

        PBM.UI.toast(

            title,

            message,

            type

        );

    }

};

/*==========================================================
        ACTIVE SIDEBAR MENU
==========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const currentPath = window.location.pathname;

    document.querySelectorAll(".sidebar-nav .nav-link").forEach(function(link){

        link.classList.remove("active");

        const path = new URL(link.href).pathname;

        if(currentPath === path){

            link.classList.add("active");

        }

    });

});

/*==========================================================
                END OF FILE
==========================================================*/