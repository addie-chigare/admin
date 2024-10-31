function navigateTo(path) {
    window.location.href = path;
}

function performSearch() {
    const searchText = document.getElementById('search-input').value;
    console.log("Searching for:", searchText);
    // Implement your API call here
    document.getElementById('search-input').value = ''; // Clear the input
}

function toggleDropdown() {
    const menu = document.getElementById('dropdown-menu');
    menu.classList.toggle('hidden');
}

// Example function to dynamically load idols
async function fetchIdols() {
    try {
        const response = await fetch('/api');
        const result = await response.json();
        const idolList = result.data.best_sellers;
        const contentDiv = document.getElementById('idol-list');

        idolList.forEach(idol => {
            const idolItem = document.createElement('div');
            idolItem.className = 'idol-item';
            idolItem.innerHTML = `
                <img src="${idol.product_photo}" alt="${idol.product_title}">
                <h3>${idol.product_title}</h3>
                <p>Price: ${idol.product_price}</p>
            `;
            contentDiv.appendChild(idolItem);
        });
    } catch (err) {
        console.error(err);
    }
}

// Fetch idols on page load
window.onload = fetchIdols;
