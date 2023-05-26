document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();

    var fileInput = document.getElementById('audio-input');
    var file = fileInput.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('audio', file);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/analyze', true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var results = JSON.parse(xhr.responseText);
                displayResults(results);
            }
        };
        xhr.send(formData);
    }
});

function displayResults(results) {
    var resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = 'Intonation: ' + results.intonation.toFixed(2) +
                           '<br>Accuracy: ' + results.accuracy.toFixed(2) +
                           '<br>Tempo Adherence: ' + results.tempo.toFixed(2);
}