var noDuplicates = [];

var duplicateFinder = function(array) {
	array.sort();
	for (var i = 0; i < array.length; i++) {
		if (array[i+1] == array[i]) {
			noDuplicates.push(array[i]);
		}
	}
	return noDuplicates;
}