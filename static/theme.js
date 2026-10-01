const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
}

function updateThemeButton() {
    const button = document.getElementById("theme-button");

    if (!button) {
        return;
    }

    const currentTheme = document.documentElement.getAttribute("data-theme");

    if (currentTheme === "dark") {
        button.textContent = "☀";
    } else {
        button.textContent = "☾";
    }
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-theme");

    if (currentTheme === "dark") {
        document.documentElement.removeAttribute("data-theme");
        localStorage.setItem("theme", "light");
    } else {
        document.documentElement.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
    }

    updateThemeButton();
}

updateThemeButton();