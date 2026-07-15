/*==========================================================
        CHARTS.JS
==========================================================*/

"use strict";

window.PBM = window.PBM || {};

PBM.register("ChartsHelper", {

    init() {

        console.log("Charts Helper Loaded");

        // Check if Chart.js library exists
        if (typeof Chart === "undefined") {

            console.warn("Chart.js library not found.");

            return;

        }

        console.log("Chart.js Ready");

    }

});