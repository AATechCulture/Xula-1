// document.querySelector("#option4454").attributes['data-label'].value

// Dictionary = {}
// for (var i = 0; i < inputs.length; i++) { 
//     input = inputs[i]
//     label = input.attributes['data-label'].value
//     isChecked = input.checked
//     Dictionary[label] = isChecked
// }
// console.log(Dictionary) 

// class name and input label
// on submit

document.querySelector("#submit").addEventListener('click', function () {
    const forms = document.getElementsByClassName('C-Data');
    const data = {};

    for (let i = 0; i < forms.length; i++) {
        form = forms[i]
        label = form.attributes['data-label'].value
        isChecked = form.checked
        data[label] = isChecked
    }

    fetch('http://localhost:8000/test', {
        method: 'POST',
        body: JSON.stringify({data}),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(responseData => {
        console.log('Server Response:', responseData);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
