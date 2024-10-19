(function () {
    if (!window.recipebookmarklet) {
        recipebookmarklet_js = document.body.appendChild(document.createElement('script'));
        recipebookmarklet_js.src = '//127.0.0.1:8000/static/js/recipebookmarklet.js?r=' + Math.floor(Math.random() * 9999999999999999);
        window.recipebookmarklet = true;
    }
    else {
        recipebookmarkletLaunch();
    }
})();