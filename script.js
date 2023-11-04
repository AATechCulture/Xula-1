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

document.getElementById('input[type="submit"]').addEventListener('click', function () {
    const forms = document.getElementsByClassName('C-Data');
    const data = {};

    for (let i = 0; i < forms.length; i++) {
        const form = forms[i];
        const formData = new FormData(form);

        formData.forEach((value, key) => {
            data[key] = value;
        });
    }

    fetch('your-server-url-here', {
        method: 'POST',
        body: JSON.stringify(data),
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
