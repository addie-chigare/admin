document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    
    form.addEventListener("submit", function(event) {
        let isValid = true;

        // Validate Name
        const name = document.getElementById("name").value.trim();
        if (name === "") {
            alert("Please enter your name.");
            isValid = false;
        }

        // Validate Address
        const address = document.getElementById("address").value.trim();
        if (address === "") {
            alert("Please enter your address.");
            isValid = false;
        }

        // Validate Contact
        const contact = document.getElementById("contact").value.trim();
        if (contact.length !== 10 || isNaN(contact)) {
            alert("Please enter a valid 10-digit contact number.");
            isValid = false;
        }

        // Validate Gender
        const gender = document.querySelector('input[name="gender"]:checked');
        if (!gender) {
            alert("Please select your gender.");
            isValid = false;
        }

        // Validate DOB
        const dob = document.getElementById("dob").value;
        if (!dob) {
            alert("Please select your date of birth.");
            isValid = false;
        }

        // Validate Email
        const email = document.getElementById("email").value.trim();
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            isValid = false;
        }

        // Validate Password
        const password = document.getElementById("password").value.trim();
        const confirmPassword = document.getElementById("confirm_password").value.trim();
        const passwordPattern = /^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{6,12}$/;
        
        if (!passwordPattern.test(password)) {
            alert("Password must be 6-12 characters long, contain at least one uppercase letter and one special character.");
            isValid = false;
        }

        // Validate Confirm Password
        if (password !== confirmPassword) {
            alert("Passwords do not match.");
            isValid = false;
        }

        // Prevent form submission if any validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });
});
