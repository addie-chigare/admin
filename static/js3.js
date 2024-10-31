document.addEventListener('DOMContentLoaded', function() {
    var productForm = document.getElementById('productForm');
    var productNameInput = document.getElementById('productName');
    var descriptionInput = document.getElementById('description');
    var contactInput = document.getElementById('contact');
    var imageUploadInput = document.getElementById('imageUpload');

    function isNumber(evt) {
        var iKeyCode = evt.which ? evt.which : evt.keyCode;
        return (iKeyCode >= 48 && iKeyCode <= 57) || iKeyCode === 8; // Allow numbers and backspace
    }

    function isString(evt) {
        var iKeyCode = evt.which ? evt.which : evt.keyCode;
        return (iKeyCode >= 65 && iKeyCode <= 90) || (iKeyCode >= 97 && iKeyCode <= 122) || iKeyCode === 32 || iKeyCode === 8; // Allow letters, space, and backspace
    }

    function isAlphanumeric(evt) {
        var iKeyCode = evt.which ? evt.which : evt.keyCode;
        return (iKeyCode >= 48 && iKeyCode <= 57) || // Numbers
               (iKeyCode >= 65 && iKeyCode <= 90) || // Uppercase letters
               (iKeyCode >= 97 && iKeyCode <= 122) || // Lowercase letters
               iKeyCode === 32 || iKeyCode === 8; // Space and backspace
    }

    productNameInput.addEventListener('keypress', function(evt) {
        if (!isString(evt)) {
            evt.preventDefault();
        }
    });

    contactInput.addEventListener('keypress', function(evt) {
        if (!isNumber(evt)) {
            evt.preventDefault();
        }
    });

    descriptionInput.addEventListener('keypress', function(evt) {
        if (!isAlphanumeric(evt)) {
            evt.preventDefault();
        }
    });

    // Check file type for image upload
    imageUploadInput.addEventListener('change', function(evt) {
        var file = evt.target.files[0];
        if (file && !file.type.startsWith('image/')) {
            alert('Please upload a valid image file.');
            imageUploadInput.value = ''; // Clear the file input
        }
    });

    // Prevent form submission if validation fails
    productForm.addEventListener('submit', function(evt) {
        var descriptionText = descriptionInput.value.trim();
        if (descriptionText.length < 10) {
            alert('Description must be at least 10 characters long.');
            evt.preventDefault(); // Prevent form from submitting
        }
    });
});
