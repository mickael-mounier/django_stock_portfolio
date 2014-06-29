$(function() {
    $('#stock_chart').highcharts('StockChart', {
        rangeSelector: {
            selected: 1
        },
        title: {
            text: stockName
        },
        series: [{
            name: stockMnemo,
            data: stockData
        }]
    });
});
