document.addEventListener('DOMContentLoaded', function() {
    var productNameInput = document.getElementById('productName');
    var priceInput = document.getElementById('price');
    var quantityInput = document.getElementById('quantity');
    var descriptionInput = document.getElementById('description');

    // Function to validate numbers only
    function isNumber(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        if (iKeyCode > 31 && (iKeyCode < 48 || iKeyCode > 57)) return false;
        return true;
    }

    // Function to validate strings only
    function isString(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        if ((iKeyCode < 65 || iKeyCode > 90) && (iKeyCode < 97 || iKeyCode > 122) && iKeyCode != 32 && iKeyCode != 8) return false;
        return true;
    }

    // Function to validate alphanumeric input
    function isAlphanumeric(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        if (iKeyCode > 31 && (iKeyCode < 65 || iKeyCode > 90) &&
            (iKeyCode < 97 || iKeyCode > 122) && iKeyCode != 46 &&
            (iKeyCode < 48 || iKeyCode > 57)) return false;
        return true;
    }

    // Add event listeners to inputs
    productNameInput.addEventListener('keypress', function(evt) {
        return isString(evt);
    });

    priceInput.addEventListener('keypress', function(evt) {
        return isNumber(evt);
    });

    quantityInput.addEventListener('keypress', function(evt) {
        return isNumber(evt);
    });

    descriptionInput.addEventListener('keypress', function(evt) {
        return isAlphanumeric(evt);
    });
});
