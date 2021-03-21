/* globals Chart:false, feather:false */
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}


(function() {
    'use strict'

    var usid = document.getElementById('iduser');
    var dataDescIncomes = [];
    var dataAmountIncomes = [];
    var numIncomes;
    var numExpenses;


    //Gaphs the income chart
    readTextFile("../static/img/income" + usid.value + ".json", function(text) {
        var data = JSON.parse(text);
        data['income'].forEach(element => {
            dataDescIncomes.push(element.desc);
            dataAmountIncomes.push(element.amount)
            numIncomes = numIncomes + 1;
        });
        // Graphs
        var incomeCanvas = document.getElementById("incomesChart");
        Chart.defaults.global.defaultFontFamily = "Lato";
        Chart.defaults.global.defaultFontSize = 18;

        var incomeData = {
            labels: dataDescIncomes,
            datasets: [{
                data: dataAmountIncomes,
                backgroundColor: [
                    "#FF6384",
                    "#63FF84",
                    "#84FF63",
                    "#8463FF",
                    "#6384FF",
                    "#010000",
                    "#630015",
                    "#d9002e",
                    "#ff9eb2",
                    "#156300",
                    "#001563", "#4e0063", "#b7abae", "#63d2ff"
                ]
            }]
        };

        var pieChart = new Chart(incomeCanvas, {
            type: 'pie',
            data: incomeData
        });

    });


    var dataDescExpenses = [];
    var dataAmountExpenses = [];

    //Graphs the Expense chart
    readTextFile("../static/img/expense" + usid.value + ".json", function(text) {
        var data = JSON.parse(text);
        data['expense'].forEach(element => {
            dataDescExpenses.push(element.desc);
            dataAmountExpenses.push(element.amount)
            numExpenses = numExpenses + 1;
        });
        // Graphs
        var expenseCanvas = document.getElementById("expensesChart")
        Chart.defaults.global.defaultFontFamily = "Lato";
        Chart.defaults.global.defaultFontSize = 18;

        var expenseData = {
            labels: dataDescExpenses,
            datasets: [{
                data: dataAmountExpenses,
                backgroundColor: [
                    "#FF6384",
                    "#63FF84",
                    "#84FF63",
                    "#8463FF",
                    "#6384FF",
                    "#010000",
                    "#630015",
                    "#d9002e",
                    "#ff9eb2",
                    "#156300",
                    "#001563", "#4e0063", "#b7abae", "#63d2ff"
                ]
            }]
        };

        var pieChart2 = new Chart(expenseCanvas, {
            type: 'pie',
            data: expenseData
        });

    });
    // Graphs
    var ctx = document.getElementById('myChart')

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var dataFirst = {
        label: "Incomes",
        data: dataAmountIncomes,
        lineTension: 0,
        fill: false,
        borderColor: 'green'
    };

    var dataSecond = {
        label: "Expenses",
        data: dataAmountExpenses,
        lineTension: 0,
        fill: false,
        borderColor: 'red'
    };

    var IncomExpenseData = {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        datasets: [dataFirst, dataSecond]
    };

    var chartOptions = {
        legend: {
            display: true,
            position: 'top',
            labels: {
                boxWidth: 80,
                fontColor: 'black'
            }
        }
    };

    var lineChart = new Chart(ctx, {
        type: 'line',
        data: IncomExpenseData,
        options: chartOptions
    });
})()