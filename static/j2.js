document.addEventListener('DOMContentLoaded', function() {
    var productNameInput = document.getElementById('productName');
    var priceInput = document.getElementById('price');
    var quantityInput = document.getElementById('qty');
    var totalAmountInput = document.getElementById('totalAmount');
    var form = document.getElementById('productForm');

    // Function to validate numbers only
    function isNumber(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        return (iKeyCode >= 48 && iKeyCode <= 57) || iKeyCode === 8; // Allow numbers and backspace
    }

    // Function to validate strings only
    function isString(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        return (iKeyCode >= 65 && iKeyCode <= 90) || // A-Z
               (iKeyCode >= 97 && iKeyCode <= 122) || // a-z
               iKeyCode === 32 || // space
               iKeyCode === 8 ||  // backspace
               iKeyCode === 46; // period
    }

    // Function to validate alphanumeric input
    function isAlphanumeric(evt) {
        var iKeyCode = (evt.which) ? evt.which : evt.keyCode;
        return (iKeyCode >= 48 && iKeyCode <= 57) || // 0-9
               (iKeyCode >= 65 && iKeyCode <= 90) || // A-Z
               (iKeyCode >= 97 && iKeyCode <= 122) || // a-z
               iKeyCode === 32 || // space
               iKeyCode === 8 ||  // backspace
               iKeyCode === 46; // period
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

    // Calculate total amount based on price and quantity
    function calculateTotal() {
        var price = parseFloat(priceInput.value);
        var quantity = parseInt(quantityInput.value);
        if (!isNaN(price) && !isNaN(quantity)) {
            totalAmountInput.value = (price * quantity).toFixed(2);
        } else {
            totalAmountInput.value = '';
        }
    }

    priceInput.addEventListener('input', calculateTotal);
    quantityInput.addEventListener('input', calculateTotal);

    // Form submit handler
    form.addEventListener('submit', function(evt) {
        var productName = productNameInput.value.trim();
        var price = priceInput.value.trim();
        var quantity = quantityInput.value;
        var description = descriptionInput.value.trim();

        // Validate price as a number
        if (isNaN(price) || parseFloat(price) <= 0) {
            alert('Please enter a valid price.');
            evt.preventDefault(); // Prevent form submission
            return;
        }

        // Validate quantity as a number
        if (isNaN(quantity) || parseInt(quantity) <= 0) {
            alert('Please enter a valid quantity.');
            evt.preventDefault(); // Prevent form submission
            return;
        }

        // Validate description (if you have a description field)
        if (description.length < 5) {
            alert('Description must be at least 5 characters long.');
            evt.preventDefault(); // Prevent form submission
            return;
        }

        // If all validations pass, allow form submission
    });
});
