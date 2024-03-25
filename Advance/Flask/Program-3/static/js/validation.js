function validateForm() {
    var name = document.getElementById('name').value;
    var age = document.getElementById('age').value;
    var genre = document.getElementById('genre').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    var dob = document.getElementById('dob').value;

    // Regular expressions for validation
    var nameRegex = /^[a-zA-Z\s]+$/;
    var ageRegex = /^\d+$/;
    var genreRegex = /^[a-zA-Z\s]+$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var phoneRegex = /^\d{10}$/;

    // Name validation
    if (!name.match(nameRegex)) {
        alert('Please enter a valid name.');
        return false;
    }

    // Age validation
    if (!age.match(ageRegex)) {
        alert('Please enter a valid age.');
        return false;
    }

    // Genre validation
    if (!genre.match(genreRegex)) {
        alert('Please enter a valid genre.');
        return false;
    }

    // Email validation
    if (!email.match(emailRegex)) {
        alert('Please enter a valid email address.');
        return false;
    }

    // Phone number validation
    if (!phone.match(phoneRegex)) {
        alert('Please enter a valid phone number (10 digits only).');
        return false;
    }

    // If all validations pass, return true to submit the form
    return true;
}

document.getElementById("registrationForm").onsubmit = function () {
    if (validateForm()) {
        // Redirect to the login page after successful registration
        window.location.href = "/login";
    }
    return false; // Prevent the form from submitting normally
};
