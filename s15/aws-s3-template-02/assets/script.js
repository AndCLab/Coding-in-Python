const nav = document.querySelector('#navbar');

if (window.scrollY >= 10) {
    nav.classList.add('scrolled');
}

window.onscroll = () => {
    if (this.scrollY <= 10) {
        nav.classList.remove('scrolled');
    } else {
        nav.classList.add('scrolled');
    }
};