/*==========================================================
        MODERNIZED HEALTHCARE PBM PORTAL
        AUTHENTICATION JAVASCRIPT
==========================================================*/

"use strict";


/*==========================================================
                AUTH MODULE
==========================================================*/

PBM.register("Auth", {

    loginForm: null,
    registerForm: null,

    loginButton: null,
    registerButton: null,

    loginLoading: null,
    registerLoading: null,

    init() {

        this.cacheDOM();

        this.hideLoading();

        this.bindEvents();

        console.log(
            "Authentication Module Loaded"
        );

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        /* Login */

        this.loginForm = document.getElementById(
            "loginForm"
        );

        this.loginButton = document.getElementById(
            "loginButton"
        );

        this.loginLoading = document.getElementById(
            "loginLoading"
        );

        /* Register */

        this.registerForm = document.getElementById(
            "registerForm"
        );

        this.registerButton = document.getElementById(
            "registerButton"
        );

        this.registerLoading = document.getElementById(
            "registerLoading"
        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        /* Login */

        if (this.loginForm) {

            this.loginForm.addEventListener(

                "submit",

                (event) => {

                    this.handleLogin(event);

                }

            );

        }

        /* Register */

        if (this.registerForm) {

            this.registerForm.addEventListener(

                "submit",

                (event) => {

                    this.handleRegister(event);

                }

            );

        }

    },

    /*----------------------------------------
            Login Submit
    ----------------------------------------*/

    handleLogin(event) {

        console.log(
            "Submitting Login Form"
        );

        this.showLoginLoading();

    },

    /*----------------------------------------
            Register Submit
    ----------------------------------------*/

    handleRegister(event) {

        console.log(
            "Submitting Register Form"
        );

        this.showRegisterLoading();

    },

    /*----------------------------------------
            Login Loading
    ----------------------------------------*/

    showLoginLoading() {

        if (this.loginButton) {

            this.loginButton.classList.add(
                "loading"
            );

            this.loginButton.disabled = true;

        }

        if (this.loginLoading) {

            this.loginLoading.hidden = false;

            this.loginLoading.style.display = "flex";

        }

    },

    hideLoginLoading() {

        if (this.loginButton) {

            this.loginButton.classList.remove(
                "loading"
            );

            this.loginButton.disabled = false;

        }

        if (this.loginLoading) {

            this.loginLoading.hidden = true;

            this.loginLoading.style.display = "none";

        }

    },

    /*----------------------------------------
            Register Loading
    ----------------------------------------*/

    showRegisterLoading() {

        if (this.registerButton) {

            this.registerButton.classList.add(
                "loading"
            );

            this.registerButton.disabled = true;

        }

        if (this.registerLoading) {

            this.registerLoading.hidden = false;

            this.registerLoading.style.display = "flex";

        }

    },

    hideRegisterLoading() {

        if (this.registerButton) {

            this.registerButton.classList.remove(
                "loading"
            );

            this.registerButton.disabled = false;

        }

        if (this.registerLoading) {

            this.registerLoading.hidden = true;

            this.registerLoading.style.display = "none";

        }

    },

    /*----------------------------------------
            Hide All Loading
    ----------------------------------------*/

    hideLoading() {

        this.hideLoginLoading();

        this.hideRegisterLoading();

    }

});

/*==========================================================
                AUTH UTILITIES
==========================================================*/

PBM.register("AuthUtils", {

    init() {

        console.log(

            "Authentication Utilities Ready"

        );

    },

    trim(value) {

        return value.trim();

    },

    isEmpty(value) {

        return value.trim() === "";

    },

    isEmail(value) {

        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/

            .test(value);

    }

});

/*==========================================================
            AUTH NOTIFICATIONS
==========================================================*/

PBM.register("AuthNotification", {

    init() {

        console.log(

            "Notification System Ready"

        );

    },

    success(message) {

        PBM.Components.Toast.show(

            message,

            "success"

        );

    },

    error(message) {

        PBM.Components.Toast.show(

            message,

            "error"

        );

    },

    warning(message) {

        PBM.Components.Toast.show(

            message,

            "warning"

        );

    },

    info(message) {

        PBM.Components.Toast.show(

            message,

            "info"

        );

    }

});

/*==========================================================
                PASSWORD MODULE
==========================================================*/

PBM.register("Password", {

    passwordInput: null,

    confirmPasswordInput: null,

    togglePassword: null,

    toggleConfirmPassword: null,

    passwordIcon: null,

    confirmPasswordIcon: null,

    passwordVisible: false,

    confirmVisible: false,

    init() {

        this.cacheDOM();

        this.bindEvents();

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        this.passwordInput = document.getElementById(
            "password"
        );

        this.confirmPasswordInput = document.getElementById(
            "confirm_password"
        );

        this.togglePassword = document.getElementById(
            "togglePassword"
        );

        this.toggleConfirmPassword = document.getElementById(
            "toggleConfirmPassword"
        );

        this.passwordIcon = document.getElementById(
            "passwordIcon"
        );

        this.confirmPasswordIcon = document.getElementById(
            "confirmPasswordIcon"
        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        if (

            this.togglePassword &&

            this.passwordInput

        ) {

            this.togglePassword.addEventListener(

                "click",

                () => this.toggleMainPassword()

            );

        }

        if (

            this.toggleConfirmPassword &&

            this.confirmPasswordInput

        ) {

            this.toggleConfirmPassword.addEventListener(

                "click",

                () => this.toggleConfirm()

            );

        }

    },

    /*----------------------------------------
            Main Password
    ----------------------------------------*/

    toggleMainPassword() {

        this.passwordVisible =

            !this.passwordVisible;

        this.passwordInput.type =

            this.passwordVisible

            ? "text"

            : "password";

        this.updatePasswordIcon();

    },

    updatePasswordIcon() {

        if (!this.passwordIcon) return;

        this.passwordIcon.classList.toggle(

            "fa-eye",

            !this.passwordVisible

        );

        this.passwordIcon.classList.toggle(

            "fa-eye-slash",

            this.passwordVisible

        );

    },

    /*----------------------------------------
            Confirm Password
    ----------------------------------------*/

    toggleConfirm() {

        this.confirmVisible =

            !this.confirmVisible;

        this.confirmPasswordInput.type =

            this.confirmVisible

            ? "text"

            : "password";

        this.updateConfirmIcon();

    },

    updateConfirmIcon() {

        if (!this.confirmPasswordIcon) return;

        this.confirmPasswordIcon.classList.toggle(

            "fa-eye",

            !this.confirmVisible

        );

        this.confirmPasswordIcon.classList.toggle(

            "fa-eye-slash",

            this.confirmVisible

        );

    },

    /*----------------------------------------
            Hide All Passwords
    ----------------------------------------*/

    hide() {

        this.passwordVisible = false;

        this.confirmVisible = false;

        if (this.passwordInput) {

            this.passwordInput.type = "password";

        }

        if (this.confirmPasswordInput) {

            this.confirmPasswordInput.type = "password";

        }

        this.updatePasswordIcon();

        this.updateConfirmIcon();

    }

});

/*==========================================================
                FORM VALIDATION
==========================================================*/

PBM.register("Validation", {

    form: null,

    init() {

        this.form = document.querySelector("form");

    },

    /*----------------------------------------
            Login Validation
    ----------------------------------------*/

    validateLogin() {

        let valid = true;

        const username = document.getElementById("username");
        const password = document.getElementById("password");

        valid &= this.required(
            username,
            "usernameError",
            "Username is required."
        );

        valid &= this.required(
            password,
            "passwordError",
            "Password is required."
        );

        return !!valid;

    },

    /*----------------------------------------
            Register Validation
    ----------------------------------------*/

    validateRegister() {

        let valid = true;

        valid &= this.required(
            document.getElementById("full_name"),
            "fullNameError",
            "Full Name is required."
        );

        valid &= this.required(
            document.getElementById("username"),
            "usernameError",
            "Username is required."
        );

        valid &= this.validateEmail();

        valid &= this.validatePassword();

        valid &= this.validateConfirmPassword();

        valid &= this.validateRole();

        valid &= this.validateTerms();

        return !!valid;

    },

    /*----------------------------------------
            Required Field
    ----------------------------------------*/

    required(input,errorId,message){

        if(!input) return true;

        if(input.value.trim()===""){

            this.showError(input,errorId,message);

            return false;

        }

        this.showSuccess(input,errorId);

        return true;

    },

    /*----------------------------------------
            Email
    ----------------------------------------*/

    validateEmail(){

        const input=document.getElementById("email");

        if(!input) return true;

        const regex=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if(!regex.test(input.value.trim())){

            this.showError(

                input,

                "emailError",

                "Enter a valid email."

            );

            return false;

        }

        this.showSuccess(

            input,

            "emailError"

        );

        return true;

    },

    /*----------------------------------------
            Password
    ----------------------------------------*/

    validatePassword(){

        const input=document.getElementById("password");

        if(!input) return true;

        const password=input.value;

        const regex=

        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/;

        if(!regex.test(password)){

            this.showError(

                input,

                "passwordError",

                "Minimum 8 characters with uppercase, lowercase, number and symbol."

            );

            return false;

        }

        this.showSuccess(

            input,

            "passwordError"

        );

        return true;

    },

    /*----------------------------------------
            Confirm Password
    ----------------------------------------*/

    validateConfirmPassword(){

        const password=document.getElementById("password");

        const confirm=document.getElementById("confirm_password");

        if(!confirm) return true;

        if(confirm.value!==password.value){

            this.showError(

                confirm,

                "confirmPasswordError",

                "Passwords do not match."

            );

            return false;

        }

        this.showSuccess(

            confirm,

            "confirmPasswordError"

        );

        return true;

    },

    /*----------------------------------------
            Role
    ----------------------------------------*/

    validateRole(){

        const role=document.getElementById("role");

        if(!role) return true;

        if(role.value===""){

            this.showError(

                role,

                "roleError",

                "Select a role."

            );

            return false;

        }

        this.showSuccess(

            role,

            "roleError"

        );

        return true;

    },

    /*----------------------------------------
            Terms
    ----------------------------------------*/

    validateTerms(){

        const terms=document.getElementById("acceptTerms");

        if(!terms) return true;

        if(!terms.checked){

            const error=document.getElementById("termsError");

            if(error){

                error.textContent="Accept Terms & Conditions.";

            }

            return false;

        }

        const error=document.getElementById("termsError");

        if(error){

            error.textContent="";

        }

        return true;

    },

    /*----------------------------------------
            Show Error
    ----------------------------------------*/

    showError(input,errorId,message){

        input.classList.remove("is-valid");

        input.classList.add("is-invalid");

        const error=document.getElementById(errorId);

        if(error){

            error.textContent=message;

        }

    },

    /*----------------------------------------
            Show Success
    ----------------------------------------*/

    showSuccess(input,errorId){

        input.classList.remove("is-invalid");

        input.classList.add("is-valid");

        const error=document.getElementById(errorId);

        if(error){

            error.textContent="";

        }

    },

    /*----------------------------------------
            Reset
    ----------------------------------------*/

    reset(){

        document.querySelectorAll(

            ".is-valid,.is-invalid"

        ).forEach(element=>{

            element.classList.remove(

                "is-valid",

                "is-invalid"

            );

        });

        document.querySelectorAll(

            ".error-message"

        ).forEach(element=>{

            element.textContent="";

        });

    }

});

/*==========================================================
                LOGIN / REGISTER SUBMISSION
==========================================================*/

PBM.register("LoginSubmission", {

    loginForm: null,

    registerForm: null,

    validation: null,

    init() {

        this.cacheDOM();

        this.validation = PBM.Validation;

        this.bindEvents();

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        this.loginForm = document.getElementById(

            "loginForm"

        );

        this.registerForm = document.getElementById(

            "registerForm"

        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        if (this.loginForm) {

            this.loginForm.addEventListener(

                "submit",

                (event) => {

                    if (

                        !this.validation.validateLogin()

                    ) {

                        event.preventDefault();

                        return;

                    }

                    PBM.Auth.showLoginLoading();

                }

            );

        }

        if (this.registerForm) {

            this.registerForm.addEventListener(

                "submit",

                (event) => {

                    if (

                        !this.validation.validateRegister()

                    ) {

                        event.preventDefault();

                        return;

                    }

                    PBM.Auth.showRegisterLoading();

                }

            );

        }

    }

});

/*==========================================================
                APPLICATION BOOTSTRAP
==========================================================*/

document.addEventListener(

    "DOMContentLoaded",

    () => {

        /* Authentication */

        if (

            PBM.Auth &&

            typeof PBM.Auth.init === "function"

        ) {

            PBM.Auth.init();

        }

        /* Password */

        if (

            PBM.Password &&

            typeof PBM.Password.init === "function"

        ) {

            PBM.Password.init();

        }

        /* Validation */

        if (

            PBM.Validation &&

            typeof PBM.Validation.init === "function"

        ) {

            PBM.Validation.init();

        }

        /* Login/Register */

        if (

            PBM.LoginSubmission &&

            typeof PBM.LoginSubmission.init === "function"

        ) {

            PBM.LoginSubmission.init();

        }

        /* Flash */

        if (

            PBM.FlashMessages &&

            typeof PBM.FlashMessages.init === "function"

        ) {

            PBM.FlashMessages.init();

        }

        /* Remember Me */

        if (

            PBM.RememberMe &&

            typeof PBM.RememberMe.init === "function"

        ) {

            PBM.RememberMe.init();

        }

        /* Keyboard */

        if (

            PBM.Keyboard &&

            typeof PBM.Keyboard.init === "function"

        ) {

            PBM.Keyboard.init();

        }

        /* Notifications */

        if (

            PBM.AuthNotification &&

            typeof PBM.AuthNotification.init === "function"

        ) {

            PBM.AuthNotification.init();

        }

        /* Utilities */

        if (

            PBM.AuthUtils &&

            typeof PBM.AuthUtils.init === "function"

        ) {

            PBM.AuthUtils.init();

        }

        /*----------------------------------------
                Hide Loading Overlays
        ----------------------------------------*/

        [

            "loginLoading",

            "registerLoading"

        ].forEach(id => {

            const overlay = document.getElementById(id);

            if (overlay) {

                overlay.hidden = true;

                overlay.style.display = "none";

            }

        });

        if (

            PBM.Components &&

            PBM.Components.Loader

        ) {

            PBM.Components.Loader.hide();

        }

        console.log(

            "========================================"

        );

        console.log(

            " Healthcare PBM Authentication Ready "

        );

        console.log(

            "========================================"

        );

    }

);

/*==========================================================
                FLASH MESSAGE MODULE
==========================================================*/

PBM.register("FlashMessages", {

    flashContainer: null,

    flashMessages: [],

    autoCloseTime: 5000,

    init() {

        this.cacheDOM();

        this.bindEvents();

        this.autoClose();

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        this.flashContainer = document.querySelector(

            ".flash-container"

        );

        this.flashMessages = document.querySelectorAll(

            ".flash-message"

        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        this.flashMessages.forEach(

            (message) => {

                const closeButton =

                    message.querySelector(

                        ".flash-close"

                    );

                if (closeButton) {

                    closeButton.addEventListener(

                        "click",

                        () => {

                            this.remove(message);

                        }

                    );

                }

            }

        );

    },

    /*----------------------------------------
            Auto Close Messages
    ----------------------------------------*/

    autoClose() {

        this.flashMessages.forEach(

            (message) => {

                setTimeout(() => {

                    this.remove(message);

                },

                this.autoCloseTime);

            }

        );

    },

    /*----------------------------------------
            Remove Message
    ----------------------------------------*/

    remove(message) {

        if (!message) {

            return;

        }

        message.style.opacity = "0";

        message.style.transform =

            "translateY(-10px)";

        setTimeout(() => {

            message.remove();

        }, 300);

    },

    /*----------------------------------------
            Remove All Messages
    ----------------------------------------*/

    clearAll() {

        this.flashMessages.forEach(

            (message) => {

                this.remove(message);

            }

        );

    }

});

/*==========================================================
                REMEMBER ME MODULE
==========================================================*/

PBM.register("RememberMe", {

    checkbox: null,

    usernameInput: null,

    storageKey: "pbmRememberedUsername",

    init() {

        this.cacheDOM();

        this.loadRememberedUser();

        this.bindEvents();

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        this.checkbox = document.getElementById(

            "remember"

        );

        this.usernameInput = document.getElementById(

            "username"

        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        if (!this.checkbox ||

            !this.usernameInput) {

            return;

        }

        this.checkbox.addEventListener(

            "change",

            () => {

                this.handleRemember();

            }

        );

        this.usernameInput.addEventListener(

            "input",

            () => {

                if (

                    this.checkbox.checked

                ) {

                    this.save();

                }

            }

        );

    },

    /*----------------------------------------
            Handle Remember Me
    ----------------------------------------*/

    handleRemember() {

        if (

            this.checkbox.checked

        ) {

            this.save();

        }

        else {

            this.clear();

        }

    },

    /*----------------------------------------
            Save Username
    ----------------------------------------*/

    save() {

        localStorage.setItem(

            this.storageKey,

            this.usernameInput.value.trim()

        );

    },

    /*----------------------------------------
            Load Username
    ----------------------------------------*/

    loadRememberedUser() {

        if (

            !this.checkbox ||

            !this.usernameInput

        ) {

            return;

        }

        const username =

            localStorage.getItem(

                this.storageKey

            );

        if (username) {

            this.usernameInput.value = username;

            this.checkbox.checked = true;

        }

    },

    /*----------------------------------------
            Clear Remembered User
    ----------------------------------------*/

    clear() {

        localStorage.removeItem(

            this.storageKey

        );

    }

});

/*==========================================================
                KEYBOARD SHORTCUTS
==========================================================*/

PBM.register("Keyboard", {

    form: null,

    usernameInput: null,

    passwordInput: null,

    init() {

        this.cacheDOM();

        this.bindEvents();

    },

    /*----------------------------------------
            Cache DOM
    ----------------------------------------*/

    cacheDOM() {

        this.form = document.getElementById(

            "loginForm"

        );

        this.usernameInput = document.getElementById(

            "username"

        );

        this.passwordInput = document.getElementById(

            "password"

        );

    },

    /*----------------------------------------
            Events
    ----------------------------------------*/

    bindEvents() {

        document.addEventListener(

            "keydown",

            (event) => {

                this.handleKeys(event);

            }

        );

    },

    /*----------------------------------------
            Keyboard Handler
    ----------------------------------------*/

    handleKeys(event) {

        switch (event.key) {

            case "Escape":

                this.handleEscape();

                break;

            case "Enter":

                this.handleEnter(event);

                break;

            default:

                break;

        }

    },

    /*----------------------------------------
            Escape Key
    ----------------------------------------*/

    handleEscape() {

        if (

            PBM.Password &&

            typeof PBM.Password.hide === "function"

        ) {

            PBM.Password.hide();

        }

    },

    /*----------------------------------------
            Enter Key
    ----------------------------------------*/

    handleEnter(event) {

        const activeElement =

            document.activeElement;

        if (

            activeElement === this.usernameInput ||

            activeElement === this.passwordInput

        ) {

            if (

                PBM.Validation &&

                !PBM.Validation.validateForm()

            ) {

                event.preventDefault();

            }

        }

    }

});

/*==========================================================
                APPLICATION BOOTSTRAP
==========================================================*/

document.addEventListener(

    "DOMContentLoaded",

    () => {

        /*----------------------------------------
                Authentication
        ----------------------------------------*/

        if (

            PBM.Auth &&

            typeof PBM.Auth.init === "function"

        ) {

            PBM.Auth.init();

        }

        /*----------------------------------------
                Password
        ----------------------------------------*/

        if (

            PBM.Password &&

            typeof PBM.Password.init === "function"

        ) {

            PBM.Password.init();

        }

        /*----------------------------------------
                Validation
        ----------------------------------------*/

        if (

            PBM.Validation &&

            typeof PBM.Validation.init === "function"

        ) {

            PBM.Validation.init();

        }

        /*----------------------------------------
                Login Submission
        ----------------------------------------*/

        if (

            PBM.LoginSubmission &&

            typeof PBM.LoginSubmission.init === "function"

        ) {

            PBM.LoginSubmission.init();

        }

        /*----------------------------------------
                Flash Messages
        ----------------------------------------*/

        if (

            PBM.FlashMessages &&

            typeof PBM.FlashMessages.init === "function"

        ) {

            PBM.FlashMessages.init();

        }

        /*----------------------------------------
                Remember Me
        ----------------------------------------*/

        if (

            PBM.RememberMe &&

            typeof PBM.RememberMe.init === "function"

        ) {

            PBM.RememberMe.init();

        }

        /*----------------------------------------
                Keyboard Shortcuts
        ----------------------------------------*/

        if (

            PBM.Keyboard &&

            typeof PBM.Keyboard.init === "function"

        ) {

            PBM.Keyboard.init();

        }

        /*----------------------------------------
                Notification System
        ----------------------------------------*/

        if (

            PBM.AuthNotification &&

            typeof PBM.AuthNotification.init === "function"

        ) {

            PBM.AuthNotification.init();

        }

        /*----------------------------------------
                Utilities
        ----------------------------------------*/

        if (

            PBM.AuthUtils &&

            typeof PBM.AuthUtils.init === "function"

        ) {

            PBM.AuthUtils.init();

        }

        console.log(

            "========================================"

        );

        console.log(

            " Healthcare PBM Authentication Loaded "

        );

        console.log(

            "========================================"

        );

        /*----------------------------------------
    Hide Loading Overlay on Page Load
----------------------------------------*/

const loadingOverlay = document.getElementById("loginLoading");

if (loadingOverlay) {
    loadingOverlay.hidden = true;
}

if (
    PBM.Components &&
    PBM.Components.Loader
) {
    PBM.Components.Loader.hide();
}

    }

);

/*==========================================================
                AUTH BOOTSTRAP
==========================================================*/

document.addEventListener("DOMContentLoaded", () => {

    const overlay = document.getElementById("loginLoading");

    if (overlay) {
        overlay.hidden = true;
        overlay.style.display = "none";
    }

    console.log("Authentication Ready");

});

/*==========================================================
                FORGOT PASSWORD
==========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("forgotPasswordForm");
    const loading = document.getElementById("forgotPasswordLoading");

    // Hide loading when page loads
    if (loading) {
        loading.hidden = true;
        loading.style.display = "none";
    }

    // Show loading when form is submitted
    if (form) {

        form.addEventListener("submit", function () {

            if (loading) {

                loading.hidden = false;
                loading.style.display = "flex";

            }

        });

    }

    // Hide loading again when page finishes loading
    window.addEventListener("pageshow", function () {

        if (loading) {

            loading.hidden = true;
            loading.style.display = "none";

        }

    });

});


/*=========================================================
            PROFILE CHANGE PASSWORD
=========================================================*/

document.addEventListener("DOMContentLoaded", function () {

    const currentPassword =
        document.getElementById("current_password");

    const newPassword =
        document.getElementById("new_password");

    const confirmPassword =
        document.getElementById("confirm_password");

    const strengthBar =
        document.getElementById("strengthBar");

    const strengthText =
        document.getElementById("strengthText");

    const passwordMatch =
        document.getElementById("passwordMatch");

    // Not on profile page
    if (!newPassword) {
        return;
    }

    /*==========================================
            PASSWORD STRENGTH
    ==========================================*/

    newPassword.addEventListener("input", function () {

        let password = newPassword.value;

        let score = 0;

        if (password.length >= 8)
            score++;

        if (/[A-Z]/.test(password))
            score++;

        if (/[a-z]/.test(password))
            score++;

        if (/[0-9]/.test(password))
            score++;

        if (/[^A-Za-z0-9]/.test(password))
            score++;

        const widths = [
            "20%",
            "40%",
            "60%",
            "80%",
            "100%"
        ];

        const colors = [
            "#ef4444",
            "#f97316",
            "#facc15",
            "#22c55e",
            "#16a34a"
        ];

        const labels = [
            "Weak",
            "Fair",
            "Good",
            "Strong",
            "Very Strong"
        ];

        if (score > 0) {

            strengthBar.style.width =
                widths[score - 1];

            strengthBar.style.background =
                colors[score - 1];

            strengthText.textContent =
                "Strength : " +
                labels[score - 1];

        }
        else {

            strengthBar.style.width = "0%";

            strengthText.textContent =
                "Password Strength";

        }

    });

    /*==========================================
            PASSWORD MATCH
    ==========================================*/

    confirmPassword.addEventListener("keyup", function () {

        if (
            confirmPassword.value === ""
        ) {

            passwordMatch.textContent = "";

            return;

        }

        if (
            newPassword.value ===
            confirmPassword.value
        ) {

            passwordMatch.textContent =
                "✔ Passwords Match";

            passwordMatch.style.color =
                "#16a34a";

        }
        else {

            passwordMatch.textContent =
                "✖ Passwords Do Not Match";

            passwordMatch.style.color =
                "#dc2626";

        }

    });

});

/*=========================================================
            SHOW / HIDE PASSWORD
=========================================================*/

function togglePassword(id, button) {

    const input =
        document.getElementById(id);

    const icon =
        button.querySelector("i");

    if (input.type === "password") {

        input.type = "text";

        icon.classList.remove("fa-eye");

        icon.classList.add("fa-eye-slash");

    }
    else {

        input.type = "password";

        icon.classList.remove("fa-eye-slash");

        icon.classList.add("fa-eye");

    }

}

document

.getElementById("confirm_password")

.addEventListener(

    "paste",

    function(e){

        e.preventDefault();

    }

);

showToast(

    "Success",

    "Password changed successfully.",

    "success"

);

document

.getElementById("current_password").value="";

document

.getElementById("new_password").value="";

document

.getElementById("confirm_password").value="";


const passwordInput = document.getElementById("new_password");

if(passwordInput){

    passwordInput.addEventListener("input", function(){

        const password = this.value;

        checkRule(
            "lengthCheck",
            password.length >= 8
        );

        checkRule(
            "upperCheck",
            /[A-Z]/.test(password)
        );

        checkRule(
            "lowerCheck",
            /[a-z]/.test(password)
        );

        checkRule(
            "numberCheck",
            /\d/.test(password)
        );

        checkRule(
            "specialCheck",
            /[^A-Za-z0-9]/.test(password)
        );

    });

}

function checkRule(id, valid){

    const item = document.getElementById(id);

    if(!item) return;

    if(valid){

        item.classList.add("valid");

        item.querySelector("i").className =
            "fa-solid fa-circle-check";

    }

    else{

        item.classList.remove("valid");

        item.querySelector("i").className =
            "fa-solid fa-circle";

    }

}