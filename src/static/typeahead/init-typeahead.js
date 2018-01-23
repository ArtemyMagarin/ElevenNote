var substringMatcher = function (strings) {
    return function findMatches(query, callback) {
        var matches;

        // an array that will be populated with substring matches
        matches = [];

        // regex used to determine if a string contains the substring `q`
        substrRegex = new RegExp(query, 'i');

        // iterate through the pool of strings and for any string that
        // contains the substring `q`, add it to the `matches` array
        $.each(strings, function (i, str) {
            if (substrRegex.test(str)) {
                matches.push(str);
            }
        });

        callback(matches);
    };
};


// var options = {};
// var dataSet = {
//     source: substringMatcher(states)
// };

// $('.typeahead').typeahead(options, dataSet);

// $('button.remove').click(
//     function () {
//         $('.typeahead').typeahead('val', '').trigger('typeahead:idle');
//     }
// );