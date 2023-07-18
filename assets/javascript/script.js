// All JavaScript in here is non-essential for functionality and readability. It is solely to stop some bs from happening

// Insert span into all menu items for extra CSS customization
function startUpTasks() {
    insertSpanInMenuItems();
    makeOpenInNewWindow();
}

function insertSpanInMenuItems() {
    menuItems = document.querySelectorAll(".menuList li > a, .menuList li:not(:has(a))")
    // Wrap menu text in span
    for(let i = 0; i < menuItems.length; i++) {
        menuItems[i].innerHTML = `<span>${menuItems[i].innerHTML}</span>`;
    }
}

function makeOpenInNewWindow() {
    menuItems = document.querySelectorAll(".newWindow a")
    // Wrap menu text in span
    for(let i = 0; i < menuItems.length; i++) {
        menuItems[i].target = "_blank";
    }
}