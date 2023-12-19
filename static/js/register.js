const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const contact = document.getElementById('contact');
const age = document.getElementById('age');
const batch =document.getElementById('batch');
form.addEventListener('submit',e=>{
    e.preventDefault();
    const formData = {
        username: username.value.trim(),
        email: email.value.trim(),
        age: age.value.trim(),
        batch: batch.value
    };
    validateInputs(formData);
});
const setSuccess=element=>{
    const inputControl=element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText='';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
}
const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    
    return emailRegex.test(String(email).toLowerCase());
};
const isValidContact = (contact) => {
    
    const contactRegex = /^[0-9]{10}$/;
    return contactRegex.test(contact);
};
const isValidAge = (age) => {
    // Check if age is a number and falls within the range of 18 to 65
    return !isNaN(age) && parseInt(age) >= 18 && parseInt(age) <= 65;
};
const setError=(element , message)=>{
    const inputControl=element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText=message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
}
const validateInputs=(formData)=>{
    const { username, email, age, batch } = formData;

    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const contactValue = contact.value.trim();
    const ageValue = age.value.trim();
    const batchValue = batch.value;

    if(usernameValue===''){
        setError(username,'UserName is required');
    }
    else{
        setSuccess(username);
    }

    if(emailValue===''){
        setError(email,'Email is required');
    }
    else if(!isValidEmail(emailValue)){
        setError(email,'Provide valid Email');
    }
    else{
        setSuccess(email);
    }

    if(contactValue===''){
        setError(contact,'Phone number is required');
    }
    // else if(!isValidEmail(contactValue)){
    //     setError(contact,'Provide valid Phone number');
    // }
    else{
        setSuccess(contact);
    }

    if (ageValue === '') {
        setError(age, 'Age is required');
    } else if (!isValidAge(ageValue)) {
        setError(age, 'Age must be between 18 and 65');
    } else {
        setSuccess(age);
    }

    if (batchValue === '' || batchValue === null) {
        setError(batch, 'Select a valid batch');
    } else {
        setSuccess(batch);
    }

};