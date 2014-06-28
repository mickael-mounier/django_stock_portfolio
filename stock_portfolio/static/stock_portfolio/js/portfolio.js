$(function() {

    function add_stock() {
        var symbol = $('#stock_searchbar').val().trim();
        if (!symbol)
            return;
        $.ajax({url: 'add/' + symbol
        }).success(function() {
            location.reload();
        });
    }

    /*************/
    /* SEARCHBAR */
    /*************/

    function yahoo_autocomplete(q, cb) {
        function _cb(data) {
            cb(data.ResultSet.Result);
        }
        YAHOO = {Finance: {SymbolSuggest: {ssCallback: _cb}}}; // Yahoo API hack
        $.ajax({url: 'http://d.yimg.com/autoc.finance.yahoo.com/autoc',
                jsonpCallback: 'YAHOO.Finance.SymbolSuggest.ssCallback',
                dataType: 'jsonp',
                data: {query: q}
               });
    }

    $('#stock_searchbar').typeahead({}, {
        name: 'yahoo_autocomplete',
        source: yahoo_autocomplete,
        displayKey: 'symbol',
        templates: {
            suggestion: function(d) {
                return '<span class="search_symbol">' + d.symbol + '</span><span class="search_name">' + d.name + '</span> <span class="search_market">(' + (d.exchDisp ? d.exchDisp + ' ' : '') + d.typeDisp + ')</span>';
            }
        }
    }).parent().css('display', 'table-cell'); // Bootstrap/typeahead compatibility bugfix

    $('#add_stock').click(add_stock);
    $('#stock_searchbar').keydown(function(e) {
        if (e.keyCode == 13)
            add_stock();
    });

});
