document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        const username = document.getElementById("username").value.trim();
        const password = document.getElementById("password").value.trim();

        if (username === "" || password === "") {
            alert("Please enter both username and password!");
            return;
        }

        // Simulate authentication (Replace with real authentication logic)
        if (username === "admin" && password === "admin123") {
            alert("Login Successful!");
            window.location.href = "dashboard.html"; // Redirect to the dashboard page
        } else {
            alert("Invalid credentials. Try again.");
        }
    });
});
