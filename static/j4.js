document.getElementById('signupForm').addEventListener('submit', function(event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;

    // Clear previous error messages
    const errorMessages = document.querySelectorAll('.error');
    errorMessages.forEach(msg => msg.remove());

    // Validate password match
    if (password !== confirmPassword) {
        event.preventDefault(); // Prevent form submission
        const error = document.createElement('div');
        error.className = 'error';
        error.textContent = 'Passwords do not match.';
        document.querySelector('.container').insertBefore(error, document.getElementById('signupForm'));
    }
});
